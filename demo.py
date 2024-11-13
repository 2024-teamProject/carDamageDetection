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
if (model_type == 'YOLOv5n'):
     custom_model = './models/v5_best.pt'
elif (model_type == 'YOLOv8n'):
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

# upload img
uploaded_file = st.file_uploader('Choose Image to upload…', type = (["jpg", "jpeg"]))
if uploaded_file is not None:
    model = YOLO(custom_model, device_type)
    inputImg = Image.open(uploaded_file)

    col_l, col_r = st.columns(2)
    col_l.image(inputImg, caption='Original')
    outputImg = model(inputImg)
    for result in outputImg:
        res = result.save(filename="./result.jpg")
    col_r.image(res, caption='Predicted')


