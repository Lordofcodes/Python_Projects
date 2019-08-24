import turtle
p=turtle.Pen()
p.up()
p.goto(100,0)
p.down()

color=( "#FF9933","green")
for i in color:
    p.left(90)
    p.color(i)
    
    p.width(100)
  
    p.circle(200,180)

   
    p.right(90)

    
p.up()
p.goto(-103,0)
p.down()
p.width(100)
p.color("blue")
p.circle(5)
p.width(3)

for i in range(25):
    p.fd(150)
    p.bk(150)
    p.left(15)
p.up()
p.goto(-450,-320)
p.right(15)    
p.write("Happy Independence Day !", move=False, align="left", font=("Arial", 50, "normal"))
p.down()

color=("#FF9933","green")
for i in color:
    p.color(i)
    p.width(10)
    p.fd(380)
