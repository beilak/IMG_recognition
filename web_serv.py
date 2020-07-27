from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import importlib

import base64
from io import BytesIO
from PIL import Image



importlib.import_module("rec")
from rec import *

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/api/', methods=['POST', 'GET', 'OPTIONS'])
def add_message():
    object = eval(list(request.form)[0])
    image_data = object['IMG'][23:]
    #do_rec(object['IMG'])
    image_data = bytes(image_data, encoding="ascii")
    #print(image_data)
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    #im.save('image.jpg')
    return do_rec( np.array(im))


if __name__ == "__main__":
    app.run()
