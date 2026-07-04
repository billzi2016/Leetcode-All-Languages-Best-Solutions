# 0463. Island Perimeter

## Cpp

```cpp
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int rows = grid.size();
        if (rows == 0) return 0;
        int cols = grid[0].size();
        int perimeter = 0;
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] == 1) {
                    perimeter += 4;
                    if (i > 0 && grid[i-1][j] == 1) perimeter -= 2;
                    if (j > 0 && grid[i][j-1] == 1) perimeter -= 2;
                }
            }
        }
        return perimeter;
    }
};
```

## Java

```java
class Solution {
    public int islandPerimeter(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int perimeter = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    perimeter += 4;
                    if (i > 0 && grid[i - 1][j] == 1) {
                        perimeter -= 2;
                    }
                    if (j > 0 && grid[i][j - 1] == 1) {
                        perimeter -= 2;
                    }
                }
            }
        }
        return perimeter;
    }
}
```

## Python

```python
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter
```

## Python3

```python
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter
```

## C

```c
int islandPerimeter(int** grid, int gridSize, int* gridColSize) {
    int perimeter = 0;
    for (int i = 0; i < gridSize; ++i) {
        int cols = gridColSize[i];
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 1) {
                // up
                if (i == 0 || grid[i - 1][j] == 0) perimeter++;
                // down
                if (i == gridSize - 1 || grid[i + 1][j] == 0) perimeter++;
                // left
                if (j == 0 || grid[i][j - 1] == 0) perimeter++;
                // right
                if (j == cols - 1 || grid[i][j + 1] == 0) perimeter++;
            }
        }
    }
    return perimeter;
}
```

## Csharp

```csharp
public class Solution
{
    public int IslandPerimeter(int[][] grid)
    {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int perimeter = 0;

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (grid[i][j] == 1)
                {
                    perimeter += 4;

                    if (i > 0 && grid[i - 1][j] == 1)
                        perimeter -= 2;
                    if (j > 0 && grid[i][j - 1] == 1)
                        perimeter -= 2;
                }
            }
        }

        return perimeter;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    let rows = grid.length, cols = grid[0].length;
    let perimeter = 0;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j] === 1) {
                perimeter += 4;
                if (i > 0 && grid[i - 1][j] === 1) perimeter -= 2;
                if (j > 0 && grid[i][j - 1] === 1) perimeter -= 2;
            }
        }
    }
    return perimeter;
};
```

## Typescript

```typescript
function islandPerimeter(grid: number[][]): number {
    const rows = grid.length;
    if (rows === 0) return 0;
    const cols = grid[0].length;
    let perimeter = 0;

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j] === 1) {
                perimeter += 4;
                if (i > 0 && grid[i - 1][j] === 1) perimeter -= 2;
                if (j > 0 && grid[i][j - 1] === 1) perimeter -= 2;
            }
        }
    }

    return perimeter;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function islandPerimeter($grid) {
        $rows = count($grid);
        if ($rows == 0) return 0;
        $cols = count($grid[0]);
        $perimeter = 0;

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($grid[$i][$j] == 1) {
                    $perimeter += 4;
                    if ($i > 0 && $grid[$i - 1][$j] == 1) {
                        $perimeter -= 2;
                    }
                    if ($j > 0 && $grid[$i][$j - 1] == 1) {
                        $perimeter -= 2;
                    }
                }
            }
        }

        return $perimeter;
    }
}
```

## Swift

```swift
class Solution {
    func islandPerimeter(_ grid: [[Int]]) -> Int {
        var perimeter = 0
        let rows = grid.count
        guard rows > 0 else { return 0 }
        let cols = grid[0].count
        
        for i in 0..<rows {
            for j in 0..<cols {
                if grid[i][j] == 1 {
                    perimeter += 4
                    if i > 0 && grid[i - 1][j] == 1 {
                        perimeter -= 2
                    }
                    if j > 0 && grid[i][j - 1] == 1 {
                        perimeter -= 2
                    }
                }
            }
        }
        return perimeter
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun islandPerimeter(grid: Array<IntArray>): Int {
        var perimeter = 0
        val rows = grid.size
        val cols = if (rows == 0) 0 else grid[0].size
        for (i in 0 until rows) {
            for (j in 0 until cols) {
                if (grid[i][j] == 1) {
                    if (i == 0 || grid[i - 1][j] == 0) perimeter++
                    if (i == rows - 1 || grid[i + 1][j] == 0) perimeter++
                    if (j == 0 || grid[i][j - 1] == 0) perimeter++
                    if (j == cols - 1 || grid[i][j + 1] == 0) perimeter++
                }
            }
        }
        return perimeter
    }
}
```

## Dart

```dart
class Solution {
  int islandPerimeter(List<List<int>> grid) {
    int rows = grid.length;
    int cols = grid[0].length;
    int perimeter = 0;

    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (grid[i][j] == 1) {
          perimeter += 4;
          if (i > 0 && grid[i - 1][j] == 1) {
            perimeter -= 2;
          }
          if (j > 0 && grid[i][j - 1] == 1) {
            perimeter -= 2;
          }
        }
      }
    }

    return perimeter;
  }
}
```

## Golang

```go
func islandPerimeter(grid [][]int) int {
    rows := len(grid)
    cols := len(grid[0])
    perimeter := 0
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if grid[i][j] == 1 {
                perimeter += 4
                if i > 0 && grid[i-1][j] == 1 {
                    perimeter -= 2
                }
                if j > 0 && grid[i][j-1] == 1 {
                    perimeter -= 2
                }
            }
        }
    }
    return perimeter
}
```

