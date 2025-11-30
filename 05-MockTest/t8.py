def f(speed1,speed2):
    x = speed2 * 3600 / 1000
    x = int(x)
    if speed1 ==  x:
        return True
    else:
        return False

if __name__  == "__main__":
    print(f(36,10))
    print(f(20,20))