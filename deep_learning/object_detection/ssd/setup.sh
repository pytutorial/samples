git clone https://github.com/tensorflow/models.git
mv models tf_models
cd tf_models

sudo apt-get install python3 python3-pip python3-tk
pip3 install tensorflow tensorflow-gpu matplotlib cython contextlib2

sudo apt-get install gcc g++ make


git clone https://github.com/cocodataset/cocoapi.git


cd cocoapi/PythonAPI

#...python2 --> python3

make

cp -r pycocotools ../../research

cd ../../research

wget https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip -O protobuf.zip

unzip protobuf.zip
./bin/protoc object_detection/protos/*.proto --python_out=.

export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

python3 object_detection/builders/model_builder_test.py
