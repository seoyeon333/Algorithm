# BAEKJOON : A-B (1001번)

# 문제 : 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력 : 첫째 줄에 A-B를 출력한다.

A, B = input('숫자를 입력해주세요 : ').split()
print(int(A)-int(B))

# 백준은 '숫자를 입력해주세요 : ' 부분을 빼고 제출해야 정답으로 처리가 된다.
