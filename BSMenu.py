__author__ = 'Samuel'
print ("-----------------------------------------------------------------------------------------------------------------------------------------------")
print ('Welcome to the Business Studies Repository. This repository currently holds the first 3 chapters of the textbook.')
print ('To make the next line of text appear or to confirm a choice, press Enter.')
print ('Make sure you follow the input directions exactly. Any wrong inputs will cause the program to crash cause i code like a depressed three year old.')
print ('Would you like to access the Flashcards or the Tests? Please Type your choice.')
print ("-----------------------------------------------------------------------------------------------------------------------------------------------")
pth0 = input()
if pth0 == 'Flashcards' or 'Flashcard' or 'flashcards' or 'flashcard' or '1' or 'one':
    import BsFlashcards
elif pth0 == 'Test' or 'Test' or 'tests' or 'test' or '2' or 'two':
    import BSTests
else:
    print ('You have chosen something that does not exist. Please restart the program.')
    input = yeet()
    print ('Sys.exit')