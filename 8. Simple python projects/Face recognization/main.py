import cv2             #importing openCv library

face_cap=cv2.CascadeClassifier("C:/Users/lokes/AppData/Roaming/Python/Python313/site-packages/cv2/data/haarcascade_frontalface_default.xml")
        #path for xml file for frontal face detection

video_cap=cv2.VideoCapture(0)   #to open camera             


while True:                                 #infinite loop for camera on continously                 
    ret,video_data=video_cap.read()             #reading frame from web cam
    color=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)       #to convert frame to grey scale for faster processing
    faces=face_cap.detectMultiScale(
        color,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40,40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )              #returns x,y,w,h of rectangle
    
    for(x,y,w,h) in faces:              #loop through detect face
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)     #to draw green rectangle with thickness 2 around each face
    
    cv2.imshow("video_live",video_data)        #to show live video feed with detected faces  
    
    if cv2.waitKey(10)==ord(" "):                   #wait for 10 s and check if space bar is pressed                
        break                                   #exit loop

video_cap.release()                                     #close the camera