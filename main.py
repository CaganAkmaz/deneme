import time
import datetime
import random
X =("yara, eklemek, çıkartmak, düşün, ufuk, alev, anne, baba")

print("Lütfen geri sayımın ardından kelimeleri yazmaya başlayın.")

time.sleep(1)
print("---------------------------------------------------------")
print("3")
time.sleep(1)
print("---------------------------------------------------------")
print("2")
time.sleep(1)
print("---------------------------------------------------------")
print("1")
time.sleep(1)
print("---------------------------------------------------------")
print("Başla!")
time.sleep(0.2)
print("---------------------------------------------------------")
print("Kelimelerin:", X)


    


before = datetime.datetime.now()

text=input("Yaz:")
after = datetime.datetime.now()

speed = after - before
seconds = round(speed.total_seconds(),2)
letter_per_second = round(len(text) / seconds,1)


print("Kelimelerini : {} saniye içerisinde yazdın.".format(seconds))
print("Saniyede {} kelime yazdın.".format(letter_per_second))

if seconds >= 20:
    print("Yavaşsın")
    
elif seconds <= 17 and seconds >= 13:
    print("Ortalama bir hız.")
    
elif seconds <= 13 and seconds >= 9:
    print("Hızlısın!")

elif seconds <= 9 and seconds >= 6:
    print("Vay canına cidden çok hızlısın!")
    
elif seconds <= 6:
    print("Parmaklarının her biri bir çita gibi çalışıyor maşallah ")
    













elif seconds <= 4 and seconds >= 0:
    print("Yoh a..")


