import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from scipy.fftpack import dct, idct

class mouseParam:
    def __init__(self, input_img_name):
        #マウス入力用のパラメータ
        self.mouseEvent = {"x":None, "y":None, "event":None, "flags":None}
        #マウス入力の設定
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)
    
    #コールバック関数
    def __CallBackFunc(self, eventType, x, y, flags, userdata):
        
        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType
        self.mouseEvent["flags"] = flags
    
    #マウスイベントを返す関数
    def getEvent(self):
        return self.mouseEvent["event"]
    
    #xとyの座標を返す関数
    def getPos(self):
        return (self.mouseEvent["x"], self.mouseEvent["y"])

if __name__ == "__main__":

    img = cv2.imread('IMG_1091.jpg')
    im_gray = rgb2gray(img)
    f = np.fft.fft2(im_gray)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))

    magnitude_spectrum2 = cv2.normalize(magnitude_spectrum, magnitude_spectrum, 0.0, 1.0, cv2.NORM_MINMAX)

    window_name = "magnituge_Spe(please click!)"
    cv2.imshow(window_name,magnitude_spectrum2)
    mouseData=mouseParam(window_name)
    
    window_name1 = "result_window"


    h,w = fshift.shape
    done = np.zeros((h,w))
    mask = np.zeros((h,w),fshift.dtype)

    while 1:
        #キー入力を1ms待ってkが27(ESC)だったらBreakする
        k =cv2.waitKey(1)
        if k == 27:
            break
        #左クリック時、周波数領域における座標を取得し空間領域に変換する(フーリエ逆変換する)
        if mouseData.getEvent()==cv2.EVENT_LBUTTONDOWN:
            x,y = mouseData.getPos()
            if x>=h or y>=w:
                continue
            elif done[x,y] == 1:
                continue
            elif done[x,y] == 0:
                #マスクをかける
                mask[x,y] = 1
                mask[h-x,w-y] = 1
                fshift_mask = fshift*mask
                
                #２次元フーリエ逆変換
                f_ishift = np.fft.ifftshift(fshift_mask)
                result = np.fft.ifft2(f_ishift)
                result_abs = np.abs(result)
                cv2.imshow(window_name1,result_abs)
                magnitude_spectrum2[x,y] = magnitude_spectrum2[x,y] * 0
                cv2.imshow(window_name,magnitude_spectrum2)
                done[x,y] = 1


    cv2.destroyAllWindows()
