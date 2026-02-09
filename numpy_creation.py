import numpy as np

# Creating a 1D NumPy array
a = np.array([10, 20, 30, 40, 45, 50])

print("1D Array:", a)
print("First element:", a[0])
print("Last element:", a[-1])

# Slicing operations
print("Slice from index 1 to 4:", a[1:4])
print("Every second element:", a[::2])
print("Reversed array:", a[::-1])

print("\n----------------------\n")

# Creating a 2D NumPy array
b = np.array([
    [10, 20, 30],
    [40, 45, 50]
])

print("2D Array:\n", b)
print("Element at position [1,1]:", b[1, 1])
print("First row:", b[0, :])
print("First column:", b[:, 0])
