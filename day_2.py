def calc_rectangle_area(length:int, breadth:int) -> int:
    return f"The area of the rectangle is {length * breadth} square units"


if __name__ == "__main__":
    length = int(input("Enter the length of the rectangle: "))
    breadth = int(input("Enter the breadth of the rectangle: "))
    print(calc_rectangle_area(length, breadth))

