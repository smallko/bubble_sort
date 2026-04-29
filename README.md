# Bubble Sort

一個簡單的泡沫排序（Bubble Sort）演算法實現。

## 演算法說明

Bubble Sort 是一種簡單的排序演算法，通過重複比較相鄰元素並交換位置來完成排序。

## 時間複雜度

- 最差：O(n²)
- 平均：O(n²)
- 最佳：O(n)

## 空間複雜度

O(1)

## 使用方法

```python
from bubble_sort import bubble_sort

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 34, 64, 90]
```

## 執行

```bash
python bubble_sort/bubble_sort.py
```