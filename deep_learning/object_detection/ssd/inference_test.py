import os
import time
import numpy as np
import tensorflow as tf
import cv2
import sys

PATH_TO_CKPT = 'frozen_graph.pb'

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

with tf.Session(graph=detection_graph) as sess:
    
    
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    boxes_node = detection_graph.get_tensor_by_name('detection_boxes:0')
    scores_node = detection_graph.get_tensor_by_name('detection_scores:0')
    classes_node = detection_graph.get_tensor_by_name('detection_classes:0')
    num_detections_node = detection_graph.get_tensor_by_name('num_detections:0')
    
    img = cv2.imread(sys.argv[1])
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h,w,_ = image.shape
    image_np_expanded = np.expand_dims(image, axis=0)
    (boxes, scores, classes, num_detections) = sess.run([boxes_node, scores_node, classes_node, num_detections_node],
                                                feed_dict={image_tensor: image_np_expanded})
    boxes = boxes[0]
    scores = scores[0]
   
    for i in range(len(boxes)):
        if scores[i] > 0.33:
            y1, x1, y2, x2 = boxes[i]
            x1 = int(x1 * w)
            y1 = int(y1 * h)
            x2 = int(x2 * w)
            y2 = int(y2 * h)
            cv2.rectangle(img, (x1,y1),(x2,y2), (0,255,0),2)
    
    cv2.imwrite('output.jpg', img)
