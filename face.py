import cv2
import pyautogui as pt
import dlib

screen_width, screen_height = pt.size()
clf = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
clf_eyes = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
predictor = dlib.shape_predictor(r"D:\python\face detection\shape_predictor_68_face_landmarks.dat")
detector = dlib.get_frontal_face_detector()



camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()
    if not success:
        break
    frame = cv2.flip(frame, 1)
    cx,cy, _ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = detector(gray)
    faces = clf.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        for face, lm in enumerate(faces):
            if face == 0:
                index_x =int(screen_width/cx*x)
                index_y =int(screen_height/cy*y)
                pt.moveTo(index_x, index_y)
    #detect all shape of frontface using dlib 
    for eye in eyes: 
        # all dimensions
        x1 = eye.left()
        x2 = eye.right()
        y1 = eye.top()
        y2 = eye.bottom()
        # landmarks 
        landmarks = predictor(gray, eye)
        #landmarks for left eye
        for n in range(36, 42):
            left_eye_x = landmarks.part(n).x
            left_eye_y = landmarks.part(n).y
            cv2.circle(frame, (left_eye_x, left_eye_y), 2, (0, 255, 0), 2)
            # left eye = left click
            if n == 38:
                left_eye_x1 = landmarks.part(n).x
                left_eye_y1 = landmarks.part(n).y
            
            if n == 37:
                left_eye_x2 = landmarks.part(n).x
                left_eye_y2 = landmarks.part(n).y
            
            if n == 40:
                right_eye_x3 = landmarks.part(n).x
                right_eye_y3 = landmarks.part(n).y
                
            if n == 41:
                right_eye_x4 = landmarks.part(n).x
                right_eye_y4 = landmarks.part(n).y
                if abs(right_eye_x3 - left_eye_x1) < 7.5 and abs(right_eye_y3 - left_eye_y1) < 7.5 and abs(right_eye_x4 - left_eye_x2) < 7.5 and abs(right_eye_y4 - left_eye_y2) < 7.5:
                    pt.click()
         
        # landmarks for right eye 
        for n in range(42, 48):
            right_eye_x = landmarks.part(n).x
            right_eye_y = landmarks.part(n).y
            cv2.circle(frame, (right_eye_x, right_eye_y), 2, (0, 255, 0), 2)
            # right eye = right click  
            if n == 44:
                left_eye_x11 = landmarks.part(n).x
                left_eye_y11 = landmarks.part(n).y
            
            if n == 43:
                left_eye_x22 = landmarks.part(n).x
                left_eye_y22 = landmarks.part(n).y
            
            if n == 46:
                right_eye_x33 = landmarks.part(n).x
                right_eye_y33 = landmarks.part(n).y
                
            if n == 47:
                right_eye_x44 = landmarks.part(n).x
                right_eye_y44 = landmarks.part(n).y
                if abs(right_eye_x33 - left_eye_x11) < 7.5 and abs(right_eye_y33 - left_eye_y11) < 7.5 and abs(right_eye_x44 - left_eye_x22) < 7.5 and abs(right_eye_y44 - left_eye_y22) < 7.5:
                    pt.rightClick()
            
           
               
    cv2.imshow('Face Detection', frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
