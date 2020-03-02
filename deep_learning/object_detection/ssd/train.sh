export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

python3 object_detection/model_main.py --model_dir=custom_data_widerface/model_dir \
	--pipeline_config_path=custom_data_widerface/ssd_mobilenet_v2_coco.config 2>&1 | tee train.log &
