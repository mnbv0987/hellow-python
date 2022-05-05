#abstract class, and interface in Python
from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
           pass
class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")
class Pentagon(Polygon):
    def noofsides(self):
           print("I have 5 sides")
R=Triangle()
R.noofsides()
R = Pentagon()
R.noofsides()


from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def balance_check(self):
      pass
    @abstractmethod
    def interest(self):
      pass
    class SBI(Bank):
     def balance_check(self):
        print("Balance is 100 rupees")
     def interest(self):
        print("SBI interest is 5 rupees")
s = SBI()
s.balance_check()
s.interest()

import abc
from abc import ABC, abstractmethod
class R(ABC):
    def rk(self):
        print("Abstract Base Class")
class K(R):
    def rk(self):
        super().rk()
        print("subclass ")
r = K()
r.rk()
