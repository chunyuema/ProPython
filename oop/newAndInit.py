class TestClass(object):
    def __new__(cls, *args, **kwargs):
        print("new is called")
        return object.__new__(cls)

    def __init__(self, testName):
        print("init is called")
        self.testName = testName


print(TestClass("Chunyue").testName)
