class Solution:
    def solution(self,a,b,c):
        if b == "+":
            answer = a + c
        elif b == "-":
            answer = a - c
        elif b == "*":
            answer = a * c
        elif b == "/":
            answer = a / c
        elif b == "%":
            answer = a % c
        else:
            answer = "그런거 없음"
        return answer

if __name__=="__main__":
    solution = Solution()
    a = int(input("첫 수: "))
    b = input("+, -, *, /, % : ")
    c = int(input("둘 수: "))
    print(solution.solution(a,b,c))
    