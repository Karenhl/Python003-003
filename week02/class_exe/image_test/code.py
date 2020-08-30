import requests
import os
from PIL import Image
import pytesseract

im = Image.open('timg.jpg')
im.show()