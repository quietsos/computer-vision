import cv2
img = cv2.imread('data/sohan.jpg')

while True:
    cv2.imshow('sohan',img)
    
    # IF we've waited at least 1 ms AND we'have pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

        
cv2.destroyAllWindows()
 