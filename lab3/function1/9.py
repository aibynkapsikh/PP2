import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Example usage:
r = float(input("Enter radius: "))
print(f"Volume: {sphere_volume(r):.2f}")
