def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    t=a
    if t<b:
        t=b
    if t<c:
        t=c
    return t
print(main(1,4,2))
