# Import necessary libraries
import cv2
import numpy as np

# Load YOLOv3 configuration and weights
net = cv2.dnn.readNet("C:\Users\Vineeth K P\object detection\yolov3.weights", "C:\Users\Vineeth K P\object detection\yoloconfg.cfg")

# Load Indian Driving Dataset classes
classes = []
with open ("C:\Users\Vineeth K P\object detection\archive\idd20kII\label\classes.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Set input image size
input_size = 416

# Load test image
img = cv2.imread("C:\Users\Vineeth K P\object detection\archive\idd20kII\label\test\259\frame0014_leftImg8bit.jpg")

# Get image dimensions
height, width, _ = img.shape

# Create blob from input image
blob = cv2.dnn.blobFromImage(img, 1/255.0, (input_size, input_size), swapRB=True, crop=False)

# Set input for YOLOv3 network
net.setInput(blob)

# Perform forward pass through network
output_layers = net.getUnconnectedOutLayersNames()
layer_outputs = net.forward(output_layers)

# Initialize lists for detected objects, their locations, and their confidence scores
class_ids = []
confidences = []
boxes = []

# Loop over each output layer
for output in layer_outputs:
    # Loop over each detection
    for detection in output:
        # Extract class ID and confidence score
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        # Filter out weak detections
        if confidence > 0.5:
            # Calculate object location and add to list of detections
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = center_x - w//2
            y = center_y - h//2
            class_ids.append(class_id)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])

# Apply non-maximum suppression to remove redundant detections
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Draw bounding boxes around detected objects and label with class name and confidence score
for i in indices:
    box = boxes[i]
    x = box[0]
    y = box[1]
    w = box[2]
    h = box[3]
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    label = f"{classes[class_ids[i]]}: {confidences[i]:.2f}"
    cv2.putText(img, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

# Display image with detected objects
cv2.imshow("Output Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()