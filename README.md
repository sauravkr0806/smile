# Smile Selfie Camera

A simple Python computer-vision project that uses your webcam to detect faces and smiles. When a smile is detected, the app saves a selfie image to a local folder.

## Features

- Captures live video from the default webcam.
- Detects faces using OpenCV's Haar Cascade classifier.
- Looks for smiles within detected face regions.
- Draws a rectangle around detected faces and displays a message when a smile is detected.
- Saves captured images in the `my_selfies/` directory.
- Press `q` to quit the camera window.

## Requirements

- Python 3
- A working webcam
- OpenCV for Python

## Installation

1. Clone or download this project.
2. Open a terminal in the project directory.
3. (Optional) Create and activate a virtual environment.

   **Windows (Command Prompt):**
   ```bat
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install the dependency:

   ```bash
   python -m pip install opencv-python
   ```

## Run the Project

Run the script from the project directory:

```bash
python smile_camera.py
```

The app opens a live webcam window. When it detects a smile, it saves an image under `my_selfies/`. Press **`q`** to close the app.

## Project Structure

```text
.
├── smile_camera.py
├── README.md
└── my_selfies/       # Created automatically when the app runs
```

## How It Works

1. Opens the default camera using OpenCV.
2. Loads OpenCV's pre-trained Haar Cascade face and smile classifiers.
3. Converts each video frame to grayscale.
4. Detects faces in the frame.
5. Searches for smiles within each detected face.
6. Displays the camera feed and saves an image when a smile is detected.

## Notes and Limitations

- The script uses camera index `0`, which usually selects the default webcam.
- Smile detection is based on a traditional Haar Cascade classifier and may produce false positives or miss smiles depending on lighting, camera quality, and face angle.
- The script may save more than one image during a sustained smile; it includes a one-second delay to reduce rapid repeated captures.
- Ensure your operating system allows Python to access the camera.

## Privacy

Images are saved locally in `my_selfies/`. Review and delete these files yourself when they are no longer needed. Get consent before capturing or saving photos of other people.

## License

No license has been specified for this project. Add a license file if you intend to publish or distribute it.
