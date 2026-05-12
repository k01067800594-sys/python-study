def dis_price(price, discount_rate): #함수명(가격, 할인율)
    discount_price=price*discount_rate/100 # 할인금액을 먼저 구함
    final_price=price-discount_price  # 가격-할인금액->진짜 금액
    return final_price  # 최종 금액 반환





# a상품: 10000원  할인율: 10
price_a=dis_price(10000,10) #dis_price 함수명
print(f"a상품은 {int(price_a)}원입니다") #할인금액을 뺀 금액 출력

# b상품: 50000원  할인율: 20
price_b=dis_price(50000,20) #dis_price 함수명
print(f"b상품은 {int(price_b)}원입니다") #할인금액을 뺀 금액 출력
