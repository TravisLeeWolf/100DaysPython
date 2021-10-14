# doubleValues = [number * 2 for number in range(1, 5)]
# print(doubleValues)

randomNames = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
longNamesInUppercase = [name.upper() for name in randomNames if len(name) > 5]
print(longNamesInUppercase)