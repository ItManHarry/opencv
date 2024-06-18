import cv2
video_file_path = r'e:/other/梦入桃花源.mp4'
print(f'Video file path is {video_file_path}')
capture = cv2.VideoCapture(video_file_path)
if capture.isOpened():
    while capture.isOpened():
        ret, frame = capture.read()
        if ret:
            cv2.imshow('Video Image', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            print('File content is empty!')
            break
else:
    print('Video file can not be opened!')
capture.release()
cv2.destroyAllWindows()