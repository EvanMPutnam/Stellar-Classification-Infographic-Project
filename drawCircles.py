import PIL.Image, PIL.ImageDraw, PIL.ImageFont

#Get nasa font information
FONT_PATH = r"resources/nasalization-rg.ttf"
FONT_NASA = PIL.ImageFont.truetype(FONT_PATH, 40)


#Setup image information
img = PIL.Image.new("RGBA", (1000, 1000))
draw = PIL.ImageDraw.Draw(img)

#Data to draw.
stellar_classification_data = {
    "O": {"x": 200, "y": 300, "r": 100, 'color': 'blue'},
    "b": {"x": 400, "y": 300, "r": 50, 'color': 'aqua'},
    "a": {"x": 500, "y": 300, "r": 17, 'color': 'turquoise'},
    "f": {"x": 600, "y": 300, "r": 13, 'color': 'white'},
    "g": {"x": 700, "y": 300, "r": 10, 'color': 'yellow'},
    "k": {"x": 800, "y": 300, "r": 8, 'color': 'orange'},
    "m": {"x": 900, "y": 300, "r": 3, 'color': 'red'},
}

#Draw the ellipse and text above it.
for key in stellar_classification_data:
    x = stellar_classification_data[key]['x']
    y = stellar_classification_data[key]['y']
    r = stellar_classification_data[key]['r']
    fill = stellar_classification_data[key]['color']
    draw.ellipse((x-r, y-r, x+r, y+r), fill, fill, 1)
    if r == 50:
        draw.text((x - 15, y-110), key, fill = 'white', font = FONT_NASA)
    elif r < 50:
        draw.text((x - 15, y-80), key, fill = 'white', font = FONT_NASA)
    else:
        draw.text((x - 15, y-150), key, fill = 'white', font = FONT_NASA)

#Save the image.
img.save("imgs/circles.png")