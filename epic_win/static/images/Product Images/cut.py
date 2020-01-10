import ufp.image 
import PIL
from PIL import Image

with Image("test.png", "r") as im:

    trimed = ufp.image.trim(im, fuzz=13.3)
    trimed.save('trimed.png')
