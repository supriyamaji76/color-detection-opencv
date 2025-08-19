# import cv2 as cv
# from PIL import Image

# from utils import get_limits


# yellow = [0, 255, 255]  # Yellow in BGR colorspace

# cap = cv.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

#     lower_limit, upper_limit = get_limits(color = yellow)

#     mask = cv.inRange(hsv_image, lower_limit, upper_limit)

#     mask_ = Image.fromarray(mask)

#     bbox = mask_.getbbox()

#     if bbox is not None:
#         x1, y1, x2, y2 = bbox

#         frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

#     cv.imshow("frame", frame)

#     if cv.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()

# cv.destroyAllWindows()

# For Multiple bounding box
import cv2 as cv
from utils import get_limits

# Yellow in BGR colorspace
yellow = [0, 255, 255]

# Start webcam capture
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV
    hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Get HSV bounds
    lower_limit, upper_limit = get_limits(color=yellow)

    # Create mask
    mask = cv.inRange(hsv_image, lower_limit, upper_limit)

    # Find contours on the mask
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes for each contour
    for contour in contours:
        if cv.contourArea(contour) > 10:  # Optional: filter small noise
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv.imshow("Yellow Detection", frame)

    # Quit on 'q' key
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
