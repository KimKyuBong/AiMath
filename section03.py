# 리스트 만들기 
# 리스트는 순서가 있어서 중복 가능 -> 벡터
# 형태는 "[]" 로 감싸지고, 원소별로 ","로 구분한다
listA = ["한파", "눈", "예보", "일부", "비", "예보"]
listB = ["눈", "예보", "퇴근길", "눈", "조심"]
listC = ["비", "예보", "일부", "눈", "비", "비", "그치다", "한파"]
listU = ["한파", "눈", "예보", "일부", "비", "퇴근길", "조심", "그치다"]

# 집합 만들기
# 집합은 순서 개념이 없어서 중복 불가능
# 형태는 "{}"로 감싸지고, 원소별로 ","로 구분한다
A = set(listA)
B = set(listB)
C = set(listC)


# 둘 차이를 비교해보세요
print(listA)
print(A)
