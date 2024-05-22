###<h1>Static Constructor</h1>

```
class MathUtils:

  @staticmethod
  def add(x, y):
    """
    Adds two numbers.

    Args:
      x: The first number.
      y: The second number.

    Returns:
      The sum of x and y.
    """
    return x + y

# Call the static method directly on the class
result = MathUtils.add(5, 3)
print(result)  # Output: 8

alternative_result = MathUtils.add(10, 2)
print(alternative_result)  # Output: 12

```


Creating a static method is not recommended, but possible (avoids using the class name).Although it reduces readability and makes the code less clear about the origin of the method.

This example defines a class MathUtils with a static method add that takes two numbers and returns their sum. The @staticmethod decorator indicates that this method is static.

The add method doesn't receive an implicit first argument like self (for instance methods) or cls (for class methods). It cannot access or modify the state of the class or its objects. We call the static method directly using the class name MathUtils.add. While possible, it's generally less readable to avoid using the class name for static methods.