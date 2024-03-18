class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        courses_info = ", ".join([f"{course.name} ({course.credits} crédits)" for course in self.courses])
        return f"Nom : {self.name}\nAge : {self.age}\nCours suivis : {courses_info}"

class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

# Création des instances de la classe Course
mathematiques = Course("Mathématiques", 4)
histoire = Course("Histoire", 3)
science = Course("Science", 5)
francais = Course("Français", 3)

# Création des instances de la classe Student
alice = Student("Alice", 20)
bob = Student("Bob", 22)

# Ajout des cours aux étudiants
alice.add_course(mathematiques)
alice.add_course(histoire)
bob.add_course(science)
bob.add_course(francais)

# Affichage des détails des étudiants avec les cours qu'ils suivent
print("Étudiant 1 :")
print(alice)

print("\nÉtudiant 2 :")
print(bob)