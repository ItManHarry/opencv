import cv2 as cv
capture = cv.VideoCapture(0)
frame_w = capture.get(cv.CAP_PROP_FRAME_WIDTH)
frame_h = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
frame_p = capture.get(cv.CAP_PROP_FPS)
print(f'Frame width : {frame_w}')
print(f'Frame height : {frame_h}')
print(f'Frames per second : {frame_p}')
if capture.isOpened():
    print('Camera has been opened...')
    while capture.isOpened():
        ret, frame = capture.read()
        if ret:
            cv.imshow('Capture image', frame)
            cv.imwrite('d:/c_0618.jpg', frame)
            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imwrite('d:/g_c_0618.jpg', gray_frame)
            cv.imshow('Gray capture image', gray_frame)
            if cv.waitKey(20) & 0xFF == ord('q'):
                print('Stop while loop...')
                break
        else:
            break
        print(frame)
        capture.release()
        cv.destroyAllWindows()
else:
    print('Camera has not been opened...')
