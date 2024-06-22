import cv2
import matplotlib.pyplot as plt

img = cv2.imread('loh.jpg', 0)
img = cv2.resize(img, (0,0), fx=1, fy=0.25)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)


if img is not None:
    plt.imshow(img, cmap='gray')
    plt.title('Imageim')
    plt.axis('off')
    plt.show()
    cv2.imwrite('new_img.jpg', img)
