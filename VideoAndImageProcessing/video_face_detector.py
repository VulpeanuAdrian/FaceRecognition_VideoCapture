import cv2,time

video = cv2.VideoCapture(0)
number_of_frames=1
while True:
    number_of_frames+=1
    check,frame=video.read()
    cv2.imshow('Capturing',frame)
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #convert to gray scale version
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

print(number_of_frames)
video.release()

cv2.destroyAllWindows()

