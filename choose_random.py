import random
def getcolor():
    color=['Snow','Snow2','Snow3','Snow4','GhostWhite','WhiteSmoke','Gainsboro','FloralWhite','OldLace','Linen','AntiqueWhite','AntiqueWhite2','AntiqueWhite3','AntiqueWhite4','PapayaWhip','BlanchedAlmond','Bisque','Bisque2','Bisque3','Bisque4','PeachPuff','PeachPuff2','PeachPuff3','PeachPuff4','NavajoWhite','Moccasin','Cornsilk','Cornsilk2','Cornsilk3','Cornsilk4','Ivory','Ivory2','Ivory3','Ivory4','LemonChiffon','Seashell','Seashell2','Seashell3','Seashell4','Honeydew','Honeydew2','Honeydew3','Honeydew4','MintCream','Azure','AliceBlue','Lavender','LavenderBlush','MistyRose','White','Black','DarkSlateGray','DimGray','SlateGray','LightSlateGray','Gray','LightGray','MidnightBlue','Navy','CornflowerBlue','DarkSlateBlue','SlateBlue','MediumSlateBlue','LightSlateBlue','MediumBlue','RoyalBlue','Blue','DodgerBlue','DeepSkyBlue','SkyBlue','LightSkyBlue','SteelBlue','LightSteelBlue','LightBlue','PowderBlue','PaleTurquoise','DarkTurquoise','MediumTurquoise','Turquoise','Cyan','LightCyan','CadetBlue','MediumAquamarine','Aquamarine','DarkGreen','DarkOliveGreen','DarkSeaGreen','SeaGreen','MediumSeaGreen','LightSeaGreen','PaleGreen','SpringGreen','LawnGreen','Chartreuse','MediumSpringGreen','GreenYellow','LimeGreen','YellowGreen','ForestGreen','OliveDrab','DarkKhaki','Khaki','PaleGoldenrod','LightGoldenrodYellow','LightYellow','Yellow','Gold','LightGoldenrod','Goldenrod','DarkGoldenrod','RosyBrown','IndianRed','SaddleBrown','Sienna','Peru','Burlywood','Beige','Wheat','SandyBrown','Tan','Chocolate','Firebrick','Brown','DarkSalmon','Salmon','LightSalmon','Orange','DarkOrange','Coral','LightCoral','Tomato','OrangeRed','Red','HotPink','DeepPink','Pink','LightPink','PaleVioletRed','Maroon','MediumVioletRed','VioletRed','Violet','Plum','Orchid','MediumOrchid','DarkOrchid','DarkViolet','BlueViolet','Purple','MediumPurple','Thistle']
    x=random.choice(color)
    print(x)
    color.remove(x)
    return x

from turtle import Turtle, Screen
from random import randint


from tkinter import *
from random import *

dataValue = 0
def getData():
    try:
        global dataValue
        dataValue = int(inputBox.get())
        window.destroy()
    except:
        popUp = Tk()
        popUpLabel = Label(popUp, text="Invalid Input")
        popUpLabel.pack()


window = Tk()
window.title("Final Project")
topFrame = Frame(window)
bottomFrame = Frame(window)
header = Label(topFrame, text="Please enter the number of most frequent letters that you want to see")
submitButton = Button(bottomFrame, text="Submit", command=getData)
inputBox = Entry(bottomFrame)

topFrame.pack(side=TOP)
bottomFrame.pack(side=BOTTOM)
header.pack()
submitButton.grid(row=0, column=1)
inputBox.grid(row=0, column=0)
window.mainloop()

with open("private.txt", "r") as words:
    frequency = {}
    total = 0
    contents = words.read().lower()
    words.seek(0);
    print(words.readlines())
    for char in contents:
        total += 1
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1

probabilities = {}
for key in frequency:
    probabilities[key] = (frequency[key]/total)

def extractMax():
    maxValue = 0
    maxKey = ""
    for key in probabilities:
        if probabilities[key] > maxValue:
            maxValue = probabilities[key]
            maxKey = key
    probabilities[maxKey] = 0
    return maxKey, maxValue

