from ultralytics import YOLO
import cv2

#loading the pre trained YOLOv8 model (nano version though, fastest but not as accurate as it's bigger versions like yolov8s)
model = YOLO("yolov8n.pt")  # nano version for speed

def detect_from_image():
    #add your image detection logic here
    image = cv2.imread("test.jpg")  #make sure test.jpg is in the same folder though and named as in the bracket
    results = model(image)
    annotated = results[0].plot()
    cv2.imshow("YOLOv8 - Image Detection", annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_from_webcam():
    #starting the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read() #cap.read() returns a boolean (ret) and the frame itself
        if not ret:
            break

        #run YOLO object detection
        results = model(frame) #return detections

        annotated_frame = results[0].plot() #draws boxes and labels on the frame

        #display the frame
        cv2.imshow("YOLOv8 Real-Time Detection", annotated_frame)

        #exit if 'e' is pressed
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

    #clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("select mode:")
    print("1. detect objects in a static image")
    print("2. real-time object detection from webcam")
    choice = input("enter your choice (1 or 2): ")

    if choice == "1":
        detect_from_image()
    elif choice == "2":
        detect_from_webcam()
    else:
        print("invalid choice...\nexiting.")