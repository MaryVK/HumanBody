from dataclasses import dataclass

@dataclass
class Organism:
    name: str
    stress: int
    preparation: int
    sleep_hours: int

    def brain(self):
        if self.preparation < 5:
            print(f"{self.name}: Мозг сообщает, что впервые видит этот предмет!")
        else:
            print(f"{self.name}: Мозг всё помнит, но отказывается сотрудничать!")


    def heart(self):
        if self.stress > 7:
            print(f"{self.name}: Сердце вылетает ! Оно пытается покинуть тело без предупреждения!")
        else:
            print(f"{self.name}: Сердце бьётся покойно, пока преподаватель не контролирует")


    def stomach(self):
        if self.sleep_hours < 5:
            print(f"{self.name}: Желудок молит покормить его")
        else:
            print(f"{self.name}: Желудок молчит, но скоро снова начнёт требовать топливо!")


    def bladder(self):
        if self.stress > 5:
            print(f"{self.name}: Мочевой пузырь требует срочного перерыва!")
        else:
            print(f"{self.name}: Мочевой пузырь решил не вмешиваться в учебный процесс!")

