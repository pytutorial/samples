import os
import sys
import json
import hashlib
import contextlib2
import tensorflow as tf
from random import shuffle
from object_detection.utils.dataset_util import *
from object_detection.dataset_tools.tf_record_creation_util import open_sharded_output_tfrecords

tag = sys.argv[1] # train/val
img_dirs = f'/home/dttvn1001/{tag}/images'
data_dir = 'data'
ann_file = f'{tag}_data.json'
record_dir = 'records'
num_shards = 10

def create_tf_example(img_file, img_width, img_height, boxes):
    img_path = os.path.join(img_dirs, img_file)
    with open(img_path, 'rb') as fid:
        encoded_jpg = fid.read()
        
    key = hashlib.sha256(encoded_jpg).hexdigest()
    xmins, ymins, xmaxs, ymaxs, classes = [], [], [], [], []
    
    for box in boxes:
        x1, y1, x2, y2 = box[:4]
        xmins.append(float(x1) / img_width)
        ymins.append(float(y1) / img_height)
        xmaxs.append(float(x2) / img_width)
        ymaxs.append(float(y2) / img_height)
        classes.append(1)
        
    feature_dict = {
        'image/height': int64_feature(img_height),
        'image/width': int64_feature(img_width),
        'image/filename': bytes_feature(img_file.encode('utf8')),
        'image/source_id': bytes_feature(img_file.encode('utf8')),
        'image/key/sha256': bytes_feature(key.encode('utf8')),
        'image/encoded': bytes_feature(encoded_jpg),
        'image/format': bytes_feature('jpeg'.encode('utf8')),
        'image/object/bbox/xmin': float_list_feature(xmins),
        'image/object/bbox/xmax': float_list_feature(xmaxs),
        'image/object/bbox/ymin': float_list_feature(ymins),
        'image/object/bbox/ymax': float_list_feature(ymaxs),
        'image/object/class/label': int64_list_feature(classes),
    }
    
    features = tf.train.Features(feature=feature_dict)
    return tf.train.Example(features=features)
    
def create_tf_records(output_prefix, examples):    
    with contextlib2.ExitStack() as tf_record_close_stack:
        output_tfrecords = open_sharded_output_tfrecords(tf_record_close_stack, output_prefix, num_shards)
        
        for idx, item in enumerate(examples):
            if idx % 100 == 0:
                print('On item {} of {}'.format(idx, len(examples)))
                
            img_file = item['file_name']
            img_width = item['img_width']
            img_height = item['img_height']
            boxes = item['boxes']

            tf_example = create_tf_example(img_file, img_width, img_height, boxes)
            
            if not tf_example:
                continue
                
            shard_idx = idx % num_shards
            output_tfrecords[shard_idx].write(tf_example.SerializeToString())
            

with open(os.path.join(data_dir, ann_file)) as f:
    examples_list = json.load(f)
    
print('Total number of example : ', len(examples_list))
create_tf_records(os.path.join(data_dir, record_dir, f'{tag}.records'), examples_list)
