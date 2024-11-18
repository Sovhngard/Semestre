import processing.video.*;
import processing.sound.*;

SoundFile um_11, dois_22, tres_33, quatro_44, cinco_55, seis_66, sete_77, oito_88, nove_99, errou, nice;

PFont f4;
String tebt1 = "Mãe";
String tebt2 = "Pai";
String tebt3 = "Irmã";
String tebt4 = "Irmão";
String tebt5 = "Avó";
String tebt6 = "Avô";
String tebt7 = "Tia";
String tebt8 = "Tio";
String tebt9 = "Prima";

boolean isMother = true; 
boolean isFather = true;  
boolean isBrother = true;   
boolean isSister = true;  
boolean isGrandma = true;     
boolean isGrandpa = true;
boolean isUncle = true;
boolean isAunt = true;
boolean isCousin = true;


PButton3 bt1_3, bt2_3, bt3_3, bt4_3, bt5_3, bt6_3, bt7_3, bt8_3, bt9_3, butano1, butano2, butano3;

PImage  ft1_3, ft2_3, ft3_3, ft4_3, ft5_3, ft6_3, ft7_3, ft8_3, ft9_3;

void setup3() {
  size(1280,720);
  f4 = createFont("San Francisco", 16);
  textFont(f4);

  // IMGS
  ft1_3 = loadImage("mom.png");
  ft2_3 = loadImage("dad.png");
  ft3_3 = loadImage("sis.png");
  ft4_3 = loadImage("bro.png");
  ft5_3 = loadImage("granny.png");
  ft6_3 = loadImage("gramps.png");
  ft7_3 = loadImage("aunt.png");
  ft8_3 = loadImage("unc.png");
  ft9_3 = loadImage("cous.png");
  
  // SONS
  um_11 = new SoundFile(this, "mother.mp3");
  dois_22 = new SoundFile(this, "father.mp3");
  tres_33 = new SoundFile(this, "sister.mp3");
  quatro_44 = new SoundFile(this, "brother.mp3");
  cinco_55 = new SoundFile(this, "grandmother.mp3");
  seis_66 = new SoundFile(this, "grandfather.mp3");
  sete_77 = new SoundFile(this, "aunt.mp3");
  oito_88 = new SoundFile(this, "uncle.mp3");
  nove_99 = new SoundFile(this, "cousin.mp3");

  bt1_3 = new PButton3(400, 180, 150, 50, tebt1);
  bt2_3 = new PButton3(720, 180, 150, 50, tebt2);
  bt3_3 = new PButton3(1030, 180, 150, 50, tebt3);
  bt4_3 = new PButton3(400, 390, 150, 50, tebt4);
  bt5_3 = new PButton3(720, 390, 150, 50, tebt5);
  bt6_3 = new PButton3(1030, 390, 150, 50, tebt6);
  bt7_3 = new PButton3(400, 600, 150, 50, tebt7);
  bt8_3 = new PButton3(720, 600, 150, 50, tebt8);
  bt9_3 = new PButton3(1030, 600, 150, 50, tebt9);
  
  botao1 = new PButton(50, 50, "Animais");
  botao2 = new PButton(50, 630, "Exercícios");
  botao3 = new PButton(50, 250, "Números");
  botao4 = new PButton(50, 350, "Família");
}

void draw3() {
  background(255);

  // FUNDO
  fill(238, 238, 238);
  noStroke();
  rect(10, 10, 290, 700, 28);
  rect(310, 10, 960, 700, 28);
  
  // BOTA AS IMGS
  image(ft1_3, 400, 40, 150, 150);
  image(ft2_3, 720, 35, 150, 150);
  image(ft3_3, 1030, 40, 150, 150);
  image(ft4_3, 400, 250, 150,150);
  image(ft5_3, 720, 250, 150, 150);
  image(ft6_3, 1030, 250, 150, 150);
  image(ft7_3, 400, 450, 150,150);
  image(ft8_3, 715, 450, 150, 150);
  image(ft9_3, 1030, 450, 150, 150);
  
  botao1.display();
  botao2.display();
  botao3.display();
  botao4.display();
  botao5.display();
  
  // BOTA OS BOTOES
  bt1_3.display();
  bt2_3.display();
  bt3_3.display();
  bt4_3.display();
  bt5_3.display();
  bt6_3.display();
  bt7_3.display();
  bt8_3.display();
  bt9_3.display();
}

void mousePressed3() { 
 
if (bt1_3.isMouseOver()) {
    if (isMother) {
      bt1_3.setText("Mother");
      um_11.play();
    } else {
      bt1_3.setText("Mãe");
    }
    isMother = !isMother;
    buttonPressed = true;
  } else if (bt2_3.isMouseOver()) {
    if (isFather) {
      dois_22.play();
      bt2_3.setText("Father");
    } else {
      bt2_3.setText("Pai");
    }
    isFather = !isFather;
    buttonPressed = true;
  } else if (bt3_3.isMouseOver()) {
    if (isBrother) {
      tres_33.play();
      bt3_3.setText("Sister");
    } else {
      bt3_3.setText("Irmã");
    }
    isBrother = !isBrother;
    buttonPressed = true;
  } else if (bt4_3.isMouseOver()) {
    if (isSister) {
      quatro_44.play();
      bt4_3.setText("Brother");
    } else {
      bt4_3.setText("Irmão");
    }
    isSister = !isSister;
    buttonPressed = true;
  } else if (bt5_3.isMouseOver()) {
    if (isGrandma) {
      cinco_55.play();
      bt5_3.setText("Grandmother");
    } else {
      bt5_3.setText("Avó");
    }
    isGrandma = !isGrandma;
    buttonPressed = true;
  } else if (bt6_3.isMouseOver()) {
    if (isGrandpa) {
      seis_66.play();
      bt6_3.setText("Grandfather");
    } else {
      bt6_3.setText("Avô");
    }
    isGrandpa = !isGrandpa;
    buttonPressed = true;
  } else if (bt7_3.isMouseOver()) {
    if (isUncle) {
      sete_77.play();
      bt7_3.setText("Aunt");
    } else {
      bt7_3.setText("Tia");
    }
    isUncle = !isUncle;
    buttonPressed = true;
  } else if (bt8_3.isMouseOver()) {
    if (isAunt) {
      oito_88.play();
      bt8_3.setText("Uncle");
    } else {
      bt8_3.setText("Tio");
    }
    isAunt = !isAunt;
    buttonPressed = true;
  } else if (bt9_3.isMouseOver()) {
    if (isCousin) {
      nove_99.play();
      bt9_3.setText("Cousin");
    } else {
      bt9_3.setText("Prima");
    }
    isCousin = !isCousin;
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

class PButton3 {
  float x, y, w, h;
  String text;
  
  PButton3(float x, float y, float w, float h, String text) {
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
