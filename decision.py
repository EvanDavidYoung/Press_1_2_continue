from decipher import *
from voice_module import * 
import speech_recognition as sr 
import recognize_speech as rs
print( "Hi, welcome to Costco. In a couple of words, please share how I can help you today.")
print( "Or, if you prefer to use the keypad, press 2 to begin.\nPara espanol, oprima 9.")

# wait for user input 
# arbitrary variables, can be changed later
voice = "voice"
mode = "speech" 
# keypad = input()




intro = """Hi, welcome to Costco. In a couple of words, please share how I can help you today.
            Or, if you prefer to use the keypad, press 2 to begin.\nPara espanol, oprima 9."""
TTS(intro)
print("<<")
keypad = input()
# speech  
if(keypad == "1"):
    prompt = "In a few words, share how I can help you today?"
    count = 0
    TTS(prompt)
    confirmation = False 
    department = "" 
    while(confirmation is False and count <= 2):
        # listen 
        text = rs.listen()
        department = decipher(text)
        print(text)
        print(department)
        # listen (yes or no) 
        TTS("Just to confirm, would you like to go to the "+department+" department?")
        confirmation = rs.confirm_listen() #returns true or false based on whether user said yes or no
        if(confirmation == False):
            count += 1 
    if(count > 2): 
        TTS("You are being directed to a representative.")  
    else:
        TTS("we are now directing you to the " + department + ".")
# keypad 
elif(keypad == "2"): 
    prompt = ""
    prompt = """For the optical department, please press 1, for the mechanical department, please press 2, 
                for the membership department, please press 3, and for the photos department, please press 4."""
    # TO DO: IMPLEMENT THE TEXT BELOW
    # wait for user input with timeout
        # if timeout, resay prompt if less than once
        # if timeout more than once redirect to general representative
    # if recieved expected input
        # redirecct to corrsponding department
    # else resay prompt
        # if more than once
            # redirect to general respresentative
    TTS(prompt)
        

# # USER CHOOSES VOICE OPTION ---
# if voice != "voice":
#     print( "user input confirmation and list out options")
#     if "0": 
#         print( "list options")
#     if "option":
#         #redirect user to option
#         if "Eyecare":
#             print( "Redirecting you to the eyecare line...")
#         if "Pharmacy":
#             print( "Redirecting you to the pharmacy line...")
#         if "Automobile":
#             print( "Redirecting you to the automobile services line...")
#         if "Returns":
#             print( "Redirecting you to the returns line...")

#     elif voice != "option":
#         count+=1    #count the number of times user cannot be understood
#         print( "Sorry, we didn't catch that. Please let us know how we can help. Or, press 0 to hear our menu options"
#         if keypad == "0":
#             print( "list out options, give users option to use keypad instead"
#             #if user decides to use keypad
#             if "1":
#                 print( "Redirecting you to the eyecare line...")
#             if "2":
#                 print( "Redirecting you to the pharmacy line...")
#             if "3":
#                 print( "Redirecting you to the automobile services line...")
#             if "4":
#                 print( "Redirecting you to the returns line...")

#         if count < 2:
#             if "option":
#                 #redirect user to option
#                 if "Eyecare":
#                     print( "Redirecting you to the eyecare line...")
#                 if "Pharmacy":
#                     print( "Redirecting you to the pharmacy line...")
#                 if "Automobile":
#                     print( "Redirecting you to the automobile services line...")
#                 if "Returns":
#                     print( "Redirecting you to the returns line...")
#         if count > 2:
#             print( "Redirecting you to general customer service line...")



# # USER CHOOSES KEYPAD OPTION ---
# if keypad:
#     print( "list out options")
#     # await user input 
#     if "0":
#         print( "list out options")
#         # await user input 
#         if "2":
#             # await user input 
#             if "1":
#                 print( "Redirecting you to the eyecare line...")
#             if "2":
#                 print( "Redirecting you to the pharmacy line...")
#             if "3":
#                 print( "Redirecting you to the automobile services line...")
#             if "4":
#                 print( "Redirecting you to the returns line...")
#         #if user times out, redirect to general customer service
#         else:
#             print( "Redirecting you to general customer service line...")
#     #if user presses 2, go to list of options
#     if "2":
#         #redirect user to option
#         if "1":
#             print( "Redirecting you to the eyecare line...")
#         if "2":
#             print( "Redirecting you to the pharmacy line...")
#         if "3":
#             print( "Redirecting you to the automobile services line...")
#         if "4":
#             print( "Redirecting you to the returns line...")
#     #if user times out, redirect to general customer service
#     else:
#         print( "Redirecting you to general customer service line...")
#input validation, if user does not press 2 initially


# keypad != "2": 
#     print( "Invalid number. Please try again.")
#     print( "Redirecting you to general customer service line...")




