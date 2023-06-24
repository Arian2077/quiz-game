import random as rnd

right_answers = ["Well done", "you got it right", "nice job", "Correct", "another score for you ", "amazing"]
c_counter = 0
score = 0
c_easy = 0
c_normal = 0
c_hard = 0


class my_quize:
    def E_questions(self):
        global score, c_easy, c_counter
        c_questions = [0, 1, 2, 3, 4, 5, 6, 7]
        for i in range(5):
            num = rnd.choice(c_questions)
            EQ = ["Who was the main villain in Batman Arkham Asylum? ",
                  "What was the Max Payne job in first and second game? ",
                  "In which game of Spider-Man you can get two endings? ",
                  "Who was the main character of Assassin Brotherhood? ",
                  "What is the name of dying light 1 city? ",
                  "Which word completes the name of this huge selling video game series, 'Call of' …",
                  "Name one the Resident Evil 0 protagonist",
                  "How many games Grand Thief Auto has? "]
            print(EQ[num])
            answer = input("Answer: ").lower()
            if num == 0:
                if answer == "joker":
                    print(rnd.choice(right_answers))
                    score += 1
                    c_easy += 1
                else:
                    print("Wrong answer, it was joker")
            elif num == 1:
                if answer == "he was a police officer" or answer == "police officer" or answer == "detective":
                    print(rnd.choice(right_answers))
                    score += 1
                    c_easy += 1
                else:
                    print("Incorrect, He was a police officer and in third game he was a bodyguard")
            elif num == 2:
                if answer == "in spider-man web of shadows" or answer == "in spiderman web of shadows" or \
                        answer == "in web of shadows" or answer == "web of shadows":
                    print(rnd.choice(right_answers))
                    score += 1
                    c_easy += 1
                else:
                    print("wrong,you can get two endings in Spider-Man Web Of Shadow!")

            elif num == 3:
                if answer == "ezio auditore" or answer == "ezio":
                    print("I mean who can forget him? correct answer")
                    score += 1
                    c_easy += 1
                else:
                    print("How you don't know him? it was Ezio Auditore")

            elif num == 4:
                if answer == "harran":
                    print(rnd.choice(right_answers))
                    score += 1
                    c_easy += 1
                else:
                    print("It is a quarantine zone in a Middle-eastern city called Harran")

            elif num == 5:
                if answer == "duty":
                    print(rnd.choice(right_answers))
                    score += 1
                    c_easy += 1
                else:
                    print("Call Of Duty, how did you miss that?")

            elif num == 6:
                if answer == "billy coen" or answer == "billy" or answer == "rebecca chambers" or answer == "rebecca":
                    print(rnd.choice(right_answers))
                    score += 1
                    c_easy += 1
                else:
                    print("Billy Coen and Rebecca chambers")

            elif num == 7:
                if answer == "17":
                    print(rnd.choice(right_answers))
                    score += 1
                    c_easy += 1
                else:
                    print("The right answer is 17")
            c_questions.remove(num)
        c_counter += 5

    def N_questions(self):
        global score, c_normal, c_counter
        c_questions = [0, 1, 2, 3, 4, 5, 6, 7]
        for i in range(5):
            num = rnd.choice(c_questions)
            MQ = ["What is the name of cannon character in assassin creed odyssey? ",
                  "Halo 3 is what type of game? ",
                  "San Andreas is a fictional US state in which game series? ",
                  "Altair must assassinate nine people who belong to what group? ",
                  "Which games character had a sidekick called Tails? ",
                  "What object in 'Super Mario Bros.' allows Mario and Luigi to grow bigger",
                  "What is the full name of 'DotA'? ",
                  "Watch Dogs 2 is set in which are of the United States?"]
            print(MQ[num])
            answer = input("Answer: ").lower()
            if num == 0:
                if answer == "kassandra":
                    print(rnd.choice(right_answers))
                    score += 2
                    c_normal += 1
                else:
                    print("It was Kassandra")
            elif num == 1:
                if answer == "first person shooter" or answer == "shooter":
                    print(rnd.choice(right_answers))
                    score += 2
                    c_normal += 1
                else:
                    print("Wrong answer,First person shooter")

            elif num == 2:
                if answer == "gta" or answer == "grand thief auto":
                    print(rnd.choice(right_answers))
                    score += 2
                    c_normal += 1
                else:
                    print("Grand thief auto which known as GTA")

            elif num == 3:
                if answer == "templars" or answer == "templar" or answer == "knights templar ":
                    print(rnd.choice(right_answers))
                    score += 2
                    c_normal += 1
                else:
                    print("The answer is knights templar")

            elif num == 4:
                if answer == "sonic":
                    print(rnd.choice(right_answers))
                    score += 2
                    c_normal += 1
                else:
                    print("The right answer is Sonic")

            elif num == 5:
                if answer == "mushroom" or answer == "a mushroom":
                    print(rnd.choice(right_answers))
                    score += 2
                    c_normal += 1
                else:
                    print("the right answer is a mushroom...")

            elif num == 6:
                if answer == "defense of the ancients":
                    print(rnd.choice(right_answers))
                    score += 2
                    c_normal += 1
                else:
                    print("DOTA stands for 'defense of the ancients' ")

            elif num == 7:
                if answer == "san francisco":
                    print(rnd.choice(right_answers))
                    score += 2
                    c_normal += 1
                else:
                    print("the right answer is San Francisco")
            c_questions.remove(num)
        c_counter += 5

    def H_questions(self):
        global score, c_hard, c_counter
        c_questions = [0, 1, 2, 3, 4, 5, 6, 7]
        for i in range(5):
            num = rnd.choice(c_questions)
            HQ = ["The original 'Resident Evil' video game was first released in what year? ",
                  "Which video game system was the first to use DVD technology? ",
                  "In Prince of Persia: The Sands of Time, Farah uses what kind of weapons? ",
                  "What was the relation of Kratos with Zeus in the game God of War? ",
                  "In what year was the first 'Assassin's Creed' released? ",
                  "The character 'Cloud' was from which of the Final Fantasy game?",
                  "How many tails does Sonic The Hedgehogs sidekick Tails have? ",
                  "Grand Theft Auto: Chinatown Wars can be played in what gaming system?"]
            print(HQ[num])
            answer = input("Answer: ").lower()
            if num == 0:
                if answer == "1996":
                    print(rnd.choice(right_answers))
                    score += 3
                    c_hard += 1
                else:
                    print("The original 'Resident Evil' video game was first released in 1996")
            elif num == 1:
                if answer == "ps2" or answer == "playstation 2":
                    print(rnd.choice(right_answers))
                    score += 3
                    c_hard += 1
                else:
                    print("it was PlayStation 2 also known as PS2")
            elif num == 2:
                if answer == "bow":
                    print(rnd.choice(right_answers))
                    score += 3
                    c_hard += 1
                else:
                    print("She was using a Bow")

            elif num == 3:
                if answer == "son":
                    print(rnd.choice(right_answers))
                    score += 3
                    c_hard += 1
                else:
                    print("Kratos was his son")

            elif num == 4:
                if answer == "2007":
                    print(rnd.choice(right_answers))
                    score += 3
                    c_hard += 1
                else:
                    print("first 'Assassin's Creed' game released in 2007")

            elif num == 5:
                if answer == "vii" or answer == "final fantasy vii":
                    print(rnd.choice(right_answers))
                    score += 3
                    c_hard += 1
                else:
                    print("the right answer is a VII...")

            elif num == 6:
                if answer == "two" or answer == "2":
                    print(rnd.choice(right_answers))
                    score += 3
                    c_hard += 1
                else:
                    print("Wrong, two ")

            elif num == 7:
                if answer == "psp":
                    print(rnd.choice(right_answers))
                    score += 3
                    c_hard += 1
                else:
                    print("Wrong, you could play it on PlayStation Portable also known as PSP")
            else:
                print("Error")
            c_questions.remove(num)
        c_counter += 5

    def p_progress(self):
        global c_easy, c_hard, c_normal
        if score == 0:
            print("You still have no progress")
        else:
            print("your score is: " + str(score) + "\n",
                  "number of easy questions that answered correctly: ", c_easy, "\n",
                  "number of normal questions that answered correctly: ", c_normal, "\n",
                  "number of hard questions that answered correctly: ", c_hard, "\n")


