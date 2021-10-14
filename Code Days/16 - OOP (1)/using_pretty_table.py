# Made by TravisLeeWolf

from prettytable import PrettyTable

table = PrettyTable()
# Add columns and data to table
# Calling methods
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Changing the attributes
table.align = "l"

print(table)