class parent:

    def method(self):
        print("calling parent method")
class child(parent):
    def __init(self):
        print("caling  child constructor")
    def method(self):
        print("calling child method")
c=parent()
c.method()
c=child()
c.method()