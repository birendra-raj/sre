#comments added by biru710@gmail.com

class Toy:
    def __init__(self, color, age):
        self.color=color
        self.age = age
    
    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __del__(self):
        return 10
        
      
action_figure=Toy('Black', 0)

print(action_figure.__str__())
print(str(action_figure))

print(action_figure.__len__())
print(len(action_figure))

print(action_figure.__del__())
del action_figure
