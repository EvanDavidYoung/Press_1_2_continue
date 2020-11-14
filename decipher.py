def decipher(s):
    # split string into array
    words_array = s.split()
    
    count_dict = {
        'OPTICAL': 0,
        'PHARMACY':  0,
        'AUTOMOTIVE': 0,
        'MEMBERSHIP': 0,
        'PRINTING': 0
    }

    # Iterate through array, checking for matches in map
    for word in words_array:
        word = clean_string(word)

        if word in OPTICAL:
            count_dict["OPTICAL"] += 1
        elif word in AUTOMOTIVE:
            count_dict["AUTOMOTIVE"]  += 1

        elif word in MEMBERSHIP:
            count_dict["MEMBERSHIP"]  += 1

        elif word in PRINTING:
            count_dict["PRINTING"]  += 1


    # returns key of the highest count value
    chosen_category = max(count_dict, key=count_dict.get)

    # if the highest count is zero, return not found
    if count_dict[chosen_category] == 0:
        return "NOTFOUND"
    print(count_dict)
    return chosen_category



def clean_string(s):
    s = s.replace(" ", "") 
    s = s.lower()
    return s





OPTICAL = {
"contact",
"contacts",
"eye",
"glasses",
"checkup",
"optometrist",
"optical",
"prescription",
"lense",
"lenses",
}

AUTOMOTIVE = {
"automotive",
"tires",
"oil",
"repair",
"auto"
}

MEMBERSHIP = {
"membership",
"renew"
}

PRINTING = {
"print", 
"printing", 
"photo",
"pictures",
"photos"
}