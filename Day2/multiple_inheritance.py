class A:
  def __init__(self):
    print("A")
  def same(self):
    print("A")
class B:
  def __init__(self):
      print("B")
  def same(self):
    print("B")
class C(A,B):
  pass
  # def same(self):
  #   print("C")
obj = C()
obj.same()
