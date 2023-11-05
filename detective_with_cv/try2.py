import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

centers = []
areas = []

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        area = cv2.contourArea(c)
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)

        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Center", (cx - 20, cy - 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv2.imshow("frame", frame)
            cv2.waitKey(1)

            centers.append((cx, cy))
            areas.append(area)

    if len(centers) > 1:
        max_index = np.argmax(areas)
        cx, cy = centers[max_index]

    print("area is.....", area)
    print("centroid is at", cx, cy)
    k = cv2.waitKey(1000)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()