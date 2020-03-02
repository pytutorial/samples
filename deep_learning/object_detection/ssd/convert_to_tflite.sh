python3 object_detection/export_tflite_ssd_graph.py \
--pipeline_config_path=train_models/model_dir/pipeline.config \
--trained_checkpoint_prefix=train_models/model_dir/model.ckpt-5000 \
--output_directory=train_models/model_dir_lite \
--add_postprocessing_op=true

tflite_convert --output_file model.tflite --graph_def_file tflite_graph.pb \
 --input_shapes  "1,300,300,3" --input_array=normalized_input_image_tensor \
 --output_arrays='TFLite_Detection_PostProcess','TFLite_Detection_PostProcess:1','TFLite_Detection_PostProcess:2','TFLite_Detection_PostProcess:3' \
 --output_format TFLITE --inference_type=QUANTIZED_UINT8 \
 --mean_values=128 --std_dev_values=128 --default_ranges_min=0 --default_ranges_max=255 --allow_custom_ops

