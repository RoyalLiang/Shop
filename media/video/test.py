# import cv2
# import uuid
#
#
# def get_video_pic(name):
#     cap = cv2.VideoCapture(name)
#     cap.set(0, int(cap.get(7) / 2))  # 取它的中间帧
#     rval, frame = cap.read()  # 如果rval为False表示这个视频有问题，为True则正常
#     if rval:
#         (h, w) = frame.shape[:2]
#         center = (w / 2, h / 2)
#
#         # 将图像旋转90度
#         M = cv2.getRotationMatrix2D(center, 90, 1.0)
#         rotated = cv2.warpAffine(frame, M, (w, h))
#         cv2.imshow("rotated", rotated)
#         cv2.waitKey(0)
#         cv2.imwrite('%s.jpg' % str(uuid.uuid4()), rotated)  # 存储为图像
#     cap.release()
#
#
# get_video_pic("test1.mp4")
import cv2
import uuid
import os
from Shop import settings

# def get_video_pic(name):
#     cap = cv2.VideoCapture(name)
#     cap.set(0, int(cap.get(7) / 2))  # 取它的中间帧
#     rval, frame = cap.read()  # 如果rval为False表示这个视频有问题，为True则正常
#     img_name = str(uuid.uuid4()) + '.jpg'
#     img_url = os.path.join(settings.MEDIA_ROOT, 'video_image')
#     if not os.path.isdir(img_url):
#         os.mkdir(img_url)
#     img_url = os.path.join(img_url, img_name)
#
#     if rval:
#         cv2.imwrite(img_url, frame)  # 存储为图像
#     cap.release()
#
#
# get_video_pic("test1.mp4")


# import time
#
# print(time.ctime())
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


