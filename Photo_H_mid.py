# -*- coding: utf-8 -*-
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

#動画ファイルを読み込む
file_name = u"H_MID.mov"
video = cv2.VideoCapture(file_name)

#フレーム数を取得
frame_count = int(video.get(7))-1
for i in range(frame_count):
    is_read, frame = video.read()
    cv2.imwrite(str(i) + ".png", frame)

#1フレームごとに画像を読み込む
for i in range(frame_count):
    img = cv2.imread(str(i) + '.png')
    h,w,c = img.shape
    H_mid_1f = 0

    #1画素ごとに輝度値を計算し、１フレームの平均を[H_mid_1f]に入れる
    for j in range(0,h):
        for k in range(0,w):
            [b,g,r] = img[j][k]/255.0
            mx,mn = max(r,g,b),min(r,g,b)
            diff = mx - mn
            if mx == mn : H = 0
            elif mx == r : H = 60 * ((g-b)/diff)
            elif mx == g : H = 60 * ((b-r)/diff) + 120
            elif mx == b : H = 60 * ((r-g)/diff) + 240
            if H < 0 : H = H + 360
            H_mid_1f = H_mid_1f + H

    H_mid_1f = H_mid_1f/(h * w)

    #何フレーム目で輝度値平均がいくらかを共に表示
    print(str(i),H_mid_1f)

    if i>0:
        l.append(H_mid_1f)
    else:
        l = [H_mid_1f]

#グラフのプロット
x = np.linspace(0,frame_count,22)
plt.plot(x,l,label="H_mid")
plt.legend()
plt.show()
