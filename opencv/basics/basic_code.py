import cv2
import numpy as np  # this library help us to deal with matrix

kernel = np.ones((5,5), np.uint8)

# displaying images :-
# image = cv2.imread('original.jpg')
# cv2.imshow('output',image)
# cv2.waitKey(0)     # 0 for infinity


# displaying videos :-
# video = cv2.VideoCapture('orignal_vid.mp4')
# while True:
#     success, image = video.read()
#     cv2.imshow("Video", image)
#     if cv2.waitKey(1) & 0xFF == ord('e'):
#         break


# diplaying webcam :-
# webcam_capture = cv2.VideoCapture(0)
#
# while True:
#     # Capture frame-by-frame
#     aryan, pandey = webcam_capture.read()
#     # Display the resulting frame
#     cv2.imshow('display', pandey)
#     if cv2.waitKey(1) & 0xFF == ord('e'):
#         exit()


# displaying images into gray :-
# image = cv2.imread('original.jpg')
# imagecolor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Aryan\'s window', imagecolor)
# cv2.waitKey(0)


# displaying images into blurred :-
# image = cv2.imread('original.jpg')
# imageblur = cv2.GaussianBlur(image, (13,13),0)   # K size will always in odd, 0 is sigma
# cv2.imshow('Aryan\'s window', imageblur)
# cv2.waitKey(0)


# displaying images edges :-
# image = cv2.imread('original.jpg')
# imageedges = cv2.Canny(image, 100,250)   # lower the value higher the detected edeges
# cv2.imshow('Aryan\'s window', imageedges)
# cv2.waitKey(0)


# displaying dilating images :-
# image = cv2.imread('original.jpg')
# imageedges = cv2.Canny(image, 100,250)   # lower the value higher the detected edeges
# imagedialation = cv2.dilate(imageedges,kernel,iterations=0)    # iterations = thickness
# cv2.imshow('Aryan\'s window', imagedialation)
# cv2.waitKey(0)


# displaying eroded images :-
# image = cv2.imread('original.jpg')
# imageedges = cv2.Canny(image, 100,250)   # lower the value higher the detected edeges
# imagedialation = cv2.dilate(imageedges,kernel,iterations=1)    # iterations = thickness
# imageeroded = cv2.erode(imagedialation,kernel,iterations=1)    # iteration =  thinness
# cv2.imshow('Aryan\'s window', imageeroded)
# cv2.waitKey(0)


# resizing and croping the image :-
# image = cv2.imread('original.jpg')
# print(image.shape)      # for displaying the shape of image
# imageresize = cv2.resize(image,(500,400))        # for resizing
# imagecropped = image[0:200,200:400]              # for cropping x:y = height , a:b = width
# cv2.imshow('Aryan\'s window1', imageresize)
# cv2.imshow('Aryan\'s window2', imagecropped)
# cv2.waitKey(0)


# colouring image
# image = cv2.imread('original.jpg')
# print(image.shape)
# image[100:200,100:200] = 0,0,0
# cv2.imshow('Aryan\'s windows', image)
# cv2.waitKey(0)


# draw shapes
# img = np.zeros((500, 500,3),np.uint8)
# cv2.line(img,(0,0), (img.shape[1], img.shape[0]), (500, 500), 5)   # line  0,0 = coordinates , (500,500) = color, 5 = thickness
# cv2.rectangle(img,(50,50),(200,200),(500, 500), 5 )                # rectangle (50,50),(200,200) = coordinates , (500,500) = color, 5 = thickness
# cv2.circle(img,(300,300),100,(500,500), 5)                         # circle (300,300) = centre coordinates , 100 =radius , (500,500) = color, 5 = thickness
# cv2.putText(img,'Shapes',(150,450),cv2.FONT_HERSHEY_PLAIN,3,(470,620,3),2)
# cv2.imshow('Aryan\'s windows', img)
# cv2.waitKey(0)


# wrap images
# img = cv2.imread('playing_cards.jpg')
# width, height = 300,400     # for output windows height
# cards_points1 = np.float32([[205,270],[385,271],[204,517],[385,515]])        # for cards corner points
# cards_points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])      # for cards corner points locations from (cards_point) variable width , height
# matrix = cv2.getPerspectiveTransform(cards_points1,cards_points2)            # transforming matrix
# image_output = cv2.warpPerspective(img,matrix,(width,height))
# cv2.imshow('Aryan\'s windows', img)
# cv2.imshow('output', image_output)
# cv2.waitKey(0)


# color detection
# def empty(a):
#     pass
#
# cv2.namedWindow('trackbars')                                    # for creating windwos
# cv2.resizeWindow('trackbars',600,320)                           # for resizing created windows
# cv2.createTrackbar('Hue min','trackbars',179,179,empty)         # .
# cv2.createTrackbar('Hue max','trackbars',179,179,empty)         # .
# cv2.createTrackbar('Sat min','trackbars',0,0,empty)             # .   -  all are trackbars
# cv2.createTrackbar('Sat max','trackbars',255,255,empty)         # .
# cv2.createTrackbar('Value min','trackbars',130,255,empty)       # .
# cv2.createTrackbar('Value max','trackbars',255,255,empty)       # .
#
# while True:
#     img = cv2.imread('car.jpg')
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
#     hue_min = cv2.getTrackbarPos('Hue min','trackbars')        # .
#     hue_max = cv2.getTrackbarPos('Hue max', 'trackbars')       # .
#     sat_min = cv2.getTrackbarPos('Sat min', 'trackbars')       # .
#     sat_max = cv2.getTrackbarPos('Sat max', 'trackbars')       # . - getting positions for all trackbars
#     value_min = cv2.getTrackbarPos('Value min', 'trackbars')   # .
#     value_max = cv2.getTrackbarPos('Value max', 'trackbars')   # .
#     print(hue_min,hue_max,sat_min,sat_max,value_min,value_max)      # printing trackbar values
#     upper = np.array([hue_max,sat_max,value_max])               # setting array for track bars
#     lower = np.array([hue_min,sat_min,value_min])               # setting array for track bars
#     mask = cv2.inRange(imgHSV,lower,upper)                     # making trackbar responsive
#     result_image = cv2.bitwise_and(img,img,mask=mask)         # combining images for final window
#
#     cv2.imshow('mask output', mask)
#     cv2.imshow('Aryan\'s window', img)
#     cv2.imshow('output', imgHSV)
#     cv2.imshow('final', result_image)
#     if cv2.waitKey(1) & 0xFF == ord('e'):
#          exit()


# detecting shapes       ( INCOMPLETE )
# img = cv2.imread('shapes.jpg')
#
# image_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       # gray image
# image_blur = cv2.GaussianBlur(image_gray,(7,7),1 )      # blurred image
# image_edge = cv2.Canny(image_blur,50,50)                # image edge
#
# cv2.imshow('shapes1', img)
# cv2.imshow('shapes2', image_gray)
# cv2.imshow('shapes3', image_blur)
# cv2.imshow('shapes4', image_edge)
# cv2.waitKey(0)



# Face detection
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('../face detection/face 2.png')
imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(image,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('aryan windows', image)
cv2.waitKey(0)
