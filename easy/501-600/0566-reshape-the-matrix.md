# 0566. Reshape the Matrix

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int m = mat.size();
        if (m == 0) return mat;
        int n = mat[0].size();
        if (m * n != r * c) return mat;
        vector<vector<int>> res(r, vector<int>(c));
        for (int i = 0; i < m * n; ++i) {
            int val = mat[i / n][i % n];
            res[i / c][i % c] = val;
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length;
        int n = mat[0].length;
        if (m * n != r * c) {
            return mat;
        }
        int[][] reshaped = new int[r][c];
        for (int i = 0; i < m * n; i++) {
            reshaped[i / c][i % c] = mat[i / n][i % n];
        }
        return reshaped;
    }
}
```

## Python

```python
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0]) if m else 0
        total = m * n
        if total != r * c:
            return mat
        flat = [num for row in mat for num in row]
        res = []
        for i in range(r):
            start = i * c
            res.append(flat[start:start + c])
        return res
```

## Python3

```python
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        flat = [mat[i][j] for i in range(m) for j in range(n)]
        return [flat[i*c:(i+1)*c] for i in range(r)]
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int*** returnColumnSizes) {
    // Adjust signature to match expected LeetCode parameters
    // However, the provided signature uses int** returnColumnSizes; we need to follow that.
    // We'll cast appropriately inside the function.
    (void)returnColumnSizes; // suppress unused warning if not used directly
    int n = matColSize[0];
    int total = matSize * n;
    
    if (total != r * c) {
        *returnSize = matSize;
        *returnColumnSizes = (int*)malloc(matSize * sizeof(int));
        for (int i = 0; i < matSize; ++i) {
            (*returnColumnSizes)[i] = n;
        }
        return mat;
    }
    
    int** res = (int**)malloc(r * sizeof(int*));
    for (int i = 0; i < r; ++i) {
        res[i] = (int*)malloc(c * sizeof(int));
    }
    
    *returnSize = r;
    *returnColumnSizes = (int*)malloc(r * sizeof(int));
    for (int i = 0; i < r; ++i) {
        (*returnColumnSizes)[i] = c;
    }
    
    for (int k = 0; k < total; ++k) {
        int origRow = k / n;
        int origCol = k % n;
        int newRow = k / c;
        int newCol = k % c;
        res[newRow][newCol] = mat[origRow][origCol];
    }
    
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] MatrixReshape(int[][] mat, int r, int c) {
        int m = mat.Length;
        int n = mat[0].Length;
        if (m * n != r * c) return mat;

        int[][] reshaped = new int[r][];
        for (int i = 0; i < r; i++) {
            reshaped[i] = new int[c];
        }

        for (int idx = 0; idx < m * n; idx++) {
            int origRow = idx / n;
            int origCol = idx % n;
            int newRow = idx / c;
            int newCol = idx % c;
            reshaped[newRow][newCol] = mat[origRow][origCol];
        }

        return reshaped;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(mat, r, c) {
    const m = mat.length;
    const n = mat[0].length;
    if (m * n !== r * c) return mat;

    const res = Array.from({ length: r }, () => new Array(c));
    for (let i = 0; i < m * n; ++i) {
        const val = mat[Math.floor(i / n)][i % n];
        res[Math.floor(i / c)][i % c] = val;
    }
    return res;
};
```

## Typescript

```typescript
function matrixReshape(mat: number[][], r: number, c: number): number[][] {
    const m = mat.length;
    const n = mat[0].length;
    if (m * n !== r * c) return mat;

    const reshaped: number[][] = Array.from({ length: r }, () => new Array(c));
    for (let i = 0; i < m * n; ++i) {
        const val = mat[Math.floor(i / n)][i % n];
        reshaped[Math.floor(i / c)][i % c] = val;
    }
    return reshaped;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $r
     * @param Integer $c
     * @return Integer[][]
     */
    function matrixReshape($mat, $r, $c) {
        $m = count($mat);
        $n = count($mat[0]);
        if ($m * $n !== $r * $c) {
            return $mat;
        }
        $result = array_fill(0, $r, array_fill(0, $c, 0));
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $idx = $i * $n + $j;
                $newRow = intdiv($idx, $c);
                $newCol = $idx % $c;
                $result[$newRow][$newCol] = $mat[$i][$j];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func matrixReshape(_ mat: [[Int]], _ r: Int, _ c: Int) -> [[Int]] {
        let m = mat.count
        let n = mat[0].count
        if m * n != r * c { return mat }
        var result = Array(repeating: Array(repeating: 0, count: c), count: r)
        for i in 0..<(m * n) {
            let origRow = i / n
            let origCol = i % n
            let newRow = i / c
            let newCol = i % c
            result[newRow][newCol] = mat[origRow][origCol]
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun matrixReshape(mat: Array<IntArray>, r: Int, c: Int): Array<IntArray> {
        val m = mat.size
        if (m == 0) return mat
        val n = mat[0].size
        if (m * n != r * c) return mat

        val result = Array(r) { IntArray(c) }
        for (idx in 0 until m * n) {
            val originalRow = idx / n
            val originalCol = idx % n
            val newRow = idx / c
            val newCol = idx % c
            result[newRow][newCol] = mat[originalRow][originalCol]
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> matrixReshape(List<List<int>> mat, int r, int c) {
    int m = mat.length;
    int n = mat[0].length;
    if (m * n != r * c) return mat;
    List<List<int>> res = List.generate(r, (_) => List.filled(c, 0));
    for (int i = 0; i < m * n; ++i) {
      int val = mat[i ~/ n][i % n];
      res[i ~/ c][i % c] = val;
    }
    return res;
  }
}
```

## Golang

```go
func matrixReshape(mat [][]int, r int, c int) [][]int {
	m := len(mat)
	n := len(mat[0])
	if m*n != r*c {
		return mat
	}
	res := make([][]int, r)
	for i := 0; i < r; i++ {
		res[i] = make([]int, c)
	}
	for i := 0; i < m*n; i++ {
		origRow, origCol := i/n, i%n
		newRow, newCol := i/c, i%c
		res[newRow][newCol] = mat[origRow][origCol]
	}
	return res
}
```

## Ruby

```ruby
def matrix_reshape(mat, r, c)
  m = mat.size
  n = mat[0].size
  return mat if m * n != r * c
  flat = mat.flatten
  res = []
  (0...r).each do |i|
    res << flat[i * c, c]
  end
  res
end
```

## Scala

```scala
object Solution {
    def matrixReshape(mat: Array[Array[Int]], r: Int, c: Int): Array[Array[Int]] = {
        val m = mat.length
        val n = if (m == 0) 0 else mat(0).length
        if (m * n != r * c) return mat

        val res = Array.ofDim[Int](r, c)
        var idx = 0
        while (idx < m * n) {
            val originalRow = idx / n
            val originalCol = idx % n
            val newRow = idx / c
            val newCol = idx % c
            res(newRow)(newCol) = mat(originalRow)(originalCol)
            idx += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn matrix_reshape(mat: Vec<Vec<i32>>, r: i32, c: i32) -> Vec<Vec<i32>> {
        let m = mat.len();
        if m == 0 {
            return mat;
        }
        let n = mat[0].len();
        let total = m * n;
        let r_usize = r as usize;
        let c_usize = c as usize;
        if total != r_usize * c_usize {
            return mat;
        }
        let mut res = vec![vec![0; c_usize]; r_usize];
        for idx in 0..total {
            let val = mat[idx / n][idx % n];
            res[idx / c_usize][idx % c_usize] = val;
        }
        res
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (matrix-reshape mat r c)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?
       (listof (listof exact-integer?)))
  (let* ((m (length mat))
         (n (if (null? mat) 0 (length (car mat))))
         (total (* m n)))
    (if (not (= total (* r c)))
        mat
        (let loop ((flat (apply append mat))
                   (rows r)
                   (acc '()))
          (if (= rows 0)
              (reverse acc)
              (let* ((row (take flat c))
                     (rest (drop flat c)))
                (loop rest (- rows 1) (cons row acc))))))))
```

## Erlang

```erlang
-module(solution).
-export([matrix_reshape/3]).

-spec matrix_reshape(Mat :: [[integer()]], R :: integer(), C :: integer()) -> [[integer()]].
matrix_reshape(Mat, R, C) ->
    case Mat of
        [] -> [];
        _ ->
            Total = length(Mat) * length(hd(Mat)),
            if R*C =/= Total ->
                    Mat;
               true ->
                    Flat = [X || Row <- Mat, X <- Row],
                    reshape_rows(Flat, C)
            end
    end.

reshape_rows(List, C) -> chunks(List, C).

chunks([], _) -> [];
chunks(L, C) ->
    {Chunk, Rest} = lists:split(C, L),
    [Chunk | chunks(Rest, C)].
```

## Elixir

```elixir
defmodule Solution do
  @spec matrix_reshape(mat :: [[integer]], r :: integer, c :: integer) :: [[integer]]
  def matrix_reshape(mat, r, c) do
    m = length(mat)
    n = if m > 0, do: length(List.first(mat)), else: 0

    if m * n != r * c do
      mat
    else
      flat = Enum.flat_map(mat, fn row -> row end)
      Enum.chunk_every(flat, c)
    end
  end
end
```
