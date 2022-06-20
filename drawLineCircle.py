def drawLineCircle(cx, xy, red, borderSize, img):

    a = cx
    b = xy
    r = red

    for x in range((a-r), (a+r)):
        for y in range((b-r), (b+r)):
            if (x-a)**2 + (y-b)**2 <= r**2:
                img[x, y] = 255

    r = red - borderSize

    for x in range((a-r), (a+r)):
        for y in range((b-r), (b+r)):
            if (x-a)**2 + (y-b)**2 <= r**2:
                img[x, y] = 000

if __name__ == "__main__": 
    
    import numpy as np
    import cv2 as cv

    img = np.zeros([500, 700], dtype=np.uint8)

    drawLineCircle(cx=250, xy=350, red=50, borderSize=1, img=img)

    cv.imshow("drawLineCircle", img)
    cv.waitKey(0)
    cv.destroyWindow