import os 
import tarfile
from six.moves import urllib 
import pandas as pd
import matplotlib.pyplot as plt  
import numpy as np 

PATH = "/Users/AbrahamHussain/Desktop/IGN Data Science /ign.csv"
ign_data = pd.read_csv(PATH, names=["score phase", "title", "url", "platform", "score", "genre", "editor's choice ", "release year", "release month", "release day"])

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices, data.iloc[test_indices]
