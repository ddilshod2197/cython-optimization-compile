# cython: boundscheck=False, wraparound=False, nonecheck=False

import cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
def fibonacci(int n):
    cdef int a = 0
    cdef int b = 1
    cdef int result = 0
    cdef int i = 0

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        while i < n - 1:
            result = a + b
            a = b
            b = result
            i += 1
        return result

def main():
    n = 30
    print(f"Fibonacci({n}) = {fibonacci(n)}")

if __name__ == "__main__":
    main()
```

```bash
# Cythonni qo'llab-quvvatlash uchun kerakli kutubxonalarni o'rnatish
pip install cython

# Cythonni qo'llab-quvvatlash uchun kerakli kutubxonalarni o'rnatish
python -m cythonize fibonacci.pyx
# Cythonni qo'llab-quvvatlash uchun kerakli kutubxonalarni o'rnatish
gcc -shared -o fibonacci.so fibonacci.c -I/usr/include/python3.x
# Cythonni qo'llab-quvvatlash uchun kerakli kutubxonalarni o'rnatish
python fibonacci.py
