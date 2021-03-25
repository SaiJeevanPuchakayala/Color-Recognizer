# Importing Required Libraries
import cv2
import numpy as np
import pandas as pd


# Reading The Image File
img = cv2.imread("Images/image1.jpg")

# Reading Color Names from CSV file
df = pd.read_csv('Color Names and Values.csv')

# Color Recognition Function
def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(df)):
        d = abs(R- int(df.loc[i,"R"])) + abs(G- int(df.loc[i,"G"]))+ abs(B- int(df.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            color_name = df.loc[i,"Color_Name"]
    return color_name

# Mouse Click to get Color Name
clicked = False
r = g = b = xpos = ypos = 0

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        
# Resultant Window Loop
cv2.namedWindow('Color Recognizer')
cv2.setMouseCallback('Color Recognizer',mouse_click)


while(1):

    cv2.imshow("Color Recognizer",img)
    if (clicked):
   
        # Text Background Rectangular Bar 
        cv2.rectangle(img,(0,20), (1500,60), (b,g,r), -1)

        # Text To Display Color_name and RGB values 
        text = "Color Name: "+recognize_color(r,g,b)+" | " +' R='+ str(r) + " | " + ' G='+ str(g) + " | " + ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2,cv2.LINE_AA)

        # For light Colors Text will be in Black Color
        if(r+g+b>=600):
           cv2.putText(img, text,(50,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False
        

# Click 'ESC' to break the loop    
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()