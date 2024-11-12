# 차량 파손 부위 감지 및 위치 파악

** 개요: **
본 프로젝트는 차량 파손부위 감지하고 위치를 파악하는 기능을 구현합니다. YOLO모델을 기반으로 하며, Roboflow의 Car damage_2 Computer Vision Project by Socar 데이터셋을 사용했습니다. 


** 주요 기능: **
목적에 맞게 학습된 모델을 이용하여 차량 파손부위 위치 파악


** 사용 모델: **
- YOLOv8 
- YOLOv5

** 사용 데이터: **
[Roboflow data](https://universe.roboflow.com/socar/car-damage_2/browse?queryText=&pageSize=50&startingIndex=50&browseQuery=true)


** 전처리: **
- ** Auto-Orient: Applied **
- ** Resize: Stretch to 416x416 **


** 증강: **
- ** Outputs per training example: 3 **
- ** Flip: Horizontal, Vertical **
- ** Crop: 0% Minimum Zoom, 20% Maximum Zoom **
- ** Rotation: Between -15° and +15° **
- ** Shear: ±15° Horizontal, ±15° Vertical **
- ** Saturation: Between -25% and +25% **
- ** Brightness: Between -25% and +25% **
- ** Exposure: Between -25% and +25% **



**구현:**
<img width="1436" alt="image" src="https://blog.kakaocdn.net/dn/bjzse7/btsKHp0Ub4A/ReKKTJeOONZbFzSASkVuIk/img.gif">


** 웹사이트 주소: **
[https://teamcheckcard.streamlit.app/](https://teamcheckcard.streamlit.app/)


** 라이선스: **
MIT 라이선스
