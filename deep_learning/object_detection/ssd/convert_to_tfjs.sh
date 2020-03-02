tensorflowjs_converter \
    --input_format=tf_saved_model \
    --output_node_names='Postprocessor/ExpandDims_1,Postprocessor/Slice' \
    --saved_model_tags=serve \
    --output_json=true \
    model_dir/saved_model \
    model_dir_tfjs
