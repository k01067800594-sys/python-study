try: # 수행문장안에 예외발생하면
    num=int(input("숫자입력"))
    res=10/num
except ValueError: #excet:예외발생시 처리(값 오류)
    print("입력오류 숫자 아님")
except ZeroDivisionError: #0으로 나눌 수 없음
    print("0으로 나눌 수 없음")
except Exception as e: #그외 나머지 예외인 경우->e 예외 저장
    print("error",e)
else: # 정상적인 경우
    print(f"결과 {res}")
finally: #공통적 수행(무조건 수행)
    print("종료")