if dataValue > len(probabilities):
    dataValue = len(probabilities)

listMax = {}
for i in range(0, dataValue):
    maxKey, maxValue = extractMax()
    listMax[maxKey] = maxValue






colors=['Snow','Snow2','Snow3','Snow4','GhostWhite','WhiteSmoke','Gainsboro','FloralWhite','OldLace','Linen','AntiqueWhite','AntiqueWhite2','AntiqueWhite3','AntiqueWhite4','PapayaWhip','BlanchedAlmond','Bisque','Bisque2','Bisque3','Bisque4','PeachPuff','PeachPuff2','PeachPuff3','PeachPuff4','NavajoWhite','Moccasin','Cornsilk','Cornsilk2','Cornsilk3','Cornsilk4','Ivory','Ivory2','Ivory3','Ivory4','LemonChiffon','Seashell','Seashell2','Seashell3','Seashell4','Honeydew','Honeydew2','Honeydew3','Honeydew4','MintCream','Azure','AliceBlue','Lavender','LavenderBlush','MistyRose','White','Black','DarkSlateGray','DimGray','SlateGray','LightSlateGray','Gray','LightGray','MidnightBlue','Navy','CornflowerBlue','DarkSlateBlue','SlateBlue','MediumSlateBlue','LightSlateBlue','MediumBlue','RoyalBlue','Blue','DodgerBlue','DeepSkyBlue','SkyBlue','LightSkyBlue','SteelBlue','LightSteelBlue','LightBlue','PowderBlue','PaleTurquoise','DarkTurquoise','MediumTurquoise','Turquoise','Cyan','LightCyan','CadetBlue','MediumAquamarine','Aquamarine','DarkGreen','DarkOliveGreen','DarkSeaGreen','SeaGreen','MediumSeaGreen','LightSeaGreen','PaleGreen','SpringGreen','LawnGreen','Chartreuse','MediumSpringGreen','GreenYellow','LimeGreen','YellowGreen','ForestGreen','OliveDrab','DarkKhaki','Khaki','PaleGoldenrod','LightGoldenrodYellow','LightYellow','Yellow','Gold','LightGoldenrod','Goldenrod','DarkGoldenrod','RosyBrown','IndianRed','SaddleBrown','Sienna','Peru','Burlywood','Beige','Wheat','SandyBrown','Tan','Chocolate','Firebrick','Brown','DarkSalmon','Salmon','LightSalmon','Orange','DarkOrange','Coral','LightCoral','Tomato','OrangeRed','Red','HotPink','DeepPink','Pink','LightPink','PaleVioletRed','Maroon','MediumVioletRed','VioletRed','Violet','Plum','Orchid','MediumOrchid','DarkOrchid','DarkViolet','BlueViolet','Purple','MediumPurple','Thistle']


def getColor():
    global colors
    rand = randint(0,150)
    color="";
    rand = randint(0,150-i)
    color = colors[rand]
    colors.remove(color)
    return color


radius=200
LABEL_RADIUS =radius*1.2
FONT=("Ariel",18, "bold")

# The pie slices

baker = Turtle()
baker.penup()
baker.sety(-radius)
baker.pendown()
i=0
for key in listMax:
    actualcolor=getColor()
    baker.fillcolor(actualcolor)
    i=i+1
    baker.begin_fill()
    baker.circle(radius, listMax[key] * 360)
    position = baker.position()
    baker.goto(0, 0)
    baker.end_fill()
    baker.setposition(position)

# The labels
baker.penup()
baker.sety(-LABEL_RADIUS)

for key in listMax:
    baker.circle(LABEL_RADIUS, listMax[key] * 360/ 2)
    baker.write(key, align="center", font=FONT)
    baker.circle(LABEL_RADIUS, listMax[key] * 360/ 2)

baker.hideturtle()

screen = Screen()
screen.exitonclick()