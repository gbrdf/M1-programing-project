import PIL
from colorthief import ColorThief
import requests
import io

img = Image.open(r"C:\Users\lucas\Desktop\img.png")  

box = (4, 157, 24, 183)
pegi = img.crop(box)
pegi

width, height = pegi.size #get image size

pegi.save("pegi.jpg") ## not mandatory

box2 = (2, 10, 7, 20)
Color_pegi = pegi.crop(box2)
Color_pegi

Color_pegi.save("couleur_pegi.jpg")


color_thief = ColorThief("C:\\Users\\lucas\\Desktop\\couleur_pegi.jpg")
## change path 

# get the dominant color
dominant_color = color_thief.get_color(quality=1)

dominant_color

