"""
Semua sintaksis dasar bahasa pemrogramman terdiri dari
1. Sekuensial : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali-kali selama kondisi terpenuhi
"""

#Sekuensial
print('Mom said, "go to the store"')
print('Budi said, "Ok!"')
print('Mom said, "Buy me 1 bottle of milk, if there is an egg buy 6"')
print('Mom said, "Ok!"')

print("in the store!")
milk_cost=1000
egg_available=True
if milk_cost>1000:
    print("exit store")
elif milk_cost==1000:
    print("milk",1)
if egg_available==False:
    print("exit store")
elif egg_available==True:
    print("egg", 6)
    print("exit store!")
print("bring 1 bottle of milk and 6 egg to Mom")
print('Mom said, "Nice"')



