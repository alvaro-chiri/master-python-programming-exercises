class StrObject:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Enter String:")

    def printString(self):
        print(self.input_string.upper())

def test_Str_Object():
    str_object = StrObject()

    str_object.get_string()

    print("Uppercase String:")
    str_object.printString()

test_Str_Object