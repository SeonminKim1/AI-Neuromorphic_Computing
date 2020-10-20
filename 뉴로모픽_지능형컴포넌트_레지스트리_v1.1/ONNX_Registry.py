from flask import Flask, render_template, send_from_directory, request, redirect,send_file
import os, time

# Flask 객체 생성
app = Flask(__name__)

# folder name
onnx_folder_path = 'onnx_folder/'
log_file_path = 'log_folder/'

# main page
@app.route('/', methods=['GET','POST'])
def main_page():
    # 파일 기본 정보들 출력
    file_list = get_filelist() # 파일 이름 리스트 반환
    file_latest_time = get_file_latest_time(file_list) # 파일 마지막 수정시간 반환
    file_size = get_filesize(file_list) # 파일 크기 반환
    # -------------------------------------------------------
    
    # upload
    if request.method == 'POST':
        upload_process()

    # -------------------------------------------------------

    # log 데이터
    fr = open(log_file_path + "log.txt", 'r+')
    log_list = fr.readlines()
    print(type(log_list), log_list)
    fr.close()

    return render_template('mainpage.html',
                           file_list=file_list,
                           file_latest_time = file_latest_time,
                           file_size = file_size,
                           log_list = log_list,
                           zip = zip, # zip이란 python 함수도 jinja에 같이 넘긴 것
                           )

# upload 기능 + log write 기능
def upload_process():
    f = request.files['file']
    print(f)
    file_name = f.filename
    file_path = os.getcwd() +'\\' + onnx_folder_path[:-1] +'\\' # 파일 저장 위치 경로
    f.save(file_path + file_name)  # 저장할 경로 + 파일명
    print(file_path + file_name + '에 파일 저장 완료')

    user_ip = request.remote_addr
    upload_time = time.strftime('%y-%m-%d %H:%M:%S')

    # txt 파일 저장
    f = open(log_file_path+"log.txt", 'a+')
    f.write(
        '(' + upload_time + ') | ' + 'Upload_Success     ' + ' | ' + file_name + ' | ' + user_ip + ' | ' + file_path + '\n')
    f.close()
    return redirect('/')

# download 기능
@app.route('/download/<filename>', methods=['GET','POST'])
def download(filename):
    return send_from_directory('onnx_folder', filename) # directory 명, 파일이름

# 시각화 python cmd 명령어 실행으로 구현
@app.route('/visualization', methods=['GET','POST'])
def visualization():
    if request.method == 'POST':
        files = os.listdir(onnx_folder_path) #지정된 디렉토리의 전체 파일 목록 가져오기
        print(files)
        for x in files:
            if(x == request.form['file']): # 파일이름이면
                os.system('start chrome http://localhost:8080') # chrome 으로 웹 페이지 띄우기
                os.system('Netron {}'.format(os.getcwd()+ '\\' + onnx_folder_path[:-1])) # netron 으로 파일 실행
                return

## 기능함수들
# 1. 파일 이름 리스트 반환
def get_filelist():
    # 파일 리스트 만들기 - onnx 파일만 출력
    dir_list = os.listdir(onnx_folder_path)
    file_list = []
    for x in dir_list:
        if '.onnx' in x or '.txt' in x:
            file_list.append(x)
    return file_list
def get_file_latest_time(file_list):
    # 파일 최근 수정날짜 정보
    latest_time = []
    latest_ls = latest_time.append
    for i in file_list:
        latest_ls(time.ctime(os.path.getmtime(onnx_folder_path + i)))  ## 최근 수정날짜 정보
    return latest_time
def get_filesize(file_list):
    # 파일 크기
    file_size = []
    size_ls = file_size.append

    # 리스트 정보들 만들어서 넘겨주기
    for i in file_list:
        size_ls(str(os.path.getsize(onnx_folder_path + i)) + ' B')  ## 파일크기
    return file_size

#서버 실행
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5060, debug = True)

