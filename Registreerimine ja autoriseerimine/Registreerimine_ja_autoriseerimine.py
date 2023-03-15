from random import*
from string import*
from tkinter import *

str0=".,:;!_*-+()/#¤%&"
str1 = '0123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()
print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
str4 = str0+str1+str2+str3
print(str4)
ls = list(str4)
print(ls)
random.shuffle(ls)
print(ls)
# Извлекаем из списка 12 произвольных значений
parool = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
print(parool)


#spiski
paroolid=["343dfA@54", "sfc234A@dsf"] 
sisselogimised=["Kasutaja_1", "Kasutaja_2"] 


def registreerimine(paroolid:list, sisselogimised:list)->bool:




#def salasona(k: int):
#    sala=""
#    for i in range(k):
#    t=choice(string.ascii_letters) #Aa...Zz
#    num=choice([1,2,3,4,5,6,7,8,9,0])
#    t_num=[t,str(num)]
#    sala+=choice(t_num)
#    return sala




##proverka parolja
#i=input("Sisesta täht => ")
#if(i.isupper()):
#    print("See on suur täht", i)
#a=input("Sisesta arv => ")
#if (a.isdigit()):
#    print("See on täisarv ", a)




aken=Tk()
aken.title("Autoriseerimine")