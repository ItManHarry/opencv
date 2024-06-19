import cv2
def decode_fourcc(fourcc):
    int_fourcc = int(fourcc)
    return "".join([chr((int_fourcc >> 8 * i) & 0xFF) for i in range(4)])
video_file_path = r'd:/video.avi'
capture = cv2.VideoCapture(video_file_path)
print('Frame width : ', capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Frame height : ', capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frames per second : ', capture.get(cv2.CAP_PROP_FPS))
print('POS MSEC', capture.get(cv2.CAP_PROP_POS_MSEC))
print('POS Frames : ', capture.get(cv2.CAP_PROP_POS_FRAMES))
print('FOURCC : ', decode_fourcc(capture.get(cv2.CAP_PROP_FOURCC)))
print('Frame count : ', capture.get(cv2.CAP_PROP_FRAME_COUNT))
print('Frame mode : ', capture.get(cv2.CAP_PROP_MODE))
print('Frame brightness : ', capture.get(cv2.CAP_PROP_BRIGHTNESS))  # 明亮度
print('Frame contrast : ', capture.get(cv2.CAP_PROP_CONTRAST))      # 对比度
print('Frame saturation : ', capture.get(cv2.CAP_PROP_SATURATION))  # 饱和度
print('Frame hue : ', capture.get(cv2.CAP_PROP_HUE))                # 色调
print('Frame gain : ', capture.get(cv2.CAP_PROP_GAIN))              # 增益
print('Frame exposure : ', capture.get(cv2.CAP_PROP_EXPOSURE))      # 曝光量
print('Frame convert RGB :', capture.get(cv2.CAP_PROP_CONVERT_RGB))
print('Frame rectification : ', capture.get(cv2.CAP_PROP_RECTIFICATION))    # 矫正
print('Frame ISO speed : ', capture.get(cv2.CAP_PROP_ISO_SPEED))    # ISO速率
print('Frame buffer size', capture.get(cv2.CAP_PROP_BUFFERSIZE))    # 缓存

if capture.isOpened():
    while capture.isOpened():
        ret, frame = capture.read()
        if ret:
            print('Current frames is : ', capture.get(cv2.CAP_PROP_POS_FRAMES))
            print('Current frames in milliseconds', capture.get(cv2.CAP_PROP_POS_MSEC))
            print('-'*80)
            cv2.imshow('Origin Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
else:
    print('Can not open the camera stream or video file!!!')
capture.release()
cv2.destroyAllWindows()