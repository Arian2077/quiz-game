import random as rnd

right_answers = ["Well done", "you got it right", "nice job", "Correct", "1 score for you ", "amazing"]

score = 0




def E_questions():
    global score
    Q1 = input("Who was the main villain in Batman Arkham Asylum? ")
    if Q1.lower() == "joker":
        print(rnd.choice(right_answers))
        score += 1
    else:
        print("Wrong answer, it was joker")

    Q2 = input("What was the Max Payne job in first and second game? ")
    if Q2.lower() == "he was a police officer" or Q2.lower() == "police officer" or Q2.lower() == "detective":
        print(rnd.choice(right_answers))
        score += 1
    else:
        print("Incorrect, He was a police officer and in third game he was a bodyguard")

    Q3 = input("In which game of Spider-Man you can get two endings? ")
    if Q3.lower() == "in spider-man web of shadows" or Q3.lower() == "in spiderman web of shadows" or \
            Q3.lower() == "in web of shadows" or Q3.lower() == "web of shadows":
        print(rnd.choice(right_answers))
        score += 1
    else:
        print("wrong,you can get two endings in Spider-Man Web Of Shadow!")

    Q4 = input("Who was the main character of Assassin Brotherhood? ")
    if Q4.lower() == "ezio auditore" or Q4.lower() == "ezio":
        print("I mean who can forget him? correct answer")
        score += 1
    else:
        print("How you don't know him? it was Ezio Auditore")

    Q5 = input("What is the name of dying light 1 city? ")
    if Q5.lower() == "harran":
        print(rnd.choice(right_answers))
        score += 1
    else:
        print("It is a quarantine zone in a Middle-eastern city called Harran")

    Q6 = input("Who was Edward Kenway? ")
    if Q6.lower() == "main character of assassin black flag" or Q6.lower() == "main character of assassin 4" \
            or Q6.lower() == "main character of assassin four" or Q6.lower() == "protagonist of assassin black flag" or \
            Q6.lower() == "protagonist of assassin 4" or Q6.lower() == "protagonist of assassin four" \
            or Q6.lower() == "ac black flag":
        print(rnd.choice(right_answers))
        score += 1
    else:
        print("He was the protagonist / main character of Assassin creed: black flag")

    Q7 = input("name one of the protagonists in Resident evil zero :) ")
    if Q7.lower() == "billy coen" or Q7.lower() == "billy" or Q7.lower() == "rebecca chambers" or Q7.lower() == "rebecca":
        print(rnd.choice(right_answers))
        score += 1
    else:
        print("Billy Coen and Rebecca chambers")


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
