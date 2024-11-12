import streamlit as st
from ultralytics import YOLO
from PIL import Image
from io import BytesIO
import torch
import sys
import os
import matplotlib.pyplot as plt

# header
st.title('Car damage detection ⚙️')
st.sidebar.title('Option')

# left bar menu
filename_extension = []
data_type = st.sidebar.radio(
        'Type', 'Image')
if (data_type == 'Image'):
    filename_extension = ['jpg','jpeg','png']
elif (data_type == 'Video'):
    filename_extension = ['mov','mpv','avi', 'mp4']
model_type = st.sidebar.radio(
        'Model',
        ('YOLOv5n', 'YOLOv8n'))
#if (model_type == 'YOLOv5n'):
#     custom_model = './models/v5_best.pt'
if (model_type == 'YOLOv8n'):
    custom_model = './models/v8_best.pt'
if torch.cuda.is_available():
    device_type = st.sidebar.radio(
        'Device',
        ('cpu', 'cuda'), disabled=True, index=1)
else:
    device_type = st.sidebar.radio(
        'Device',
        ('cpu', 'cuda'), disabled=True, index=0)


# bytes를 bytesio형태로 변환
def get_bytesio_from_bytes(image_bytes):
    image_io = BytesIO(image_bytes)
    return image_io
# for err fix
sys.setrecursionlimit(10**7)


folder_path = st.text_input('Input folder path')
file_paths = []
if os.path.isdir(folder_path):
    for fn in os.listdir(folder_path):
        fp = f'{folder_path}/{fn}'
        if os.path.isfile(fp):
            file_paths.append(fp)
input_file = st.selectbox('Select file', options=file_paths)

print(input_file)
model = YOLO(custom_model, device_type)

if input_file:
    col_l, col_r = st.columns(2)
    col_l.image(f'{input_file}', caption='Original')
    output_file_preview = model(input_file)
    for result in output_file_preview:
        res = result.save(filename="./result.jpg")
    col_r.image(f'{res}', caption='Predicted')


