import cv2

img = cv2.imread("base.png")

median = cv2.medianBlur(img, 9)
cv2.imshow('base', img)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('median', median)
cv2.waitKey()
cv2.destroyAllWindows()

hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
v1 = cv2.inRange(hsv, (0, 0, 10), (15, 255, 200))
v2 = cv2.inRange(hsv, (160, 190, 50), (179, 255, 255))
v = cv2.add(v1,v2)
cv2.imshow('mascara', v)
cv2.waitKey()
cv2.destroyAllWindows()

final = cv2.bitwise_and(img, img, mask = v)
cv2.imshow('resposta', final)
cv2.waitKey()
cv2.destroyAllWindows()

S = 10
V = 10

def S_trackbar(val):
        global S
        S = val
        tratamento()

def V_trackbar(val):
    global V
    V = val
    tratamento()

def tratamento():
    v1 = cv2.inRange(hsv, (0, 0, 0), (15, 255, 200))
    v2 = cv2.inRange(hsv, (160, 172, 172), (179, 255, 255))
    v = cv2.add(v1,v2)
    final = cv2.bitwise_and(median, median, mask = v)
    cv2.imshow('janela', final)

cv2.namedWindow('janela')
cv2.createTrackbar('S', 'janela' , 0, 255, S_trackbar)
cv2.createTrackbar('V', 'janela' , 0, 255, V_trackbar)
S_trackbar(50)
cv2.waitKey()
cv2.destroyAllWindows()