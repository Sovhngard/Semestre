import processing.video.*;
import processing.sound.*;
String texto1 = "";

// Variáveis para os botões
int buttonWidth = 200;
int buttonHeight = 50;
int correctButtonIndex = 1;  

PButton botao1, botao2, botao3, botao4, botao5;


String butantan1 = "Vaca, cavalo, porco";
String butantan2 = "Pássaro, pato, vaca";
String butantan3 = "Cavalo, pássaro, vaca";

// cores botoes antigos
color correctColor = color(0, 255, 0);
color defaultColor = color(200, 200, 200);

Movie video1;
Movie video2;
Movie video3;
Movie video4;
Movie video5;
Movie currentVideo;

void setup_exer() {
  size(1280, 720);
  PFont f = createFont("San Francisco", 16);
  textFont(f);

  video1 = new Movie(this, "farm.mov");
  video2 = new Movie(this, "fam.mov");
  video3 = new Movie(this, "num.mov");
  video4 = new Movie(this, "cor.mov");
  video5 = new Movie(this, "vidro_fim.mov");

  errou = new SoundFile(this, "wrong.mp3");
  nice = new SoundFile(this, "correct.mp3");

  currentVideo = video1;
  currentVideo.loop(); 
  
  botao1 = new PButton(50, 50, "Animais");
  botao2 = new PButton(50, 630, "Exercícios");
  botao3 = new PButton(50, 250, "Números");
  botao4 = new PButton(50, 350, "Família");
  botao5 = new PButton(50, 150, "Cores");
  
  butano1 = new PButton3(320, 600, 300, 50, butantan1);
  butano2 = new PButton3(635, 600, 300, 50, butantan2);
  butano3 = new PButton3(950, 600, 300, 50, butantan3);

  texto1 = "Quais os animais que o Sr. MacDonald possui em sua fazenda?";
}

void draw_exer() {
  background(255);

  // INTERFACE
  fill(238, 238, 238);
  noStroke();
  rect(10, 10, 290, 700, 28);
  rect(310, 10, 960, 700, 28);

  // RETANGULO VIDEO
  rect(430, 60, 720, 400, 0);

  // VIDEO FUNDO
  if (currentVideo.available()) {
    currentVideo.read();  //bag p carregar os frames 
  }
  image(currentVideo, 430, 60, 720, 400); //desneha video fundo

  fill(0);
  stroke(255);
  strokeWeight(5);
  text(texto1, width / 2 - 90, height - 200, 500, 40);

  // Exibir botões
  botao1.display();
  botao2.display();
  botao3.display();
  botao4.display();
  botao5.display();

  butano1.display();
  butano2.display();
  butano3.display();
}

void mousePressed_exer() {

  if (butano1.isMouseOver() && correctButtonIndex == 1) {
    nice.play();
    switchVideo_exer(); 
  } else if (butano2.isMouseOver() && correctButtonIndex == 2) {
    nice.play();
    switchVideo_exer();
  } else if (butano3.isMouseOver() && correctButtonIndex == 3) {
    nice.play();
    switchVideo_exer();
  } else {
    errou.play(); 
  }

  //botows pra ter navegar nas telas do lado
  if (telaAtual != 0) {
    if (botao1.isClicked()) {
      video1.stop();
      video2.stop();
      video3.stop();
      video4.stop();
      video5.stop();
      setup2();
      telaAtual = 1;
    } else if (botao2.isClicked()) {
      video1.stop();
      video2.stop();
      video3.stop();
      video4.stop();
      video5.stop();
      setup_exer();
      telaAtual = 2;
    } else if (botao3.isClicked()) {
      video1.stop();
      video2.stop();
      video3.stop();
      video4.stop();
      video5.stop();
      setup_num();
      telaAtual = 3;
    } else if (botao4.isClicked()) {
      video1.stop();
      video2.stop();
      video3.stop();
      video4.stop();
      video5.stop();
      setup3();
      telaAtual = 4;
    } else if (botao5.isClicked()) {
      video1.stop();
      video2.stop();
      video3.stop();
      video4.stop();
      video5.stop();
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


void switchVideo_exer() {
  //para o video q ta tocando
  currentVideo.stop();

  // troca os videos
  if (currentVideo == video1) {
    currentVideo = video2;
    texto1 = "Qual a ordem na qual os familiares foram apresentados na música?";
    butano1.setText("Irmão, irmã, mãe, pai, tio, avô");
    butano2.setText("Tio, mãe, avó, primo, pai, tia");
    butano3.setText("Irmã, tio, avó, irmão, mãe, avô");
    nice.play();
    correctButtonIndex = 1; 
  } else if (currentVideo == video2) {
    currentVideo = video3;
    texto1 = "Qual a forma correta de se falar 'número' em inglês?";
    butano1.setText("Numeric");
    butano2.setText("Number");
    butano3.setText("Numero");
    nice.play();
    correctButtonIndex = 2;
  } else if (currentVideo == video3) { 
    currentVideo = video4;
    textSize(16);
    texto1 = "Na música, as cores são apresentadas na seguinte ordem:";
    textSize(12);
    butano1.setText("Roxo, laranja, verde, preto, vermelho, marrom");
    butano2.setText("Preto, amarelo, verde, vermelho, roxo, marrom");
    butano3.setText("Azul, vermelho, verde, amarelo, laranja, roxo");
    nice.play();
    correctButtonIndex = 3;
  } else if (currentVideo == video4) {
    textSize(16);
    currentVideo = video5;
    texto1 = "Obrigado por assistir o video!";
    butano1.setText("Obirgado");
    butano2.setText("Pela");
    butano3.setText("Preferência");
  }

  // deixa o video em loop
  currentVideo.loop();
}

class PButton_exer {
  float x, y, w, h;
  String label;

  PButton_exer(float x, float y, float w, float h, String label) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.label = label;
  }

  void display() {
    fill(255);
    rect(x, y, w, h);
    fill(0);
    textAlign(CENTER, CENTER);
    text(label, x + w / 2, y + h / 2);
  }

  boolean isMouseOver() {
    return mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + h;
  }

  void setText(String newLabel) {
    label = newLabel;
  }
}
