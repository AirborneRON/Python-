#idea is to create lines that using all the data will create a #circle of results, and those with higher grades will have a longer #lines which anything ober the 40 pass rate will change colour randomly.
Markslist = [52,47,57,49,59,62,44,76,52,52,44,59,59,79,59,42,57,48,80,43,72,74,59,44,57,55,49,54,54] 

from graphics import *
file = open("visualisation_list")
Vlist = file.read()
file.close()


window = GraphWin("Visualisation", 1100, 700)

mark = Markslist


sline = Line(Point(20,20),Point(20,620))
sline.setWidth(2)
sline.draw(window)

bline = Line(Point(20,620),Point(1020,620))
bline.setWidth(2)
bline.draw(window)


    # couldn't get it to draw all the box's in a loop which was annoying and i know bad code 

for item in mark:
    print mark
    bar = Rectangle(Point(20,30),Point(mark[0]*10,40))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    
    bar = Rectangle(Point(20,50),Point(mark[1]*10,60))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 70),Point(mark[2]*10,80))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(20,90),Point(mark[3]*10,100))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 110),Point(mark[4]*10,120))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(20,130),Point(mark[5]*10,140))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 150),Point(mark[6]*10,160))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(20,170),Point(mark[7]*10,180))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 190),Point(mark[8]*10,200))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    
    bar = Rectangle(Point(20,210),Point(mark[9]*10,220))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 230),Point(mark[10]*10,240))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(20,250),Point(mark[11]*10,260))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 270),Point(mark[12]*10,280))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(20,290),Point(mark[13]*10,300))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 310),Point(mark[14]*10,320))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(20,330),Point(mark[15]*10,340))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 350),Point(mark[16]*10,360))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    
    bar = Rectangle(Point(20,370),Point(mark[17]*10,380))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 390),Point(mark[18]*10,400))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(20,410),Point(mark[19]*10,420))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 430),Point(mark[20]*10,440))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(20,450),Point(mark[21]*10,460))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 470),Point(mark[22]*10,480))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(20,490),Point(mark[23]*10,500))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 510),Point(mark[24]*10,520))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    
    bar = Rectangle(Point(20,530),Point(mark[25]*10,540))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 550),Point(mark[26]*10,560))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(20,570),Point(mark[27]*10,580))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(20, 590),Point(mark[28]*10,600))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    pline = Line(Point(420,20),Point(420,620))
    pline.setOutline('yellow')
    pline.setWidth(1)
    pline.draw(window)
    
    window.setBackground(color_rgb(90,202,234))
    
    
    
#above passLine
    
    bar = Rectangle(Point(420,30),Point(mark[0]*10,40))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    
    bar = Rectangle(Point(420,50),Point(mark[1]*10,60))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 70),Point(mark[2]*10,80))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(420,90),Point(mark[3]*10,100))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 110),Point(mark[4]*10,120))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(420,130),Point(mark[5]*10,140))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 150),Point(mark[6]*10,160))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(420,170),Point(mark[7]*10,180))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 190),Point(mark[8]*10,200))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    
    bar = Rectangle(Point(420,210),Point(mark[9]*10,220))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 230),Point(mark[10]*10,240))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(420,250),Point(mark[11]*10,260))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 270),Point(mark[12]*10,280))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(420,290),Point(mark[13]*10,300))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 310),Point(mark[14]*10,320))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(420,330),Point(mark[15]*10,340))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 350),Point(mark[16]*10,360))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    
    bar = Rectangle(Point(420,370),Point(mark[17]*10,380))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 390),Point(mark[18]*10,400))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(420,410),Point(mark[19]*10,420))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 430),Point(mark[20]*10,440))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(420,450),Point(mark[21]*10,460))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 470),Point(mark[22]*10,480))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(420,490),Point(mark[23]*10,500))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 510),Point(mark[24]*10,520))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    
    bar = Rectangle(Point(420,530),Point(mark[25]*10,540))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 550),Point(mark[26]*10,560))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)
    
    bar = Rectangle(Point(420,570),Point(mark[27]*10,580))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)

    bar = Rectangle(Point(420, 590),Point(mark[28]*10,600))
    bar.setFill(color_rgb(255,200,200))
    bar.setOutline(color_rgb(255,20,20))
    bar.draw(window)




    window.getMouse()
    