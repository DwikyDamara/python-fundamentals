print("\nList comprehension using del")
Book_list=["Atom","Proton","Neutron","Elektron","Solid"]
del Book_list[:]
print(Book_list)

print("\nList comprehension fill start and end")
Book_list=["Atom","Proton","Neutron","Elektron","Solid"]
del Book_list[0:-1] # Start:End
print(Book_list)

print("\nList comprehension fill start and end and step")
Book_list=["Atom","Proton","Neutron","Elektron","Solid"]
del Book_list[0::3] # Start:End:Step
print(Book_list)

print("\nCreate new list based on old list Using list comprehension")
New_Book_list=Book_list[:]
del Book_list[:]
print("This is old book list after del all list")
print(Book_list)
print("This is new book list")
print(New_Book_list)

print("Create collection from book list using slicing")
Book_list=["Atom","Proton","Neutron","Elektron","Solid"]
Atomic_Collection=Book_list[0:4]
print(Atomic_Collection)