## Ruby

```ruby
def island_perimeter(grid)
  return 0 if grid.empty?
  rows = grid.size
  cols = grid[0].size
  perimeter = 0
  rows.times do |i|
    cols.times do |j|
      next unless grid[i][j] == 1
      perimeter += 4
      perimeter -= 2 if i > 0 && grid[i - 1][j] == 1
      perimeter -= 2 if j > 0 && grid[i][j - 1] == 1
    end
  end
  perimeter
end
```

## Scala

```scala
object Solution {
    def islandPerimeter(grid: Array[Array[Int]]): Int = {
        var perimeter = 0
        val rows = grid.length
        if (rows == 0) return 0
        val cols = grid(0).length

        for (i <- 0 until rows) {
            for (j <- 0 until cols) {
                if (grid(i)(j) == 1) {
                    perimeter += 4
                    if (i > 0 && grid(i - 1)(j) == 1) perimeter -= 2
                    if (j > 0 && grid(i)(j - 1) == 1) perimeter -= 2
                }
            }
        }
        perimeter
    }
}
```

## Rust

```rust
impl Solution {
    pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        if rows == 0 {
            return 0;
        }
        let cols = grid[0].len();
        let mut perim = 0;
        for i in 0..rows {
            for j in 0..cols {
                if grid[i][j] == 1 {
                    if i == 0 || grid[i - 1][j] == 0 {
                        perim += 1;
                    }
                    if i + 1 == rows || grid[i + 1][j] == 0 {
                        perim += 1;
                    }
                    if j == 0 || grid[i][j - 1] == 0 {
                        perim += 1;
                    }
                    if j + 1 == cols || grid[i][j + 1] == 0 {
                        perim += 1;
                    }
                }
            }
        }
        perim as i32
    }
}
```

## Racket

```racket
(define/contract (island-perimeter grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (> rows 0) (length (first grid)) 0)))
    (let loop ((i 0) (perim 0))
      (if (= i rows)
          perim
          (let inner ((j 0) (p perim))
            (if (= j cols)
                (loop (+ i 1) p)
                (let ((cell (list-ref (list-ref grid i) j)))
                  (if (= cell 1)
                      (let* ((right (if (< (+ j 1) cols)
                                        (list-ref (list-ref grid i) (+ j 1))
                                        0))
                             (down (if (< (+ i 1) rows)
                                       (list-ref (list-ref grid (+ i 1)) j)
                                       0))
                             (add (- 4 (* right 2) (* down 2))))
                        (inner (+ j 1) (+ p add)))
                      (inner (+ j 1) p)))))))))
```

## Erlang

```erlang
-module(solution).
-export([island_perimeter/1]).

-spec island_perimeter(Grid :: [[integer()]]) -> integer().
island_perimeter(Grid) ->
    Rows = length(Grid),
    island_perimeter_rows(Grid, 0, Rows, 0).

island_perimeter_rows(_Grid, RowIdx, Rows, Acc) when RowIdx >= Rows ->
    Acc;
island_perimeter_rows(Grid, RowIdx, Rows, Acc) ->
    Row = lists:nth(RowIdx + 1, Grid),
    Cols = length(Row),
    NewAcc = island_perimeter_cols(Row, Grid, RowIdx, 0, Cols, Acc),
    island_perimeter_rows(Grid, RowIdx + 1, Rows, NewAcc).

island_perimeter_cols(_Row, _Grid, _RowIdx, ColIdx, Cols, Acc) when ColIdx >= Cols ->
    Acc;
island_perimeter_cols(Row, Grid, RowIdx, ColIdx, Cols, Acc) ->
    Cell = lists:nth(ColIdx + 1, Row),
    Add = case Cell of
        1 ->
            Up = get(Grid, RowIdx - 1, ColIdx),
            Down = get(Grid, RowIdx + 1, ColIdx),
            Left = get(Grid, RowIdx, ColIdx - 1),
            Right = get(Grid, RowIdx, ColIdx + 1),
            4 - (Up + Down + Left + Right);
        _ -> 0
    end,
    island_perimeter_cols(Row, Grid, RowIdx, ColIdx + 1, Cols, Acc + Add).

get(Grid, R, C) ->
    Rows = length(Grid),
    if R < 0 orelse R >= Rows orelse C < 0 ->
            0;
       true ->
            Row = lists:nth(R + 1, Grid),
            Cols = length(Row),
            if C >= Cols -> 0; true -> lists:nth(C + 1, Row) end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec island_perimeter(grid :: [[integer]]) :: integer
  def island_perimeter(grid) do
    rows = length(grid)
    cols = if rows == 0, do: 0, else: length(List.first(grid))

    Enum.reduce(0..rows - 1, 0, fn i, acc ->
      row = Enum.at(grid, i)

      Enum.reduce(0..cols - 1, acc, fn j, acc2 ->
        if Enum.at(row, j) == 1 do
          up =
            if i == 0 or Enum.at(Enum.at(grid, i - 1), j) == 0,
              do: 1,
              else: 0

          down =
            if i == rows - 1 or Enum.at(Enum.at(grid, i + 1), j) == 0,
              do: 1,
              else: 0

          left =
            if j == 0 or Enum.at(row, j - 1) == 0,
              do: 1,
              else: 0

          right =
            if j == cols - 1 or Enum.at(row, j + 1) == 0,
              do: 1,
              else: 0

          acc2 + up + down + left + right
        else
          acc2
        end
      end)
    end)
  end
end
```
