import math
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    
    return (bool(int(math.sqrt(a))))
x=main(a=121)
print(x)