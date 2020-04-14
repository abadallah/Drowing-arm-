import cv2 as cv
import random as rng
import sys
import numpy as np
import matplotlib.pyplot  as plt
from venv.rdp import rdp
import Check_In
rng.seed(12345)


def thresh_callback():

    #Remove the Next Line if U will Use Canny
    #canny_output = src_gray


    canny_output = cv.Canny(src_gray,50,75)

    # Detect edges using Canny
    cv.imshow('canny_output', canny_output)

    # findContours
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

    # Draw contours To Show
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)

   #To Print All Countours List In test
    np.set_printoptions(threshold=sys.maxsize)

    fina= FindOuterCountour(contours,hierarchy)
    # LOOP to draw All Countours to show
    for i in range(len(fina)):
            color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
            cv.drawContours(drawing, fina, i, color)

    # Show in a window
    cv.imshow('Contourxs', drawing)
    WriteInfile(fina)



def FindOuterCountour(con,hei):
    #Solve Problem Of Double Iine if u usee canny
    #Work in Closed Shapes Only
    ResultCountours=[]
    ret = cv.matchShapes(con[2],con[5],1,1.0)
    dist = cv.pointPolygonTest(con[3],(con[5][0][0][0],con[5][0][0][1]),True)
    area = cv.contourArea(con[3])

    for i,c in enumerate(con):
        childindex=hei[0][i][2]
        if hei[0][i][0]==-2:
            pass
        elif childindex==-1:
          ResultCountours.append(c)

        elif(childindex>=0):
            if  len(c)>len(con[childindex]):
                ResultCountours.append(c)
                hei[0][childindex][0]=-2
            else:
                ResultCountours.append(con[childindex])







    print(len(ResultCountours))
    return ResultCountours





def WriteInfile(con):
    file = open("text.gcode", "w")
    PinUp = 1
    file.write("G30 Z0.1 \n")



    for a in con:
        mypass=[]
        jj=[]
        approx =rdp(a,0.9)
        for b in approx :
            #
            passone=[b[0][0],b[0][1]]
            mypass.append(passone)

        mypass.append([approx[0][0][0],approx[0][0][1]])
        jj=Check_In.chkin(mypass)
        for n,x in enumerate(jj):
             file.write("G1 X" + str(x[0]) + " Y" +
                               str(x[1]) + " F3500.00  E3500.00" + "\n")
             if PinUp == 1:
                file.write("G1 Z-2 F1200 E1200 \n")
                PinUp = 0
        PinUp=1
        file.write("G1 Z2 F1200 E1200 \n")



    file.close()




# Load source image


if __name__ == "__main__":
    #Read Image
    src = cv.imread('test32.jpg')

    # dsize
    #dsize = (500, 500)

    # resize image
    #src = cv.resize(src, dsize)

    #Convert BitmapImage To GrayScale Image and Rotate
    src_gray = cv.cvtColor(cv.flip(src,0,src) , cv.COLOR_BGR2GRAY)

    #prewitt
    #kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    #kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    #img_prewittx = cv.filter2D(src_gray, -1, kernelx)
    #img_prewitty = cv.filter2D(src_gray, -1, kernely)

    #cv.imshow("Prewitt X", img_prewittx)
    #cv.imshow("Prewitt Y", img_prewitty)

    #PerForme Blue To reduce the Noisy
    src_gray = cv.blur(src_gray, (2, 2))
    #Or Perform GaussianBlur

    #src_gray = cv.Laplacian(src_gray,cv.THRESH_BINARY)


   # Perform THreashold If We will not use canny
    #ret,src_gray = cv.threshold(src_gray,117,255,cv.THRESH_BINARY)


    #iF ther is No Image
    if src is None:
        exit(0)


    # Create Window
    cv.imshow("image",src)

    thresh_callback()
    cv.waitKey()
