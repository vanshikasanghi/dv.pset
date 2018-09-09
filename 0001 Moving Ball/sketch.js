function setup()
{
  createCanvas(1000,1000);
  strokeWeight(1);
}
var x=500, speed = 10;
function draw()
 { 
    clear();
    
    x = x + speed;
    ellipse(x,500,100,100);

    if(x>600)
    {
      x = x + speed
      speed = speed - 1;
    }
    else if (x<200)
    {
      x = x + speed
      speed = speed + 1;
    }
}