import random
bk=int(input("Kuantum sayısı"))
amk=bk-1
liste=list(range(0,amk)) #açısal momentum kuantum sayısı
mk=2*amk+1
liste2=list(range(mk,mk+1))
liste3=list(range(-len(liste),len(liste)+1))#manyetik kuantum sayısı
alfabe=["s","p","d","f"]
orbitalg="{}{}".format(len(liste),random.choice(alfabe))#orbital gösterimi tek
orbital_sayisi=list(range(1,len(liste3)+1,2))#orbital sayısı
print(orbital_sayisi)