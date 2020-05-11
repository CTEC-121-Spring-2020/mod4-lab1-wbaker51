"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import *

def main():
    '''
    win = GraphWin("Title", 600, 300)

    p = Point(100,200)
    x = p.getX()
    y = p.getY()
    print("x and y:", x, y)

    input()
    '''
    win = GraphWin("Bill's Window", 600, 600)

    p1 = Point(50,50)
    p2 = Point(100,100)
    r1 = Rectangle(p1, p2)
    r1.draw(win)

    r2 = Rectangle(Point(200,200), Point(250,250))
    r2.draw(win)

    input()

main()    