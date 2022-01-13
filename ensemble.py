import os
import cv2
import numpy as np
import shutil

out = './results_ensemble/'
if not os.path.isdir(out):
    os.mkdir(out)

a = './results_1/'
b = './results_9/'
c = './results_10/'

r_list = [a, b, c]

file_paths = os.listdir(a)
for f in file_paths:
    img_a = cv2.imread(a + f)
    img_b = cv2.imread(b + f)
    img_c = cv2.imread(c + f)
    img_new = np.zeros(shape=img_a.shape)
    for i in range(3):
        img_new[..., i] = (img_a[..., i] / 3 +
                           img_b[..., i] / 3 + img_c[..., i] / 3)

    cv2.imwrite(out + f, img_new)
