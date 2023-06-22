import automobile

#create instances of automobile
auto1 = automobile.Automobile("Mercury", "Sable", "1234", 3.0, "Bob", 2000)
auto2 = automobile.Automobile("Honda", "Accord", "23456", 2.2, "Alice", 2003)

#change auto2 year
auto2.__year = 2020

#change auto1 owner
auto1.set_owner('Jerry')


auto_list = []
auto_list.append(auto1)
auto_list.append(auto2)

#print each automobile's info
for auto in auto_list:
    auto.print_data()
    print(f' This Automobile is {auto.get_age()} years old')
