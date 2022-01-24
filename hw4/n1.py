from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv [1:])
        print(f" salary - { time* rate + bonus}")
    except ValueError:
        print("введите 3 числа, только цифры  ")

# use edit configurations

salary()

