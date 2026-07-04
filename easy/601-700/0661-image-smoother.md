# 0661. Image Smoother

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int m = img.size();
        int n = img[0].size();
        vector<vector<int>> res(m, vector<int>(n, 0));
        const int dirs[9][2] = {{-1,-1},{-1,0},{-1,1},
                                {0,-1},{0,0},{0,1},
                                {1,-1},{1,0},{1,1}};
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int sum = 0, cnt = 0;
                for (auto &d : dirs) {
                    int x = i + d[0], y = j + d[1];
                    if (x >= 0 && x < m && y >= 0 && y < n) {
                        sum += img[x][y];
                        ++cnt;
                    }
                }
                res[i][j] = sum / cnt;
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[][] imageSmoother(int[][] img) {
        int m = img.length;
        int n = img[0].length;
        // First pass: compute smoothed values and encode them in higher bits
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int sum = 0, cnt = 0;
                for (int di = -1; di <= 1; di++) {
                    int ni = i + di;
                    if (ni < 0 || ni >= m) continue;
                    for (int dj = -1; dj <= 1; dj++) {
                        int nj = j + dj;
                        if (nj < 0 || nj >= n) continue;
                        sum += img[ni][nj] & 255; // original value
                        cnt++;
                    }
                }
                int avg = sum / cnt;
                img[i][j] |= (avg << 8); // store in higher bits
            }
        }
        // Second pass: extract the smoothed values
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                img[i][j] = img[i][j] >> 8;
            }
        }
        return img;
    }
}
```

## Python

```python
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(img)
        n = len(img[0])
        res = [[0] * n for _ in range(m)]
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),  (0, 0),  (0, 1),
                (1, -1),  (1, 0),  (1, 1)]
        for i in range(m):
            for j in range(n):
                s = cnt = 0
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        s += img[ni][nj]
                        cnt += 1
                res[i][j] = s // cnt
        return res
```

## Python3

```python
from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        offsets = [-1, 0, 1]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for di in offsets:
                    ni = i + di
                    if 0 <= ni < m:
                        for dj in offsets:
                            nj = j + dj
                            if 0 <= nj < n:
                                total += img[ni][nj]
                                count += 1
                result[i][j] = total // count

        return result
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** imageSmoother(int** img, int imgSize, int* imgColSize, int* returnSize, int** returnColumnSizes) {
    if (imgSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    
    int rows = imgSize;
    int cols = imgColSize[0];   // matrix is rectangular per problem constraints
    
    int **res = (int **)malloc(rows * sizeof(int *));
    *returnColumnSizes = (int *)malloc(rows * sizeof(int));
    for (int i = 0; i < rows; ++i) {
        res[i] = (int *)malloc(cols * sizeof(int));
        (*returnColumnSizes)[i] = cols;
    }
    
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            int sum = 0, cnt = 0;
            for (int dr = -1; dr <= 1; ++dr) {
                int nr = r + dr;
                if (nr < 0 || nr >= rows) continue;
                for (int dc = -1; dc <= 1; ++dc) {
                    int nc = c + dc;
                    if (nc < 0 || nc >= cols) continue;
                    sum += img[nr][nc];
                    ++cnt;
                }
            }
            res[r][c] = sum / cnt;   // integer division floors automatically
        }
    }
    
    *returnSize = rows;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[][] ImageSmoother(int[][] img)
    {
        int m = img.Length;
        int n = img[0].Length;
        int[][] result = new int[m][];
        for (int i = 0; i < m; i++)
            result[i] = new int[n];

        int[] dirs = { -1, 0, 1 };
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int sum = 0;
                int count = 0;
                foreach (int di in dirs)
                {
                    int ni = i + di;
                    if (ni < 0 || ni >= m) continue;
                    foreach (int dj in dirs)
                    {
                        int nj = j + dj;
                        if (nj < 0 || nj >= n) continue;
                        sum += img[ni][nj];
                        count++;
                    }
                }
                result[i][j] = sum / count; // integer division floors automatically
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} img
 * @return {number[][]}
 */
