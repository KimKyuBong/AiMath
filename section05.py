# 문장의 벡터화(임베딩), 자카드유사도, 유클리드유사도, 코사인유사도
import numpy as np
T1 = '사회 고도화 아직도~~~'.split(' ')
T2 = '놀라운 속도~~~'.split(' ')
T3 = '사회 발전 ~~~~'.split(' ')
T4 = '빠른 속도 사회 발전~~~~'.split(' ')

U = set(T1) | set(T2) | set(T3) | set(T4) # 단어사전 만들기
U = list(U) # 단어사전의 단어에 순서 부여

print(U)

print(len(set(T1)))



def M_Vec(M, X): # M을 바탕으로 X를 벡터화 하는 함수
    veclist = []
    for i in range(len(M)):
     # 1부터 listM의 원소 개수까지 i에 대입하며 아래 내용을 반복한다.
        veclist.append(X.count(M[i])) 
        # listM의 i번째 원소가 포함된 개수를 세서 i번째 원소로 넣는다.
    return(np.array(veclist))

print(M_Vec(U, T1))
print(M_Vec(U, T2))
print(M_Vec(U, T3))
print(M_Vec(U, T4))


def J(X, Y): # 자카드 유사도
    X, Y = set(X), set(Y)
    return(len(X&Y)/len(X|Y))


def L(A, B): # 유클리디안 유사도 정의
    return(np.linalg.norm(B-A))
    #　벡터a와 벡터b 의 거리를 반환한다.

def C(a,b): # 코사인 유사도 기능 정의
    return(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))) 
    # a와 b의 내적을 a의 크기와 b의 크기의 곱으로 나눈다


import numpy as np
def J(X, Y): # 자카드 유사도
    X, Y = set(X), set(Y)
    return(len(X&Y)/len(X|Y))


def L(A, B): # 유클리디안 유사도 정의
    return(np.linalg.norm(B-A))
    #　벡터a와 벡터b 의 거리를 반환한다.

def C(a,b): # 코사인 유사도 기능 정의
    return(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))) 
    # a와 b의 내적을 a의 크기와 b의 크기의 곱으로 나눈다


VA = np.array([1,0,0,1,0,0,0,0,1,1,0,1])
VB = np.array([1,0,1,0,1,1,1,1,0,1,1,0])
VC = np.array([1,0,0,0,1,0,0,0,1,1,1,1])
VD = np.array([1,0,1,0,1,0,1,1,0,1,1,1])


print(L(VA,VC))
print(L(VA,VD))
print(L(VB,VC))
print(L(VB,VD))


print(C(VA,VC))
print(C(VA,VD))
print(C(VB,VC))
print(C(VB,VD))
