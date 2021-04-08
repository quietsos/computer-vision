import cv2
import numpy as np
import matplotlib.pyplot as plt



#############
## Function ##
##############


def drawImage(event,x,y,flags,param):
    
    if (event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img,(x,y),50,(0,0,255),-1)
    
    if(event == cv2.EVENT_RBUTTONDOWN):
        cv2.rectangle(img,(x,y),(x+50,y+50),(255,0,0),3)


        


#################################################
## connect image window with callback function ##
#################################################

cv2.namedWindow(winname ='draw')
cv2.setMouseCallback('draw',drawImage)

###############
## Show image ##
###############

img = np.zeros((512,512,3))
plt.imshow(img)

while True:
    cv2.imshow('draw',img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()