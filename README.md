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



