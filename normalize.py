original_text = input("Введите текст: ")
normalized_text = " ".join(original_text.split())
words = normalized_text.split()

print(f"Исходная строка: '{original_text}'")
print(f"Длина исходной строки: {len(original_text)}")
print(f"Нормализованный текст: '{normalized_text}'")
print(f"Длина нормализованного текста: {len(normalized_text)}")
print(f"Количество слов: {len(words)}")
