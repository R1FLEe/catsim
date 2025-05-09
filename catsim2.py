#class Stundent:
 #   print("Hi!")
 #   def __init__(self, mark=12):
 #       self.mark = 12
  #      print("It is exellent")



#first_student = Stundent()
#second_student = Stundent(mark=2)

#Stundent.__init__(self=first_student)
#print(first_student.mark)
#print(second_student.mark)


import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to eat")
        self.progress += 0.15
        self.gladness -= 0.01

    def to_sleep(self):
        print("i will sleep")
        self.gladness += 1.5

    def to_chill(self):
        print("Time to poop")
        self.gladness += 0.4
        self.progress -= 0.2

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression')
            self.alive = False

        if self.progress > 5:
            print('Passed externaly...')
            self.alive = True
    def end_day(self):
        print(f'Gladness = {round(self.gladness, 2)}')
        print(f'Progress = {round(self.progress, 2)}')


    def live(self, day):
        day_info = f'Day {day} of {self.name}\'s life'
        print(f'{day_info:^50}')
        life_cube = random.randint(1, 3)
        if life_cube == 1:
            self.to_chill()
        elif life_cube == 2:
            self.to_sleep()
        elif life_cube == 3:
            self.to_study()
        self.end_day()
        self.is_alive()


nick = Student(name='Кота')
for day in range(1, 366):
    if nick.alive == False:
        break
    nick.live(day)






