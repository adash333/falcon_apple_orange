# original code from https://recipe.narekomu-ai.com/2017/10/chainer_web_demo_2/
# and http://momijiame.tumblr.com/post/39378516046/python-%E3%81%AE-flask-%E3%81%A7-rest-api-%E3%82%92%E4%BD%9C%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%8B

from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, jsonify, request, url_for, abort, Response

import numpy as np
from PIL import Image
from datetime import datetime

from keras.preprocessing import image
from keras.models import model_from_json
import sys
import io

import json

app = Flask(__name__)
@app.route('/debug', methods = ['GET', 'POST'])
def upload_file():
  if request.method == 'GET':
    return render_template('index.html')
  if request.method == 'POST':
    # アプロードされたファイルを保存する
    #f = request.files['file']
    #filepath = "./static/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    #f.save(filepath)
    # モデルを使って判定する

    # data = req.get_param('file').file.read()
    data = request.files['file'].read()
    pilimg = Image.open(io.BytesIO(data))

    ### load model and weight
    model = model_from_json(open('apple_orange_model.json').read())
    model.load_weights('apple_orange_weights.h5')

    image = np.array(pilimg.resize((25, 25)))
    image = image.transpose(2, 0, 1)
    image = image.reshape(1, image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]
    x = np.array([image / 255.])
    result = model.predict_classes(x)
    proba = model.predict_proba(x)

    predict = result[0].tolist()
    result = classes[predict]
    predict_proba = proba[0].tolist()
    result_proba = predict_proba[predict]

    response = jsonify({'result':result, 'probability':result_proba})

    # res.status = falcon.HTTP_200
    response.status_code = 200

    return response
    # res.body = json.dumps({'result':result, 'probability':result_proba})

# 画像認識のイニシャライズ
result_dir = 'results'
classes = ["apple", "orange"]

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=int("8000"),debug=True)
