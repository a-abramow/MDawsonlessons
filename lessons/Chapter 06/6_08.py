# Доступ отовсюду
# Демонстрирует работу с глобальным переменными


def read_global():
    print("В области видимости функции read_global() значение value равно", value)


def shadow_global():
    value = -10
    print("В области видимости функции shadow_global() значение value равно", value)
