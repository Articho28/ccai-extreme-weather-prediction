import cv2
from model import PlantPredictionModel
from PIL import Image
import numpy
model = PlantPredictionModel("model.json", "model.h5")
font = cv2.FONT_HERSHEY_SIMPLEX

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    # returns camera frames along with bounding boxes and predictions
    def get_frame(self):
        _, fr = self.video.read()
        cv2.imwrite("i.png", fr)
        resized_i = cv2.resize(fr, (255, 255))
        cv2.imwrite("a.png", resized_i)
        # gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        pred = model.predict_disease(numpy.expand_dims(resized_i, axis=0))
        print(pred)
        cv2.imshow('frame',fr)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pass
        _, jpeg = cv2.imencode('.jpg', fr)
        return jpeg.tobytes()

