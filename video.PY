import cv2

def pVideo():
    vid=cv2.VideoCapture(0)
    while(vid.isOpened()):
        ret,frame=vid.read()
        cv2.imshow('Video',frame)
        cv2.waitKey(1)
    
    vid.release()
    cv2.destroyAllWindows()


def main():
    pVideo()
   

if __name__ == "__main__":
    main()