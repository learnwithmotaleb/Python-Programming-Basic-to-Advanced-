class Student:
     university = "Northern University"

     def change_Univerty(self, new_Name):
          self.university = new_Name



print(Student.university)
Student.change_Univerty("Uttara University")
print(Student.university)