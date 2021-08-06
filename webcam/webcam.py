import cv2
video = cv2.VideoCapture(0)

first_frame = None

while True:
    check,frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    deltaframe = cv2.absdiff(first_frame,gray)
    thread_delta = cv2.threshold(deltaframe,30,255,cv2.THRESH_BINARY)[1]
    thread_delta = cv2.dilate(thread_delta,None,iterations=2)

    (conts,_) = cv2.findContours(thread_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cont in conts:
        if cv2.contourArea(cont) < 1000:
            continue
        status=1
        (x,y,w,h) = cv2.boundingRect(cont)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("Cap",gray)
    cv2.imshow("Frame",deltaframe)
    cv2.imshow("thresshold",thread_delta)
    cv2.imshow("Color frame",frame)
    print(gray)
    print(status)
    key = cv2.waitKey(1)
    if key == 1:
        break
video.release()
cv2.destroyAllWindows