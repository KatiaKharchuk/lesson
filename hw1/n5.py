revenue = float(input("введите значание выручки -"))
cost = float(input("ВВедите значание издержек"))
result = revenue - cost
if result > 0:
    print(f"congraduations")
    print(f"рентабельность выручки - {result / person:2f}")
    persons = int(input("workers -"))
    print(f"result - {result / person:.2f}")
elif result <0:
    prin(f"убыток- {-result}")
else:
    print(f"zero")
