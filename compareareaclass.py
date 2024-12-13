class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Function to compare two rectangles by their area
def compare_rectangles(rect1, rect2):
    area1 = rect1.area()
    area2 = rect2.area()
    if area1 > area2:
        print(f"Rectangle 1 with area {area1} is larger than Rectangle 2 with area {area2}.")
    elif area1 < area2:
        print(f"Rectangle 2 with area {area2} is larger than Rectangle 1 with area {area1}.")
    else:
        print(f"Both rectangles have the same area of {area1}.")

# Create two Rectangle objects
rect1 = Rectangle(10, 5)
rect2 = Rectangle(8, 6)

# Display the areas and perimeters
print("Rectangle 1:")
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())

print("\nRectangle 2:")
print("Area:", rect2.area())
print("Perimeter:", rect2.perimeter())

# Compare the two rectangles by their area
compare_rectangles(rect1, rect2)
