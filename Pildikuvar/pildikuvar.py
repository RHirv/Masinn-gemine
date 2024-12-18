import cv2  

# Funktsioon, mis rakendab pildile erinevaid efekte
def apply_effect(image, effect_type):
    if effect_type == 'gray':  # Muudab pildi halltoonidesse
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif effect_type == 'rotate':  # Pöörab pildi 90 kraadi päripäeva
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif effect_type == 'flip':  # Peegeldab pildi vertikaalselt
        return cv2.flip(image, 0)
    elif effect_type == 'resize':  # Muudab pildi suuruseks 200x200 pikslit
        return cv2.resize(image, (200, 200))
    elif effect_type == 'blur':  # Lisab pildile hägususe (Gaussian Blur)
        return cv2.GaussianBlur(image, (15, 15), 0)
    elif effect_type == 'edge':  # Tuvastab pildil servad (Canny algoritm)
        return cv2.Canny(image, 100, 200)
    return image

def main():

    # Loeb pildi failist 'image.jpg'
    image = cv2.imread('image.jpg')  

    # Kontrollib, kas pildi laadimine õnnestus
    if image is None:  
        print("Viga pildi avamisel")
        return

    # Küsib kasutajalt, mitu efekti ta soovib näha
    num_windows = int(input("Sisesta, mitut erinevat effekti sa näha tahad (1-6): "))
    if num_windows < 1 or num_windows > 6:
        print("Palun sisesta number vahemikus 1 kuni 6.")  # Kuvab veateate, kui sisend on vale
        return

    # Nimekiri saadaval olevatest efektidest
    effects = ['gray', 'rotate', 'flip', 'resize', 'blur', 'edge']

    # Loop, mis rakendab ja kuvab valitud arvu efekte
    for i in range(num_windows):
        effect_type = effects[i]  # Valib vastava efekti nimekirjast
        modified_image = apply_effect(image, effect_type)  # Rakendab efekti pildile
        cv2.imshow(f"Aken {i+1}", modified_image)  # Kuvab muudetud pildi uues aknas

    cv2.waitKey(0)  # Ootab, kuni kasutaja vajutab klahvi
    cv2.destroyAllWindows()  # Sulgeb kõik avatud aknad
    

if __name__ == "__main__":
    main()  
