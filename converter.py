# convert.py
# IPO or program description

from graphics import *

def main():
    # create a window object
    win = GraphWin("Celsius Converter", 400, 300)

    # create text objects
    celsiusTempString =    "Celsius Temperature:   "
    fahrenheitTempString = "Fahrenheit Temperature:"

    # create Text boxes
    Text(Point(150,50), celsiusTempString).draw(win)
    Text(Point(150, 250), fahrenheitTempString).draw(win)

    # create center box
    Rectangle(Point(125, 100), Point(275, 200)).draw(win)

    # create button text
    buttonText = Text(Point(200, 150), "Convert It")
    buttonText.draw(win)

    # create input and output fields
    inputCelsiusField = Entry(Point(300, 50), 5)
    inputCelsiusField.setText("0.0")
    inputCelsiusField.draw(win)

    outputFahrenheitField = Text(Point(300, 250), "")
    outputFahrenheitField.draw(win)

    win.getMouse()

    celsiusTemperature = float(inputCelsiusField.getText())
    fahrenheit = 9.0/5.0 * celsiusTemperature + 32

    # display results
    outputFahrenheitField.setText(round(fahrenheit, 2))

    # update button text
    buttonText.setText("Quit")

    # wait for final click to end
    win.getMouse()

main()    