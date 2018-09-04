# --- Define your functions below! ---
# --- Intro to knwoing the person ---
def intro():
    print("Hello, this is chatbot")
    person = input("What is your name?")
    print('Nice to meet you '  +  person )
    print ("I'm your virtual friend")

    print('Lets get to know you '  + person )
    answer= input("What's your favorite color?")
    print("Mine too")

    answer = input("What is your favorite food?")
    print("I like Tuna")

    print("Let's keep going!")
    activity = input("What do you do on your free time?")
    print(activity + ' seems very intresting! ')

    answer = input ("Who's your celebrity crush?")
    print ("Ha what a coincidence, that's mine too!")

    answer = input ("what is your favorite TV show?")
    print ("I prefer Pretty Little Liars")

#--- would you rather games ---

def getToKnow():
    answer1 = input("Would you rather, fly or teleport?")
 # while (wouldYouRather1)
 #    print ("answer1")
    #while answer is neither, say not a choice and then copy in line 29
    wouldYouRather1 (answer1)
    if answer1 == ("fly" or "teleport"):
        print("That's cool")
    else:
        print ("Not a choice, try again")

    answer2= input("Would you rather, be a great Brianna or Brianna? ")
    wouldYouRather2 (answer2)
    if answer2 == ("Brianna" or "Brianna"):
        print("Interesting")
    else:
        print ("Not a choice, try again")
    answer2= input("Would you rather, be a great singer or dancer? ")
    wouldYouRather2 (answer2)
    if answer2 == ("singer" or "dancer"):
        print("Interesting")
    else:
        print ("Not a choice, try again")

#--last question --
    answer3 = input ("Did you like this?")
    lastQuestion (answer3)

# --- def games ---
def wouldYouRather1(game):
    if game == ("fly"):
        game= input("Where would you fly to?")
    elif game == ("teleport"):
        game = input ("where would you teleport?")

def wouldYouRather2(game_1):
    if game_1 == ("singer"):
        game_1 = input("why?")

    elif game_1 == ("dancer"):
        game_1= input("why?")

def lastQuestion (end):
    if end == ("yes"):
        print("thank you")

    elif end == ("no"):
        print ("That wasn't very nice")

# --- return value ---

def main():
    intro()
    getToKnow()

#        answer = input("Would you rather, fly or teleport?")
#        processInput (answer)
#        print("That's cool")
#        answer= input("Would you rather, be a great singer or dancer? ")
#        processInput (answer)
#        answer = input ("Did you like this?")
#        processInput (answer)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
