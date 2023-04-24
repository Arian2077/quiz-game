import random as rnd

right_answers = ["Well done", "you got it right", "nice job", "Correct", "1 score for you ", "amazing"]
loop = 5
score = 0
rnum = []


def E_questions():
    global score, loop, rnum
    for i in range(loop):
        num = rnd.randint(0, loop)
        if num not in rnum:
            rnum.append(num)
            EQ = ["Who was the main villain in Batman Arkham Asylum? ",
                  "What was the Max Payne job in first and second game? ",
                  "In which game of Spider-Man you can get two endings? ",
                  "Who was the main character of Assassin Brotherhood? ",
                  "What is the name of dying light 1 city? ", "Who was Edward Kenway? ",
                  "Name one the Resident Evil 0 protagonist",
                  "How many games Grand Thief Auto has? "]
            print(EQ[num])
            answer = input("Answer: ").lower()
            if num == 0:
                if answer == "joker":
                    print(rnd.choice(right_answers))
                    score += 1
                else:
                    print("Wrong answer, it was joker")
            elif num == 1:
                if answer == "he was a police officer" or answer == "police officer" or answer == "detective":
                    print(rnd.choice(right_answers))
                    score += 1
                else:
                    print("Incorrect, He was a police officer and in third game he was a bodyguard")

            elif num == 2:
                if answer == "in spider-man web of shadows" or answer == "in spiderman web of shadows" or \
                        answer == "in web of shadows" or answer == "web of shadows":
                    print(rnd.choice(right_answers))
                    score += 1
                else:
                    print("wrong,you can get two endings in Spider-Man Web Of Shadow!")

            elif num == 3:
                if answer == "ezio auditore" or answer == "ezio":
                    print("I mean who can forget him? correct answer")
                    score += 1
                else:
                    print("How you don't know him? it was Ezio Auditore")

            elif num == 4:
                if answer == "harran":
                    print(rnd.choice(right_answers))
                    score += 1
                else:
                    print("It is a quarantine zone in a Middle-eastern city called Harran")

            elif num == 5:
                if answer == "main character of assassin black flag" or answer == "main character of assassin 4" \
                        or answer == "main character of assassin four" or answer == "protagonist of assassin black flag" or \
                        answer == "protagonist of assassin 4" or answer == "protagonist of assassin four" \
                        or answer == "ac black flag":
                    print(rnd.choice(right_answers))
                    score += 1
                else:
                    print("He was the protagonist / main character of Assassin creed: black flag")

            elif num == 6:
                if answer == "billy coen" or answer == "billy" or answer == "rebecca chambers" or answer == "rebecca":
                    print(rnd.choice(right_answers))
                    score += 1
                else:
                    print("Billy Coen and Rebecca chambers")

            elif num == 7:
                if answer == "17":
                    print(rnd.choice(right_answers))
                    score += 1
                else:
                    print("The right answer is 17")
            else:
                print("Error")
        else:
            loop += 1
            print(loop)


def M_questions():
    pass


def H_questions():
    pass


def C_questions():
    pass


def p_progress():
    print("you answered " + str(score) + " questions correctly")
    print("you answered " + str((score / 4) * 100) + "% of questions correct")


print("Welcome to my gaming quiz!")
name = input("Can I ask your name? ")
if name.lower() == "no":
    print("no problem,I gonna call you user :)")
    name = "user"
elif name.lower() == "yes":
    name = input("So what is your name? ")
    print("")
while True:
    print("1.Start\n" + "2.My progress\n" + "3.Exit\n")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("1.Easy\n" + "2.Medium\n" + "3.Hard\n")
        difficulty = input("Choose the difficulty: ")
        if difficulty == "1":
            playing = input("okay " + name + " shall we begin the quiz? ").lower()
            if playing.lower() != "yes":
                print("okay then, bye", name)
                quit()
            print("So let the game begin :) ")
            E_questions()
        elif difficulty == "2":
            pass
        elif difficulty == "3":
            pass
        else:
            print("error")
    elif choice == "3":
        print("thank you for playing ", name)
        break
    else:
        print("Error")
