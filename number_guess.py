#بازی حدس عدد
import random
secret=random.randint(1 , 20)
i=0
k=0

while i!=secret:
    i=int(input("az 1 ta 20 hads bezan:"))
    k+=1
    if i < secret:
        print("bozorg tar")
    elif i>secret:
        print("koochak tar")
print("afarin peyda kardi")
print("tedad hads ha:  "k,)
