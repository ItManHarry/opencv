import cv2
capture = cv2.VideoCapture(0)
f_w = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
f_h = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
print(f'Frame width {f_w}, height {f_h}, frames per second {fps}')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(r'd:/video.avi', fourcc, int(fps), (int(f_w), int(f_h)), True)
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        out.write(frame)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
out.release()
cv2.destroyAllWindows()