def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Example usage:
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if is_triangle(a, b, c):
    print("It is possible to form a triangle with sides {}, {}, and {}.".format(a, b, c))
else:
    print("It is not possible to form a triangle with sides {}, {}, and {}.".format(a, b, c))
