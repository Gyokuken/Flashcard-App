import os

# there will be 2 feilds : 
# Add and take quiz -> this take quiz is just traversal of dictionary

master = {}
case = "0"
while case!="2":
    case = str(input("\nTo Add : Press 1\nTo take a quiz : Press 0\nTo exit : Any Other key\n-->"))
    if case == "0":
        strques = str(input("\nEnter the question : "))
        strans = str(input("Enter the answer : "))
        strans.rstrip(" ") #removing the whitespaces
        master[strques] = strans

    elif case== "1" :
        # This will traverse through the dictionary
        if not master:
            os.system("clear")
            print("The dictionary was empty!!!\n")
            continue
        correct = 0
        total = 0
        for x in master:
            ans = str(input(f"{x} : "))
            ans.rstrip(" ")
            if master[x] == ans :
                correct+=1
                total+=1
            else :
                total+=1
        accuracy = (correct/total) * 100
        print(f"The accuracy is {accuracy:.2f}%\n")


    else :
        case = "2"
print("Program exitted successfully!!")