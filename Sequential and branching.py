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
print("Budi walk to the store.")
print("in the store!")

# Percabangan
milk_cost=1000
egg_available=True
print('Budi ask to storekeeper"How much for 1 bottle of milk?"')
print(f'Storekeeper said,"{milk_cost}"')
if milk_cost==1000:
    print('Budi said,"Nice, enough!"')
    print('Budi said,"Then is there an egg"')
    print('Storekeeper said,"Yes')
    if egg_available==True:
        print('Budi said,"buy 1 bottle of milk and 6 eggs"')
    else:
        print('Budi said,"just buy 1 bottle of milk"')
print("exit store!")
print("bring 1 bottle of milk and 6 egg to Mom")
print('Mom said, "Nice"')



