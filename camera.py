import cv2
import datetime
import os


def takePicture():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Take a photo of your trash!")

    img_counter = 0

    while img_counter < 1:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            ct = datetime.datetime.now()
            print("current time:-", ct)

            # dt store timestamp of current date
            dt = ct.date()


            img_name = "opencv_frame_{}.png".format(img_counter)

            '''
            dir_path = os.path.dirname(os.path.realpath(img_name))
            foldername = f'{dt}-hack112-main'
            directory = f'{dir_path}\{foldername}'
            os.chdir(directory)
            '''

            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

            cam.release()
            cv2.destroyAllWindows()
