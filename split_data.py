import os
import random
from shutil import copyfile
import pandas as pd

def split_data(test_size=0.25):
    data_dir = '.' + os.sep + 'data'
    train_dir = os.path.join(data_dir, 'train')
    test_dir = os.path.join(data_dir, 'test')
    tac_dir = os.path.join(data_dir, 'tac_readings')
    train_tac_dir = os.path.join(train_dir, 'tac_readings')
    test_tac_dir = os.path.join(test_dir, 'tac_readings')

    for path in [train_tac_dir, test_tac_dir]:
        if not os.path.exists(path):
            os.makedirs(path)

    # Divide all PIDS into train and test PIDS
    pid_dict = dict([(k.split('_')[0], k) for k in os.listdir(tac_dir)])
    pids = list(pid_dict.keys())
    test_pids = random.sample(pids, round(len(pids) * test_size))
    train_pids = [pid for pid in pids if not pid in test_pids]

    # Create filtered acc dfs 
    all_acc_df = pd.read_csv(os.path.join(data_dir, 'all_acc_data.csv'))
    train_mask = all_acc_df['pid'].isin(train_pids)
    train_acc_df = all_acc_df[train_mask]
    test_acc_df = all_acc_df[~train_mask]

    # Write dfs to csvs
    train_acc_df.to_csv(os.path.join(train_dir, 'acc_data.csv'))
    test_acc_df.to_csv(os.path.join(test_dir, 'acc_data.csv'))

    # Copy TAC files to the directory that the PID was assigned to
    for pid in test_pids:
        copyfile(os.path.join(tac_dir, pid_dict[pid]), os.path.join(test_tac_dir, pid_dict[pid]))

    for pid in train_pids:
        copyfile(os.path.join(tac_dir, pid_dict[pid]), os.path.join(train_tac_dir, pid_dict[pid]))

if __name__ == "__main__":
    split_data()