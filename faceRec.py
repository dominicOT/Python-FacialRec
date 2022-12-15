import pyttsx3
import cv2
import sys



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice
engine.setProperty('rate', 190) #voice speed
engine.setProperty('volume', 1.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


    
# Get user supplied values
imagePath = "moun.jpg"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    #flags = cv2.CASCADE_SCALE_IMAGE
    #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

speak("Found {0} faces!".format(len(faces)))
print("Found {0} faces!".format(len(faces)))


# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
