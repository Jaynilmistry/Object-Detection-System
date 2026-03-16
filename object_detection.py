import cv2
import numpy as np

# Load YOLO model
net = cv2.dnn.readNet("models/yolov3.weights", "models/yolov3.cfg")

# Ensure layer names are correctly fetched
layer_names = net.getLayerNames()
unconnected_out_layers = net.getUnconnectedOutLayers()

if len(unconnected_out_layers.shape) == 1:  # Fix for the scalar issue
    output_layers = [layer_names[i - 1] for i in unconnected_out_layers]
else:
    output_layers = [layer_names[i[0] - 1] for i in unconnected_out_layers]

# Load class labels
with open("models/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

def detect_objects(image_path=None, is_webcam=False, webcam_frame=None):
    if is_webcam and webcam_frame is not None:
        image = webcam_frame
    else:
        image = cv2.imread(image_path)

    height, width, _ = image.shape

    # Preprocessing
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    # Detect objects
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x, center_y, w, h = (detection[:4] * np.array([width, height, width, height])).astype("int")
                x, y = int(center_x - w / 2), int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply Non-Maximum Suppression (NMS)
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    detected_info = []
    for i in indices.flatten():
        x, y, w, h = boxes[i]
        label = f"{classes[class_ids[i]]}: {confidences[i]:.2f}"
        detected_info.append(label)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image, detected_info
