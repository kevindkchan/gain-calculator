try:
    new = float(input("input new price: "))
    old = float(input("input old price: "))
except ValueError:
    print("bro enter a number")
else:
    gain = (new - old) / old * 100
    print(f"total percentage gain: {gain:.2f}%")
