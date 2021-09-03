class A:
  name = "Fahad"
  def __init__(self):
      print("A")
class B(A):
  def __init__(self):
      print("B")
class C(B):
  def __init__(self):
      print("C")
  def send(self):
    print(self.name)
obj = C()
obj.send()
