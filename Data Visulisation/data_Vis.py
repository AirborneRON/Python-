#idea is to create lines that using all the data will create a #circle of results, and those with higher grades will have a longer #lines which anything ober the 40 pass rate will change colour randomly.
Markslist = [52,47,57,49,59,62,44,76,52,52,44,59,59,79,59,42,57,48,80,43,72,74,59,44,57,55,49,54,54] 

from graphics import *
file = open("visualisation_list")
Vlist = file.read()
file.close()


window = GraphWin("Visualisation", 500, 500)




bar = Rectangle(Point(20,100),Point(50,400))
bar.setFill(color_rgb(200,200,200))
bar.setOutline(color_rgb(255,20,20))
bar.draw(window)


while true:
    

window.getMouse()
    