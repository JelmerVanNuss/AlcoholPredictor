import os
import pandas as pd

def process_data(split):
    data_path = os.path.join("data", split)

    ### Accelerometer data
    acc_data = pd.read_csv(os.path.join(data_path, "acc_data.csv"))

    acc_data["time"] = pd.to_datetime(acc_data["time"], unit='ms')
    acc_data["v"] = (acc_data["x"]**2 + acc_data["y"]**2 + acc_data["z"]**2)**0.5

    ### TAC reading
    tac_dir = os.path.join(data_path, "tac_readings")

    all_tac_data = pd.DataFrame(columns=["pid", "timestamp", "TAC_Reading"])

    for f in os.listdir(tac_dir):
        pid = f.split('_')[0]

        tac_data = pd.read_csv(os.path.join(tac_dir, f))

        tac_data["timestamp"] = pd.to_datetime(tac_data["timestamp"], unit='s')
        tac_data["pid"] = pid

        all_tac_data = all_tac_data.append(tac_data)
    
    # merge so that every tac reading is associated to the last 30 minutes of acc readings
    data = pd.merge_asof(
        acc_data.sort_values('time'),
        all_tac_data.sort_values('timestamp'),
        left_on='time',
        right_on='timestamp',
        by='pid',
        tolerance = pd.Timedelta('30minutes'),
        direction='backward'
    )[["pid", "time", "timestamp", "v", "TAC_Reading"]]

    data = data.groupby(['pid', 'timestamp', 'TAC_Reading'])['v'].apply(lambda x : list(x[-100:]))
    
    data.to_csv(os.path.join(data_path, "processed_data.csv"))

if __name__ == "__main__":
    process_data("train")
    process_data("test")