#-*- coding: utf-8 -*-
import sys
print(sys.argv, len(sys.argv))

print(sys.platform)
print(sys.version)
print(sys.copyright)
print(sys.path)

#상위 디렉토리에 lib가 있을 경우 path를 추가해서 접근할 있게 한다.
#sys.path.append("절대경로 or os의 현재 위치를 가져오면 될꺼당아래 내용 참고")

#base camp 위치를 os별로 자동으로 가져오는 방법
#dir_name = os.path.dirname(__file__)
#a_path = os.path.abspath(dir_name)
#up_dir = os.path.join(a_path,"..")
#sys.path.append(os.path.abspath(up_dir))


print("__file__ ==> ", __file__)
print(dir(sys))
#ps1 .. run in console
#sys.ps1 = '$python> '



sa = sys.argv
if len(sa) < 2:
    sys.exit()

#with open(sa[1], "r", encoding="utf-8") as file: 
with open(sa[1], "r") as file:
    for line in file:
        print(line.strip().decode('utf-8').encode('euc-kr'))



