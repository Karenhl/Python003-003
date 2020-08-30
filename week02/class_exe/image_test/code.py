import requests
import os
from PIL import Image
import pytesseract

# 打开并显示图片
im = Image.open('timg.jpg')
im.show()

# 灰度处理图片
gray = im.convert('L')
gray.save('g_timg.jpg')
im.close()

# 二值化
threshold = 100
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table, '1')
out.save('b.jpg')

th = Image.open('b.jpg')
print(pytesseract.image_to_string(th, lang='chi_sim+eng'))