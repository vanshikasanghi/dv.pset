function setup() 
{
  createCanvas (600,400);
  strokeWeight(1);
}

var x = 30, s = 10;

function draw()
{
  clear();
  x = x + s;

  ellipse(x, 200, 100, 100);
  ellipse(600-x, 200, 100, 100);

  if(x > 570)
  {
    s = 0
  }

  if( x < 30)
  {
    s = 0
  }
}