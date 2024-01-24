class Trapezoid:

    def __init__(self):
        self.n = int(input("Enter number of divisions: "))
        self.a = float(input("Enter starting a value on Ox: "))
        self.b = float(input("Enter ending b value Ox: "))
        self.fun = input("Enter the function (e.g., x**2, sin(x), etc.): ")

    def decode(self, fun):
        try:
            func = lambda x: eval(fun)
            return func
        except Exception as e:
            print(f"Error decoding function: {e}")
            return None

    def calculation(self):
        x = (self.b - self.a) / self.n
        func = self.decode(self.fun)

        if func is None:
            return None
        
        suma = 0

        for i in range(self.n + 1):
            xi = self.a + i * x
            if i == 0 or i == self.n:
                suma += func(xi)
            else:
                suma += 2 * func(xi)

        result = x * suma / 2
        return result

trapezoid_instance = Trapezoid()
result = trapezoid_instance.calculation()

if result is not None:
    print("The approximate definite integral is:", result)
