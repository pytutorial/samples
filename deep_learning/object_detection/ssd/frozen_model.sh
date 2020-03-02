
python3 object_detection/export_inference_graph.py \
--input_type image_tensor \
--pipeline_config_path custom_data_widerface/ssd_mobilenet_v2_coco.config \
--trained_checkpoint_prefix custom_data_widerface/model_dir/model.ckpt-11011 \
--output_directory model_dir
