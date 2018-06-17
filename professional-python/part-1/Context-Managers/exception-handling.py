"""
If the __exit__ method receives an exception, it has the responsibility to handle the exception:
It has three options:
a) It can propogate the exception(causing ito be re-raised after __exit__ finishes) (by returning False)
b) It can suppress the exception (by returning True)
c) It can rasie a different exception (a different exception is raised in __exit__ method and is used in place
   of the exceptions it was sent)
"""
