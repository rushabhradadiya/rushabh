def compare_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    
    if area > perimeter:
        return "Area is greater than Perimeter"
    else:
        return "Perimeter is greater than or equal to Area"

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
print(compare_area_perimeter(length, breadth))