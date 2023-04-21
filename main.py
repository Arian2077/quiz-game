print("Welcome to my gaming quiz!")

name = input("Can I ask your name? ")
score = 0

if name.lower() == "no":
    print("no problem,I gonna call you user :)")
    name = "user"
elif name.lower() == "yes":
    name = input("So what is your name? ")

playing = input("okay " + name + " shall we begin the quiz? ").lower()

if playing.lower() != "yes":
    print("okay then, bye", name)
    quit()
print("So let the game begin :) ")

Q1 = input("Who was the main villain in Batman Arkham Asylum? ")
if Q1.lower() == "joker":
    print("Well done")
    score += 1
else:
    print("Wrong answer, it was joker")

Q2 = input("What was the Max Payne job in first and second game? ")
if Q2.lower() == "he was a police officer" or Q2.lower() == "police officer":
    print("you got it right")
    score += 1
else:
    print("Incorrect, He was a police officer and in third game he was a bodyguard")

Q3 = input("In which game of Spider-Man you can get two endings? ")
if Q3.lower() == "in spider-man web of shadow" or Q3.lower() == "in spiderman web of shadow" or \
        Q3.lower() == "in web of shadow" or Q3.lower() == "web of shadow":
    print("nice job", name)
    score += 1
else:
    print("wrong,you can get two endings in Spider-Man Web Of Shadow!")

Q4 = input("Who was the main character of Assassin Brotherhood? ")
if Q4.lower() == "ezio auditore" or Q4.lower() == "ezio":
    print("I mean who can forget him? correct answer")
    score += 1
else:
    print("How you don't know him? it was Ezio Auditore")

print("you answered " + str((score / 4) * 100) + "% of questions correct")


