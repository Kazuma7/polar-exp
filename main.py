import cv2 as cv

cv.namedWindow("polarCGH", cv.WINDOW_NORMAL)   
for i in range(255):
    print("color_check:" + str(i))
    filename = "image/checker_" + str(i) + ".png"
    polarCGH = cv.imread(filename)
    #window詳細設定
    cv.setWindowProperty("holo", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN) 
    #windowをセカンドディスプレイに合わせる
    polarCGH = polarCGH[int((1024-600)/2):int((1024-600)/2+600), int((1024-792)/2):int((1024-792)/2+792)]
    cv.moveWindow("polarCGH", 1921, 0) 
    #CGHを反転
    polarCGH = cv.flip(polarCGH, 0)                                                       
    cv.imshow("polarCGH", polarCGH)  
    cv.waitKey(0)

