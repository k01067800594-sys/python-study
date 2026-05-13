import random
def get_lotto():
    numbers=[] #비어있는 리스트
    while len(numbers)<6: #numbers=>6자리까지 반복
        n=random.randint(1,45) #무작위 수 발생 (1~45)사이
        if n not in numbers: # 포함하지 않냐
            # 중복 방지
            numbers.append(n) # c추가
    return numbers # 6개의 숫자가 있는 리스트
    
print(f"로또번호는 {get_lotto()}입니다")
# get_lotto 함수 호출->