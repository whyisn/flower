import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.bgcolor('#000000')
t.speed(100) 
col = ('#FAF8F1','#A555EC','#62B6B7','#FB2576','#62B6B7','#E6DDC4')

for n in range(8):
  for x in range(8):
    t.speed(x+10)
    for i in range(2):
      t.pensize(2)
      t.circle(8+n*20, 90)
      t.lt(90)
    t.lt(45)
  t.pencolor(col[n%4])
