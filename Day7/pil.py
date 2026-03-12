import PIL
from PIL import Image
from PIL import ImageDraw

img1 = Image.open("img1.jpg")

img1.show()
#Rotating Img 90 degree
img1.rotate(90, PIL.Image.NEAREST, expand=1)

#Flip the image vertically
vertical_flip = img1.transpose(PIL.Image.FLIP_TOP_BOTTOM)
vertical_flip.show()

#Flip the image horizontally
horizontal_flip = img1.transpose(PIL.Image.FLIP_LEFT_RIGHT)
horizontal_flip.show()

#write Text on img
draw = ImageDraw.Draw(img1)
draw.text((100, 150), "Text written",(0, 0, 0))
img1.show()
