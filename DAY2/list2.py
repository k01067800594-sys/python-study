movie_list=["아바타","왕사남","살목지","극한직업"]
print(movie_list)

movie_list.insert(1,"범죄도시") #삽입
print(movie_list)

movie_list.append("슈퍼맨") #추가
print(movie_list)

movie_list.remove("살목지") #값을 지정하여 삭제
print(movie_list)

#del : 명령어
del movie_list[2]
print(movie_list) #요소 위치 지정 삭제

x=10
print(x)
del x
#print(x)

print(len(movie_list)) #len : 길이

a=[1,2,3]
print(sum(a))

# 90, 50, 80, 70, 55
a=[90, 50, 80, 70, 55]
avg=sum(a)/len(a)
print(avg)

#tuple : 나열, 리스트와 유사하지만 변경 불가
tuple=(1,2,3,4)
print(tuple)
print(tuple[2])
# tuple[2]=50 #값 변경 안됨
# print(tuple)

six_tuple=(1,2,3,4,5,6)
print(six_tuple)