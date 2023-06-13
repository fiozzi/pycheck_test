def division(a: int, b: int) -> float:
    if b == 0:
        return None
    return float(a/b)

if __name__ == '__main__':
    print(division(3,5))
    print(division(15,5))
    print(division(15,0))
    
