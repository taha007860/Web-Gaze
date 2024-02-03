# Face Mesh-Based Screen Magnification Tool 🖥️🔍

## Overview 👀
Developed for the Tech for Accessibility Hackathon organized by the American University of Beirut, this tool employs computer vision to track facial landmarks. It magnifies parts of the computer screen based on the user's gaze direction, enhancing accessibility for users with visual impairments.

## Features 🌟
- **Face Mesh Tracking**: Utilizes MediaPipe's face mesh solution for accurate facial landmark tracking. 🤖
- **Dynamic Screen Magnification**: Magnifies screen areas based on gaze, aiding visually impaired users. 🔎
- **Customizable Magnification**: Users can adjust the magnification level and the size of the magnified screen area. 🔍⚙️
- **Real-Time Feedback**: Live display of the region of interest with facial landmarks. 🖼️

## Usage 🚀
1. Run the script to start webcam and face mesh tracking. 🎥
2. The program sets a baseline for gaze direction using the initial nose tip position. 👃
3. Detects gaze shifts by measuring the distance moved from the baseline. 👀
4. Magnifies the screen area where the user's gaze is directed. 🖥️

## Configuration 🔧
- **Magnification Level**: Adjust `magnification` to change the zoom level. 🔍
- **Band Size**: Change `band_height` and `band_width` to alter the size of the magnified area. 📏

## Exiting the Application ❌
Press 'q' in the ROI window to safely shut down the webcam and terminate the program. 🛑

## Contributions 🤝
We welcome contributions to improve gaze tracking accuracy and expand functionality. 👐

## Acknowledgements
Special thanks to the American University of Beirut for hosting the Tech for Accessibility Hackathon and fostering the development of accessibility solutions. 🎓

## Watch Demo
https://github.com/taha007860/Contact-Book/assets/96583299/a26d5cd7-4513-4243-b95f-d0d753cdb623

