#  * 금액을 입력받은 후 우리나라 화폐종류별로 해당 갯수를 표기하는 프로그램
#     * [요구사항] 금융업을 하는 고객사로부터 프로그램 개발요청이 들어왔습니다.
#     * 금액을 입력받은 후 우리나라 화폐종류별로 해당 갯수를 표기하는 프로그램입니다.
#     * 예를들어, 125,520 원을 입력하면 화면에 이렇게 보이게 하면 됩니다.
#     * 표시하고 10원미만은 절삭
#       ******************************************************
#          요청금액 : 126520 원
#          5만원 : 2매
#          1만원 : 2매
#          5천원 : 1매
#          1천원 : 1매
#          5백원 : 1개
#          백원 : 0개
#          오십원 : 0개
#          십원 : 2개
#       ********************************************************

class Solution:
    def solution(self, money):
        title = " ### 화폐교환 ### "
        aster = "*"*30
        change_5man = int(money / 50000)
        change_1man = int(money % 50000 / 10000)
        change_5cheon = int(money % 50000 % 10000 / 5000)
        change_1cheon = int(money % 50000 % 10000 % 5000 / 1000)
        change_5back = int(money % 50000 % 10000 % 5000 % 1000 / 500)
        change_1back = int(money % 50000 % 10000 % 5000 % 1000 % 500 / 100)
        change_5ship = int(money % 50000 % 10000 % 5000 % 1000 % 500 % 100 / 50)
        change_1ship = int(money % 50000 % 10000 % 5000 % 1000 % 500 % 100 % 50 / 10)
        answer = f"요청금액: {money}원"
        result = (
            f"{title} \n{aster}\n {answer} \n{aster} \n"
            f"5만원: {change_5man}매 \n"
            f"1만원: {change_1man}매 \n"
            f"5천원: {change_5cheon}매 \n"
            f"1천원: {change_1cheon}매 \n"
            f"5백원: {change_5back}매 \n"
            f"1백원: {change_1back}매 \n"
            f"5십원: {change_5ship}매 \n"
            f"1십원: {change_1ship}매 \n"
        )
        return result

if __name__=="__main__":
    solution = Solution()
    money = int(input("돈: "))
    print()
    print(solution.solution(money))