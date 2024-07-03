# Fibonacci as Python extension

Use a virtual environment for all operations

```
python3 -m venv .venv
source .venv/bin/activate
```

Compile the C library with:

```
python -m pip install build
python -m build
```

Install the library:

```
pip3 install dist/fibonacciExtension-0.1.0-cp312-cp312-linux_x86_64.whl 
```
