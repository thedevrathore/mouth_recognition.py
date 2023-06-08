Mouth Recognition
This is a Python script that performs real-time mouth recognition using the OpenCV and dlib libraries. It detects faces in video frames captured from a webcam, identifies the mouth landmarks, and applies a filter based on the mouth width.

Prerequisites
Before running the script, make sure you have the following dependencies installed:

Python 3.x
OpenCV (cv2)
dlib
numpy
You can install the required dependencies using pip:


pip install opencv-python dlib numpy
Additionally, you need to download the dlib shape predictor model file. You can obtain the model file from the following link:
shape_predictor_68_face_landmarks_GTX.dat

Usage
Clone or download the script to your local machine.

Place the shape_predictor_68_face_landmarks_GTX.dat file in the same directory as the script.

Run the script using the following command:


python mouth_recognition.py
The script will access your webcam and display the mouth recognition in a window titled "Mouth Recognition".

Press the 'q' key to quit the program.

Description
The script performs the following steps:

Imports the necessary libraries: cv2, dlib, and numpy.

Initializes the face detector and shape predictor using the dlib models.

Defines a function distance to calculate the Euclidean distance between two points.

Defines a function apply_filter to apply a filter to the frame based on the mouth width.

Initializes the video capture object to access frames from the webcam.

Enters a continuous loop to read frames from the video capture object.

Converts the frame to grayscale and detects faces using the face detector.

For each detected face, extracts the mouth landmarks using the shape predictor.

Applies the filter based on the mouth width to the frame.

Displays the filtered frame in a window titled "Mouth Recognition".

Waits for the user to press the 'q' key to exit the loop and terminate the program.

Releases the video capture object and closes all OpenCV windows.

Feel free to modify the code and experiment with different filters or functionality.

Note: Ensure that you have a working webcam connected to your computer before running the script.

License
This script is released under the MIT License.

Author: [Dev Rathore]
Email: [rathoredev044@gmail.com]
