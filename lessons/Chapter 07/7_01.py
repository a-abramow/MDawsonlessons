# Прочитаем
# Демонстрирует чтение из текстового файла

print("Открываю и закрываю файл")
text_file = open("read_it.txt", "r", encoding='utf-8')
text_file.close()

print("Печатаю файл посимвольно.")
text_file = open("read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nЧитаю файл целиком.")
