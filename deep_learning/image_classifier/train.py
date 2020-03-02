import os
import glob
import argparse
import numpy as np
from keras.models import Model, load_model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.applications.densenet import DenseNet169, preprocess_input
from config import *

num_classes = len(labels)

class DataGenerator:
    def __init__(self, data_dir, tag, batch_size):
        self.data_dir = data_dir
        self.tag = tag
        self.batch_size = batch_size
        self.current_chunk = 0
        self.current_index = 0
        self.load_data()

    def load_data(self):
        Xfile = 'X{}_{}.np'.format(self.tag, self.current_chunk)
        
        if not os.path.exists(os.path.join(self.data_dir, Xfile)):
            self.current_chunk = 0
            Xfile = 'X{}_{}.np'.format(self.tag, self.current_chunk)

        X = np.fromfile(os.path.join(self.data_dir, Xfile), dtype=np.uint8)
        self.X = preprocess_input(X.reshape((-1, img_size, img_size, 3)).astype('float32'))
        
        Yfile = 'Y{}_{}.np'.format(self.tag, self.current_chunk)
        self.Y = np.fromfile(os.path.join(self.data_dir, Yfile), dtype=np.uint8)
        self.Y = self.Y.reshape((-1, num_classes)).astype('float32')

        self.N = len(self.X)
        self.current_index = 0
        
        indexes = np.random.permutation(self.N)
        self.X = self.X[indexes]
        self.Y = self.Y[indexes]


    def next_batch(self):
        Xb = np.zeros((batch_size, img_size, img_size, 3), dtype=np.float32)
        Yb = np.zeros((batch_size, num_classes), dtype=np.float32)

        while True:
            if self.current_index + self.batch_size > self.N:
                self.current_chunk += 1
                self.load_data()

            for i in range(batch_size):
                Xb[i] = self.X[self.current_index % self.N]
                Yb[i] = self.Y[self.current_index % self.N]
                self.current_index += 1

            yield Xb, Yb


def createModel(lr=1e-3):
    model = DenseNet169(include_top=False)
    x = model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(2048, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    new_model = Model(model.input, predictions)    
    return new_model

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', '-d', default='data')
    parser.add_argument('--learning_rate', '-lr', type=float, default=1e-3)
    parser.add_argument('--pretrained_model', '-p', default='')
    
    args = parser.parse_args()

    Ntrain = len(glob.glob(os.path.join(args.data_dir, 'Xtrain*.np'))) * chunk_size
    Nval = len(glob.glob(os.path.join(args.data_dir, 'Xval*.np'))) * chunk_size

    train_generator = DataGenerator(args.data_dir, 'train', batch_size)
    val_generator = DataGenerator(args.data_dir, 'val', batch_size)

    if args.pretrained_model != '':
        model = load_model(args.pretrained_model)
    else:
        model = createModel()

    opt = SGD(lr=args.learning_rate, momentum=0.9, decay=2.5e-5, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    
    early_stopping = EarlyStopping(monitor='val_acc', patience=5)

    filepath = 'model-{epoch:03d}-loss{loss:.3f}-val_acc{val_acc:.3f}.h5'
    checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')

    callbacks = [early_stopping , checkpoint ]

    model.fit_generator(generator=train_generator.next_batch(),
                    steps_per_epoch=Ntrain//batch_size,
                    epochs=10,
                    validation_data=val_generator.next_batch(),
                    validation_steps=Nval//batch_size,
                    callbacks=callbacks, verbose=True)
