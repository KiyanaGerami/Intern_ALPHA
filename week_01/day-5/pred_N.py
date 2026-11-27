# Snippet 1


a = "5"
b = 3
print(a * b)              # Predict: 555
print(int(a) * b)         # Predict: 15
print(a + str(b))         # Predict: 53
print(float(a) / 2, int(a) // 2, -7 // 2)  # Predict: 2.5 2 -4

# Snippet 2

name = "  Mina  "
name.strip()
print(f"[{name}]")        # Predict: [  Mina  ]
name = name.strip().upper()
print(f"[{name}]", len(name))  # Predict: [MINA] 4
print(name[1:3], name[-1], name[::-1])  # Predict: IN A ANIM

# Snippet 3

total = 10 + 20 * 3 ** 2 / 6
print(total)              # Predict: 40.0
print(0.1 * 3 == 0.3, round(0.1 * 3, 2) == 0.3)  # Predict: False True
print(round(2.5), round(3.5), round(2.675, 2))   # Predict: 2 4 2.67
print(int("  42  "), int(9.99))                  # Predict: 42 9
