# Install Python and its Libraries successfully and write this 3 code as single code and post screenshot of your output..

# import OpenCV library
import cv2

# Read Image
img = cv2.imread(r'E:\Python\Projects\Pantech Solutions - Internships\AI Internship\Day 3\Untitled.png')

# Image Properties
print(img.size)
print(img.shape)
print(img.dtype)

# convert Color image to Grayscale image
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Write Image
cv2.imwrite("E:\Python\Projects\Pantech Solutions - Internships\AI Internship\Day 3\GrayImage.jpg",grayImg)

# Show Original & Grayscale image
cv2.imshow("Original",img)
cv2.imshow("GrayImg",grayImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
