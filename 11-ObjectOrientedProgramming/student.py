# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.kierunek=""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.kierunek = "Psychologia"
    student2.name = "Olivia"
    student2.age = 21
    student2.kierunek= "Zarządzanie"
    student3.name= 'Ania'
    student3.age = 18
    student3.kierunek = "Informatyka stosowana"


    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old {student1.kierunek}')
    print(f'{student2.name}, {student2.age} years old {student2.kierunek}')
    print(f'{student3.name}, {student3.age} years old {student3.kierunek}')

if __name__ == "__main__":
    main()