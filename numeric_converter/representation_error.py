import matplotlib.pyplot as plt
import math


def estimate_error(num, max_bits):
    errors = []
    bits_axis = []
    real_val = num
    
    for bits in range(1, max_bits + 1):
        factor = 2 ** bits # bin
        integer_temp = int(real_val * factor)
        trunc_val = integer_temp / factor
        error = abs(real_val - trunc_val)
        
        bits_axis.append(bits)
        errors.append(error)
        
    return bits_axis, errors


def plot(num, max_bits):
    bits_x, errors_y = estimate_error(num, max_bits)
    plt.figure(figsize=(10, 6))
    plt.semilogy(bits_x, errors_y, marker='o', linestyle='-', color='b')
    plt.title(f'Error de Representación de {num} según cantidad de Bits')
    plt.xlabel('Cantidad de Bits (Precisión)')
    plt.ylabel('Error Absoluto (Escala Log)')
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.show()
