from glob import glob
import os.path

json_files = glob(r'D:\meta_data\*.json')
for x in json_files:
    if not os.path.isdir(x):  # 파일만 걸러내기
        try:
            filename = os.path.splitext(x)  # 확장자와 순수파일명 구분하기
            new_filename = filename[0].replace('.json', '')
            os.rename(x, new_filename + '.json')
        except:
            print('error')