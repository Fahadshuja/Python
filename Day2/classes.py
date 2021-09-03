class student:
  name_cl = "Fahad"
  age_cl = 21
  def __init__(self,name,age,degree):
    self.name = name
    self.age = age
    self.degree = degree

  def detail(self):
    print(f"Student {self.name}  is {self.age} years old and belong to {self.degree} Department")

  @classmethod
  def detail_class(cls):
      cls.age_cl=23
      print(f"Student {cls.name_cl}  is {cls.age_cl} years old")

  def check_updation(self):
    print(self.age_cl)

stu1= student("Ali",22,"Electrical Engineer")
# stu1.check_updation()
stu = student("Fahad",21,"Computer Science")
stu.detail_class()
stu1.check_updation()
