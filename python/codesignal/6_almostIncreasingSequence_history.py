

# 되는 케이스 예

# sequence = [1, 3, 2]
# sequence = [10, 1, 2, 3, 4, 5]
# sequence = [0, -2, 5, 6]
# sequence = [1, 1]
# sequence = [1, 2, 5, 3, 5]
# sequence = [1, 2, 3, 4, 3, 6]
sequence = [1, 2, 3, 4, 99, 5, 6]
# sequence = [123, -17, -5, 1, 2, 3, 12, 43, 45]
# sequence = [3, 5, 67, 98, 3]


# 안되는 케이스 예

# sequence = [1, 2, 1, 2]
# sequence = [1, 2, 3, 4, 5, 3, 5, 6]
# sequence = [40, 50, 60, 10, 20, 30]


# # 1) 맥스값 이후의 변수의 개수가 1이 아니면 False -> 너무 일부분만 고려.
# def almostIncreasingSequence(sequence):
#     for i in range(len(sequence)):
#         i = sequence.index(max(sequence))
#         if len(sequence) - i - 1 == 1:
#             return True
#         else:
#             return False


# # 2) 최대값 제거 후 순차적으로 증가하는지 확인 -> 최대값제거라는 설정이 모순
# def almostIncreasingSequence(sequence):
#
#     i = sequence.index(max(sequence))
#     del sequence[i]
#     temp = 0
#     for n in range(len(sequence)):
#         if n == 0:
#             temp = sequence[0]
#         elif temp >= sequence[n]:
#             return False
#         else:
#             temp = sequence[n]
#     return True


# # 3) Brute force - submit 32/34 (time exceed)

# def almostIncreasingSequence(sequence):
#     num = 0
#     temp = 0
#     for i in range(len(sequence)):
#         print(f'{i}번째 지웁니다.')
#         temp = sequence[i]
#         del sequence[i]
#         print(sequence)
#         if len(sequence) == 1:
#             return True
#         for n in range(len(sequence)):
#             if n == 0:
#                 num = sequence[0]
#             elif len(sequence) == 1:
#                 return True
#             elif num >= sequence[n]:
#                 print('False:break문 호출')
#                 break
#             elif n == len(sequence) - 1:
#                 print('true입니다.')
#                 return True
#             else:
#                 num = sequence[n]
#         print(f'{i}번째 안됨')
#         sequence.insert(i, temp)
#     print('검문소설치')
#     return False


# 4) 누나 방법 - tests 14/17
# [1, 2, 1, 2]
# [1, 2, 3, 4, 5, 3, 5, 6]
# [40, 50, 60, 10, 20, 30]
# 이렇게 같은 수 사이에 작은 수가 들어가 있는 경우 캐치 못함.

# def almostIncreasingSequence(sequence):
#
#     n = 0
#     for i in range(len(sequence)-1):
#         if sequence[i] > sequence[i+1]:
#             n -= 1
#         elif sequence[i] == sequence[i+1]:
#             n -= 1
#     if n > -2:
#         return True
#     else:
#         return False


# 5) 내 방법 + 누나방법 | Brute force(2) - submit 32/34 (time exceed)
#
# def almostIncreasingSequence(sequence):
#
#     num = 0
#     temp = 0
#     if len(sequence) < 3:
#         return True
#     for i in range(len(sequence)):
#         temp = sequence[i]
#         del sequence[i]
#
#         print(sequence,'로 시작합니다.')
#         for n in range(len(sequence)-1):
#             if sequence[n] >= sequence[n+1]:
#                 print(f'n {n}번째 실패:탈출')
#                 break
#             elif n == len(sequence)-2:
#                 print('성공')
#                 return True
#             print(f'n {n}번째 실패:탈출')
#         print(f'i {i}번째 실패:탈출\n')
#         sequence.insert(i, temp)
#     print('최종실패')
#     return False


# 6) 안되는 케이스가 아니라 되는 케이스를 잘 봤을 때 생각난 아이디어
# Tests 16/17 : [1, 2, 3, 4, 3, 6]


