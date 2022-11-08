name = input("type your name: ")
print("welcome", name, "to this adventure!")

answer = input("You are driving in the woods alone. You are not sure where you are and there is no cell signal. Suddenly you approach a fork in the road. Will you go left or right?")

if answer == "left":
    answer = input("you come across an old cabin. It looks abandoned. Press A to keep driving, Press B to enter the cabin and look for help: ")
    
    if answer == "A":
        print('You decide to keep driving')
    elif answer == "B":
        print('You pull over and walk towards the cabin. Its old and the windows are shuttered. You open the door' )
    else:
        print('Not a valid option.')



elif answer == "right":
       answer = input('As you drive down this narrow road, it begins to get dark. You are running out of daylight and are thinking of resting for the night. Further ahead you spot a glimmer coming from a nearby lake. As you drive closer you see a small beach which would make an ideal campsite. Press A to stop here for a nights rest. Press B on keep driving')

        if answer == "A":
            print('you unload your gear and set up camp for the night. ')
        elif answer == "B":
            print('you keep driving, going deeper into the woods. Suddenly you come across a large stream that you must cross. As you roll into the water you notice the river moving faster. About halfway a surge of water comes from upstream and starts to carry your car away. Press A to abandon your vehicle and swim to shore. Press B to stay inside the car and try to cross')

                if answer == "A":
                    print('')
else: 
        print('not a valid option')