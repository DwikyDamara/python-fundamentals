Book_list=["Atom","Proton","Neutron","Elektron","Solid"]
print(Book_list)

print("\nUsing for")
for book in Book_list:
    print(book)

print("\nSpecific indeks element")
print(Book_list[1])
print(Book_list[2])

print("\nUsing for in range")
for book in range(0,len(Book_list)):
    print(Book_list[book])

print("\nList can be added multiple type data ")
Library_Data=["Sawala", 1995, 2200.5, -500000]
for i in range(0,len(Library_Data)):
    print(Library_Data[i])

print("\nAdd data to the end list using append")
Book_list.append("Molecul")
print(Book_list)

print("\nReplace data to specific index place")
Book_list[4]="Liquid"
print(Book_list)

print("\nDelete data in specific indeks place and saving it using pop")
Book_Trashbin=Book_list.pop(4)
print(Book_list)

print(f"\nbuku yang disisihkan adalah {Book_Trashbin}")

print("\nUsing pop to delete end index list")
Book_list.pop()
print(Book_list)

print("\nBy using minus, python read from reverse end")
Book_list.pop(-1)
print(Book_list)

print("\nDelete All list using clear")
Book_list.clear()
print(Book_list)

print("\nDelete data in specific indeks place without saving it using del")
Book_list=["Atom","Proton","Neutron","Elektron","Solid"]
del Book_list[4]
print(Book_list)


