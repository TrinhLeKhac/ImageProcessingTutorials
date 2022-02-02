import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow("frame", image)

    if cv2.waitKey(5) == ord('q'):
        # ord('q') ordinal value of q in ASCII
        # cv2.waitKey(delay) => FPS = 1000/delay
        # rerun while FPS times in second, capture key 'q' pressed => break
        break
cap.release()
cv2.destroyAllWindows()
