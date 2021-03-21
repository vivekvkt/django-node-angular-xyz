import cv2

# capture frames from a video

cap = cv2.VideoCapture('/home/vivek/Documents/programing_coding_test/open_cv/car_detections/carv2.mp4')


car_cascade = cv2.CascadeClassifier('/home/vivek/Documents/programing_coding_test/open_cv/car_detections/carx.xml')

# loop runs if capturing has been initialized.
while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('sKSama', frames )
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()
