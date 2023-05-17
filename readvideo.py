import cv2 as cv

# Rescaling the video to our desired size because the video is way too big
#this method of rescaling works for videos images and also live videos
def rescale_frame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
def changeres(width,height):
    # Change the resolution of the video 
    #it works only for live videos
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('C:/Users/gajul/OneDrive/Desktop/MLprojects/opencv/corgidog.mp4')
while True:
    isTrue, frame = capture.read()
    # Check if frame is valid
    if not isTrue:
        # If frame is None, video capture is unsuccessful or reached the end of the video
        break
    # Call the rescale_frame function
    resized_frame = rescale_frame(frame)
    # Display the original frame
    cv.imshow('doggy', frame)
    # Display the resized frame
    cv.imshow('dog', resized_frame)
    # The frame displays until we press the 'd' key
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
#similarly we can do this for the images instead of videos

