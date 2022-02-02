import cv2
import random


image = cv2.imread("assets/dark_wallpaper.jpg", cv2.IMREAD_COLOR)
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

for i in range(100):
    for j in range(image.shape[1]):
        image[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow("wallpaper", image)
cv2.imwrite("assets/new_image.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()