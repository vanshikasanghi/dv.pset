function setup() 
{
  createCanvas(1000,1000);
}
var theta = 0, r1=400, r2=100, radius = 50;
var x, y;
function draw() 
{
  translate(500, 500);
  clear();
  //for elliptical nature
  x=r1*cos(theta); 
  y=r2*sin(theta);
  
  ellipse(x,y,radius,radius); //moving body
  ellipse(0,0,radius,radius); //stationery body
  
  theta = theta + PI/10;
}