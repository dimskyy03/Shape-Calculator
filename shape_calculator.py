class Rectangle:
  def __init__(self,width, height):
    self.width = width
    self.height = height
  
  def set_width(self,width):
    self.width = width
  
  def set_height(self, height):
    self.height = height
    
  def get_area(self):
    self.area = self.width * self.height
    return self.area

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  def get_picture(self):
    star = '*'
    picture = ''
    if self.width > 50 or self.height > 50 :
      return 'Too big for picture.'
    else : 
      for i in range(self.height):
        picture = picture + star * self.width + '\n'
      return picture
  
  def __str__(self):
    name = Rectangle.__name__
    string = name + '(' + 'width=' + str(self.width) + ',' + 'height=' + str(self.height) + ')' + '\n'
    return string

  def get_amount_inside(self,__class__):
    if self.get_area() == __class__.get_area() :
      return 1
    elif self.get_area() < __class__.get_area() :
      return False
    else :
      return int(self.width/__class__.side) * int(self.height/__class__.side)

class Square(Rectangle):
  def __init__(self,side):
    Rectangle.__init__(self,side,side)
    self.side = side


  def set_side(self,side):
    self.side = side

  def get_area(self):
    return self.side ** 2
  
  def get_diagonal(self):
    return (self.side ** 2 + self.side ** 2) ** .5

  def __str__(self):
    name = Square.__name__
    string = name + '(' + 'side=' + str(self.side) + ')' + '\n'
    return string

  def get_picture(self):
    star = '*'
    picture = ''
    if self.side > 50 :
      return 'Too big for picture.'
    else :
      for i in range(self.side):
        picture = picture + star * self.side + '\n'
      return picture