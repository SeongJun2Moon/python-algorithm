def solution():
    money = 2160
    unit = [500, 100, 50, 10]
    for i in unit:
        count = money // i
        money = money % i
        print(f"{i}원 {count}개")
        

if __name__=="__main__":
    solution()