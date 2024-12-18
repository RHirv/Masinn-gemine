import cv2 as cv

# Threshold funktsioon
def apply_threshold(image, threshold_value):
    retval, threshold_image = cv.threshold(image, threshold_value, 255, cv.THRESH_BINARY)
    return threshold_image

# Blur funktsioon
def apply_blur(image, blur_value):
    if blur_value % 2 == 0:
        blur_value += 1
    return cv.GaussianBlur(image, (blur_value, blur_value), 0)

# Dilate funktsioon
def apply_dilate(image, dilate_value):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (dilate_value, dilate_value))
    return cv.dilate(image, kernel)

# Erode funktsioon
def apply_erode(image, erode_value):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (erode_value, erode_value))
    return cv.erode(image, kernel)

# Canny servade tuvastamise funktsioon
def apply_canny(image, canny_value):
    return cv.Canny(image, canny_value, canny_value * 2)

def on_change(value):
    pass

def main():
    print("Valikud:")
    print("1 - Threshold")
    print("2 - Blur")
    print("3 - Dilate")
    print("4 - Erode")
    print("5 - Canny")
    
    # Kasutaja sisend meetodi valikuks
    method_choice = input("Sisesta töötluse number (1-5): ").strip()

    # Meetodid ja nende maksimaalsed trackbari väärtused
    if method_choice == "1":
        method_function = apply_threshold
        max_value = 255
        method_name = "Threshold"
    elif method_choice == "2":
        method_function = apply_blur
        max_value = 50
        method_name = "Blur"
    elif method_choice == "3":
        method_function = apply_dilate
        max_value = 20
        method_name = "Dilate"
    elif method_choice == "4":
        method_function = apply_erode
        max_value = 20
        method_name = "Erode"
    elif method_choice == "5":
        method_function = apply_canny
        max_value = 255
        method_name = "Canny"
    else:
        print("Vale valik! Palun vali arv vahemikus 1-5.")
        return

    # Pildi laadimine
    image = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)
    if image is None:
        print("Pilt 'image.jpg' ei leitud!")
        return

    # Loome akna ja trackbari
    window_name = f"{method_name} Processing"
    cv.namedWindow(window_name)
    cv.createTrackbar(method_name, window_name, 1, max_value, on_change)

    while True:
        # Trackbari väärtus
        value = cv.getTrackbarPos(method_name, window_name)

        # Rakenda valitud töötlemismeetod
        processed_image = method_function(image, value)

        # Näita töödeldud pilti
        cv.imshow(window_name, processed_image)

        # Välju, kui vajutatakse 'q'
        key = cv.waitKey(10)
        if key == ord('q'):
            break


    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
