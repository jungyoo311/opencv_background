import cv2 as cv
img = cv.imread('/Users/jung/Desktop/research/opencv_background/image/cybertruck.jpeg')

cv.imshow('cybertruck',img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('cybertruck-gray', gray)

# blur = cv.GaussianBlur(img, (31,31), cv.BORDER_DEFAULT)
# cv.imshow('cybertruck-blur', blur)

# blur2 = cv.bilateralFilter(img,9,75,75)
# cv.imshow('cybertruck-blur2', blur2)

#Canny: edge detection
canny = cv.Canny(img, 125,175)
cv.imshow('cybertruck-canny', canny)

#dilate: dilating the img: expands the white regions(or bright areas) in the image
dilated = cv.dilate(canny, (13,13), iterations = 5)
cv.imshow('cybertruck-dilated', dilated)

#erode: opposite to dilated
eroded = cv.erode(dilated, (3,3), iterations = 3)
cv.imshow('cybertruck-eroded', eroded)

#resize: change the size of the img to 500 x 500
resized = cv.resize(canny, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('cybertruck-resized', resized)

#cropping: cut out the portion of the img
cropped = img[100:, 300:800]
cv.imshow('cybertruck-cropped', cropped)

# if (cv2.waitKey(1) & 0xFF == ord('q')):
#     break
cv.waitKey(0)