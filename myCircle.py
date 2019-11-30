class Circle: 
    import math
    k=math.pi
    def __init__(self,radius=1):        
        if radius < 0:
            raise ValueError("Radius cannot be negative") 
        else:
            self.radius=radius
            
        #self.area=Circle.k * (self.radius ** 2)
  
    #So the Property keyword let's us access a method as if it were an attribute
    #And the symbol {} get's the most current value for the variable radius
    
    @property
    def radius(self):       #I want to ensure that when radius is set from outside the class, the value is not negative                            
        return self._radius
    
    @radius.setter
    def radius(self,radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative") 
        else:
            self._radius=radius
    @property      
    def diameter(self):
        if self.radius < 0:
            raise ValueError("Radius cannot be negative") 
        else:
            return '{}'.format(self.radius * 2)
    
    @diameter.setter
    def diameter(self,diameter):
        self.radius=(self.diameter)/2
        
    @property
    def area(self):
        if self.radius < 0:
            raise ValueError("Radius cannot be negative") 
        else:
            return '{}'.format(Circle.k * (self.radius ** 2))
    
    
       