# 손실함수 구하기, 미분 (교과서 129p 2번 해결)
import sympy as sp # 수식을 다루는 라이브러리 sympy
import numpy as np # 배열, 행렬 등을 다루는 라이브러리 numpy
import matplotlib.pyplot as plt # 그래프 그리는 라이브러리 pyplot


x = sp.Symbol("x") # 수식에서 쓸 변수 지정 
a = sp.Symbol("a")
p = sp.Symbol("p")

# 자료 입력
listx = [1.2, 0.5, 1.5, 1.3]
listy = [1.5, 0.7, 1.8, 1.5]

# 추세선 제시
fx = a*x

# 손실함수 초기화
La = 0

# 손실함수 구성
for i in range(4):
  La += ((listy[i]-a*listx[i])**2) /4

# 손실함수 전개 (보기 좋으라고 한건데, 안해도 미분, 해 구하는덴 지장없음)
sp.pprint(sp.expand(La))

# 손실함수 미분
sp.pprint(La.diff("a"))

# 손실함수 미분이 0이되는 a값 찾기(최적 추세선 찾기)
# fx = 0 인 x값 찾기 >> sp.solve(fx,x)

Op_a = sp.solve(La.diff("a"),a)
print(Op_a)


# 최적 추세선을 이용하여 값 예측
# fx에 k 대입 >> fx.subs(x, k)
Op_fx = fx.subs(a,Op_a[0])
print(Op_fx)
print(Op_fx.subs(x,1.8))

plt.plot(listx,listy,'ro') # 입력한 자료(listx, listy) 빨간 점으로 출력
plt.plot(listx,[Op_fx.subs(x,t) for t in listx]) # 찾은 추세선 그리기 (기본값이 파란색이라 그냥 그림)
plt.show() # 보여줘
