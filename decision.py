
print "Hi, welcome to Costco. In a couple of words, please share how I can help you today."
print "Or, if you prefer to use the keypad, press 2 to begin.\nPara espanol, oprima 9."

# arbitrary variables, can be changed later
voice = "voice"
keypad = "2"
count = 0

# USER CHOOSES VOICE OPTION ---
if voice:
    print "user input confirmation and list out options"

    if "0": 
        print "list options"

    if "option":
        #redirect user to option
        if "Eyecare":
            print "Redirecting you to the eyecare line..."
        if "Pharmacy":
            print "Redirecting you to the pharmacy line..."
        if "Automobile":
            print "Redirecting you to the automobile services line..."
        if "Returns":
            print "Redirecting you to the returns line..."

    elif voice != "option":
        count+=1    #count the number of times user cannot be understood
        print "Sorry, we didn't catch that. Please let us know how we can help. Or, press 0 to hear our menu options"
        if "0":
            print "list out options, give users option to use keypad instead"
            #if user decides to use keypad
            if "1":
                print "Redirecting you to the eyecare line..."
            if "2":
                print "Redirecting you to the pharmacy line..."
            if "3":
                print "Redirecting you to the automobile services line..."
            if "4":
                print "Redirecting you to the returns line..."

        if count < 2:
            if "option":
                #redirect user to option
                if "Eyecare":
                    print "Redirecting you to the eyecare line..."
                if "Pharmacy":
                    print "Redirecting you to the pharmacy line..."
                if "Automobile":
                    print "Redirecting you to the automobile services line..."
                if "Returns":
                    print "Redirecting you to the returns line..."
        if count > 2:
            print "Redirecting you to general customer service line..."



# USER CHOOSES KEYPAD OPTION ---
if keypad:
    print "list out options"

    if "0":
        print "list out options"
        if "2":
            #redirect user to option
            if "1":
                print "Redirecting you to the eyecare line..."
            if "2":
                print "Redirecting you to the pharmacy line..."
            if "3":
                print "Redirecting you to the automobile services line..."
            if "4":
                print "Redirecting you to the returns line..."
        #if user times out, redirect to general customer service
        else:
            print "Redirecting you to general customer service line..."
    #if user presses 2, go to list of options
    if "2":
        #redirect user to option
        if "1":
            print "Redirecting you to the eyecare line..."
        if "2":
            print "Redirecting you to the pharmacy line..."
        if "3":
            print "Redirecting you to the automobile services line..."
        if "4":
            print "Redirecting you to the returns line..."
    #if user times out, redirect to general customer service
    else:
        print "Redirecting you to general customer service line..."
        
#input validation, if user does not press 2 initially
elif keypad != "2": 
    print "Invalid number. Please try again."
    if keypad:
        print "list out options"

        if "0":
            print "list out options"
            if "2":
                #redirect user to option
                if "1":
                    print "Redirecting you to the eyecare line..."
                if "2":
                    print "Redirecting you to the pharmacy line..."
                if "3":
                    print "Redirecting you to the automobile services line..."
                if "4":
                    print "Redirecting you to the returns line..."
            #if user times out, redirect to general customer service
            else:
                print "Redirecting you to general customer service line..."
        #if user presses 2, go to list of options
        if "2":
            #redirect user to option
            if "1":
                print "Redirecting you to the eyecare line..."
            if "2":
                print "Redirecting you to the pharmacy line..."
            if "3":
                print "Redirecting you to the automobile services line..."
            if "4":
                print "Redirecting you to the returns line..."
        #if user times out, redirect to general customer service
        else:
            print "Redirecting you to general customer service line..."




