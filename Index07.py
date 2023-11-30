def main():
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a="good"
    n=4
    if len(a)<=n:
        return False
    if len(a)>=n:
        return a[n]
print(main())
