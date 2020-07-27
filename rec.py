import cv2
import numpy as np

import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

def do_rec(input_img):
    bbox, label, conf = cv.detect_common_objects(input_img)
    if (np.count_nonzero(label) > 15 ):
        label = ""
    label = str(label)
    return label
    