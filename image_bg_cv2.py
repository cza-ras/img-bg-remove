import cv2

#folder path
input_path="Projects/img-bg-remove/sample_image.jpg"
output_path="Projects/img-bg-remove/ready_image_cv2.jpg"

# Set the background color (in BGR format)
background_color = (255, 255, 255)

# Load the image
image = cv2.imread(input_path)

# Create a mask for the background pixels (black for background, white for foreground)
mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)[1]

# Invert the mask (white for background, black for foreground)
mask = cv2.bitwise_not(mask)

# Replace the background pixels with the specified color
image[mask == 0] = background_color

# Save the final image with the plain color background
cv2.imwrite(output_path, image)