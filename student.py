class Students:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} has a {self.patronus} patronus."

    def charm(self):
        match self.patronus.lower():
            case "stag":
                return "Expecto stag!"
            case "otter":
                return "Expecto otter!"
            case "jack russell terrier":
                return "Expecto terrier!"
            case _:
                return "Expecto patronum!"

def main():
    student = get_student()
    if student:
        print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    try:
        return Students(name, house, patronus)
    except ValueError as e:
        print(e)
        return None

if __name__ == "__main__":
    main()