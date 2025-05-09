import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

class DataReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None
 
    def read(self):
        if self.filepath.endswith('.parquet'):
            self.data = pd.read_parquet(self.filepath)
        elif self.filepath.endswith('.csv'):
            self.data = pd.read_csv(self.filepath)
        elif self.filepath.endswith('.txt'):
            self.data = pd.read_csv(self.filepath, header=None)
        else:
            raise ValueError("Unsupported file format")
        return self.data
 
    def show_head(self, rows=5):
        if self.data is not None:
            print(self.data.head(rows))
        else:
            print("No data loaded. Call read() first.")

    def load_and_show_cifar(self, count=1):
        print("\nLoading and displaying CIFAR-10 dataset...")
        (images, labels), _ = tf.keras.datasets.cifar10.load_data()
        print(f"Loaded {len(images)} images.")

        plt.figure(figsize=(10, 2))
        for i in range(count):
            plt.subplot(1, count, i + 1)
            plt.imshow(images[i])
            plt.axis('off')
            plt.title(f"Label: {labels[i][0]}")
        plt.show()
 
# File paths
files = [
    "/Users/nencyanghan/Desktop/MSE800/week4/Sample_data_2.parquet",
    "/Users/nencyanghan/Desktop/MSE800/week4/sample_text.txt",
    "/Users/nencyanghan/Desktop/MSE800/week4/sample_junk_mail.csv"  
]
 
# Read and show each file
for file in files:
    print(f"\nReading file: {file}")
    reader = DataReader(file)
    reader.read()
    reader.show_head(2)
    reader.load_and_show_cifar(count=1)
