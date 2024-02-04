from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Use your YOLOv3 setup and configuration here
net = cv2.dnn.readNet('carbest.weights', 'car.cfg')
classes = []

def detect_objects(frame):
    
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    net = cv2.dnn.readNetFromDarknet("car.cfg", "carbest.weights")
    net

    classes=['car']
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Open the video file
    video_path = "0"  # Replace with the path to your video file
    cap = cv2.VideoCapture(video_path)


    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Use int() to convert float to int
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    #out1=cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
    out1 = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (width, height))

    while True:
        ret, frame = cap.read()  # Read a frame from the video
        if not ret:
            break

        height, width, channels = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Object detection and non-maximum suppression
        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y + 30), font, 3, color, 3)

        # Write the frame to the output video
        out1.write(frame)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture, release the video writer, and close OpenCV windows
    cap.release()
    out1.release()
    cv2.destroyAllWindows()

    return processed_frame

def video_feed():
    cap = cv2.VideoCapture('your_video_source')  # Update with your video source
    while True:
        ret, frame = cap.read()
        processed_frame = detect_objects(frame)

        # Convert the frame to JPEG format
        _, jpeg = cv2.imencode('.jpg', processed_frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed_route():
    return Response(video_feed(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
