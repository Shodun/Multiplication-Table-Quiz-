import random
while True:
    list1=[3,4,6,7,8,9]
    list2=[3,4,6,7,8,9]
    number1=random.choice(list1)
    number2=random.choice(list2)
    result=number1*number2
    result2 = int(input(str(number1) + "x" + str(number2) + ":"))

    if (result == result2):

        print("Correct answer")
    else:
        print("Wrong answer: "+str(result))
    continue




