from PIL import Image
import random

def generateList(wid,hit):
    my_list.clear()
    for i in range(1, (wid*hit) - 1):
        my_list.append(random.randint(0, 256))

width = 1280
height = 800
my_list = [0, 1]
# for i in range(1, 1024000-1):
#     my_list.append(random.randint(0, 256))
generateList(width, height)
img = Image.new('RGBa', (width, height))
pic = img.split()

pic[3].putdata(my_list)
generateList(width, height)
pic[2].putdata(my_list)
generateList(width, height)
pic[1].putdata(my_list)

img = Image.merge("RGB", (pic[1], pic[2], pic[3]))
img.save('image.png')


