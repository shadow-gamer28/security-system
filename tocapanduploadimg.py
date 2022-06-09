import cv2
import dropbox
import time
import random

start_time = time.time()
def take_snapshot():
    number=random.randint(0,100)
    video_Captureobject = cv2.VideoCapture(0)
    result=True
    while(result):
        ret, frame = video_Captureobject.read()
        img_name='img' + str(number) + '.png'
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result=False
    return img_name
    print("SNAPSHOT TAKEN!!!")
    video_Captureobject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BJK2oR-5gdEyyEOZOESE1wHGac2i75RIjM-iOr8r46vax0N9IHYjn8s11uexkeXGs-hvSOo7GKSo8wOu7zMBFceEYCD0Nz332eINXr1P4yqr7nCg1LNn159hkHrb18Nma1rjNQ8"
    file = img_name
    file_from = file
    file_to = '/newfolder/' + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f :
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED :) !!")

def main():
    while(True):
        if((time.time()-start_time)>=2):
            name=take_snapshot()
            upload_file(name)
main()