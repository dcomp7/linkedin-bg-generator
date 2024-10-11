import random
from PIL import Image, ImageDraw, ImageFont

def createLinkedInBackground():
    width, height = 1584, 396
    image = generateRandomBackground(width, height)
    draw = ImageDraw.Draw(image)
    drawAsciiArt(draw, width, height)
    saveImage(image, "output.png")

def generateRandomBackground(width, height):
    backgroundColor = 0,0,0
    return Image.new("RGB", (width, height), backgroundColor)

def drawAsciiArt(draw, width, height):
    asciiCharacters = '@%#*+=-:.)(!/|%";?^][}{|+-'
    fontSize = 16
    font = ImageFont.truetype("font/SplineSansMono-Medium.ttf", fontSize) 

    spacing = int(fontSize * 0.7)
    for y in range(0, height, spacing):
        for x in range(0, width, spacing):
            char = random.choice(asciiCharacters)
            draw.text((x, y), char, font=font, fill=randomColor())

def randomColor():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def saveImage(image, fileName):
    image.save(fileName, "PNG")

if __name__ == "__main__":
    createLinkedInBackground()