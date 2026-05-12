#ㅍ이썬은 변수를 찾을때 가까운 영역부터 찾음
#LEGB 규칙(Local -> Enslosing -> Global -> Built-in)
#Local -> 함수 내부 변수
#Enclosing -> 바깥 함수 변수
#Global -> 함수 밖 변수
#Built-in -> Python이 기본 제공하는 이름(print, input, len...)
#스코프(scope): 범위
a = '홍길동'
b = 99
#global(전역)

def function1(): #Enclosing(중첩)
    a = '이순신'
    c = [1 ,2 ,3]
    
    def function2(): #local(지역)
        d = (1, 2, 3)
        print('Local a =',a) # 이순신
        print('Local b =',b) # 99
        print('Local c =',c) # [1,2,3]
        print('Local d =',d) # (1,2,3)
        
    
    function2()
    print('Enclosing a =',a) # 이순신
    print('Enclosing b =',b) # 99
    print('Enclosing c =',c) # [1,2,3]
    #print('Enclosing d =',d) # error
function1()
print('Global a =',a) # 홍길동
print('Global b =',b) # 99
#print('Global c =',c) # error c는 function1 안에 있음
#print('Global d =',d) # error d는 function2() 안에 있음