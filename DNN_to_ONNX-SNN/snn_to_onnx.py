import onnx

# 기존 ONNX 모델을 Load 하고 SNN-ONNX 로 변환
# 활성화 함수 LIF 형태로 변환
class convert_snnOnnx:
    def __init__(self):
        return

    # input path, result_path, neuron type
    def run(self, onnx_path, result_path, neuron_type):
        sn_index = 1  # 활성화 함수 이름 라벨링 필요 변수

        # ONNX MODEL LOAD
        onnx_model = onnx.load(onnx_path)
        onnx_model.producer_name = 'snn2onnx'
        node_len = len(onnx_model.graph.node) # 13

        # 각 ONNX node 들 접근.
        for index in range(node_len):
            # 각 op_type 들이 relu, sigmoid, tanh 등이면 neruon_type 으로 변경 (LIF)
            # LIF_1, LIF_2, LIF_3 ... 이렇게 변환해나감.
            op_type = onnx_model.graph.node[index].op_type.lower() # 다 소문자로 변경

            # 활성화 함수가 relu, sigmoid, tanh 이면 -> LIF 로 변환
            if op_type == "lif" or op_type == "sigmoid" or op_type == "tanh":
                onnx_model.graph.node[index].op_type = neuron_type  # 문자열
                onnx_model.graph.node[index].name = neuron_type + "_" + str(sn_index)
                sn_index = sn_index + 1
        onnx.save(onnx_model, result_path)

if __name__ == "__main__":
    onnx_file_path = "model/lenet-1.onnx"
    result_file_path = "model/lenet-1_snn.onnx"
    cso = convert_snnOnnx()  # 객체 생성
    cso.run(onnx_file_path, result_file_path, "LIF")  # 활성화함수 LIF 로 변환
    print('변환완료')

