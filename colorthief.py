Project: Critical AI as Iconology - Color Analysis 
              

Description: This script utilizes the ColorThief library to extract dominant color palettes from 95 AI-generated Orientalist images, revealing normative "yellow-brown" dominant colours in the model's output.

import numpy

import PIL

!pip install colorthief

import colorthief

import math

from PIL import Image

def create_grid(images, cols):
    rows = math.ceil(len(images) / cols)
    width = images[0].width
    height = images[0].height

    grid = Image.new('RGB', (width * cols, height * rows))

    for i, img in enumerate(images):
        grid.paste(img, ((i % cols) * width, (i // cols) * height))

    return grid

# Usage
images = [Image.open(f"../image{i}.jpeg") for i in range(1, 31)]
grid = create_grid(images, 5)
grid.save("dynamic_grid.jpeg")

from colorthief import ColorThief

import glob

dominant_colours = []

list = glob.glob(r'../*.jpeg')
for name in list:
  print(name)
  color1 = ColorThief(name)
  dominant = color1.get_color(quality=1) # dominant colour palette for this image
  dominant_colours.append(dominant)

dominant_colours

print(len(dominant_colours))

visualisation = """<html><table>"""

Loop through adding rows of 5 cells

cols = 5
i = 0
length = len(dominant_colours)
for colour in dominant_colours:
  visualisation+=f"<tr><td style=\"background-color:rgb{dominant_colours[i]}; width:10%\">&nbsp;&nbsp;</td><td style=\"background-color:rgb{dominant_colours[i+1]}; width:10%\">&nbsp;&nbsp;</td><td style=\"background-color:rgb{dominant_colours[i+2]}; width:10%\">&nbsp;&nbsp;</td><td style=\"background-color:rgb{dominant_colours[i+3]}; width:10%\">&nbsp;&nbsp;</td><td style=\"background-color:rgb{dominant_colours[i+4]}; width:10%\">&nbsp;&nbsp;</td></tr>"
  i+=cols
  length -= cols
  if length < cols: #stop if we don't have enough remaining images to fill a complete row
    break

visualisation += "</table></html>"

visualisation

with open("visualisation.html", "w") as f:
  f.write(visualisation)

Create a check and improve the HTML: print the filenames in a square to make sure they're in the required order.

import glob, re

filenames = glob.glob('../image*.jpeg')

# arrange the files in the order of numbers in their names: image1, image2, ... image30
filenames = sorted(
    filenames,
    key=lambda p: int(re.search(r'(\d+)', p).group())
)

print(filenames)

cols = 5
for i in range(0, len(filenames), cols):
    row_files = filenames[i:i+cols]
    print(', '.join(row_files))

for i, (name, colour) in enumerate(zip(filenames, dominant_colours), start=1):
    print(i, name, colour)
    if i >= 10:   # check the first 10 images to match the names and dominant colours
        break

cols = 5
visualisation = "<html><table border='1' cellspacing='0' cellpadding='4'>"

for idx, (name, colour) in enumerate(zip(filenames, dominant_colours)):

    if idx % cols == 0:
        visualisation += "<tr>"

    num = idx + 1
    
    visualisation += (
        f'<td style="background-color:rgb{colour}; '
        f'width:80px; height:80px; text-align:center; '
        f'font-size:10px; color:#000;">'
        f'{num}<br>{name}'
        f'</td>'
    )

    if (idx + 1) % cols == 0:
        visualisation += "</tr>"

if len(dominant_colours) % cols != 0:
    visualisation += "</tr>"

visualisation += "</table></html>"

with open("visualisation_debug.html", "w") as f:
    f.write(visualisation)

from IPython.display import Image, display
display(Image('dynamic_grid.jpeg'))

from IPython.display import HTML, display

display(HTML(visualisation))
