import imquality.brisque as brisque
import PIL.Image
import os

image_folder = r'C:\Users\seanl\Documents\01_UBC\Academics\Year 4\NVD\MPACT\Images'
sum_score = 0
i = 0
score = []
filename = []
for root, dirs, files in os.walk(image_folder, topdown=False):
    for file in files:
        print("Scoring " + file)
        img = PIL.Image.open(os.path.join(root,file))
        score.append(brisque.score(img))
        filename.append(file)
        print(score[i])
        sum_score = sum_score + score[i]
        i = i + 1
        
average_score = sum_score/i
        
print("Average Score: " + str(average_score))