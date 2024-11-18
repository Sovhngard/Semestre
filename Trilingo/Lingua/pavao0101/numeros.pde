import processing.video.*;
import processing.sound.*;

SoundFile um_1, dois_2, tres_3, quatro_4, cinco_5, seis_6, sete_7, oito_8, nove_9, dez_10, zero_0, num_00;

PFont f3;
String zero = "Zero";
String um = "Um";
String dois = "Dois";
String tres = "Três";
String quatro = "Quatro";
String cinco = "Cinco";
String seis = "Seis";
String sete = "Sete";
String oito = "Oito";
String nove = "Nove";
String dez = "Dez";
String num = "Número";

boolean isZero = true;
boolean isOne = true; 
boolean isTwo = true;  
boolean isThree = true;   
boolean isFour = true;  
boolean isFive = true;     
boolean isSix = true;
boolean isSeven = true;
boolean isEight = true;
boolean isNine = true;
boolean isTen = true;
boolean isNum = true;

PButton2 bt_um, bt_dois, bt_tres, bt_quatro, bt_cinco, bt_seis, bt_sete, bt_oito, bt_nove, bt_dez, bt_zero, bt_num;
PButton_num botaoVoltar2_num, botaoProximo2_num;

PImage ft_um, ft_dois, ft_tres, ft_quatro, ft_cinco, ft_seis, ft_sete, ft_oito, ft_nove, ft_dez, ft_zero, ft_num;

void setup_num() {
  size(1280, 720);
  f = createFont("San Francisco", 16);
  textFont(f);

  // IMGS
  ft_um = loadImage("1.png");
  ft_dois = loadImage("2.png");
  ft_tres = loadImage("3.png");
  ft_quatro = loadImage("4.png");
  ft_cinco = loadImage("5.png");
  ft_seis = loadImage("6.png");
  ft_sete = loadImage("7.png");
  ft_oito = loadImage("8.png");
  ft_nove = loadImage("9.png");
  ft_dez = loadImage("10.png");
  ft_zero = loadImage("0.png");
  ft_num = loadImage("num.png");
  
  // SONS
  um_1 = new SoundFile(this, "one.mp3");
  dois_2 = new SoundFile(this, "two.mp3");
  tres_3 = new SoundFile(this, "three.mp3");
  quatro_4 = new SoundFile(this, "four.mp3");
  cinco_5 = new SoundFile(this, "five.mp3");
  seis_6 = new SoundFile(this, "six.mp3");
  sete_7 = new SoundFile(this, "seven.mp3");
  oito_8 = new SoundFile(this, "eight.mp3");
  nove_9 = new SoundFile(this, "nine.mp3");
  dez_10 = new SoundFile(this, "ten.mp3");
  zero_0 = new SoundFile(this, "zero.mp3");
  num_00 = new SoundFile(this, "num.mp3");

  // BOT ESQUERDA
  botao1 = new PButton(50, 50, "Animais");
  botao2 = new PButton(50, 630, "Exercícios");
  botao3 = new PButton(50, 250, "Números");
  botao4 = new PButton(50, 350, "Família");
  botao5 = new PButton(50, 150, "Cores");

  //botoes da aula
  bt_um = new PButton2(400, 180, 100, 50, um);
  bt_dois = new PButton2(640, 180, 100, 50, dois);
  bt_tres = new PButton2(870, 180, 100, 50, tres);
  bt_quatro = new PButton2(1100, 180, 100, 50, quatro);
  bt_cinco = new PButton2(400, 390, 100, 50, cinco);
  bt_seis = new PButton2(640, 390, 100, 50, seis);
  bt_sete = new PButton2(870, 390, 100, 50, sete);
  bt_oito = new PButton2(1100, 390, 100, 50, oito);
  bt_nove = new PButton2(400, 600, 100, 50, nove);
  bt_dez = new PButton2(640, 600, 100, 50, dez);
  bt_zero = new PButton2(870, 600, 100, 50, zero);
  bt_num = new PButton2(1100, 600, 100, 50, num);
}

void draw_num() {
  background(255);

  // FUNDO
  fill(238, 238, 238);
  noStroke();
  rect(10, 10, 290, 700, 28);
  rect(310, 10, 960, 700, 28);

  // IMGS
  image(ft_um, 400, 60, 100, 100);
  image(ft_dois, 640, 60, 100, 100);
  image(ft_tres, 870, 60, 100, 100);
  image(ft_quatro, 1100, 60, 100, 100);
  image(ft_cinco, 400, 260, 100, 100);
  image(ft_seis, 640, 260, 100, 100);
  image(ft_sete, 870, 260, 100, 100);
  image(ft_oito, 1100, 260, 100, 100);
  image(ft_nove, 400, 480, 100, 100);
  image(ft_dez, 640, 480, 100, 100);
  image(ft_zero, 870, 480, 100, 100);
  image(ft_num, 1100, 480, 100, 100);

  botao1.display();
  botao2.display();
  botao3.display();
  botao4.display();
  botao5.display();

  bt_um.display();
  bt_dois.display();
  bt_tres.display();
  bt_quatro.display();
  bt_cinco.display();
  bt_seis.display();
  bt_sete.display();
  bt_oito.display();
  bt_nove.display();
  bt_dez.display();
  bt_zero.display();
  bt_num.display();

}

