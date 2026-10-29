text = input("Введите строку: ")
words = text.split()
count = 0

print("Подходящие слова:")
for word in words:
    clean_word = word.strip(".,!?:;").lower()
    if len(clean_word) == 0:
        continue
    if clean_word.startswith("а"):
        print(clean_word)
        count += 1
if count == 0:
    print("Нет совпадений")
    print(f"Количество: 0")
else:
    print(f"Общее количество: {count}")
