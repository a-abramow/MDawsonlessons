# Законсервируем
# Демонструрует консервацию данных и доступ к ним через интерфейс полки

import pickle
import shelve

print("Консервация списков.")
variety = ["огурцы", "помидоры", "капуста"]
shape = ["целые", "кубиками", "соломкой"]
brand = ["Главпродукт", "Чумак", "Бондюэль"]
f = open("pickles1.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()
