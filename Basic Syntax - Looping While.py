# Perulangan
Candy_total = 10
Candy_eaten = 0
print(f'Candy Total = {Candy_total}')
print(f'Candy Eaten = {Candy_eaten}')
while Candy_eaten < Candy_total:
    Candy_eaten = Candy_eaten + 1
    print(f'{Candy_eaten} Candy eaten')
print(f'Total Candy Eaten ="{Candy_eaten}"')

Book = 10
Book_Mastered = 0
Read_Count = 0
print(f'Book Total = {Book}')
print(f'Book Read and Mastered = {Book_Mastered}')
while Book>Book_Mastered:
    if Book_Mastered == 7:
        while Read_Count<20:
            for Read_Count in range (1, 21):
                print(f'Book {Book_Mastered + 1} was read for {Read_Count}x')
            Book_Mastered = Book_Mastered + 1
    else:
        Book_Mastered = Book_Mastered + 1
        print(f'Book {Book_Mastered} is Mastered')

