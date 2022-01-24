while True:
    days = 1
    start_km = float(input('начальный результат -'))
    target_km = float(input('finish result -'))
    if start_km <= 0 or target_km < 0:
        print('result should be bigger than zerro ')
    else:
        while start_km < target_km:
            start_km *= 1.1
            days += 1
        print(f'Human be at the finish in {days}')
