import numpy as np
from skimage import io, img_as_ubyte
from skimage.transform import rotate, AffineTransform, warp 
from skimage.util import random_noise
import os
import random
import cv2
import matplotlib.pyplot as plt

# Imagens Origianis
if os.path.isdir('DB_Oficial') == False:
    print('A Pasta DB_Oficial nao foi encontrada')
else:
    print('A Pasta DB_Oficial foi encontrada')
    images_path = os.path + '/DB_Oficial'
#Imagens Modificadas
