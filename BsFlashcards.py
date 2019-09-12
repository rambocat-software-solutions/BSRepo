__author__ = 'Samuel'
print ("-----------------------------------------------------------------------------------------------------------------------------------------------")
print ('Welcome to the Flashcards menu. Please choose the chapter number you would like to review.')
print ('    ')
print ('1. Understanding Business Activity')
print ('2. People in Business')
print ('3. Marketing')
print ('4. Coming Soon')
print ('5. Coming Soon')
print ('6. Coming Soon')
print ('7. Back to Menu')
print ("-----------------------------------------------------------------------------------------------------------------------------------------------")
pth1 = input()
if pth1 == "1" or 'One' or 'one':
    import BSCptr1_1
    hold = input()
elif pth1 == '2' or 'Two' or "two":
    import BSCptr2_1
    hold = input()
elif pth1 == '3' or 'Three' or 'three':
    import BSCptr3_1
    hold = input()
elif pth1 == '7' or 'Seven' or 'seven' or 'back' or 'Back' or 'Back to Menu' or 'back to menu':
    import BSMenu
    hold = input()
else:
    print ('You have chosen something that does not exist. Please restart the program.')
    input = yeet()
    print ('Sys.exit')