var imageSmoother = function(img) {
    const m = img.length;
    const n = img[0].length;
    const res = Array.from({ length: m }, () => Array(n).fill(0));
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            let sum = 0, cnt = 0;
            for (let di = -1; di <= 1; ++di) {
                const ni = i + di;
                if (ni < 0 || ni >= m) continue;
                for (let dj = -1; dj <= 1; ++dj) {
                    const nj = j + dj;
                    if (nj < 0 || nj >= n) continue;
                    sum += img[ni][nj];
                    cnt++;
                }
            }
            res[i][j] = Math.floor(sum / cnt);
        }
    }
    
    return res;
};
```

## Typescript

```typescript
function imageSmoother(img: number[][]): number[][] {
    const m = img.length;
    const n = img[0].length;
    const result: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let sum = 0, cnt = 0;
            for (let di = -1; di <= 1; di++) {
                const ni = i + di;
                if (ni < 0 || ni >= m) continue;
                for (let dj = -1; dj <= 1; dj++) {
                    const nj = j + dj;
                    if (nj < 0 || nj >= n) continue;
                    sum += img[ni][nj];
                    cnt++;
                }
            }
            result[i][j] = Math.floor(sum / cnt);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $img
     * @return Integer[][]
     */
    function imageSmoother($img) {
        $m = count($img);
        $n = count($img[0]);
        $res = array_fill(0, $m, array_fill(0, $n, 0));
        $dirs = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1],  [0, 0],  [0, 1],
            [1, -1],  [1, 0],  [1, 1]
        ];
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $sum = 0;
                $cnt = 0;
                foreach ($dirs as $d) {
                    $x = $i + $d[0];
                    $y = $j + $d[1];
                    if ($x >= 0 && $x < $m && $y >= 0 && $y < $n) {
                        $sum += $img[$x][$y];
                        ++$cnt;
                    }
                }
                $res[$i][$j] = intdiv($sum, $cnt);
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func imageSmoother(_ img: [[Int]]) -> [[Int]] {
        let m = img.count
        let n = img[0].count
        var result = Array(repeating: Array(repeating: 0, count: n), count: m)
        
        for i in 0..<m {
            for j in 0..<n {
                var sum = 0
                var cnt = 0
                for dx in -1...1 {
                    for dy in -1...1 {
                        let x = i + dx
                        let y = j + dy
                        if x >= 0 && x < m && y >= 0 && y < n {
                            sum += img[x][y]
                            cnt += 1
                        }
                    }
                }
                result[i][j] = sum / cnt
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun imageSmoother(img: Array<IntArray>): Array<IntArray> {
        val m = img.size
        val n = img[0].size
        for (i in 0 until m) {
            for (j in 0 until n) {
                var sum = 0
                var cnt = 0
                for (dx in -1..1) {
                    val x = i + dx
                    if (x !in 0 until m) continue
                    for (dy in -1..1) {
                        val y = j + dy
                        if (y !in 0 until n) continue
                        sum += img[x][y] % 256
                        cnt++
                    }
                }
                val avg = sum / cnt
                img[i][j] = img[i][j] + avg * 256
            }
        }
        for (i in 0 until m) {
            for (j in 0 until n) {
                img[i][j] = img[i][j] ushr 8
            }
        }
        return img
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> imageSmoother(List<List<int>> img) {
    int m = img.length;
    int n = img[0].length;
    List<List<int>> res = List.generate(m, (_) => List.filled(n, 0));
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int sum = 0;
        int cnt = 0;
        for (int di = -1; di <= 1; di++) {
          for (int dj = -1; dj <= 1; dj++) {
            int ni = i + di;
            int nj = j + dj;
            if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
              sum += img[ni][nj];
              cnt++;
            }
          }
        }
        res[i][j] = sum ~/ cnt;
      }
    }
    return res;
  }
}
```

## Golang

```go
func imageSmoother(img [][]int) [][]int {
    m := len(img)
    if m == 0 {
        return [][]int{}
    }
    n := len(img[0])
    res := make([][]int, m)
    for i := 0; i < m; i++ {
        res[i] = make([]int, n)
    }

    dirs := []int{-1, 0, 1}
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            sum, cnt := 0, 0
            for _, di := range dirs {
                for _, dj := range dirs {
                    ni, nj := i+di, j+dj
                    if ni >= 0 && ni < m && nj >= 0 && nj < n {
                        sum += img[ni][nj]
                        cnt++
                    }
                }
            }
            res[i][j] = sum / cnt
        }
    }
    return res
}
```

## Ruby

```ruby
def image_smoother(img)
  m = img.length
  n = img[0].length

  (0...m).each do |i|
    (0...n).each do |j|
      sum = 0
      cnt = 0
      (-1..1).each do |dx|
        ni = i + dx
        next if ni < 0 || ni >= m
        (-1..1).each do |dy|
          nj = j + dy
          next if nj < 0 || nj >= n
          sum += img[ni][nj] & 255
          cnt += 1
        end
      end
      avg = sum / cnt
      img[i][j] |= (avg << 8)
    end
  end

  (0...m).each do |i|
    (0...n).each do |j|
      img[i][j] = img[i][j] >> 8
    end
  end

  img
