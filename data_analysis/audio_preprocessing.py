from glob import glob
import os.path
import subprocess

# 특정확장자를 가진 목록뽑기(ex: *.opus) or 전부 다 가져오기(*)
files = glob(r'D:\wav\*.opus')

for x in files:
    if not os.path.isdir(x):  # 파일만 걸러내기
        filename = os.path.splitext(x)  # 확장자와 순수파일명 구분하기

        # MR버전 제거
        if 'instrumental' in filename[0] or '(inst)' in filename[0]:
            os.remove(x)
        else:
            # temp(임시), m4a(중복) 파일은 제거
            if filename[1] == '.temp' or filename[1] == '.m4a':
                os.remove(x)
                print('{} ---- removed'.format(filename))
            else:
                # convert opus to wav
                try:
                    # 순수파일명에 wav확장자 붙이기
                    os.rename(x, filename[0]  + '.wav')
                except:
                    # 중복된 wav 파일이 있을 경우 제거
                    os.remove(x)
                    print('{} ---- removed'.format(filename))

# separate audio signal
original_files = glob(r'D:\voice_samples\*.wav')
for y in original_files:
    y=original_files[0]
    # command = 'spleeter separate -i ' + '"' + y + '"' + " -p spleeter:4stems-16kHz" + ' -o "D:\\wav\\separated/"'
    command = 'spleeter separate -i ' + '"' + y + '"' + ' -o "D:\\wav\\separated/"'
    subprocess.run(command)
