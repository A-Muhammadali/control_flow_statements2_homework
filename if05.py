def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    t=n%10
    if t<n//10000:
        t=n//10000
    if t<n//1000%10:
        t=n//1000%10
    if t<n//100%10:
        t=n//100%10
    if t<n//10%10:
        t=n//10%10
    return t
print(main(59762))
