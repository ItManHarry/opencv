import cv2
video_file_path = r'd:/video.avi'
capture = cv2.VideoCapture(video_file_path)
frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1
while capture.isOpened() and frame_index >= 0:
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = capture.read()
    if ret:
        print('Current frames is : ', capture.get(cv2.CAP_PROP_POS_FRAMES))
        print('Current frames in milliseconds', capture.get(cv2.CAP_PROP_POS_MSEC))
        cv2.imshow('Frame', frame)
        frame_index -= 1
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()