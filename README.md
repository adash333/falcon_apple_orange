# falcon_apple_orange

りんごとオレンジを識別するWEB APIです。Falconを用いています。
画像を送ると、リンゴかオレンジが判定して、jsonを返してきます。

（環境）
Windows 8.1
Anaconda 4.4.0
Python 3.6.1
Tensorflow 1.2.1
Keras 2.0.6

pip install cython falcon gunicorn falcon-multipart

http://curl.haxx.se/download.html の下の方へ行って、Windows用のファイルをダウンロードして、Windowsの環境変数のPATHを通す。
→　参考：http://web-dev.hatenablog.com/entry/windows/install-curl

＜使い方＞

（１）適当な画像を拾ってきて、falcon_predict.py と同じフォルダにimage001.jpgという名前で保存

（２）Anaconda Promptを起動して、falcon_predict.py と同じフォルダに移動してから、
python falcon_predict.py

（３）コマンドプロンプトを起動して、falcon_predict.py と同じフォルダに移動してから、
curl -X POST http://localhost:8000/debug -H "Content-Type: multipart/form-data" -F "file=@image001.jpg"

# 解説ページ

「Pythonで画像処理のWebAPIを作る ～Falcon編～」を写経してみる
2017/10/29
http://twosquirrel.mints.ne.jp/?p=20670

Kerasで自前データで機械学習した成果をWEBで公開（Keras+Flask）（１）
2017/10/26
http://twosquirrel.mints.ne.jp/?p=20440

自前のデータでKerasで画像分類を写経してみる（１）
2017/7/31 2017/8/4
http://twosquirrel.mints.ne.jp/?p=19448
