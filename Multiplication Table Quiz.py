import random,time
print("Made by SHODUN")

Language= int(input("Please Select Language/Lütfen Dil Seçiniz 1.Türkçe/2.English: "))
if Language==1:
    Answer="Doğru Cevap: "
    WrongAnswer="Yanlış Cevap: "
    Negatif="Negatif Sayı Olsun mu 1.Evet/2.Hayır: "
    Valid="Lütfen Geçerli Bir Şey giriniz "

elif Language==2:
    Answer = "Correct Answer "
    WrongAnswer = "Wrong Answer: "
    Valid="Please enter something valid"
    Negatif="Do you want negative numbers 1.Yes/2.No"
Negative=int(input(Negatif))
if Negative==1:
    list1 = [3, 4, 6, 7, 8, 9, -3, -4, -6, -7, -8, -9]
    list2 = [3, 4, 6, 7, 8, 9, -3, -4, -6, -7, -8, -9]

elif Negative==2:
    list1 = [3, 4, 6, 7, 8, 9, ]
    list2 = [3, 4, 6, 7, 8, 9, ]
while True:

    number1=random.choice(list1)
    number2=random.choice(list2)
    result=number1*number2
    result2 = int(input(str(number1) + " x " + str(number2) + ":"))

    if (result == result2):

        print(Answer)
    else:
        print(str(WrongAnswer)+str(result))
    continue








