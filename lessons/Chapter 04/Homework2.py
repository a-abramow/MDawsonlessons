# Задание 2
# Читаем текст наоборот!

print("Поковеркаем слова")
text = input("Введите любую фразу: ")
print("В переменной text хранится фраза:", text)
print("Во фразе всего ", len(text), " символов.")

new_text = text[::-1]
print("Наоборот ваша фраза выглядит так:", end=" ")
print(new_text)
