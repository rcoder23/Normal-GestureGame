import cv2
import pyautogui
import numpy as np
cap=cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hand.xml')
count = 0
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hands=hand_cascade.detectMultiScale(gray,1.5,2)
    # cv2.imshow('hand',hands)
    contour=hands
    contour=np.array(contour)
    
    # print(contour)
    if count==0:
        cv2.putText(img=frame, text='Lefts Play the Game', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
        for (x, y, w, h) in hands:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if count>0:
        if len(contour)==1:
            cv2.putText(img=frame, text='Up Pressed ', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
            pyautogui.press("up")
            
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        elif len(contour)==0:
            cv2.putText(img=frame, text='Normal', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 0, 255))


    count+=1

    
    cv2.imshow('Drive',frame)
    
    
    if(cv2.waitKey(5)==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()