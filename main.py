import cv2 as cv

class Main:
    videos = ["Paladins/BK_and_Raum.mp4", "Paladins/BK_triple.mp4", 
              "Paladins/Jenos_catch_Ash.mp4", "Paladins/Viktor_have_wings.mp4"]
    sequence_frames = []

    for video in videos:
        i = 0

        back = cv.createBackgroundSubtractorMOG2()
        capture = cv.VideoCapture(cv.samples.findFileOrKeep(video))

        if not capture.isOpened:
            print('unable to open')
            exit(0)

        while True:
            ret, frame = capture.read()
            if frame is None:
                break

            fgMask = back.apply(frame)

            cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
            cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
            
            cv.imshow('Frame', frame)
            cv.imshow('FG Mask', fgMask)

            if i == 10:
                sequence_frames.append(frame)
            
            keyboard = cv.waitKey(30)
            if keyboard == 'q' or keyboard == 27:
                break

            i = i + 1
    
    file = open("frames_paladins.txt", "w")
    file.write(str(sequence_frames[0].tolist()))
    file.close()

if __name__ == "__main__":
    pass
