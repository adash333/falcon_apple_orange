# falcon_apple_orange

りんごとオレンジを識別するWEB APIです。Falconを用いています。(Flaskを用いたflask_predict.pyも掲載しました)
画像を送ると、リンゴかオレンジが判定して、その結果と確率をjsonで返してきます。

（環境）
Windows 8.1
Anaconda 4.4.0
Python 3.6.1
Tensorflow 1.2.1
Keras 2.0.6

keras, tensorflowのインストール方法
http://twosquirrel.mints.ne.jp/dokuwiki/doku.php/windows%E3%81%A7%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%92%E5%B0%8E%E5%85%A5%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95#windowsにkeras_tensorflow_をインストール

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

Falcon(Python)で画像分類（apple-orange）のWebAPIとPHPフロントエンド
2017/11/1
http://twosquirrel.mints.ne.jp/?p=20772


