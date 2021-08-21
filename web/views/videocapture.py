from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

import sys
import cv2
import time
import threading

import dlib

# Dlib 正向人脸检测器 / Use frontal face detector of Dlib
detector = dlib.get_frontal_face_detector()


class Face_Register:
    def __init__(self):
        self.path_photos_from_camera = "data/data_faces_from_camera/"
        self.font = cv2.FONT_ITALIC

        self.existing_faces_cnt = 0         # 已录入的人脸计数器 / cnt for counting saved faces
        self.ss_cnt = 0                     # 录入 personX 人脸时图片计数器 / cnt for screen shots
        self.current_frame_faces_cnt = 0    # 录入人脸计数器 / cnt for counting faces in current frame

        self.save_flag = 1                  # 之后用来控制是否保存图像的 flag / The flag to control if save
        self.press_n_flag = 0               # 之后用来检查是否先按 'n' 再按 's' / The flag to check if press 'n' before 's'

        # FPS
        self.frame_time = 0
        self.frame_start_time = 0
        self.fps = 0

    # 获取处理之后 stream 的帧数 / Update FPS of video stream
    def update_fps(self):
        now = time.time()
        self.frame_time = now - self.frame_start_time
        self.fps = 1.0 / self.frame_time
        self.frame_start_time = now

    # 生成的 cv2 window 上面添加说明文字 / PutText on cv2 window
    def draw_note(self, img_rd):
        # 添加说明 / Add some notes
        cv2.putText(img_rd, "Face Register", (20, 40), self.font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img_rd, "FPS:   " + str(self.fps.__round__(2)), (20, 100), self.font, 0.8, (0, 255, 0), 2,
                    cv2.LINE_AA)
        cv2.putText(img_rd, "Faces: " + str(self.current_frame_faces_cnt), (20, 140), self.font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

camera = cv2.VideoCapture(0)

def Video():
    while True:
        success,frame = camera.read()
        Face_Register_con = Face_Register()
        # kk = cv2.waitKey(1)
        # faces = detector(frame, 1)  # Use Dlib face detector
        #
        # # 5. 检测到人脸 / Face detected
        # if len(faces) != 0:
        #     # 矩形框 / Show the ROI of faces
        #     for k, d in enumerate(faces):
        #         # 计算矩形框大小 / Compute the size of rectangle box
        #         height = (d.bottom() - d.top())
        #         width = (d.right() - d.left())
        #         hh = int(height / 2)
        #         ww = int(width / 2)
        #
        #         # 6. 判断人脸矩形框是否超出 480x640 / If the size of ROI > 480x640
        #         if (d.right() + ww) > 1048 or (d.bottom() + hh > 580) or (d.left() - ww < 0) or (d.top() - hh < 0):
        #             cv2.putText(frame, "OUT OF RANGE", (20, 300), Face_Register_con.font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
        #             color_rectangle = (0, 0, 255)
        #             save_flag = 0
        #             if kk == ord('s'):
        #                 print("请调整位置 / Please adjust your position")
        #         else:
        #             color_rectangle = (0, 255, 0)
        #             save_flag = 1
        #
        #         cv2.rectangle(frame,
        #                       tuple([d.left() - ww, d.top() - hh]),
        #                       tuple([d.right() + ww, d.bottom() + hh]),
        #                       color_rectangle, 3)
        #
        # Face_Register_con.current_frame_faces_cnt = len(faces)
        #
        # # 9. 生成的窗口添加说明文字 / Add note on cv2 window
        # Face_Register_con.draw_note(frame)
        #


        # 11. Update FPS
        Face_Register_con.update_fps()
        if not success:
            break
        else:
            ret,buffer = cv2.imencode('.jpg',frame)

            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n')




def getVideo(request):
    return StreamingHttpResponse(Video(), content_type='multipart/x-mixed-replace; boundary=frame')