# def almostIncreasingSequence(sequence):
#
#     # if len(sequence) < 3:
#     #     return True
#
#     imax = sequence.index(max(sequence))
#     imin = 0
#
#     # 0. (최솟값이 2개일 때) 뒤에것으로
#     for i in range(len(sequence)):
#         j = len(sequence) - 1 - i
#         m = min(sequence)
#         if sequence[j] == m:
#             imin = j
#             break  # break이 없으면 덮어씌어진다.
#
#     # print(f'max: {imax+1}번째')
#     # print(f'min: {imin+1}번째')
#
#     # 1. (앞의)최대값 제거
#
#     temp = sequence[imax]
#     del sequence[imax]
#     print(sequence)
#     for i in range(len(sequence) - 1):
#         if sequence[i] >= sequence[i + 1]:
#             break
#         if i == len(sequence) - 2:
#             return True
#     # 최대값 다시 원상복귀
#     sequence.insert(imax, temp)
#
#     # 2. (뒤의)최소값 제거
#     del sequence[imin]
#     print(sequence)
#     for i in range(len(sequence) - 1):
#         if sequence[i] >= sequence[i + 1]:
#             break
#         if i == len(sequence) - 2:
#             return True
#     return False
#
#
#     # 3. (뒤의) 동일한 값 제거
#
#     # del sequence[same]


# 9) sort 꼼수 | submit 31/34 (time exceed)

# def almostIncreasingSequence(sequence):
#     if len(sequence) < 3:
#         return True
#     num = 0
#     temp = 0
#     for i in range(len(sequence)):
#         print(f'{i}번째 지웁니다.')
#         temp = sequence[i]
#         del sequence[i]
#         print(sequence)
#
#         sequence_sorted = sorted(sequence)
#         print(sequence_sorted)
#
#         # 1. 중복요소 비교
#         if len(sequence) != len(set(sequence)):
#             sequence.insert(i, temp)    # 이것빠지면 중복요소있을 때 하나 못채워줌.
#             continue
#
#         # 2. 같은함수인지 비교
#         for j in range(len(sequence)):
#             if sequence_sorted[j] != sequence[j]:
#                 continue
#             if j == len(sequence)-1:
#                 print(f'{i}번째 성공')
#                 return True
#         sequence.insert(i, temp)
#     return False


# 10. sorted + len/set 비교 | submit 31/34 (time exceed)


# def almostIncreasingSequence(sequence):
#
#     if len(sequence) < 3:
#         return True
#     temp = 0
#     for i in range(len(sequence)):
#         # print(f'{i}번째 지웁니다.')
#         temp = sequence[i]
#         del sequence[i]
#         # print(sequence)
#
#         sequence_sorted = sorted(sequence)
#         # print(sequence_sorted)
#
#         # 1. 중복요소 비교
#         if len(sequence) != len(set(sequence)):
#             sequence.insert(i, temp)  # 이것빠지면 중복요소있을 때 하나 못채워줌.
#             continue
#
#         # 2. 같은함수인지 비교
#         for j in range(len(sequence)):
#             if sequence_sorted[j] != sequence[j]:
#                 continue
#             if j == len(sequence) - 1:
#                 # print(f'{i}번째 성공')
#                 return True
#         sequence.insert(i, temp)
#     return False


def almostIncreasingSequence(sequence):
    s = sequence
    s2 = s[:]
    deleted = 0
    if (len(s) - len(set(s))) > 1:
        return False
    elif len(set(s)) == 1:
        return True

    for i in range(len(s) - 1):
        if s2[i] < s2[i + 1]:
            continue
        else:
            del s[i:i + 2]
            deleted += 1

    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False

    if deleted > 1:
        return False
    else:
        return True


# def almostIncreasingSequence(sequence, found=?????):
#     # print(sequence)
#     local_max = -100000
#     ??? i, num in enumerate(????????):
#     if num <= local_max:
#         if ?????:
#             return False
#         else:
#             if ? == 1:
#                 return almostIncreasingSequence(sequence[?:], True)
#                 elif i == len(????????)-1:
#                 return True
#             else:
#                 ?????? almostIncreasingSequence(sequence[:i - 1] +????????[
#                     i:], True) or almostIncreasingSequence(????????[: i]+sequence[i + 1:], ????)
#             else:
#             local_max = num
#
#     return ????

print(almostIncreasingSequence(sequence))