end
```

## Scala

```scala
object Solution {
  def imageSmoother(img: Array[Array[Int]]): Array[Array[Int]] = {
    val m = img.length
    val n = img(0).length
    val res = Array.ofDim[Int](m, n)

    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        var sum = 0
        var cnt = 0
        var r = i - 1
        while (r <= i + 1) {
          var c = j - 1
          while (c <= j + 1) {
            if (r >= 0 && r < m && c >= 0 && c < n) {
              sum += img(r)(c)
              cnt += 1
            }
            c += 1
          }
          r += 1
        }
        res(i)(j) = sum / cnt
        j += 1
      }
      i += 1
    }

    res
  }
}
```

## Rust

```rust
impl Solution {
    pub fn image_smoother(img: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = img.len();
        if m == 0 {
            return vec![];
        }
        let n = img[0].len();
        let mut res = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                let mut sum = 0;
                let mut cnt = 0;
                for di in -1i32..=1 {
                    for dj in -1i32..=1 {
                        let ni = i as i32 + di;
                        let nj = j as i32 + dj;
                        if ni >= 0 && (ni as usize) < m && nj >= 0 && (nj as usize) < n {
                            sum += img[ni as usize][nj as usize];
                            cnt += 1;
                        }
                    }
                }
                res[i][j] = sum / cnt;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (image-smoother img)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((m (length img))
         (n (if (zero? m) 0 (length (car img))))
         (offsets (list (cons -1 -1) (cons -1 0) (cons -1 1)
                       (cons 0 -1) (cons 0 0) (cons 0 1)
                       (cons 1 -1) (cons 1 0) (cons 1 1))))
    (build-list m
      (lambda (i)
        (build-list n
          (lambda (j)
            (let ((sum 0) (cnt 0))
              (for ([off offsets])
                (let* ((ni (+ i (car off))) (nj (+ j (cdr off))))
                  (when (and (>= ni 0) (< ni m) (>= nj 0) (< nj n))
                    (set! sum (+ sum (list-ref (list-ref img ni) nj)))
                    (set! cnt (+ cnt 1)))))
              (quotient sum cnt)))))))
```

## Erlang

```erlang
-spec image_smoother(Img :: [[integer()]]) -> [[integer()]].
image_smoother([]) -> [];
image_smoother(Img) ->
    Rows = length(Img),
    Cols = length(hd(Img)),
    lists:map(
        fun(I) ->
            lists:map(
                fun(J) ->
                    Vals = neighbor_vals(Img, Rows, Cols, I, J),
                    Sum = lists:sum(Vals),
                    Count = length(Vals),
                    Sum div Count
                end,
                lists:seq(0, Cols - 1)
            )
        end,
        lists:seq(0, Rows - 1)
    ).

neighbor_vals(Img, MaxR, MaxC, I, J) ->
    [ get(Img,R,C) ||
        Di <- [-1,0,1],
        Dj <- [-1,0,1],
        R = I + Di,
        C = J + Dj,
        R >= 0, R < MaxR,
        C >= 0, C < MaxC
    ].

get(Img, R, C) ->
    Row = lists:nth(R + 1, Img),
    lists:nth(C + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec image_smoother(img :: [[integer]]) :: [[integer]]
  def image_smoother(img) do
    m = length(img)
    n = if m == 0, do: 0, else: length(hd(img))

    for i <- 0..(m - 1) do
      for j <- 0..(n - 1) do
        {sum, cnt} =
          Enum.reduce(-1..1, {0, 0}, fn di, acc ->
            Enum.reduce(-1..1, acc, fn dj, {s, c} = a ->
              ni = i + di
              nj = j + dj

              if ni >= 0 and ni < m and nj >= 0 and nj < n do
                val = img |> Enum.at(ni) |> Enum.at(nj)
                {s + val, c + 1}
              else
                a
              end
            end)
          end)

        div(sum, cnt)
      end
    end
  end
end
```
