import cv2
import numpy as np



##############
## FUNCTION ##
##############

def draw_circle(event,x,y,flags,param):   #creating function for draw on image with mouse
    
    if event == cv2.EVENT_LBUTTONDOWN:      # check the condition is mouse left button are taps
        cv2.circle(img,(x,y),20,(0,255,0),-1)   #drawing the circle filled with color on existing image




############################################################
## CONNECT CALLBACK FUNCTION TO SHOWING IMAGE WITH OPENCV ##
############################################################

cv2.namedWindow(winname='my_drawing')    #set the window name
cv2.setMouseCallback('my_drawing',draw_circle) #connect window with callback function


###############################
## SHOWING IMAGE WITH OPENCV ##
###############################


# img = np.zeros(shape=(512,512,3),dtype=np.int8)
img = np.zeros((512,512,3),np.int8 )   #creating an empty image

while True:
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()





