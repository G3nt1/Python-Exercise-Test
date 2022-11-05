def language():
    name = input("what is your name?? \n ")
    lang = input("what language you like? G, I, A, E  \n")

    if lang.upper() == "G":
        print("Guten Tag " + name)
    elif lang.upper() == "I":
        print("Ciao  " + name)
    elif lang.upper() == "A":
        print("Pershendetje " + name)
    else:
        print("Hello " + name)


language()
