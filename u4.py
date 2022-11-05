def language(name, lang):
    
    if lang.upper() == "G":
        print("Guten Tag " + name )
    elif lang.upper() == "I":
        print("Ciao  " + name)
    elif lang.upper() == "A":
        print("Pershendetje " + name)
    else:
        print("Hello " + name )
        

language("Ambra", "A")


