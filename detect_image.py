# Finding Single Dot
# import cv2 as cv
# from PIL import Image
# from utils import get_limits  # Make sure 'get_limits' is defined in utils.py

# # Yellow in BGR
# yellow = [0, 255, 255]

# # Load the image (path to the image you want to test)
# image_path = "/Users/supriyamaji/Desktop/Code/Computer_Vision/color-detection-opencv/image/testImage.png"  # Replace with actual path
# frame = cv.imread(image_path)

# if frame is None:
#     print("Error: Image not found or path is incorrect.")
#     exit()

# # Convert to HSV color space
# hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

# # Get HSV bounds for yellow
# lower_limit, upper_limit = get_limits(color=yellow)

# # Create mask
# mask = cv.inRange(hsv_image, lower_limit, upper_limit)

# # Convert mask to PIL Image to use getbbox()
# mask_pil = Image.fromarray(mask)

# # Get bounding box
# bbox = mask_pil.getbbox()

# # Draw rectangle if yellow region is found
# if bbox is not None:
#     x1, y1, x2, y2 = bbox
#     frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

# # Show the result
# cv.imshow("Detected Yellow", frame)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Finding Multiple dots
import cv2 as cv
from utils import get_limits

# Yellow in BGR
yellow = [0, 255, 255]

# Load the image
image_path = "/Users/supriyamaji/Desktop/Code/Computer_Vision/color-detection-opencv/image/testImage3.png"
frame = cv.imread(image_path)

if frame is None:
    print("Error: Image not found or path is incorrect.")
    exit()

# Convert to HSV color space
hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

# Get HSV bounds for yellow
lower_limit, upper_limit = get_limits(color=yellow)

# Create mask
mask = cv.inRange(hsv_image, lower_limit, upper_limit)

# Find contours in the mask
contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw a rectangle around each detected yellow region
for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the result
cv.imshow("Detected Yellow Regions", frame)
cv.waitKey(0)
cv.destroyAllWindows()