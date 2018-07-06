zoo = ("penguin", "leopard", "jaguar", "ibok")

print(zoo.index("jaguar"))

for value in zoo:
    if value == "penguin":
        print("yes!")

(p, l, j, i) = zoo
print(l)
print(p)

zoo_list = []
for i in zoo:
    zoo_list.append(i)

print(zoo_list)

zoo_list.extend(["python", "orangutan", "dugong"])
zoo_tuple = tuple(zoo_list)
print(zoo_tuple)