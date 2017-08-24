if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = tuple()
    for num in integer_list:
        t = t + (num,)
    
    print hash(t)