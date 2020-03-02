import os
import argparse
import cv2
import sys
import random
import numpy as np

from keras.utils import to_categorical
from config import *

train_factor = 0.7
num_classes = len(labels)

def saveData(outdir, tag, data):
    X = []
    Y = []
    N = len(data)
    index = 0

    for i, (img_path, label) in enumerate(data):
        img = cv2.imread(img_path)
        img = cv2.resize(img, (img_size, img_size))
        img =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        X.append(img)
        
        Y.append(to_categorical(label, num_classes))

        if len(X) >= chunk_size or (i + 1) == N:
            Xfile = os.path.join(outdir, 'X{}_{}.np'.format(tag, index))
            Yfile = os.path.join(outdir, 'Y{}_{}.np'.format(tag, index))
            np.array(X).tofile(Xfile)
            np.array(Y, dtype=np.uint8).tofile(Yfile)
            X = []
            Y = []
            index += 1
            print('Processed {}/{} {} images'.format(i + 1, N, tag))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--indir', '-i', default='Images')
    parser.add_argument('--outdir', '-o', default='data')
    args = parser.parse_args()
    
    data = []
    index = 0

    for root, dirs, files in os.walk(args.indir):
        label = root.split('/')[-1]        
        for file in files:
            img_path = os.path.join(root, file)
            data.append((img_path, labels.index(label)))

    random.shuffle(data)

    N = len(data)
    Ntrain = int(N * train_factor)

    train_data = data[:Ntrain]
    val_data = data[Ntrain:]
    
    saveData(args.outdir, 'train', train_data)
    saveData(args.outdir, 'val', val_data)
