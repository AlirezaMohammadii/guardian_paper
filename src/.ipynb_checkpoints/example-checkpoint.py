import os
import numpy as np


def read_npy_files(directory):
    npy_files = [file for file in os.listdir(directory) if file.endswith(".npy")]

    for npy_file in npy_files:
        file_path = os.path.join(directory, npy_file)
        try:
            data = np.load(file_path)
            print(f"Loaded {npy_file} successfully. Shape: {data.shape}")
            # Process the loaded data as needed
        except Exception as e:
            print(f"Error loading {npy_file}: {str(e)}")


if __name__ == "__main__":
    npy_directory = "F:/1.Deakin university/Python/13_10_2023_My_Project_1/guardian_paper/data/sample_dataset/npy"
    read_npy_files(npy_directory)
