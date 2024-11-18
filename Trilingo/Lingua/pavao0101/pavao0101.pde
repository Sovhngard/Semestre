import processing.video.*;
import processing.sound.*;
PFont f2;

int telaAtual = 0;

void setup() {
  size(1280, 720);
  f2 = createFont("San Francisco", 16);
  textFont(f2);

  botao1 = new PButton(50, 50, "Animais");
  botao2 = new PButton(50, 630, "Exercícios");
  botao3 = new PButton(50, 250, "Números");
  botao4 = new PButton(50, 350, "Família");
  botao5 = new PButton(50, 150, "Cores");
  
}

void draw() {
  background(255);

  if (telaAtual == 0) {
    // Tela principal
    fill(238, 238, 238);
    noStroke();
    rect(10, 10, 290, 700, 28);
    rect(310, 10, 960, 700, 28);
    
    botao1.display();
    botao2.display();
    botao3.display();
    botao4.display();
    botao5.display();
    
  } else if (telaAtual == 1) {
    draw1();
  } else if (telaAtual == 2) {
    draw_exer();
  } else if (telaAtual == 3) {
    draw_num();
  } else if (telaAtual == 4) {
    draw3();
  } else if (telaAtual == 5) {
    draw5();
  }
}


void funcao01() {
  setup2();
  draw1();
  mousePressed2();
}

void funcao02() {
  
  setup_exer();
  draw_exer();
  mousePressed_exer();
}

void funcao03() {

  setup_num();
  draw_num();
  mousePressed_num();
}

void funcao04() {

  setup3();
  draw3();
  mousePressed3();
}

void funcao05() {

  setup5();
  draw5();
  mousePressed5();
}

void mousePressed() {
  for (int i = 0; i < 3; i++) {
     int x = i * (buttonWidth + 20) + 450;
     int y = height - 100;
  }

  if (telaAtual == 0) {
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


class PButton {
  float x, y;
  String label;
  float w = 200;
  float h = 50;

  PButton(float x, float y, String label) {
    this.x = x;
    this.y = y;
    this.label = label;
  }

  void display() {
    fill(255);
    rect(x, y, w, h, 20);
    fill(0);
    textAlign(CENTER, CENTER);
    text(label, x + w / 2, y + h / 2);
  }

  boolean isClicked() {
    return mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + h;
  }
}
