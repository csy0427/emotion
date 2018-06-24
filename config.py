# Depends on your system, the OpenCV pre-trained classifiers for
# face / eyes detection could be in different folder
FACE_CASCADE_FILE = '/usr/local/Cellar/opencv/3.4.1_5/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml'
#FACE_CASCADE_FILE = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"

EYE_CASCADE_FILE = "/usr/local/Cellar/opencv/3.4.1_5/share/OpenCV/haarcascades/haarcascade_eye.xml"
#EYE_CASCADE_FILE = "/usr/share/opencv/haarcascades/haarcascade_eye.xml"

# Size of the face images used for training
DEFAULT_FACE_SIZE = (200, 200)

# Filename for storing  face recognizer result
RECOGNIZER_OUTPUT_FILE = "train_result.out"
