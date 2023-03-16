Candy_total = 10
Candy_eaten = 0
print(f'Candy Total = {Candy_total}')
print(f'Candy Eaten = {Candy_eaten}')
while Candy_eaten < Candy_total:
    Candy_eaten = Candy_eaten + 1
    print(f'{Candy_eaten} Candy eaten')
print(f'Total Candy Eaten ="{Candy_eaten}"')

Book_Total = 10
Book_Read_and_Mastered = 0
Book_Count_Read = 0
print(f'Book Total = {Book_Total}')
print(f'Book Read and Mastered = {Book_Read_and_Mastered}')
while Book_Total>Book_Read_and_Mastered:
    if Book_Read_and_Mastered == 9:
        while Book_Count_Read<20:
            for Book_Count_Read in range (1,21):
                print(f'Book {Book_Read_and_Mastered} was read for {Book_Count_Read}x')

    else:
        Book_Read_and_Mastered = Book_Read_and_Mastered + 1
        print(f'Book {Book_Read_and_Mastered} is Mastered')

