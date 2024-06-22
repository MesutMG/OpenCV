import cv2
import random
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('loh.jpg', cv2.IMREAD_COLOR)

#print(type(img)) #numpy.ndarray

print(img.shape)
percentage = 50
randlist = np.random.choice(1062, size=int(img.shape[1]*percentage/100), replace=False)

for i in randlist:
    for j in range(img.shape[1]):
        img[i, j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
c1 = 300
c2 = 700
c3 = 200
c4 = 500
for i in range(6):
    tag = img[c1:c2, c3:c4]
    c1 += 25
    c2 += 25
    c3 += 25
    c4 += 25
    print(c1,c2,c3,c4)
    img[c1:c2, c3:c4] = tag
    c1 += 25
    c2 += 25
    c3 += 25
    c4 += 25

if img is not None:
    plt.imshow(img, cmap='gray')
    plt.title('Imageim')
    plt.axis('off')
    plt.show()
    cv2.imwrite('new_img.jpg', img)
