function setup() 
{
  createCanvas(800,800);
}
var theta = 0, r = 200, radius = 200;
var x, y;
function draw() 
{
  translate(400,400);
  clear();
  //for circular nature
  x=r*cos(theta); 
  y=r*sin(theta);
  
  ellipse(x,y,radius,radius); //moving body
  
  theta = theta + PI/40;
}
