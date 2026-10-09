class Individual:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"I am called {self.name}")
        
person = Individual("Bob")
person()
# Outputs: I am called Bob
