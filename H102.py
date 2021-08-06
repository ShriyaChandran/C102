import cv2
import dropbox
import time
import random

start_time= time.time()

def choose():
    print("Which subject will you be studying today?")
    print("1. SCIENCE")
    print("2. MATH")
    print("3. ENGLISH")
    print("4. SECOND LANGUAGE")
    choice= input("Enter the number here: ")

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
    access_token = '_Bgdhqo7_xYAAAAAAAAAARtC0Haxqrq_gp-4--NI8mQhI6AETdfOCU6sYMDQfMLo'
    fileFrom = img_name
    if(choice==1):
        fileTo = '/Science/' + (img_name)
    elif(choice==2):
        fileTo = '/math/' + (img_name)
    elif(choice==3):
        fileTo = '/english/' + (img_name)
    else:
        fileTo = '/Second language/' + (img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(fileFrom, 'rb') as f:
        dbx.files_upload(f.read(), fileTo, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")



def main():
    while(True):
        if((time.time()-start_time)>=5):
            print("You should have completed reading a chapter of the book.")
            name=take_snapshot()
            upload_file(name)

main()
        