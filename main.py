import cv2 as cv
from PIL import Image

class Teste:
    def draw_image(self, image_path:str, number:int) -> None:
        def newImg(image_path):
            to_correct = open(image_path).readlines()
            image_todraw = []

            i = 0
            for image in to_correct:
                image = image.replace(']', '')
                image = image.replace('[', '')
                image = image.rstrip()
                image = image.split(', ')

                image[0] = int(image[0])
                image[1] = int(image[1])
                image[2] = int(image[2])

                image_todraw.append(image)

            img = Image.new('RGB', (1280, 720), 'white')
            
            image_order = 0
            i = 0
            
            while i < 720:
                j = 0
                while j < 1280:
                    img.putpixel((j, i), (image_todraw[image_order][0], image_todraw[image_order][1], image_todraw[image_order][2]))
                    image_order = image_order + 1
                    j = j + 1
                i = i + 1

            img.save('frame_'+str(number)+'.png')

            return img

        wallpaper = newImg(image_path)
        wallpaper.show('frame')

    def inital(self):
        videos = ["Paladins/BK_and_Raum", "Paladins/BK_triple", 
                  "Paladins/Jenos_catch_Ash", "Paladins/Viktor_have_wings"]
        sequence_frames = []

        for video in videos:
            back = cv.createBackgroundSubtractorMOG2()
            capture = cv.VideoCapture(cv.samples.findFileOrKeep(video+".mp4"))

            if not capture.isOpened:
                print('unable to open')
                exit(0)

            while True:
                ret, frame = capture.read()

                if frame is None:
                    break

                """cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
                cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
                        cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))"""
                
                print(str(capture.get(cv.CAP_PROP_POS_FRAMES)))
                cv.imshow('Frame', frame)
                
                keyboard = cv.waitKey(30)
                if keyboard == 'q' or keyboard == 27:
                    break
        
                file = open(video+"/frame_"+str(capture.get(cv.CAP_PROP_POS_FRAMES))+".txt", "w")
                correction = frame.tolist()

                for pixel_line in correction:
                    for pixel in pixel_line:
                        file.write(str(pixel)+"\n")

                file.close()

if __name__ == "__main__":
    t = Teste()
    t.inital()
    #t.draw_image("Paladins/BK_and_Raum/frame_"+str(i)+".txt", i)

