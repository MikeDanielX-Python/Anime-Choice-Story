import random

titulo = "Welcome to the Kamen rider/ Anime Story"
print("\n" + titulo + "\n" + "-" * len(titulo))
print("\n""This, is the adventure that will decide how good of a hero you are""\n"
      "Including, if you can save this world""\n")

gender = input("Select your gender [M/F]:""\n")

if gender.upper() == "M" or gender.upper() == "F":
    print("Gender set""\n")
else:
    gender2 = input("Put your Gender:""\n")
    if gender2.upper() == "NO" or gender2 == "n":
        print("Okay then bye bye")
        exit()
    else:
        print("Gender set""\n")

name = input("Put your name:" "\n")
print("Name" + " " + "'" + name + "'" + " " + "has been set""\n")
print(name + " " + "was in School, walking in the corridor, to go to his class""\n"
"For that" + " " + name + " " + "needed to climb the stairs, which was annoying for him""\n"
"Suddenly, a high explosion could be heared from the other side of the School""\n"

"\n""You went running to see what happened, where suddenly, you saw people""\n"
"running away from the whole scene and you could see the siluettes of monsters""\n"
"comming in the School""\n")

choice = input("Now, is your choice, what will you do?: ""\n"
               "a - Run away""\n"
               "b - Fight""\n"
               "Answer:" + " ")

if choice.lower() == "a":
    print("\n""You started to run away, out of desesperation""\n"
          "You run fast and you leave behind some other people, but you see that""\n"
          "the monsters are caching up and they start to kill people""\n")

    choice_runaway = input("What will you do then?: ""\n"
                           "a - Continue Running""\n"
                           "b - Save people""\n"
                           "Answer:" + " ")

    if choice_runaway.lower() == "a":
        print("\n""You decide to protect yourself and run, but they catch up too fast""\n"
              "You die""\n"
              "\n""The end")
        exit()
    else:
        print("\n""You decide to protect people but you dont have power again the monsters""\n"
              "You die""\n"
              "\n""The end")
        exit()

elif choice.lower() == "b":
    print("\n""As you determine to fight the monsters, you see in the ground a watch""\n"
          "A watch that caught you attention, A watch looks like is not from this world""\n"
          "A watch that could kill you? is a monster watch? is what?""\n")
    choice_fight = input("\n""what will you do?""\n"
                         "a - Take the watch""\n"
                         "b - Not Taking the watch""\n"
                         "Answer:" + " ")
    watch = False

    if choice_fight == "a":
        print("\n""You put on the watch as fast as you can and you have a weird feeling...""\n")
        watch = True
    else:
        print("you forget about the watch""\n")

    print("After that instant, you realise that a monster is going to swing you""\n"
          "with a giant bat, where did it come from?""\n"
          "Trying to defend yourself as you cant dodge from the speed""\n"
          "You cross your arms to protect yourself""\n")
    if watch:
        print("As the bat connects your arm, you dont feel anything, you hear a voice in your head""\n"
              "Heeeenshin time, ora ora!""\n")
        number = int(input("Say a number:"))
        number_random = number * random.randint(1, 100)

        print("\n""Checking preferences accourding to total heroes""\n"
              "\n""Total heroes are:" + str(number_random) + "\n")

        print("\n""Attention: Upgrade possible to multiples heroes""\n"
              "Accept?""\n"
              "Yes""\n"
              "Upgrade Successful""\n")

        characters = input("\n""Select a Character:""\n"
                           "a - Naruto""\n"
                           "b - Yusuke""\n"
                           "c - Asta""\n"
                           "Answer:" + " ")

        print("\n""As you say he's name, you realise you where spacing that moment""\n"
              "\n""You are in the same place, same scenario but your hand is extended to the bat""\n"
              "Like if you stopped the swing of the monster with your own hands?""\n"
              "Looking at your hands, you realize you have become an that Character" "\n"
                                                                                  
              "\n""All the knowledge of that character is integrated and inputed into you""\n"
              "by the watch system? memories? imagination?""\n"
              "And you know what to do""\n")

        end_good = "At the end, you saved everyone as everybody runned away in time""\n" \
                   "And the transfomation stops, leaving you inconcious from exhaustion""\n"\
                   "As you wake up, you realize everything that happened and everyone is fine""\n"\
                   "You smile with happiness while you see the sun"

        if characters.lower() == "a":
            print("you Kagebunshin to all the other characters you have and full on fight")
            print(end_good)
            exit()

        elif characters.lower() == "b":
            print("Spiritual power, reigan at the end""\n")
            print(end_good)
            exit()

        else:
            print("\n""You selected Asta as a character but the Demon inside his magic powers""\n"
              "consumes you and takes posession of your soul""\n"
              "Although he kills all the monsters, you dont exist again""\n"
              "Everyone is saved but your soul dies""\n")
            exit()
    else:
        print("you just died from the hit")
else:
    print("So you are standing there?""\n"
          "You just die in the worst way possible")
    exit()
