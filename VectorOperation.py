import math
import numpy as np
import matplotlib.pyplot as plt

def create_vector(components):
    return components

def add_vectors(vector1, vector2):
    if len(vector1) == len(vector2):
        result = [x + y for x, y in zip(vector1, vector2)]
        return result
    else:
        raise ValueError("Vector harus memiliki dimensi yang sama untuk melakukan pertambahan!!")

def subtract_vectors(vector1, vector2):
    if len(vector1) == len(vector2):
        result = [x - y for x, y in zip(vector1, vector2)]
        return result
    else:
        raise ValueError("Vector harus memiliki dimensi yang sama untuk melakukan pengurangan!!")

def input_vector(component_number):
    components = input(f"Masukkan komponen vektor ke-{component_number} (pisahkan dengan spasi): ")
    components = [float(x) for x in components.split()]
    return components

def plot_2d_vector(vector, color, label):
    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)
    plt.xlim(0, max(vector) + 1)
    plt.ylim(0, max(vector) + 1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.legend()
    plt.show()

# Input vektor
vector1 = input_vector(1)
vector2 = input_vector(2)

print("Vector 1:", vector1)
print("Vector 2:", vector2)

# Penjumlahan
sum_vector = add_vectors(vector1, vector2)
print("Sum:", sum_vector)

# Pengurangan
diff_vector = subtract_vectors(vector1, vector2)
print("Difference:", diff_vector)

# Visualisasi 2D jika vektor memiliki 2 komponen
if len(vector1) == 2:
    plot_2d_vector(vector1, 'b', 'Vector 1')
    plot_2d_vector(vector2, 'r', 'Vector 2')
    plot_2d_vector(sum_vector, 'g', 'Sum Vector')
    plot_2d_vector(diff_vector, 'y', 'Difference Vector')
