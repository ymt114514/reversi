# reversi
int board[][] = new int[10][10];
int bw;
int pass,side;
int num0,numB,numW;

void setup(){
size(400, 400);
side=height/8;
startPosition();
showBoard();
}

void draw(){
passCheck();
}

void mousePressed(){
int i = floor(mouseX/side +1);
int j = floor(mouseY/side +1);

if (validMove(i,j)){
movePiece(i,j);
bw = -bw;
showBoard();
}
}

void keyPressed() {
if (key=='r') {
startPosition();
showBoard();
}
}

void startPosition() {
bw=1;

for (int i=0;i<=9;i++){
for (int j=0;j<=9;j++){
if ((i==4&&j==5) || (i==5&&j==4)) {board[i][j]=1;}
else if ((i==4&&j==4) || (i==5&&j==5)) {board[i][j]=-1;}
else if (i==0||j==0||i==9||j==9) {board[i][j]=2;}
else {board[i][j]=0;}
}
}
}

void showBoard(){

background(0,160,0);
stroke(0);
for (int i=1;i<=8;i++){
line(iside,0, iside,height);
line(0,iside, 8side,i*side);
}

noStroke();
num0=numB=numW=0;
for (int i=1;i<=8;i++){
for (int j=1;j<=8;j++){
if (board[i][j]==1){ //黒(1)
fill(0);
ellipse((i-1)side +side/2, (j-1)side +side/2, 0.9side, 0.9side);
numB++;
}
else if (board[i][j]==-1){(-1)
fill(255);
ellipse((i-1)side +side/2, (j-1)side +side/2, 0.9side, 0.9side);
numW++;
}
else if (validMove(i,j)){
pass=0;
num0++;

    
    if(bw==-1){fill(255, 255, 255, 200);}
    else if(bw==1){fill(0, 0, 0, 200);}
    ellipse((i-1)*side +side/2, (j-1)*side +side/2, side/3, side/3);
  }
}
}
}
boolean validMove(int i, int j){
if(i<1||8<i || j<1||8<j){return false;}
if (board[i][j]!=0) {return false;}
int ri, rj;
for (int di=-1; di<=1; di++)
for (int dj=-1; dj<=1; dj++)
ri=i+di; rj=j+dj;

  while (board[ri][rj]==-bw){
    ri+=di;  rj+=dj; 
  
    if (board[ri][rj]==bw){return true;} 
  }
}
}

return false;
}

void movePiece(int i, int j){
board[i][j] = bw;

int ri, rj;
for (int di=-1; di<=1; di++){
for (int dj=-1; dj<=1; dj++){
ri=i+di; rj=j+dj;

  while (board[ri][rj]==-bw){
    ri+=di;  rj+=dj;
    
   
    if (board[ri][rj]==bw){
      ri-=di; rj-=dj; 
      
      while (!(i==ri&&j==rj)){
        board[ri][rj] = bw; 
        ri-=di; rj-=dj;
      }
    }
  }
}
}
}
void passCheck(){
if (num0==0 && pass<=1){
pass++;
bw = -bw;
showBoard();
}

if (pass==2){
fill(255,0,0);
textSize(1.0*side);
textAlign(CENTER);

if (numW<numB){text("Black win", width/2,height/2);} 
else if (numB<numW){text("White win", width/2,height/2);} 
else {text("Draw", width/2,height/2);}
}
}

