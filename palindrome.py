text = input("Введите текст: ")
clean_text = text.lower().replace(" ", "")

if len(clean_text) == 0:
    print("Нет текста")
else:
    if clean_text == clean_text[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")
