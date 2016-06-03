class Kangaroo(object):
    def __init__(self,pouch_content):
        self.pouch_content= [] #has to be empty list
        
        
    def __add__(self,other):
        self.pouch_content.append(other)
        return self.pouch_content
    
    
angie= kangaroo("...")
angie.__add__("banana")
    # def __str__(self):
