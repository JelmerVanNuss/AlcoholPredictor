echo "Mergind data"
./merge_data.sh

echo "Validating data"
# great-expectations checkpoint run checkpoint_tac2
# great-expectations checkpoint run checkpoint_tac2

echo "Splitting into train/test split"
python split_data.py

echo "Processing data"
python process_data.py

echo "Training model"
python train.py
