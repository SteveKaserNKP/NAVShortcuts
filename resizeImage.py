import os
import PIL
from PIL import Image

def resizeImage(img_path, img_save_path, basewidth):
    img = Image.open(img_path)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(img_save_path)

basewidth = 75
img_path = os.path.join(os.path.dirname(__file__), 'icons', 'png', 'icon_2009R2.png')
img_save_path = os.path.join(os.path.dirname(__file__), 'icons', 'png', f'icon_2009R2_{basewidth}.png')

resizeImage(img_path, img_save_path, basewidth)