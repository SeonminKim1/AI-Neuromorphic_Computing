# Neuromorphic_Computing
- 뉴로모픽 아키텍처 기반 자율형 IoT 응용 통합개발환경
- (Integrated Development Environment for Autonomic IoT Applications based on Neuromorphic Architecture)

Neuromorphic Computing 연구
Member : ISYSLAB - 김선민, 진선미, 이지영, 한병현


### 1. 뉴로모픽 ONNX-ML 기본 (20.06.15)
- ONNX, ONNX Runtime, Scikit-learn to ONNX 조사
- Protobuf 공부
- ONNX Runtime Version 1.0 / 최신버전 Install 실패 / 최신버전에는 Pytorch 상으로 Training 기능이 
- Scikit Learn으로 Model Training 
- Skl2learn 이용하여 .ONNX Model Protobuf 형식으로 변환(Writing)
- Netron 이용 Visualizing

### 2. ONNX Runtime 조사 (20.07.07)
- Scikit-learn to .onnx 변환 내용추가
- Onnx Runtime (ORT) 조사 / Pytorch Training 기능, 다양한 플랫폼 등 에서 사용가능
- ONNX Runtime vs Scikit-learn Benchmarks 비교 (연산자 비교)
- ONNX Runtime 분석

### 3. ONNX Runtime 조사 + 지능형컴포넌트 항목 (20.07.20)
- ORT 조사 및 공부
- 지능형컴포넌트 레지스트리 (1) : Flask 기반의 ONNX 파일 관리 (웹 UI)
  - 기능 3가지 : 파일 리스트 확인 / 파일 등록 (upload) / 파일 다운 (Download)
  
- 지능형컴포넌트 레지스트리 (2) : ONNX Log 관리
  - 파일관리하면서 발생하는 Event 에 대한 Log 남기기

### 4. 지능형 컴포넌트 레지스트리 v1.0 완성 (20.8.4)
#### 지능형 컴포넌트 레지스트리 기능 구현 
- (1) ONNX 파일 리스트 보기
- (2) ONNX 파일 Download 하기
- (3) ONNX 파일 Upload 하기
- (4) ONNX 파일 Netron 이용 시각화하기
  - Python에 Netron 설치 후 python 코드 이용 cmd 명령어 실행 방식
- 결과 링크 : [https://github.com/neurom-iot/onnx-registry]

### 5. Nengo, Nengo-DL / ONNX Runtime 공부 정리 및 내용 회의 및 향후방향 정리 (8.14 금)

#### -- ONNX Runtime --
- (1) .onnx 파일 구조를 어떻게 읽어오는지 (key-value로 구성되어있는 protobuf를 어떻게 읽어오는지?) 
- (2) 읽어온 후 ONNX-RUNTIME 추론시 onnx-runtime 클래스 중 어디를 참조하는지-아마 nodeArg)

#### -- Nengo –
- (1) Nengo-dl 사용법 공부 (API)
- (2) Nengo-dl 에서 Tensorflow를 이용한 LIF 작동 공부


### 핵심 참고 문헌
- https://www.nengo.ai/nengo-dl/examples/from-tensorflow.html // nengo-DL Tensorflow와 코드비교
- https://www.nengo.ai/nengo-dl/simulator.html // nengo-dl simulator서 data 확인
- https://www.nengo.ai/nengo-dl/reference.html // nengo-dl api document
- https://forum.nengo.ai/t/saving-the-model-after-training-in-nengo-core/1176/5 // nengo 모델 가중치 저장하고서, 불러와서 반영하는 법.
- https://github.com/microsoft/onnxruntime/blob/master/docs/Versioning.md // onnxruntime, onnx version 호환 
- https://github.com/microsoft/onnxruntime/blob/master/docs/AddingCustomOp.md // onnxruntime adding new operator

### 6. onnxruntime 관련 자체 정리 (20.09.09)
- (1) ONNX Runtime의 Inference 과정 (ONNX 연산자 호출 및 Load 과정)
- (2) Custom ONNX 연산자를 만들어서 추가하는 방법(protobuf로 감싸서 구조 정의하는 것과는 다름)
- (3) (09.10 회의 결론)
   - ONNX Runtime 은 C API 를 참조하는 것으로 확인/ pybind_state.py, ONNXRuntime 1.0 github 파일 폴더에서 py 파일안에 C관련 API가 있음4
   - pybind 로 연결시키는 것으로 파악.
   
### 7. ONNX 레지스트리 업데이트 & ONNX 모델 추론 시스템 구현
- (1) ONNX 레지스트리
  - download, visualization 버튼 이동
    - (case1) 목록 리스트 이름 클릭시 - 새로운 창 뜨고 download나 visualization
    - (case2) 목록 리스트 안에 항목으로 download or visualization 버튼
  - visualization 화면에서, 상대에 그래프 정보 관련 출력 (Visualization 화면 꾸미기)
    - Prediction REST API
 - (2) ONNX 모델 추론 시스템 구현
  - 해당 ONNX 판별식(API) 짜기
    - ML, DL / SNN 구분 API
  - 각 모델 Type 따라 추론 시스템 구현
    - SNN -> Nengo -> Nengo Simulator ==> 1차년도 Upgrade
    - DL / ML -> ONNX Runtime ==> ONNX Runtime - run() 메소드 이용

### 8. 7번내용 심화
- (1) ONNX 레지스트리
    - download, visualization
    - 추론 결과 반환하는 RESTFul API
- (2) 판별식 update
    - 1차구분 : SNN 인지 아닌지 (SNN 일경우 Nengo 모델로 변환) - 활성화함수로 체크
    - 2차구분 : SNN이 아닌경우 ML인지, DL인지 연산자 형태로 구분 - 연산자로 체크
- (3) .NPZ 파일 분석 및 Nengo 가중치 ONNX 삽입

### 9. KCS 2020 논문투고 및 마무리
- (1) ONNX 레지스트리 관리
  - 메인기능 : Upload 기능, Download 기능, 목록 View 기능, 모델 Visualization 기능
- (2) ONNX 모델 판별법
  - 판별기준 1차, 2차 정리 완료
- (3) .NPZ 파일 분석 및 Nengo <-> ONNX 모델 가중치 교환
  - Keras 기반의 모델에 .npz 가중치 삽입 및 교환
- (4) KCS 2020 논문 투고 완료
