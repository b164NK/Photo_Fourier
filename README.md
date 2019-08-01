# Opencv等で画像の取得、フーリエ変換逆変換をリアルタイムで行う（マウスで周波数を指定）
<バージョン>

Python 3.6.5 :: Anaconda custom (64-bit)

<コードの説明>
7~28:

mouseParam(クラス)の宣言。マウスのクリックから座標を取得するためのクラス。

32~33:

[img]に画像をcv2で読み込み、[im_gray]にグレースケール変換して保持させる。

34~35:

二次フーリエ変換をしたのちに、高周波成分と低周波成分の入れ替えを行う。

36~42:

[magnitude_spectrum]を計算し、正規化してwindowに表示。これをクリックして座標を得る。

44:

変換後の画像を表示するうwindowの名前を宣言。

47:

[h],[w]に縦幅横幅を保持させる。

48:

[done]は、マウスクリックで同じ座標が取得された時に計算を省くための変数。

49:

[mask]は、クリックされた座標以外の周波数成分を０にするために[fshift]に掛けるための変数。

51~76:

ESCキーが押されない限り、ループ

57~76:

左クリック時、周波数領域における座標を取得し二次フーリエ逆変換を行う。

65~67:

指定された周波数領域のみ1を代入した[mask]を[fshift]に掛ける。

70~76:

マスク掛けした[fshift_mask]を高周波成分と低周波成分の入れ替えをしたのちに２次元フーリエ逆変換を行い、絶対値をとって[result_window]に表示。

79:

全てのウィンドウを閉じる

<参考サイト>

http://lang.sist.chukyo-u.ac.jp/classes/OpenCV/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html

<-numpyを使ったフーリエ変換の部分

http://whitecat-student.hatenablog.com/entry/2016/11/09/225631

<-マウスクリック座標取得の方法について

https://algorithm.joho.info/programming/python/opencv-fft-py/

<-画像のフーリエ変換について

https://algorithm.joho.info/image-processing/fourier-transform/

<-画像のフーリエ変換の実装例について

http://tatabox.hatenablog.com/entry/2013/07/20/202705

<-magnitude_spectrumの正規化について

<実行の様子>



![demo](https://github.com/b164NK/Photo_Fourier/blob/master/H_MID_3.wiki/images/Result_Fourier.gif)
