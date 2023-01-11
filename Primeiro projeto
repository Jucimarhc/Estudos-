// variavel bolinha
let xBolinha = 300;
let yBolinha = 200;
let diametro = 15;
let raio = diametro /2 ;
// velocidade Bolinha
let XBolinha = 6;
let YBolinha = 6;

//variavel raquete 
let xRaquete = 5;
let yRaquete = 150;
//comprimento raquete
let cRaquete = 10;
// altura raquete
let aRaquete = 90 ;
let colidiu = false;
//raquete openente
let xRaqueteO = 585;
let yRaqueteO = 150;
let VelocidadeyO;
//placar do jogo
let meuspontos = 0;
let pontosoponente = 0;
//sons do jogo 
let raquetada;
let trilha;
let ponto ;

function preload(){
  trilha= loadSound("trilha.mp3");
  ponto = loadSound("ponto.mp3");
  raquetada= loadSound("raquetada.mp3");
}


function setup() {
  createCanvas(600, 400);
  trilha.loop();
}

function draw() {
  background(0);
  bolinha();
  raquete(xRaquete,yRaquete);
  raquete(xRaqueteO,yRaqueteO);
  movimentobolinha();
  colisaobolinha();
  movimentotaquete();
  colisaoraquete(xRaquete,yRaquete);
  colisaoraquete(xRaqueteO,yRaqueteO);
  movimentaraqueteo();
  placar();
  contagem();
  
}
function raquete(x,y){
  rect(x,y,cRaquete,aRaquete );
}

function bolinha(){
   circle(xBolinha, yBolinha, diametro);
}
function movimentobolinha(){
   xBolinha += XBolinha;
  yBolinha += YBolinha;
}
function colisaobolinha (){
  if(xBolinha + raio > width || xBolinha - raio < 0){
    XBolinha *=-1
        }
  if(yBolinha + raio > height ||yBolinha - raio < 0){
    YBolinha *= -1
    
    }
}
function movimentotaquete(){
  if(keyIsDown(UP_ARROW)){
    yRaquete -= 10;
  }
  if(keyIsDown(DOWN_ARROW)){
    yRaquete += 10;
  }
}
function colisaoraquete(x,y){
 colidiu = collideRectCircle(x, y,cRaquete,aRaquete, xBolinha, yBolinha,raio);
  if(colidiu){
    XBolinha *= -1;
  raquetada.play();
  }
}
  

function movimentaraqueteo(){
    if(keyIsDown(87)){
    yRaqueteO -= 10;
  }
  if(keyIsDown(83)){
    yRaqueteO += 10;
  }
} 

function placar(){
  stroke(255);
  textAlign(CENTER);
  textSize(16);
  fill(color(255 ,140 , 0));
  rect(150,10,40,20);
  fill(255);
  text(meuspontos , 170 ,26);
  fill(color(255 ,140 , 0));
  rect(450, 10, 40, 20);
  fill(255);
  text(pontosoponente, 470 , 26);
}

function contagem(){
  if(xBolinha > 590){
    meuspontos += 1;
    ponto.play();
  }
  if (xBolinha < 10){
    pontosoponente += 1;
    ponto.play();
  }
}
