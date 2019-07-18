# OpenCV等でカメラ画像を取得し、毎フレームごとの輝度の平均値を計算
<バージョン>
Python 3.6.5 :: Anaconda custom (64-bit)

<コードの説明>
8~9:[file_name]に動画ファイル名入れ、[video]に動画ファイルを読み込む

12~15:[frame_count]に動画のフレーム数を入れ、１フレーム毎にpngファイルを同一ディレクトリ内に生成する

18~44:[img]に１フレーム分の画像ファイルを読み込み、forの２重ループで１画素分の輝度値を計算し[H]に入れる。[H_mid_1f]には１フレーム分の全画素の輝度値の合計を入れて、36行目の計算によってそのフレームにおける輝度値の平均が入れられる。39行目では[H_mid_1f]の値とその時のフレームが標準出力されるようにしており、計算状況を目視で確認で切るようになっている。40~44行目で[l]という配列に各フレームの輝度値平均を順に格納しているのは、後述のグラフプロットに用いるためである。

47~50:[x]に0から[frame_count]を22分割した配列を入れ、これと配列[l]を用いてグラフをプロットする

<参考サイト>
https://www.tech-tech.xyz/opencv_video.html#1
<-「動画を１フレームごとに画像へ変換」の部分

https://algorithm.joho.info/programming/python/opencv-rgb-to-hsv-color-space/
<-「HSV色空間に変換」の「方法１」の部分

https://note.nkmk.me/python-list-append-extend-insert/
<-「末尾に要素を追加」の部分

https://qiita.com/KntKnk0328/items/5ef40d9e77308dd0d0a4
<-「インスタンスを明言してプロットする」の部分

<実行の様子>

![demo](https://raw.github.com/wiki/b164NK/H_MID_3/images/Result_H_mid.gif)
