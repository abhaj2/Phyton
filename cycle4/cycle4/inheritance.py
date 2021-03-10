class parent:
    def __init__(self):
        print("Calling parent constructor")
    def parentfunction(self):
        print("This is the parent function")
class child(parent):
    def __init__(self):
        print("calling child constructor")
    def childfunction(self):
        print("This is the child function")
c = child()
c.childfunction()
c.parentfunction()
