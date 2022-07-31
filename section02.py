import numpy as np # numpy 라이브러리를 사용할껀데, np라고 부를께

# A, B행렬 선언 
A = np.matrix([[-1, 1, 2],[-1,1,3],[-1,1,0]])
B = np.matrix([[2, 4, 1],[1,2,1],[5,2,-2]])

# 행렬의 실수배
print(3*A)

# 행렬의 합
print(A+B)

# 행렬의 곱
print(A*B)

