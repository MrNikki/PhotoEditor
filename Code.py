#Вліво
    #rotated_image = image.rotate(ГРАДУСИ)
#Вправо
    #rotated_image = image.rotate(ГРАДУСИ)
#Дзеркало
    #horizontally_flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
#Різкість
    #image.filter(ImageFilter.SHARPEN(10))
#Ч/Б
    #grayscale_image = image.convert("L")
#Зменшити яскравість
    #Image.point(lambda x: x * 0.5): Зменшує яскравість зображення на 50%
#Збільшити яскравість
    #Image.point(lambda x: x * 2): Збільшує яскравість зображення на 50%
#Рельєф
    #embossed_image = image.emboss()
#Соляризація
    #Image.solarize(ЧИСЛО)
# Зробити зображення сепієвим
    #sepia_image = image.point(lambda x: 0.299 * x + 0.587 * x + 0.114 * x)
