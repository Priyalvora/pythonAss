x = int(input("Enter the altitude"))
if x <= 1000:
    print("Safe to land")
elif x > 1000 or x < 5000:
    print("Bring down to 1000")
else:
    print("Turn Around")
