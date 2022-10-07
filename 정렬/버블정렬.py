import random

class Solution:
    def solution(self):
        keys = ["1st","2st","3st","4st","5st"]
        dc = {}
        print('### 랜덤숫자 ###')
        print("*"*30)
        for i in keys:
            randnumber = random.randint(1, 11)
            dc[i] = randnumber
        for k,v in dc.items():
            print(f"랜덤숫자{k}: {v}")
        print("*"*30)

if __name__=="__main__":
    solution = Solution()
    solution.solution()