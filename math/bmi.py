class Solution:
    def solution(self, name, kg, cm, biman):
        title = " ### 비만도 계산 ### "
        aster = "*"*30
        schema = "이름 키(cm) 몸무게(kg) 비만도"
        values = f'{name} {cm} {kg} {biman}'
        return f"{aster} \n {title} \n {aster} \n {schema} \n {aster} \n {values} \n {aster}"

if __name__=="__main__":
    solution = Solution()
    name = input("이름: ")
    kg = input("몸무게: ")
    cm = input("키: ")
    bmi = float(kg)/(float(cm)**2/10000)
    if bmi >= 35:
        biman = "고도비만"
    elif 30 <= bmi <= 34.9:
        biman = "중(重)도 비만 (2단계 비만)"
    elif 25 <= bmi <= 29.9:
        biman = "경도 비만 (1단계 비만)"
    elif 23 <= bmi <= 24.9:
        biman = "과체중"
    elif 18.5 <= bmi <= 22.9:
        biman = "정상"
    else:
        biman = "저체중"
    print(solution.solution(name, kg, cm, biman))


