while True:
    user_month = input("введити номер месяца от 1 до 12:")
    if user_month.isdigit() and 0 < int(user_month) <= 12:
        season_1 = ["зима", "весна", "лето", "осень", "зима"]
        season_2 = {0:"зима", 1:"весна", 2:"лето", 3:"осень", 4:"зима"}
        print (f'список сезонов - {season_1[int(user_month) // 3]}/nСловарь сезонов - {season_2[int(user_month) //3]}')
        break
    else:
        print("ошибка")
