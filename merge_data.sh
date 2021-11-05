echo "merging user data"
python merge_data.py

echo "removing user data files"
rm data/user_data/accelerometer/*
rm data/user_data/tac/*
