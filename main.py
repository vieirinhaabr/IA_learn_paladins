import cv2 as cv
from PIL import Image

class Teste:
    def draw_image(self, image_path:str) -> None:
        def newImg(image_path):
            to_correct = open(image_path).readlines()
            image_todraw = []

            for image in to_correct:
                image = image.replace(']', '')
                image = image.replace('[', '')
                image = image.rstrip()
                r, g, b = image.split()
                img_list = []
                image_todraw.append(img_list)

            print(image_todraw)

            img = Image.new('RGB', (1280, 720), 'white')
            
            i = 0
            for pixel_line in image_todraw:
                #print(i)
                j = 0
                for pixel in pixel_line:
                    #print(j)
                    #img.putpixel((j, i), (255,255,255))
                    j = j + 1
                i = i + 1

            img.save('frame.png')

            return img

        wallpaper = newImg(image_path)
        wallpaper.show('frame')

    def inital(self):
        videos = ["Paladins/BK_and_Raum.mp4"]
        """videos = ["Paladins/BK_and_Raum.mp4", "Paladins/BK_triple.mp4", 
                "Paladins/Jenos_catch_Ash.mp4", "Paladins/Viktor_have_wings.mp4"]"""
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

                cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
                cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
                        cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
                
                cv.imshow('Frame', frame)

                #sequence_frames.append(frame)
                
                keyboard = cv.waitKey(30)
                if keyboard == 'q' or keyboard == 27:
                    break
        
                file = open("Paladins/BK_and_Raum/frame_"+str(i)+".txt", "w")
                correction = frame.tolist()

                for pixel_line in correction:
                    for pixel in pixel_line:
                        file.write(str(pixel)+"\n")

                file.close()

                i = i + 1

if __name__ == "__main__":
    t = Teste()
    #t.inital()
    t.draw_image("Paladins/BK_and_Raum/frame_0.txt")

