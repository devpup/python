#-*- coding: utf-8 -*-
s = "123"

try:
    print(int(s) + 1)
    print(int(s) / 1)

except ValueError as ve:
    print("ValueError occurs!!!", ve)

except ZeroDivisionError as e:
    print("ValueError occurs!!!", e)

except :
    print("Error occurs!!!")

else:
    print("elseeeeeeeeeeeeeee")

finally:
    print("ABCDEFG")

# try:
#     # 예외 발생 가능 코드들
# except:
#     # 예외시 처리될 구문
# except:
#     pass    #씹겠다?!
# else:
#     #예외가 없을 경우 실행되는 부분

# finally:
#     #예외가 있던 없던 실행되는 부분