import cv2
import time
import os

def main():
    # 1. Setup the camera
    video_capture = cv2.VideoCapture(0) # 0 is usually the default laptop camera

    # 2. Load the classifiers (Pre-trained models for Face and Smile)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

    print("--- Smile Selfie App Started ---")
    print("Press 'q' to quit.")
    
    # Create a folder for selfies if it doesn't exist
    if not os.path.exists("my_selfies"):
        os.makedirs("my_selfies")

    while True:
        # 3. Read image from camera
        ret, frame = video_capture.read()
        if not ret:
            break

        # 4. Convert to GrayScale (Better for detection)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 5. Detect Faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Region of Interest (ROI) - Only look for smiles inside the face
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # 6. Detect Smiles inside the face
            # scaleFactor=1.8 and minNeighbors=20 makes it strict (real smiles only)
            smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)

            if len(smiles) > 0:
                cv2.putText(frame, "SMILE DETECTED!", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
                # Save the selfie
                img_name = f"my_selfies/smile_{int(time.time())}.png"
                cv2.imwrite(img_name, frame)
                print(f"Selfie captured: {img_name}")
                
                # Small delay to prevent taking 100 photos in 1 second
                time.sleep(1) 

        # 7. Display the video feed
        cv2.imshow('Smile Selfie Cam', frame)

        # Quit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()