void mousePressed_num() {

  if (bt_um.isMouseOver()) {
    if (isOne) {
      bt_um.setText("One");
      um_1.play();
    } else {
      bt_um.setText("Um");
    }
    isOne = !isOne;
    buttonPressed = true;
  } else if (bt_dois.isMouseOver()) {
    if (isTwo) {
      dois_2.play();
      bt_dois.setText("Two");
    } else {
      bt_dois.setText("Dois");
    }
    isTwo = !isTwo;
    buttonPressed = true;
  } else if (bt_tres.isMouseOver()) {
    if (isThree) {
      tres_3.play();
      bt_tres.setText("Three");
    } else {
      bt_tres.setText("Três");
    }
    isThree = !isThree;
    buttonPressed = true;
  } else if (bt_quatro.isMouseOver()) {
    if (isFour) {
      quatro_4.play();
      bt_quatro.setText("Four");
    } else {
      bt_quatro.setText("Quatro");
    }
    isFour = !isFour;
    buttonPressed = true;
  } else if (bt_cinco.isMouseOver()) {
    if (isFive) {
      cinco_5.play();
      bt_cinco.setText("Five");
    } else {
      bt_cinco.setText("Cinco");
    }
    isFive = !isFive;
    buttonPressed = true;
  } else if (bt_seis.isMouseOver()) {
    if (isSix) {
      seis_6.play();
      bt_seis.setText("Six");
    } else {
      bt_seis.setText("Seis");
    }
    isSix = !isSix;
    buttonPressed = true;
  } else if (bt_sete.isMouseOver()) {
    if (isSeven) {
      sete_7.play();
      bt_sete.setText("Seven");
    } else {
      bt_sete.setText("Sete");
    }
    isSeven = !isSeven;
    buttonPressed = true;
  } else if (bt_oito.isMouseOver()) {
    if (isEight) {
      oito_8.play();
      bt_oito.setText("Eight");
    } else {
      bt_oito.setText("Oito");
    }
    isEight = !isEight;
    buttonPressed = true;
  } else if (bt_nove.isMouseOver()) {
    if (isNine) {
      nove_9.play();
      bt_nove.setText("Nine");
    } else {
      bt_nove.setText("Nove");
    }
    isNine = !isNine;
    buttonPressed = true;
  } else if (bt_dez.isMouseOver()) {
    if (isTen) {
      dez_10.play();
      bt_dez.setText("Ten");
    } else {
      bt_dez.setText("Dez");
    }
    isTen = !isTen;
    buttonPressed = true;
  } else if (bt_zero.isMouseOver()) {
    if (isZero) {
      zero_0.play();
      bt_zero.setText("Zero");
    } else {
      bt_zero.setText("Zero");
    }
    isZero = !isZero;
    buttonPressed = true;
  } else if (bt_num.isMouseOver()) {
    if (isNum) {
      num_00.play();
      bt_num.setText("Number");
    } else {
      bt_num.setText("Número");
    }
    isNum = !isNum;
    buttonPressed = true;
  }

  if (telaAtual != 0) {
   
    if (botao1.isClicked()) {
      setup2();  
      telaAtual = 1; 
    } else if (botao2.isClicked()) {
      setup_exer(); 
      telaAtual = 2; 
    } else if (botao3.isClicked()) {
      setup_num();
      telaAtual = 3;
    } else if (botao4.isClicked()) {
      setup3();
      telaAtual = 4;
    } else if (botao5.isClicked()) {
      setup5();
      telaAtual = 5;
    }
    
  } else if (telaAtual == 1) {
    mousePressed2();  
  } else if (telaAtual == 2) {
    mousePressed_exer();
  } else if (telaAtual == 3) {
    mousePressed_num();
  } else if (telaAtual == 4) {
    mousePressed3();
  } else if (telaAtual == 5) {
    mousePressed5();
  }

}

class PButton_num {
  float x, y, w, h;
  String text;

  PButton_num(float x, float y, float w, float h, String text) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.text = text;
  }

  void display() {
    // HOVER
    if (isMouseOver()) {
      fill(200); 
    } else {
      fill(255); 
    }
    rect(x, y, w, h, 28); 
    fill(0);
    textAlign(CENTER, CENTER);
    text(text, x + w / 2, y + h / 2); 
  }

  boolean isMouseOver() {
    return mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + h;
  }

  void setText(String newText) {
    text = newText;
  }
}
