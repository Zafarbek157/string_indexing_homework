def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=s//10000
    b=s//1000
    e=b%10 # 2-raqam
    d=s//100
    f=d%10 # 3-raqam
    m=a//10
    n=m%10 # 4-raqam
    l=s%10 # 5-raqam
    
    return a+e+f+n+l
print(main(12345))