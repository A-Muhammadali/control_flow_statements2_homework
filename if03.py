def main(a,b,c):
    """
    Determine the number between large and small.
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
    p=a
    if p>b:
        p=b
    if p>c:
        p=c
    return a*b*c//p//t
print(main(1,4,2))

    
