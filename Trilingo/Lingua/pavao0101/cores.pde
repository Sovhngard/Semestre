import processing.video.*;
import processing.sound.*;

String tebc1 = "Vermelho";
String tebc2 = "Laranja";
String tebc3 = "Amarelo";
String tebc4 = "Verde";
String tebc5 = "Azul";
String tebc6 = "Roxo";

boolean isRed = true; 
boolean isOrange = true;  
boolean isYellow = true;   
boolean isGreen = true;  
boolean isBlue = true;     
boolean isPurple = true;

SoundFile red, orange, yellow, green, blue, purple;

PButton5 btcor1, btcor2, btcor3, btcor4, btcor5, btcor6;

void setup5() {
  size(1280,720);
  f = createFont("San Francisco", 16);
  textFont(f);
  
  red = new SoundFile(this, "red.mp3");
  orange = new SoundFile(this, "orange.mp3");
  yellow = new SoundFile(this, "yellow.mp3");
  green = new SoundFile(this, "green.mp3");
  blue = new SoundFile(this, "blue.mp3");
  purple = new SoundFile(this, "purple.mp3");
 
  btcor1 = new PButton5(400, 240, 150, 50, tebc1);
  btcor2 = new PButton5(720, 240, 150, 50, tebc2);
  btcor3 = new PButton5(1030, 240, 150, 50, tebc3);
  btcor4 = new PButton5(400, 570, 150, 50, tebc4);
  btcor5 = new PButton5(720, 570, 150, 50, tebc5);
  btcor6 = new PButton5(1030, 570, 150, 50, tebc6);
  
  botao1 = new PButton(50, 50, "Animais");
  botao2 = new PButton(50, 630, "Exercícios");
  botao3 = new PButton(50, 250, "Números");
  botao4 = new PButton(50, 350, "Família");
  botao5 = new PButton(50, 150, "Cores");
}

void draw5() {
  background(255);

  // FUNDO
  fill(238, 238, 238);
  noStroke();
  rect(10, 10, 290, 700, 28);
  rect(310, 10, 960, 700, 28);
  
  stroke(#FFFFFF);
  strokeWeight(8);
  fill(#D90416);//vermelho
  rect(400, 65, 150, 150);
  fill(#F25C05);//laranja
  rect(720, 65, 150, 150);
  fill(#F2CB05);//amarelo
  rect(1030, 65, 150, 150);
  fill(#2CBF04);//verde
  rect(400, 400, 150, 150);
  fill(#0420BF);//azul
  rect(720, 400, 150, 150);
  fill(#982CC9);//roxo
  rect(1030, 400, 150, 150);
  
  noStroke();
  botao1.display();
  botao2.display();
  botao3.display();
  botao4.display();
  botao5.display();
  
  // Exibe os botões
  btcor1.display();
  btcor2.display();
  btcor3.display();
  btcor4.display();
  btcor5.display();
  btcor6.display();
}

void mousePressed5() {

 if (btcor1.isMouseOver()) {
    if (isRed) {
      btcor1.setText("Red");
      red.play();
    } else {
      btcor1.setText("Vermelho");
    }
    isRed = !isRed;
    buttonPressed = true;
  } else if (btcor2.isMouseOver()) {
    if (isOrange) {
      orange.play();
      btcor2.setText("Orange");
    } else {
      btcor2.setText("Laranja");
    }
    isOrange = !isOrange;
    buttonPressed = true;
  } else if (btcor3.isMouseOver()) {
    if (isYellow) {
      yellow.play();
      btcor3.setText("Yellow");
    } else {
      btcor3.setText("Amarelo");
    }
    isYellow = !isYellow;
    buttonPressed = true;
  } else if (btcor4.isMouseOver()) {
    if (isGreen) {
      green.play();
      btcor4.setText("Green");
    } else {
      btcor4.setText("Verde");
    }
    isGreen = !isGreen;
    buttonPressed = true;
  } else if (btcor5.isMouseOver()) {
    if (isBlue) {
      blue.play();
      btcor5.setText("Blue");
    } else {
      btcor5.setText("Azul");
    }
    isBlue = !isBlue;
    buttonPressed = true;
  } else if (btcor6.isMouseOver()) {
    if (isPurple) {
      purple.play();
      btcor6.setText("Purple");
    } else {
      btcor6.setText("Roxo");
    }
    isPurple = !isPurple;
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

class PButton5 {
  float x, y, w, h;
  String text;
  
  PButton5(float x, float y, float w, float h, String text) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.text = text;
  }
  
  void display() {
    // MUDA A COR NO HOVER
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
