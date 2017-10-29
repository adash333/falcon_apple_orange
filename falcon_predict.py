# coding:utf-8

# original code from https://github.com/aidiary/keras-examples/blob/master/vgg16/test_vgg16/test_vgg16
# and http://blog.apitore.com/2017/09/27/python-webapi-falcon/
# original code from https://recipe.narekomu-ai.com/2017/10/chainer_web_demo_2/

# falcon_vgg16.py

import falcon
import json
import io
import os
import sys
from keras.applications.vgg16 import VGG16
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
import numpy as np
from datetime import date
from datetime import datetime
from PIL import Image
from falcon_multipart.middleware import MultipartMiddleware

from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import sys

import codecs, json

from keras.preprocessing import image
from keras.models import model_from_json
import sys


class DebugResource:
    def on_post(self, req, res):
        """Handles POST requests"""

        data = req.get_param('file').file.read()

        # アプロードされたファイルを保存する
        # f = request.files['file']
        #filepath = "./static/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        #data.save(filepath)

        pilimg = Image.open(io.BytesIO(data))
        # x = np.asarray(pilimg)

        # モデルを使って判定する

        ### load model and weight
        model = model_from_json(open('apple_orange_model.json').read())
        model.load_weights('apple_orange_weights.h5')

        # 画像を読み込み、グレースケールに変換し、28x28pixelに変換し、numpy配列へ変換する。
        # 画像の1ピクセルは、それぞれが0-255の数値。
        # image = np.array(Image.open(filepath).convert("L").resize((28, 28)))
        image = np.array(pilimg.resize((25, 25)))
        image = image.transpose(2, 0, 1)
        image = image.reshape(1, image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]
        result = model.predict_classes(np.array([image / 255.]))
        # image = np.array(pilimg.convert("L").resize((28, 28)))
        # print(filepath)
        # さらにフラットな1次元配列に変換。
        # image = image.reshape(1, 784).astype("float32")[0]
        # result = model.predict_classes(np.array([image / 255.]))
        # print("result:", result[0], "（0:りんご, 1:オレンジ）")
        predict = result[0].tolist()
        result = classes[predict]

        # クラスを予測
        # 入力は1枚の画像なので[0]のみ
        # pred = model.predict(x)[0]

        # 予測確率が高いトップ5を出力
        #top = 5
        #top_indices = pred.argsort()[-top:][::-1]
        #result = classes[top_indices[0]]

        # 予測確率が高いトップ1を出力
        res.status = falcon.HTTP_200
        res.body = json.dumps({'result':result})

# 画像認識のイニシャライズ
result_dir = 'results'

classes = ["apple", "orange"]

# WebAPIの起動
api = falcon.API(middleware=[MultipartMiddleware()])
api.add_route('/debug', DebugResource())

# 起動する
if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 8000, api)
    httpd.serve_forever()
