import cv2
# input=cv2.imread('image.png')
# dimension=input.shape
# size=input.size
# input[0,27]=(255,255,255)
# b=input[0,27,1]
# topleftcorner = input[0:315, 0:269]
# topleftcorner[:] = (255,255,255)
# print(dimension)
# print(size)
# print(b)
input=cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)
input[9,15]=0
i=input[9,15]
cv2.imshow('output',input)
print(i)
cv2.waitKey(0)
cv2.destroyAllWindows()