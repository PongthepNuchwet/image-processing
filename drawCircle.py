def drawCircle(cx, xy, red, img):

    a = cx
    b = xy
    r = red

    for x in range((a-r), (a+r)):
        for y in range((b-r), (b+r)):
            if (x-a)**2 + (y-b)**2 <= r**2:
                try:
                    img[x, y] = 255
                except:
                    pass

if __name__ == "__main__": 
    
    import numpy as np
    import cv2 as cv

    img = np.zeros([500, 700], dtype=np.uint8)
    
    drawCircle(cx=430, xy=650, red=100, img=img)

    cv.imshow("drawCircle", img)
    cv.waitKey(0)
    cv.destroyWindow