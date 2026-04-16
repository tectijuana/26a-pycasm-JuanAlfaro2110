/*
╔══════════════════════════════════════════════════════════════╗
║                        Aplicacion de C                       ║
║                           bridge.c                           ║
╠══════════════════════════════════════════════════════════════╣
║ Asignatura : Lenguajes de Interfaz                           ║
║ Autor(a)   : Alfaro Guerra Juan Jesus                        ║
║ Fecha      : 2026/04/16                                      ║
╠══════════════════════════════════════════════════════════════╣
║ Descripción:                                                 ║
║ Módulo en lenguaje C que funciona como puente (wrapper)      ║
║ entre funciones implementadas en Assembly (ARM64) y          ║
║ aplicaciones de alto nivel (como Python mediante ctypes).    ║
║                                                              ║
║ Este archivo declara las funciones externas definidas en     ║
║ Assembly y expone una API en C que facilita su integración   ║
║ y uso desde otros lenguajes.                                 ║
╚══════════════════════════════════════════════════════════════╝

*/
// Wrapper C

#include <stdint.h>

// Declaraciones ASM
long add_asm(long a, long b);
long sub_asm(long a, long b);
long mul_asm(long a, long b);
long max_asm(long a, long b);
long min_asm(long a, long b);
long sum_array_asm(long* arr, long n);
long count_even_asm(long* arr, long n);
long dot_product_asm(long* a, long* b, long n);

// Exportar API
long add(long a, long b) { return add_asm(a,b); }
long sub(long a, long b) { return sub_asm(a,b); }
long mul(long a, long b) { return mul_asm(a,b); }
long max(long a, long b) { return max_asm(a,b); }
long min(long a, long b) { return min_asm(a,b); }

long sum_array(long* arr, long n){
    return sum_array_asm(arr,n);
}

long count_even(long* arr, long n){
    return count_even_asm(arr,n);
}

long dot_product(long* a, long* b, long n){
    return dot_product_asm(a,b,n);
}