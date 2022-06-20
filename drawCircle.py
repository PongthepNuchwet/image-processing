def drawCircle(cx,xy,red,img) :

    a = cx
    b = xy
    r = red

    for x in range((a-r), (a+r)):
        for y in range((b-r), (b+r)):
            if (x-a)**2 +(y-b)**2 <= r**2:
                try :
                    img[x, y] = 255
                except :
                    pass

    

