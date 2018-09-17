var img;
function preload()
{
  img = loadImage('turtle.jpg');
}
function setup()
{
  createCanvas(4000,4000);
  image(img,400,400);
}
function keypPressed()
{
  if(keyCode == LEFT_ARROW)
  {
    x = 300;
    image(img,x,400);
    x = x - 20;
  }
  else if(keyCode == RIGHT_ARROW)
  {
    x = 500;
    image(img,x,400);
    x = x + 20;
  }
  else
  {
  }
  if(keyCode == UP_ARROW)
  {
    y = 300;
    image(img,400,y);
    y = y - 20;
  }
  else if(keyCode == DOWN_ARROW)
  {
    y = 500;
    image(img,400,y);
    y = y + 20;
  }
  else
  {
  }
}
