time = int(input("введите время в сек"))
hour = time // 3600
minute = (time // 60) - (hour * 60)
secunda = time % 60
print(f"{hour:02}:{minute:02}:{secunda:02}")


