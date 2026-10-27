from HumanBody.organism import Organism

student1 = Organism("Паникёр", 10, 2, 4)
student2 = Organism("Отличник", 4, 10, 8)
student3 = Organism("Ночной герой", 8, 7, 2)

print("~~~~~ ЭКЗАМЕН: ПАНИКЁР ~~~~~")
student1.brain()
student1.heart()
student1.stomach()
student1.bladder()
print()

print("~~~~~ ЭКЗАМЕН: ОТЛИЧНИК ~~~~~")
student2.brain()
student2.heart()
student2.stomach()
student2.bladder()
print()

print("~~~~~ ЭКЗАМЕН: НОЧНОЙ ГЕРОЙ ~~~~~")
student3.brain()
student3.heart()
student3.stomach()
student3.bladder()