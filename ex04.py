from ultralytics import YOLO
import cv2 as cv

# Lae YOLO mudel
model = YOLO('yolo11n.pt')

# Ava video
capture = cv.VideoCapture("autod.mp4")

# Kontrolli, kas video avamine õnnestus
if not capture.isOpened():
    print("Video avamine ebaõnnestus!")
    exit()

# Tsükkel video kaadrite töötlemiseks
while True:
    ret, image = capture.read()
    if not ret:
        print("Video lõpp või kaadri lugemise viga.")
        break

    image = cv.resize(image, (640, 360))

    # Kasuta YOLO mudelit kaadri töötlemiseks
    results = model(image)[0]

    # Loenda autod kaadris
    car_count = 0

    #Kastide ja tekstide joonistamine
    for box in results.boxes:
        coordinates = box.xyxy[0].tolist()  
        confidence = round(box.conf[0].item(), 2)  
        class_id = int(box.cls)  
        class_name = results.names[class_id]  

        # Filtreeri ainult autod
        if class_name.lower() == "car":  
            car_count += 1
            
            cv.rectangle(image, (int(coordinates[0]), int(coordinates[1])), (int(coordinates[2]), int(coordinates[3])), (255, 0, 0), 2)
            cv.putText(image, f"{class_name} {confidence:.2f}", (int(coordinates[0]), int(coordinates[1] - 10)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Kuvame kaadris tuvastatud autode arvu
    cv.putText(image, f"Autosid kaadris: {car_count}", (20, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

    # Kuva töödeldud kaader
    cv.imshow('Autode tuvastamine', image)

    # Vajuta "q", et lõpetada
    key = cv.waitKey(10) & 0xFF
    if key == ord("q"):
        break

# Lõpetamine
capture.release()
cv.destroyAllWindows()
