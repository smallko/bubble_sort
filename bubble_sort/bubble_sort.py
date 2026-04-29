"""
Bubble Sort Algorithm

Bubble Sort 是一種簡單的排序演算法,通過重複比較相鄰元素並交換位置来排序。
時間複雜度: O(n^2)
空間複雜度: O(1)
"""


def bubble_sort(arr):
    """
    對陣列進行泡沫排序（由小到大）
    
    Args:
        arr: 要排序的列表
    
    Returns:
        排序後的列表
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = bubble_sort(numbers.copy())
    print("Original:", numbers)
    print("Sorted:", sorted_numbers)