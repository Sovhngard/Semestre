import processing.video.*;
import processing.sound.*;

SoundFile sound, gal, por, cav, vac, ca, ga;
boolean buttonPressed = false;

boolean funcao1Ativa = false;
boolean funcao2Ativa = false;
boolean funcao3Ativa = false;

boolean isChicken = true; 
boolean isPig = true;  
boolean isCow = true;   
boolean isHorse = true;  
boolean isDog = true;     
boolean isCat = true;

PFont f;
String tebt12 = "Galinha";
String tebt22 = "Porco";
String tebt32 = "Vaca";
String tebt42 = "Cavalo";
String tebt52 = "Cachorro";
String tebt62 = "Gato";

PButton2 bt11, bt21, bt31, bt41, bt51, bt61;
PButton botaoVoltar2, botaoProximo2;

PImage ft1, ft2, ft3, ft4, ft5, ft6;

void setup2() {
  size(1280, 720);
  f = createFont("San Francisco", 16);
  textFont(f);

  // IMGS
  ft1 = loadImage("galinha.png");
  ft2 = loadImage("porco.png");
  ft3 = loadImage("vaca.png");
  ft4 = loadImage("cavalo.png");
  ft5 = loadImage("cachorro.png");
  ft6 = loadImage("gato.png");
  
  // MUSICAS
  gal = new SoundFile(this, "chicken.mp3");
  por = new SoundFile(this, "pig.mp3");
  cav = new SoundFile(this, "horse.mp3");
  vac = new SoundFile(this, "cow.mp3");
  ca = new SoundFile(this, "dog.mp3");
  ga = new SoundFile(this, "cat.mp3");

  botao1 = new PButton(50, 50, "Animais");
  botao2 = new PButton(50, 630, "Exercícios");
  botao3 = new PButton(50, 250, "Números");
  botao4 = new PButton(50, 350, "Família");
  botao5 = new PButton(50, 150, "Cores");

  bt11 = new PButton2(400, 240, 150, 50, tebt12);
  bt21 = new PButton2(720, 240, 150, 50, tebt22);
  bt31 = new PButton2(1030, 240, 150, 50, tebt32);
  bt41 = new PButton2(400, 570, 150, 50, tebt42);
  bt51 = new PButton2(720, 570, 150, 50, tebt52);
  bt61 = new PButton2(1030, 570, 150, 50, tebt62);
}

void draw1() {
  background(255);

  // FUNDO
  fill(238, 238, 238);
  noStroke();
  rect(10, 10, 290, 700, 28);
  rect(310, 10, 960, 700, 28);

  // MOSTRA AS IMGS
  image(ft1, 345, 50, 261, 204);
  image(ft2, 665, 50, 261, 204);
  image(ft3, 955, 25, 261, 204);
  image(ft4, 350, 350, 261, 204);
  image(ft5, 675, 390, 261, 204);
  image(ft6, 985, 390, 261, 204);

  // BOT LATERAIS
  botao1.display();
  botao2.display();
  botao3.display();
  botao4.display();
  botao5.display();

  // BOT ANIMAIS
  bt11.display();
  bt21.display();
  bt31.display();
  bt41.display();
  bt51.display();
  bt61.display(); 
}

void mousePressed2() {

if (bt11.isMouseOver()) {
    if (isChicken) {
      bt11.setText("Chicken");
      gal.play();
    } else {
      bt11.setText("Galinha");
    }
    isChicken = !isChicken; 
    buttonPressed = true;
  } else if (bt21.isMouseOver()) {
    if (isPig) {
      por.play();
      bt21.setText("Pig");
    } else {
      bt21.setText("Porco");
    }
    isPig = !isPig;
    buttonPressed = true;
  } else if (bt31.isMouseOver()) {
    if (isCow) {
      vac.play();
      bt31.setText("Cow");
    } else {
      bt31.setText("Vaca");
    }
    isCow = !isCow;
    buttonPressed = true;
  } else if (bt41.isMouseOver()) {
    if (isHorse) {
      cav.play();
      bt41.setText("Horse");
    } else {
      bt41.setText("Cavalo");
    }
    isHorse = !isHorse;
    buttonPressed = true;
  } else if (bt51.isMouseOver()) {
    if (isDog) {
      ca.play();
      bt51.setText("Dog");
    } else {
      bt51.setText("Cachorro");
    }
    isDog = !isDog;
    buttonPressed = true;
  } else if (bt61.isMouseOver()) {
    if (isCat) {
      ga.play();
      bt61.setText("Cat");
    } else {
      bt61.setText("Gato");
    }
    isCat = !isCat;
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

class PButton2 {
  float x, y, w, h;
  String text;

  PButton2(float x, float y, float w, float h, String text) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.text = text;
  }

  void display() {
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
