import cv2
import mediapipe as mp
import time 

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture('workout.mp4')
pTime = 0

while True:
    success, img = cap.read()

    height, width, _ = img.shape
    max_width = 1000  
    max_height = 800 
    scale = min(max_width / width, max_height / height)
    img = cv2.resize(img, None, fx=scale, fy=scale) 

    imgRGB = cv2.cvtColor(img , cv2.COLOR_RGB2BGR)
    result =  pose.process(imgRGB)
    if (result.pose_landmarks):
        mpDraw.draw_landmarks(img , result.pose_landmarks, mpPose.POSE_CONNECTIONS,
        landmark_drawing_spec=mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
        connection_drawing_spec=mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2)
        )



     #FPS frames per second
    cTime = time.time()
    fps = 1/ (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS : {int(fps)}", (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)

    cv2.imshow("Image",img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break