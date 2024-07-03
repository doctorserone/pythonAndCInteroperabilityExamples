from distutils.core import setup, Extension

def main():
    setup(name="fibonacciExtension",
          version="0.1.0",
          description="Python extension for fibonacci",
          author="Andrés Álvarez Iglesias",
          author_email="andres.alvarez.iglesias@gmail.com",
          ext_modules=[Extension("fibonacciExtension", ["fibonacci.c"])])

if __name__ == "__main__":
    main()