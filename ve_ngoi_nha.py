import turtle

turtle.bgcolor("cyan")
turtle.speed(10)

turtle.pensize(3)

turtle.fillcolor("blue")
turtle.begin_fill()

turtle.goto(0,-200)
turtle.goto(-150,-200)
turtle.goto(-150,0)
turtle.goto(0,0)
    
turtle.end_fill()

#mai nha
turtle.fillcolor("pink")
turtle.begin_fill()
    
turtle.goto(-75, 60)
turtle.goto(-150, 0)
turtle.goto(0, 0)

turtle.end_fill()

#trai nha
turtle.fillcolor("yellow")
turtle.begin_fill()

turtle.goto(0, -200)
turtle.goto(200,-100)
turtle.goto(200, 100)
turtle.goto(0, 0)

turtle.end_fill()

#mai nha
turtle.fillcolor("orange")
turtle.begin_fill()

turtle.goto(-75, 60)
turtle.goto(125,160)
turtle.goto(200, 100)
turtle.goto(0, 0)
    
turtle.end_fill()

#cua truoc nha
turtle.penup()
turtle.goto(-45, -200)
turtle.pendown()
    
turtle.fillcolor("green")
turtle.begin_fill()

turtle.goto(-45, -100)
turtle.goto(-105,-100)
turtle.goto(-105,-200)
turtle.goto(-45,-200)
    
turtle.end_fill()   
    
#cua trai nha
turtle.penup()
turtle.goto(50, -150)
turtle.pendown()
    
turtle.fillcolor("white")
turtle.begin_fill()

turtle.left(30)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)

turtle.end_fill()   

 #tang 1 cay
turtle.penup()
turtle.goto(350, 30)
turtle.pendown()
    
turtle.fillcolor("green")
turtle.begin_fill()

turtle.goto(440, -60)
turtle.goto(260,-60)
turtle.goto(350,30)

turtle.end_fill() 

#tang 2 cay
turtle.penup()
turtle.goto(350, 100)
turtle.pendown()
    
turtle.fillcolor("green")
turtle.begin_fill()

turtle.goto(420, 30)
turtle.goto(280,30)
turtle.goto(350,100)

turtle.end_fill() 
 
#tang 3 cay
turtle.penup()
turtle.goto(350, 100)
turtle.pendown()
    
turtle.fillcolor("green")
turtle.begin_fill()

turtle.goto(400, 100)
turtle.goto(350,150)
turtle.goto(300,100)
turtle.goto(350,100)
    
turtle.end_fill()      
       
#goc cay
turtle.penup()
turtle.goto(350, -60)
turtle.pendown()
    
turtle.fillcolor("brown")
turtle.begin_fill()

turtle.goto(360, -60)
turtle.goto(360,-110)
turtle.goto(340,-110)
turtle.goto(340,-60)
turtle.goto(350,-60)


turtle.end_fill()        
    
#mat troi

turtle.penup()
turtle.goto(-250, 300)
turtle.pendown()
    
turtle.fillcolor("yellow")
turtle.begin_fill()

turtle.circle(40)

turtle.end_fill()      
    
#tia nang

turtle.penup()
turtle.goto(-210, 260)
turtle.pendown()
    

turtle.forward(50)

turtle.penup()
turtle.goto(-170, 300)
turtle.pendown()

turtle.left(90)
turtle.forward(50)

turtle.penup()
turtle.goto(-210, 340)
turtle.pendown()

turtle.left(90)
turtle.forward(50)

turtle.penup()
turtle.goto(-250, 300)
turtle.pendown()

turtle.left(90)
turtle.forward(50)

       
    
turtle.done()