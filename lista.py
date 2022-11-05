def fillon_me(s, fillon):
    # return s.startswith(fillon)
    # return s[:len(fillon)] == fillon
    for char in s:
        if char in fillon:





print(fillon_me("Ambra", "Amb"))
print(fillon_me("Ambra", "A"))
print(fillon_me("Ambra", "R"))
print(fillon_me("Ambra", "Ambr"))
