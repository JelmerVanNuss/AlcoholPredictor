import os
import pandas as pd


def merge_data():
    """ Read data from disk and append all new user data """
    ### Accelerometer data
    # load current accelerometer dataset
    acc_data = pd.read_csv(os.path.join("data", "all_acc_data.csv"))

    # append user accelerometer data
    user_acc_data_dir = os.path.join("data", "user_data", "accelerometer")

    for f in os.listdir(user_acc_data_dir):
        user_acc_data = pd.read_csv(os.path.join(user_acc_data_dir, f))
        acc_data = acc_data.append(user_acc_data, ignore_index=True)

    # save result
    acc_data.to_csv(os.path.join("data", "all_acc_data.csv"))

    ### TAC data
    tac_dir = os.path.join("data", "tac_readings")

    existing_pids = [f.split('_')[0] for f in os.listdir(tac_dir)]

    user_tac_data_dir = os.path.join("data", "user_data", "tac")

    for f in os.listdir(user_tac_data_dir):
        pid = f.split('_')[0]

        # append data to existing user if it exists, otherwise create new one
        if pid in existing_pids:
            tac_reading_data = pd.read_csv(os.path.join(tac_dir, f))
            user_tac_reading_data = pd.read_csv(os.path.join(user_tac_data_dir, f))

            tac_reading_data = tac_reading_data.append(user_tac_reading_data)
        else:
            tac_reading_data = pd.read_csv(os.path.join(user_tac_data_dir, f))

        tac_reading_data.to_csv(os.path.join(tac_dir, f))


if __name__ == "__main__":
    merge_data()
