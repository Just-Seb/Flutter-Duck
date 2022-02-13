import cv2
import face_recognition

videoCapture = cv2.VideoCapture(0)

face_locations = []

while True:
    ret, frame = videoCapture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)

    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.circle(frame, (int(((right + left) / 2)), int(((top + bottom) / 2))), 10, (0,0,255), 5)
        print(((bottom - left), (top - right)))

    cv2.imshow('Video', frame)
    print(face_locations)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break