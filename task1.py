from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem("Maximizing_Production", LpMaximize)

lemonade = LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = LpVariable('FruitJuice', lowBound=0, cat='Continuous')

model += lemonade + fruit_juice

model += 2*lemonade + 1*fruit_juice <= 100  # Water
model += 1*lemonade <= 50  # Sugar
model += 1*lemonade <= 30  # Lemon Juice
model += 2*fruit_juice <= 40  # Fruit Puree

model.solve()

print(f"Optimal amount of Lemonade: {lemonade.varValue:.2f}")
print(f"Optimal amount of Fruit Juice: {fruit_juice.varValue:.2f}")
print(f"Maximum total production: {lemonade.varValue + fruit_juice.varValue:.2f}")
