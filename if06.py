def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    p=0
    t=n%10
    if t<n//10000:
        t=n//10000
        p=5
    if t<n//1000%10:
        t=n//1000%10
        p=4
    if t<n//100%10:
        t=n//100%10
        p=3
    if t<n//10%10:
        t=n//10%10
        p=2
    if t==n%10:
        p=1
    return p
print(main(59762))
