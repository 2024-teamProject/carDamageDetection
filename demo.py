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
        'Type',
        ('Image', 'Video', 'Youtube'), disabled=True, index=0)
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





# !!! DRAG로 파일 업로드 할 때 __ in progress
# if (len(filename_extension) > 0):
#     st.text("")
#     # 입력 경로
#     input_file = st.file_uploader("파일을 선택해주세요.", type=filename_extension)
#     if input_file:
#         input_image_preview = get_bytesio_from_bytes(input_file.getvalue())
#         # print('type(str(input_file.getvalue())) 타입: ', type(str(input_file.getvalue())))

#         # print('input_image_preview 타입: ', type(input_image_preview))
#         output_file_preview = model(str(input_file.getvalue()))
#         # print('input_file.getvalue() 타입: ', type(input_file.getvalue()))

#         # for result in output_file_preview:
#         #     res = result.save(filename="data/result/image.jpg")
#         # 레이아웃 선정
#         cols = st.columns(2)
#         for i in range(1,3):
#             if (i == 1):
#                 cols[0].image(input_image_preview)
#             # elif ():
#                 # cols[1].image(res)
# else:
#     print('Youtube URL section')
#     input_file = []


st.write('/Users/jjnoh/opt/anaconda3/envs/py3.12/streamlit/data/sample_images')
folder_path = st.text_input('Input folder path')
file_paths = []
if os.path.isdir(folder_path):
    for fn in os.listdir(folder_path):
        fp = f'{folder_path}/{fn}'
        if os.path.isfile(fp):
            file_paths.append(fp)
input_file = st.selectbox('Select file', options=file_paths)
print('어제까지의 이미지의 타입: ', type(input_file))


# 클릭액션
## 클릭 스테이터스 변환
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
## 모델 런 액션
def test_action():
    st.session_state.clicked = True
    with st.container(border=True):
        st.write('Button clicked!')
        st.slider('Select a value')

model = YOLO(custom_model, device_type)

if input_file:
    col_l, col_r = st.columns(2)
    col_l.image(f'{input_file}', caption='Original')
    output_file_preview = model(input_file)
    for result in output_file_preview:
        res = result.save(filename="./result.jpg")
    col_r.image(f'{res}', caption='Predicted')


st.button('Run', on_click=test_action)