print("Welcome to my gaming quiz!")
name = input("Can I ask your name? ")
if name.lower() == "no":
    print("no problem,I gonna call you user :)")
    name = "user"
elif name.lower() == "yes":
    name = input("So what is your name? ")
print("okay " + name + " ,let me give you some tips about how to play: " + "\n" +
      "1.Please be careful on dictation of words" + "\n" + "2.you can write with capital letter or small letter " + "\n"
      + "3.Easy questions have 1 score , Normal questions have 2 score and hard questions has 3 score" + "\n" +
      "4.Try to enjoy the game ;) " + '\n')

obj = my_quize()

while True:
    print("1.Start\n" + "2.My progress\n" + "3.Exit\n")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("1.Easy\n" + "2.Normal\n" + "3.Hard\n")
        difficulty = input("Choose the difficulty: ")
        if difficulty == "1":
            print("So let the game begin :) ")
            obj.E_questions()
        elif difficulty == "2":
            print("So let the game begin ;) ")
            obj.N_questions()
        elif difficulty == "3":
            print("So you think you know a lot,lets get it started")
            obj.H_questions()
        else:
            print("error")
    elif choice == "2":
        obj.p_progress()
    elif choice == "3":
        print("thank you for playing ", name)
        break
    else:
        print("Error")
