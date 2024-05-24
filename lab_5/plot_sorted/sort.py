import random
def counting(element, left, right):
    comparison = 0
    moves = 0
    pivot = element[(right + left) // 2]
    i = left
    j = right
    while True:
        while element[i] < pivot:
            comparison += 1
            i += 1
        while element[j] > pivot:
            comparison += 1
            j -= 1
        if i >= j:
            return (comparison, moves, j)
        moves += 1
        element[i], element[j] = element[j], element[i]
def quick_sort(element, left, right):
    if left >= 0 and right >= 0 and left < right:
        (comparison, moves, p) = counting(element, left, right)
        (lcomparison, lmoves) = quick_sort(element, left, p)
        (rcomparison, rmoves) = quick_sort(element, p + 1, right)
        return(comparison + lcomparison + rcomparison, moves + lmoves + rmoves)
    return (0,0)
