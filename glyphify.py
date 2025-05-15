# glyphify - image to ascii art
# depends pip install click pillow

import click
import numpy as np
from PIL import Image

ASCII_CHARS_LEVEL_1="@%#*+=-;. "
ASCII_CHARS_LEVEL_2="@#$%&WM8BZDHKXQO*+=;:,."
ASCII_CHARS_LEVEL_3="@@@@@###%%%&&&MMMWWW888ZZZDDDHHHKKKXXQOOooo***+++===;;;;:::,,,...."

@click.command()
@click.argument("image_path")
@click.option("--width", default=100, help="Set ASCII art width")
@click.option("--output", default=None, help="Save ASCII art to a file")
@click.option("--level", default=1, help="Level of detail (1-3)")

def image_to_ascii(image_path, width, level, output):
    img=Image.open(image_path).convert("L") # conver to greyscale
    
    # resize image and maintain aspect ratio
    aspect_ratio=img.height/img.width
    new_height=int(width*aspect_ratio*0.55) # adjust for proprtions
    img=img.resize((width,new_height))
    
    ASCII_CHARS=ASCII_CHARS_LEVEL_1
    #set level , level 1 is default and if undefined
    if level==1:
        ASCII_CHARS=ASCII_CHARS_LEVEL_1
    elif level==2:
        ASCII_CHARS=ASCII_CHARS_LEVEL_2
    elif level==3:
        ASCII_CHARS=ASCII_CHARS_LEVEL_3
    
    #convert pixels to ascii characters
    pixels=np.array(img)
    ascii_image="\n".join("".join(ASCII_CHARS[min(pixel//(255//(len(ASCII_CHARS)-1)),len(ASCII_CHARS)-1)] for pixel in row) for row in pixels)
    
    # print or save the output
    if output:
        with open(output, "w") as f:
            f.write(ascii_image)
        print(f"ASCII art saved to {output}")
    else:
        print(ascii_image)

if __name__=="__main__":
    image_to_ascii()