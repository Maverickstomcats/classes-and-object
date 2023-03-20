#create a house class
class anime:
  #constructor method are  called methods
  #variables in classes are attributes:
  def __init__(self,area,windows,width,height,colors,floors,occupied):
    self.area = area
    self.windows = windows
    self.width = width
    self.height = height
    self.colors = colors
    self.floors = floors
    self.occupied = occupied 

def area(width,height):
  return width * height