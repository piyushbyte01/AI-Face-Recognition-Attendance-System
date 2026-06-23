import os
import cv2
from database import insert_student, student_exists

def TakeImage(l1, l2, haarcasecade_path, trainimage_path, message, err_screen, text_to_speech):

    # ---------------- INPUT VALIDATION ----------------
    if not l1 or not l2:
        text_to_speech("Please enter Enrollment Number and Name")
        return

    Enrollment = str(l1)
    Name = str(l2)

        # ---------------- DUPLICATE CHECK ----------------
    if student_exists(Enrollment):
        msg = f"Enrollment {Enrollment} already registered"
        message.configure(text=msg)
        text_to_speech(msg)
        return

    try:
        # ---------------- CAMERA START ----------------
        cam = cv2.VideoCapture(0)

        if not cam.isOpened():
            text_to_speech("Camera not opening")
            return

        # ---------------- FACE DETECTOR ----------------
        detector = cv2.CascadeClassifier(haarcasecade_path)

        if detector.empty():
            text_to_speech("Haarcascade file not loaded")
            return

        # ---------------- IMAGE STORAGE FOLDER ----------------
        path = os.path.join(trainimage_path, f"{Enrollment}_{Name}")
        os.makedirs(path, exist_ok=True)

        text_to_speech("Camera started. Look at camera")

        sampleNum = 0
        max_samples = 50

        # ---------------- CAPTURE LOOP ----------------
        while True:
            ret, img = cam.read()

            if not ret or img is None:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                sampleNum += 1

                face_img = gray[y:y+h, x:x+w]

                file_name = os.path.join(
                    path,
                    f"{Name}_{Enrollment}_{sampleNum}.jpg"
                )

                cv2.imwrite(file_name, face_img)

                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

                cv2.putText(
                    img,
                    f"Captured {sampleNum}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

            cv2.imshow("Face Capture (Press Q to stop)", img)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q") or sampleNum >= max_samples:
                break

        # ---------------- CLEANUP ----------------
        cam.release()
        cv2.destroyAllWindows()

        # ---------------- SAVE TO MYSQL ----------------
        insert_student(Enrollment, Name)

        msg = f"Images saved successfully for {Enrollment} - {Name}"
        message.configure(text=msg)
        text_to_speech(msg)

    except Exception as e:
        print("ERROR:", e)
        text_to_speech("Something went wrong")
        cv2.destroyAllWindows()