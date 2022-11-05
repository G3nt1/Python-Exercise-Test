numbers = []
# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter a number at location ", i, ":")
#  # accept float number from user
    item = float(input())
    numbers.append(item)

print("User list", numbers)


#versioni me emra
emrat = []
for i in range(1,7):
# i kalon ne range nga 1-7 dhe percakton vendin e input
    print("Shkruani nje emer ne vendin ", i,)
# items mbledhe te dhebat e inputev
    items=input()
#emrat bejne append items te marra nga inputet
    emrat.append(items)
print("Emrat e listes jane", emrat)