class person:
  def __init__(self):
      print ("Hello World from person class")
  def detail(self):
      print("this is detail from person class")

class men(person):
  # def __init__(self):
  #     super().__init__()
  #     print("Hello from men class")
  def detail(self):
      # super().detail() # call the super function..
      print("this is detail from men class")

obj = men()
obj.detail()
