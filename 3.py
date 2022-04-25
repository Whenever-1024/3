import cv2

video = cv2.VideoCapture("rtsp://admin:123456@10.162.33.50:554/unicast/c1/s1/live")

while True:
    _, frame = video.read()
    cv2.imshow("RTSP", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()