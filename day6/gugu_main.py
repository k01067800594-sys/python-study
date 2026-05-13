from gugu_modul import *

while True:
    print("\n====구구단====")
    print("1.세로 구구단")
    print("2.가로 구구단")
    print("0.종료")

    choice=int(input("선택:"))

    if choice == 1:
        v_gugudan()

    elif choice == 2:
        h_gugudan()

    elif choice == 0:
        print("종료")
        break

    else:
        print("입력 오류")