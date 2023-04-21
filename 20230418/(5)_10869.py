# BAEKJOON : 사칙연산 (10869번)

# 문제 : 두 자연수 A와 B가 주어진다.
# 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

# 출력 : 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

A, B = input('숫자를 입력해주세요 : ').split()

A = int(A)
B = int(B)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A % B)

# 백준은 '숫자를 입력해주세요 : ' 부분을 빼고 제출해야 정답으로 처리가 된다.
