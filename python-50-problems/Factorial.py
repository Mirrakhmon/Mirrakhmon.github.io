from datetime import datetime


class Factorial:
    """Compute n! with input validation.

    n must be a non-negative integer; anything else is rejected
    at assignment time (TypeError / ValueError).
    """

    def __init__(self, n):
        self.n = n  # routed through the setter: even the first value gets validated

    @property
    def n(self):
        """Getter: return current n."""
        return self._n

    @n.setter
    def n(self, value):
        """Setter: validate type and sign, store in self._n."""
        if not isinstance(value, int):
            raise TypeError("n must be int")
        if value >= 0:
            self._n = value  # _n, not n: otherwise the setter calls itself (recursion)
        else:
            raise ValueError("n cannot be negative")

    def __str__(self):
        return f"{self.n}! = {self.compute()}"

    def compute(self):
        """Compute n! with a loop. Returns int."""
        n = self.n
        m = 1  # product starts at 1, not 0
        for i in range(1, n + 1):
            m *= i
        return m


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")

print(Factorial(5))     # 5! = 120
print(Factorial(1))     # 1! = 1
print(Factorial(0))     # 0! = 1  (edge case: range gives 0 iterations, m stays 1)
print(Factorial(10))    # 10! = 3628800

try:
    print(Factorial(-3))
except ValueError as e:
    print(f"Caught: {e}")

# mutation test: the setter must also work on a live object
f = Factorial(5)
print(f)                # 5! = 120
f.n = 10
print(f)                # 10! = 3628800