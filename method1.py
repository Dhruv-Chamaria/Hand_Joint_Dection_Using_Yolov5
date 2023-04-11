import cv2 
import numpy as np 

# Read the image 
lista = os.listdir('dir path to test imaegs')
lista[:len(lista)-1]
for i in lista[300:]:
    # read image
    img = cv2.imread(f"dir path to test imaegs{i}")
    img1 = cv2.imread(f"dir path to test imaegs{i}")
    # Convert to grayscale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit = 1)
    equalized1 = clahe.apply(gray) + 10

    # Blur using 3 * 3 kernel 
    gray_blurred = cv2.blur(equalized1, (3,3)) 

    # Apply Hough transform on the blurred image 
    detected_circles = cv2.HoughCircles(gray_blurred,  
                    cv2.HOUGH_GRADIENT, 100, 120, param1 = 70, 
                    param2 = 30, minRadius = 1, maxRadius = 40) 

    # Draw circles that are detected 
    if detected_circles is not None: 

        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 

        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 

            # Draw the circumference of the circle 
            cv2.circle(img, (a, b), r, (0, 255, 0), 2) 

            # Draw a small circle (of radius 1) to show the center. 
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 

    # # Display the image 
    # cv2.imshow("Detected Hand Joints", np.hstack([img])) 

    # # Exit window when 'q' is pressed 
    # if cv2.waitKey(0) & 0xFF == ord('q'): 
    #     cv2.destroyAllWindows()
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(30, 30))

    axes[0].set_title("Original")
    axes[0].imshow(img1, cmap="gray")
    axes[1].set_title("Histogram Equalization")
    axes[1].imshow(np.hstack([img]))
    for i in axes:
        i.axis("off")
    plt.show()