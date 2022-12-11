import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.bgcolor('#000000')
  
for i in range(180):
  t.speed(0) 
  t.color('#A555EC')
  t.circle(190 - i, 90)
  t.left(90)
  t.color('#62B6B7')
  t.circle(190 - i, 90)
  t.left(18)