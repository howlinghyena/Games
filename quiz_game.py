print("Welcome to my computer quiz")

playing = input("Wanna Play? ")
print(playing)

if playing.lower() != "yes":
    quit() 

print("okay! Let's Play")
score = 0

answer = input("what does cpu stand for?")
if answer == "central processing unit":
    print ('correct!')
    score += 1
else:
    print ("incorrect")


answer = input("What does RAM stand for?")
if answer == "random access memory":
    print ('correct!')
    score += 1
else:
    print ("incorrect")

answer = input("What does GPU stand for?")
if answer == "graphical processing unit":
    print ('correct!')
    score += 1
else:
    print ("incorrect")  

answer = input("What does GPU stand for?")
if answer == "graphical processing unit":
    print ('correct!')
    score += 1
else:
    print ("incorrect")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")