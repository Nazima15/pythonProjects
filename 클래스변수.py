class LoginResult:
    success = 0
    np_user=1
    wrong_password=2

    def __init__(self, r=0):
        self.result = r

r1=LoginResult(0)
r2=LoginResult(1)
r3=LoginResult(2)
print(LoginResult.success)  # 클래스명으로 접근 (추천)
