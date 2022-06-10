import cv2
import numpy as np

img = cv2.imread("tomate.jpg")

blur = cv2.blur(img, (9,9))
cv2.imshow("blur", blur)
cv2.waitKey() 
cv2.destroyAllWindows()

hsv = cv2.cvtColor( blur, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)
cv2.waitKey() 
cv2.destroyAllWindows()

k=np.ones((3,3), np.uint8)

v1 = cv2.inRange(hsv, (0,50,200), (10,255,255))
v2 = cv2.inRange(hsv, (160,50,200), (179,255,255))
v=cv2.add(v1,v2)
cv2.imshow("mascara", v)
cv2.waitKey() 
cv2.destroyAllWindows()

final = cv2.bitwise_and(img, img, mask=v)
cv2.imshow("tomate", final)
cv2.waitKey() 
cv2.destroyAllWindows()

cont = cv2.Canny(final, 100, 100)
cv2.imshow("contorno", cont)
cv2.waitKey() 
cv2.destroyAllWindows()

d = cv2.dilate(cont,k,iterations = 12)
e = cv2.erode(d,k,iterations = 8)
contorno,_= cv2.findContours(e, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(e, contorno, 0, (0,0,255), 1)
cv2.imshow("contorno", e)
cv2.waitKey() 
cv2.destroyAllWindows()

for c in contorno:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
    cv2.putText(img, "tomate", ((x),(y-5)),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    M = cv2.moments(c)

cv2.imshow("tomate", img)
cv2.waitKey() 
cv2.destroyAllWindows()