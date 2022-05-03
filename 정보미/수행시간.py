import time, random

def evaluate_n2(A, x):
   # code for O(n^2)-time function
   start = time.process_time()
   sum=0
   cal=0
   for i in range(0,n):
      multiple=1
      cal=A[i]
      for j in range(0,i):
         multiple=multiple*x
      sum+=cal*multiple
   end = time.process_time()
   return end-start
   
def evaluate_n(A, x):
    #code for O(n)-time function
   start = time.process_time()
   sum=0
   for i in range(0,n):
      sum+=A[i]*(x**i)
   end = time.process_time()
   return end-start
   
x=int(input('x값을 입력하시오: '))
random.seed()
# random 함수 초기화
# n 입력받음
n = int(input('n값을 입력하시오: '))
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A=[]
for i in range(0,n):
   a=random.randint(-1000,1000)
   A.append(a)
# evaluate_n2 호출
a=evaluate_n2(A, x)
# evaluate_n 호출
b=evaluate_n(A, x)
# 두 함수의 수행시간 출력
print(a,b)
