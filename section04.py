# 집합 만들기
# set(리스트) 형식으로 만들 수 있다.
# 이때 "원소1 원소2 원소3 ... 원소n".split(' ') 이라고 쓰면, 
# ' '(띄어쓰기) 를 기준으로 리스트가 만들어져서 사용하기 편리하다.

P = set("쥐 호랑이 용".split(" ")) # 
Q = set("소 호랑이 용".split(" ")) # 
R = set("쥐 소 호랑이 뱀".split(" ")) # 


print(P) # 
print(Q) # 
print(R) # 


print(len(P | Q)) # P 합집합 Q 의 갯수
print(len(P & Q)) # P 교집합 Q 의 갯수

print(len(P & Q)/len(P | Q)) # P, Q의 자카드 유사도
print(len(P & R)/len(P | R)) # P, R의 자카드 유사도
print(len(R & Q)/len(R | Q)) # R, Q의 자카드 유사도
