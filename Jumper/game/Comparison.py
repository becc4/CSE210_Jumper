
class comparison():
<<<<<<< HEAD

    def compare(word,user_input):
        list_of_text = list(word)
        letter = user_input

        for letters in list_of_text:
            pass


        #compares if the user input matches a letter in the word 

        #returns either true or false 




=======
#Check if the user input matches the letter of the word
    def compare(word,user_input):
        list_of_text = list(word)
        _user_letter = user_input

        for i in list_of_text:
            if i == _user_letter:
                return True

            else:
                return False
>>>>>>> 2d40d65e85738eec87cbe14f2d9c62062f4c397e
