def my_pow_fun(x,y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Х должен быть больше 0, У должен бть больше 0"
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1 / x
                return f 'результат возведения x в степень y: {round(result, 6)}'
    except ValueError:
        return "только с числами"

print(my_pow_fun(55, -9))
