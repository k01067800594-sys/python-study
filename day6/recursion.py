#재귀 호출(함수)(함수 내부에서 자기자신을 호출)
#5!(팩토리얼):1*2*3*4*5
# def fact(n): #fact:함수명(매개변수는 1개)
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1) 


# a=int(input("정수 입력:")) #예) 5입력
# res=fact(a) #함수 호출, 인수 a(정수) 보냄
# # 반환되어서 온 결과값을 res 저장
# print(a,"!는",res,"이다")

# 순환(재귀)함수를 활용하여 1부터 입력받은 숫자까지 합을 구하는 프로그램을 작성하시오
# 입력받은 수가 8
# 8+7+6+5+4+3+2+1=합계
# 출력 1~8(입력받은 숫자)까지의 합
def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1)

sum=int(input("정수 입력:"))
res=add(sum)
print(f"1부터 {sum}까지의 합은 {int(res)}")