import os
from PIL import Image

def pdf():
    images = []
    filename = [i for i in os.listdir()]
    for i in range(len(filename)):
        images.append(Image.open(filename[i]))
    for i in range(len(filename)):
        images[i] = images[i].convert('RGB')

    images[0].save('./output.pdf',save_all=True, append_images=images[1:])
    os.chdir("../../")