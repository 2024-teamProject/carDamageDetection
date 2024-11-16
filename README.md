# 차량 파손 부위 감지 및 위치 파악 (Car Damage Detection)
<br/>

### 개요:
본 프로젝트는 차량 파손부위 감지하고 위치를 파악하는 기능을 구현합니다. YOLO모델을 기반으로 하며, Roboflow의 Car damage_2 Computer Vision Project by Socar 데이터셋을 사용했습니다. 


#### 주요 기능:
목적에 맞게 학습된 모델을 이용하여 차량 파손부위의 위치를 파악합니다.


#### 사용 모델:
- YOLOv8 
- YOLOv5


#### 사용 데이터:
[Roboflow data](https://universe.roboflow.com/socar/car-damage_2/browse?queryText=&pageSize=50&startingIndex=50&browseQuery=true)


#### 전처리:
-  Auto-Orient: Applied
-  Resize: Stretch to 416x416


#### 증강:
-  Outputs per training example: 3
-  Flip: Horizontal, Vertical
-  Crop: 0% Minimum Zoom, 20% Maximum Zoom
-  Rotation: Between -15° and +15°
-  Shear: ±15° Horizontal, ±15° Vertical
-  Saturation: Between -25% and +25%
-  Brightness: Between -25% and +25%
-  Exposure: Between -25% and +25%


#### 실험:
- Aihub에 있는 Socar 차량 파손 데이터를 이용하여 초기 모델을 세팅했습니다.
- 하지만 학습율이 오르지 않아 Roboflow에 있는 Socar car damage 2로 데이터셋을 변경했습니다.
- 100에포크에서 mAP가 증가하는 형태의 그래프가 보이기에 300에포크로 증가시켜 진행했습니다.
- 300에서도 성능은 나왔지만 해당 데이터셋이 멀티클래스라 분산된다고 판단해 클래스를 하나 제거했습니다.
- 3개로 줄인 클래스의 데이터를 가지고 500에포크로 학습시켜 정확도를 크게 높였습니다.


<br/>
* Labeled
<img width="450" alt="image" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdrnL23%2FbtsKFgdRf5j%2FnH6YmGXljivxfBtZF4mQ50%2Fimg.png">
* Predicted
<img width="450" alt="image" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmITWz%2FbtsKHwThOXh%2FlVl7aDSzxS13X1zTxyKpsk%2Fimg.png">

<br/>
* Result
<img width="800" alt="image" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fv2mo2%2FbtsKHeL44XW%2F0DrGxXEFChLbCd0HQMfajK%2Fimg.png">


#### 구현:
<img width="1436" alt="image" src="https://blog.kakaocdn.net/dn/bjzse7/btsKHp0Ub4A/ReKKTJeOONZbFzSASkVuIk/img.gif">


#### 웹사이트 주소:
[https://teamcheckcard.streamlit.app/](https://teamcheckcard.streamlit.app/)


#### 라이선스:
MIT 라이선스
