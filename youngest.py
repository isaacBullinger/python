
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
ages=[]
names=[]
young_age=100
young_name=''

for line in people:
    split_line = line.split(' ')
    name = split_line[0].strip()
    names.append(name)
    split_line = line.split(' ')
    age = int(split_line[1].strip())
    ages.append(age)
    if age<young_age:
        young_age=age
        young_name=name
print(f'The youngest person is: {young_name}, age {young_age}.')