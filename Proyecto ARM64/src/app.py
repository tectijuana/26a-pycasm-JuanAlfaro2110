# ╔══════════════════════════════════════════════════════════════╗
# ║                     Aplicacion de Python                     ║
# ║                             app.py                           ║
# ╠══════════════════════════════════════════════════════════════╣
# ║ Asignatura : Lenguajes de Interfaz                           ║
# ║ Autor(a)   : Alfaro Guerra Juan Jesus                        ║
# ║ Fecha      : 2026/04/16                                      ║
# ╠══════════════════════════════════════════════════════════════╣
# ║ Descripción:                                                 ║
# ║ Programa en Python que integra una función escrita en        ║
# ║ Assembly (ARM64) mediante ctypes para realizar operaciones   ║
# ║ aritméticas de alto rendimiento.                             ║
# ║                                                              ║
# ║ Se ejecuta una suma utilizando una librería compartida       ║
# ║ (libops.so) y se mide su rendimiento mediante un benchmark   ║
# ║ de múltiples iteraciones para evaluar la eficiencia del      ║
# ║ código en bajo nivel.                                        ║
# ╚══════════════════════════════════════════════════════════════╝

import ctypes
import time

lib = ctypes.CDLL("./build/libops.so")

lib.add.argtypes = [ctypes.c_long, ctypes.c_long]
lib.add.restype = ctypes.c_long

print("ASM ADD:", lib.add(10, 20))

# Benchmark
def bench():
    start = time.time()
    for _ in range(10_000_000):
        lib.add(1,2)
    end = time.time()
    print("ASM:", end - start)

bench()