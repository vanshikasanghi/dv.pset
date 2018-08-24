function setup()
{
  createCanvas(800,800);
  noFill();
  strokeWeight(2);
}
var w=800, x=100,speed=10;

function draw()
{
  translate(0,200);
   clear();
   x = x+speed;
   ellipse(x,200,100,100);
   //x=x+speed;
   if(x<1 || x>700)
    {
      speed = speed - 1;
    }
    if(x<1)
    {
      speed=speed+1;
    }
    if(x>799)
    {
      speed= speed-1;
    }
}
