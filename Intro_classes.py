class Person:
    # This function is called whenever a new Person object is created. The
    # self parameter refers to the object itself, i.e. the instance of the
    # class that is being created.
    def __init__(self, first, last):
        self.first = first
        self.middle = None
        self.last = last
        
    def __str__(self):
      if self.middle != None:
        return self.first + ' ' + self.middle + ' ' + self.last
      return self.first + ' ' + self.last
        
    def add_middle_name(self, middle):
        self.middle = middle


class Student(Person):
    def __init__(self, first, last):
        super().__init__(first, last)  # Call parent's __init__() function
        self.grades = []
        self.average = 0
    
    def __str__(self):
        return Person.__str__(self) + ' ' + str(self.grades)
    
    def add_grade(self, grade, max_grade, weight):
        self.grades.append((grade, max_grade, weight))
        
    def grades_average(self):
      max_weight,weighted_sum = 0,0
      
      if self.grades == []:
        return None
      
      for grade, max_grade, weight in self.grades:
        max_weight += weight
        weighted_sum += ((grade/max_grade)*weight)
      
      self.average = float(weighted_sum/max_weight)*100
      return self.average
    
    def __lt__(self, other):
      if self.grades != [] and other.grades != []:
        return self.grades_average() < other.grades_average()
      return False
    
    def __gt__(self, other):
      if self.grades != [] and other.grades != []:
        return self.grades_average() > other.grades_average()
      return False
    
    def __eq__(self, other):
      if self.grades != [] and other.grades != []:
        return self.grades_average() == other.grades_average()
      return False
    
    def __ge__(self, other):
      if self.grades != [] and other.grades != []:
        return self.grades_average() >= other.grades_average()
      return False
    
    def __le__(self, other):
      if self.grades != [] and other.grades != []:
        return self.grades_average() <= other.grades_average()
      return False
    
    def __ne__(self, other):
      if self.grades != [] and other.grades != []:
        return self.grades_average() != other.grades_average()
      return False
# This is to list all the methods in the Student class. See which one(s) of
# those you have to implement for part #3 of the assignment...
for f in [func for func in dir(Student) if callable(getattr(Student, func))]:
    print(f)
    
me = Student('Travis','Brown')
me.add_grade(90,100,1.0)
me.add_grade(20,25,2.0)

him = Student('Daniel','Lawla')
him.add_grade(9,100,1.0)
him.add_grade(2,25,2.0)

print(me.__str__())
print(me.grades_average())
print(me.__lt__(him))
me.add_middle_name('Jordan')
print(me.__str__())