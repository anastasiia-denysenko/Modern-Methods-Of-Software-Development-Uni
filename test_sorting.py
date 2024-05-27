from plot_line import counting, quick_sort
import pytest
def test_sort():
    a = random.sample(range(-1000, 1000), 10)
    n = a.copy()
    a.sort()
    quick_sort(n, 0, len(n)-1)
    assert a==n
