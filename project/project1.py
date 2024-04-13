import cv2

# Load the video
video_path =r"C:\Users\mayur\OneDrive\Desktop\project\19570048-uhd_3840_2160_24fps.mp4"
cap = cv2.VideoCapture(video_path)

# Load the image
image_path = r"C:\Users\mayur\OneDrive\Desktop\project\basketballbrad.jpg"
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# Get the width and height of the image
image_height, image_width, _ = image.shape

# Define the position to overlay the image on the video
x_position =50
y_position =50

# Get the dimensions of the video frames
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a window with dimensions matching the video frame
cv2.namedWindow('Video with Image Overlay', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video with Image Overlay', frame_width, frame_height)

# Read each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Overlay the image on the frame
    overlay = frame.copy()
    overlay[y_position:y_position+image_height, x_position:x_position+image_width] = image

    # Blend the overlay with the frame
    opacity = 0.9  # You can adjust the opacity here
    cv2.addWeighted(overlay, opacity, frame, 1 - opacity, 0, frame)

    # Display the frame
    cv2.imshow('Video with Image Overlay', frame)

    # Press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
