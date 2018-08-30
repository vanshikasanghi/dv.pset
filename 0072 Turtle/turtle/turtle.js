var img;
function preload()
{
  img = loadImage('turtle.jpg');
}
function setup()
{
  createCanvas(800,800);
  image(img,400,400);
}
function keypPressed()
{
  if(keyCode == LEFT_ARROW)
  {
    image(img,300,400);
  }
  else if(keyCode == RIGHT_ARROW)
  {
    image(img,500,400);
  }
  else
  {
  }
  if(keyCode == UP_ARROW)
  {
    image(img,400,300);
  }
  else if(keyCode == DOWN_ARROW)
  {
    image(img,400,500)
  }
  else
  {
  }
}
