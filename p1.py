def check_guess(guess,answer):
    global score
    still_guessing =True
    attempt=0
    while still_guessing and attempt<3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score+1
            still_guessing= False
        else:
            if attempt<2:
                guess =input("sorry wrong answer,tryagain")
                attempt=attempt+1
            if attempt==3:
                print ("Correct answer is ",answer)
score = 0
print ("guess the animal")
guess1 = input("which bear lives at the north pole?")
check_guess(guess1,"polar bear")
guess2 = input("which is the fatest land animal?")
check_guess(guess2,"cheetah")
guess3 =input("which is the largest animal?")
check_guess(guess3,"Blue whale")
print("your score is",str(score))
