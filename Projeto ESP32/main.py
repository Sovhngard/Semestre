from machine import Pin, I2C, ADC, PWM
import time
import dht
from umqtt.simple import MQTTClient
import network
import i2c_lcd


sda = Pin(21) 
scl = Pin(22)  
i2c = I2C(0, sda=sda, scl=scl, freq=400000)


lcd = i2c_lcd.I2cLcd(i2c, 0x27, 2, 16)


sensor1 = dht.DHT22(Pin(23))
sensor2 = dht.DHT22(Pin(2))
sensor3 = dht.DHT22(Pin(19))

yellow = Pin(4, Pin.OUT)
green = Pin(18, Pin.OUT)
red = Pin(5, Pin.OUT)

potenciometro1 = ADC(Pin(34))
potenciometro2 = ADC(Pin(35))
potenciometro3 = ADC(Pin(36))

MQTT_CLIENT_ID = "Cliente10000"
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = "avila"
MQTT_PASSWORD = ""
MQTT_TOPIC1 = "msg_weverton"
MQTT_TOPIC2 = "msg_estevao"  


escolha = 1


def callback(topic, msg):
    global escolha
    mensagem = str(msg.decode())
    if mensagem == "UBS Santa Isabel":
        client.publish(MQTT_TOPIC1, "UBS Santa Isabel")
        escolha = 1
    elif mensagem == "UBS Tijuca":
        client.publish(MQTT_TOPIC1, "UBS Tijuca")
        escolha = 2
    elif mensagem == "UBS Bairro CPA":
        client.publish(MQTT_TOPIC1, "UBS Bairro CPA")
        escolha = 3


print("Tentando conectar", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')  
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Conectado!")


def reconnect_mqtt():
    global client
    try:
        client.disconnect()  
    except:
        pass  
    
    try:
        client.connect()
        client.subscribe(MQTT_TOPIC2)
        print("Dando conect no MQTT!")
    except Exception as e:
        print(f"Erro conect no MQTT: {e}")
        time.sleep(5)
        reconnect_mqtt() 


print("Conectando ao server do MQTT... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.set_callback(callback)
reconnect_mqtt()  

def ler_sensor(sensor, potenciometro):
    sensor.measure()
    temperatura = sensor.temperature()
    humidade = sensor.humidity()
    adc_value = potenciometro.read()
    decibeis = (adc_value/4095)*100
    return temperatura, humidade, decibeis

def atualizar_lcd(temperatura, humidade, decibeis, cor):
    lcd.clear()
    lcd.putstr(f"T: {temperatura}C Hum: {humidade}% db: {decibeis:.2f}")
    time.sleep(2)
    lcd.clear()
    if humidade < 50:
        lcd.putstr("Humidade muito baixa")
    elif humidade > 60:
        lcd.putstr("Humidade muito alta")
    else:
        lcd.putstr("Humidade normal")
    time.sleep(2)
    lcd.clear()
    if decibeis <= 55:
        lcd.putstr("Poluicao sonora baixa")
    elif decibeis <= 70:
        lcd.putstr("Poluicao sonora moderada")
    else:
        lcd.putstr("Poluicao sonora alta")
    cor.on()
    time.sleep(2)
    cor.off()


while True:
    try:
        client.check_msg() 
        yellow.off()
        green.off()
        red.off()
        
        if escolha == 1:
            temperatura, humidade, decibeis = ler_sensor(sensor1, potenciometro1)
        elif escolha == 2:
            temperatura, humidade, decibeis = ler_sensor(sensor2, potenciometro2)
        elif escolha == 3:
            temperatura, humidade, decibeis = ler_sensor(sensor3, potenciometro3)
        
        if humidade < 50 or humidade > 60:
            atualizar_lcd(temperatura, humidade, decibeis, yellow if humidade < 50 else red)
        else:
            atualizar_lcd(temperatura, humidade, decibeis, green)
    
    except Exception as e:
        print(f"Erro no loop principal: {e}")
        time.sleep(1)
