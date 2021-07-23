import cv2
import dropbox
import time
import random

start_time= time.time()

def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result= True
    number=random.randint(0,100)
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name="img" + str(number) + ".jpg"
        cv2.imwrite(img_name, frame)
        start_time=time.time()
        result= False
    return img_name
    print("snapshot taken of the chapters you have completed.")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = '-biOiMM0yLL4AAAAAAAAAAfTXdghR_YPHh7HZKyhcf75EcWpLFyN-osG2livBAi1D'
    fileFrom = img_name
    fileTo = '/ScreenshotsOfEachChapter/' + (img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(fileFrom, 'rb') as f:
        dbx.files_upload(f.read(), fileTo, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=10):
            print("You should have completed reading a chapter of the book.")
            name=take_snapshot()
            upload_file(name)

main()
        