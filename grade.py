class Solution:
    def solution(self,lan,eng,math):
        title = "===성적표==="
        total = lan + eng + math
        avg = total/3
        grade = ""
        if avg >= 90:
            grade = "A"
        elif 80 <= avg < 90:
            grade = "B"
        elif 70 <= avg < 80:
            grade = "C"
        elif 60 <= avg < 70:
            grade = "D"
        elif 50 <= avg < 60:
            grade = "D"
        else:
            grade = "F"
        return f"{title} \n 총점: {total:.1f} 평균: {avg:.1f} 학점: {grade}"

if __name__=="__main__":
    solution = Solution()
    lan = float(input("국어: "))
    eng = float(input("영어: "))
    math = float(input("수학: "))
    print(solution.solution(lan,eng,math))