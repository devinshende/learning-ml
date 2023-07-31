from tqdm import tqdm
import pandas as pd
import tensorflow as tf
from pprint import pprint
from rich import print as show
from datetime import datetime, timedelta
import time
import numpy as np
import seaborn as sns
import ast
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from rich import print

simulation_runs = pd.read_csv("simulation_runs.csv")

def calculate_area(str):
    #where p1 in the bottom left = (x1,y1) and p2 in the bottom left = (x2,y2)
    L = ast.literal_eval(str)
    x1, y1, x2, y2 = float(L[0]), float(L[1]), float(L[2]), float(L[3])
    
    area = (x2-x1) * (y2-y1)
    return abs(area)

def normalize(series):
    return MinMaxScaler().fit_transform(np.array(series).reshape(-1,1))

useful_columns = [
    "sim_time",
    # "run_end",
    # "run_start",
    # "output",
    "extent",
    "surface_moisture",
    "timestep",
    "wind_direction",
    "wind_speed",
    "canopy_moisture",
]
run_data = simulation_runs.get(useful_columns)
column = run_data.apply(lambda row: calculate_area(row["extent"]), axis=1)
run_data = run_data.assign(area=column)


run_data = run_data.drop(columns="extent")

run_data = run_data.drop_duplicates()

print(run_data.count())

y = np.array(run_data["sim_time"])
X = run_data.drop(columns="sim_time")

for col in X.columns:
	X[col] = normalize(X[col])

print(X.head())
print(y)

X_train, X_test, y_train, y_test = train_test_split(     
	X, y, test_size=0.2, random_state=42)
X_train = np.array(X_train)


model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(6,)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10)
])
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
)

model.fit(
    ds_train,
    epochs=6,
    validation_data=ds_test,
)