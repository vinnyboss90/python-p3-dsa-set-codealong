class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    
    
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary = {}
        return self
    
    def __str__(self):
        string = "MySet: {"
        for value in self.dictionary:
            string += f"{value},"
        string = string[0:(len(string) - 1)] + "}"
        return string