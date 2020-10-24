# coding:utf8

import cv2
import pyzbar.pyzbar as pyzbar


class CodeDetect():
    def __init__(self):
        self.flag = False
        self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def decodeDisplay(self, image):
        barcodes = pyzbar.decode(image)
        for barcode in barcodes:
            # 条形码数据为字节对象，所以如果我们想在输出图像上
            # 画出来，就需要先将它转换成字符串
            barcodeData = barcode.data.decode("utf-8")
            # 向终端打印条形码数据和条形码类型
            # print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
            self.flag = True
            return barcodeData

    def detect(self):
        while not self.flag:
            # 读取当前帧
            ret, frame = self.camera.read()
            # 转为灰度图像
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            code = self.decodeDisplay(gray)
            # cv2.waitKey(5)
            # cv2.imshow("camera", image)
            if code != None:
                self.camera.release()
                cv2.destroyAllWindows()
                return code
