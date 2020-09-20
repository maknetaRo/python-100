import random


def name_array(file):
    with open(file) as fp:
        new_list = []
        for line in fp:
            new_list.append(line.strip())
    return new_list


file = "male_first_names.txt"
male_names = name_array(file)

file = "female_first_names.txt"
female_names = name_array(file)

file = "last_names.txt"
last_names = name_array(file)


def random_name():
    gender = input("Male or female: ")
    if gender.lower() == "male":
        result = f"{random.choice(male_names)} {random.choice(last_names)}"
    elif gender.lower() == "female":
        result = f"{random.choice(female_names)} {random.choice(last_names)}"
    else:
        result = "Please write 'male' or 'female' to randomly print out the name or pres 'Ctrl+C' to end."
    return result


try:
    while True:
        print(random_name())
except KeyboardInterrupt:
    pass

