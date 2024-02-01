#!/bin/bash

# Change to the directory where your Python scripts are located
# cd /path/to/your/scripts/directory

# Run the Python scripts one by one
# python3 pre_process_npy.py
python3 pre_process_embedding.py
python3 save_model.py
# echo "Model ID from save_model.py: $model_id"

python3 train.py
# echo "name_training from train.py: $name_training"

python3 test.py 
python3 knn_stat.py

# run ./run_all.sh into ubuntu terminal