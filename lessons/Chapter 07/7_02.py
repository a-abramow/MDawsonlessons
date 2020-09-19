# Запишем
# Демонстрируется запись в текстовый файл

print("Создаю текстовый файл методом write().")
text_file = open("write_it.txt", "w", encoding='utf-8')

text_file.write("Первая строка номер 1\n")
text_file.write("Вторая строка номер 2\n")
text_file.write("Третья строка номер 3\n")
text_file.close()

print("\nЧитаю вновь созданный файл.")
text_file = open("write_it.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()

print("Создаю текстовый файл методом writelines().")
text_file = open("write_it2.txt", "w", encoding='utf-8')
lines = ["Строка номер 1\n"
         "Строка номер 2\n"
         "Строка номер 3\n"]
text_file.writelines(lines)
text_file.close()

print("\nЧитаю вновь созданный файл.")
text_file = open("write_it2.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()
