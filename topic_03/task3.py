print("\nТестування функцій словників")
d = {"технології": 1, "програмування": 2, "лабораторна": 3}
print("Початковий словник:", d)

d.update({"пайтон": 4})
print("update({'пайтон': 4}):", d)

print("keys():", list(d.keys()))

print("values():", list(d.values()))

print("items():", list(d.items()))

del d["програмування"]
print("del d['програмування']:", d)

d.clear()
print("clear():", d)