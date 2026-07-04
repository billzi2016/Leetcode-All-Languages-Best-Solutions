# 0598. Range Addition II

## Cpp

```cpp
class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        if (ops.empty()) return m * n;
        int minA = m, minB = n;
        for (const auto& op : ops) {
            minA = min(minA, op[0]);
            minB = min(minB, op[1]);
        }
        return minA * minB;
    }
};
```

## Java

```java
class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        if (ops == null || ops.length == 0) {
            return m * n;
        }
        int minA = m;
        int minB = n;
        for (int[] op : ops) {
            if (op[0] < minA) minA = op[0];
            if (op[1] < minB) minB = op[1];
        }
        return minA * minB;
    }
}
```

## Python

```python
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        min_a = m
        min_b = n
        for a, b in ops:
            if a < min_a:
                min_a = a
            if b < min_b:
                min_b = b
        return min_a * min_b
```

## Python3

```python
from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        min_a, min_b = m, n
        for a, b in ops:
            if a < min_a:
                min_a = a
            if b < min_b:
                min_b = b
        return min_a * min_b
```

## C

```c
int maxCount(int m, int n, int** ops, int opsSize, int* opsColSize) {
    if (opsSize == 0) return m * n;
    int min_a = m;
    int min_b = n;
    for (int i = 0; i < opsSize; ++i) {
        int a = ops[i][0];
        int b = ops[i][1];
        if (a < min_a) min_a = a;
        if (b < min_b) min_b = b;
    }
    return min_a * min_b;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxCount(int m, int n, int[][] ops) {
        if (ops == null || ops.Length == 0) return m * n;
        int minA = m;
        int minB = n;
        foreach (var op in ops) {
            if (op[0] < minA) minA = op[0];
            if (op[1] < minB) minB = op[1];
        }
        return minA * minB;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} ops
 * @return {number}
 */
var maxCount = function(m, n, ops) {
    if (ops.length === 0) return m * n;
    let minRow = m;
    let minCol = n;
    for (let i = 0; i < ops.length; i++) {
        const [a, b] = ops[i];
        if (a < minRow) minRow = a;
        if (b < minCol) minCol = b;
    }
    return minRow * minCol;
};
```

## Typescript

```typescript
function maxCount(m: number, n: number, ops: number[][]): number {
    if (ops.length === 0) return m * n;
    let minA = m, minB = n;
    for (const [a, b] of ops) {
        if (a < minA) minA = a;
        if (b < minB) minB = b;
    }
    return minA * minB;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $ops
     * @return Integer
     */
    function maxCount($m, $n, $ops) {
        if (empty($ops)) {
            return $m * $n;
        }
        $minRow = $m;
        $minCol = $n;
        foreach ($ops as $op) {
            if ($op[0] < $minRow) {
                $minRow = $op[0];
            }
            if ($op[1] < $minCol) {
                $minCol = $op[1];
            }
        }
        return $minRow * $minCol;
    }
}
```

## Swift

```swift
class Solution {
    func maxCount(_ m: Int, _ n: Int, _ ops: [[Int]]) -> Int {
        var minA = m
        var minB = n
        for op in ops {
            if op[0] < minA { minA = op[0] }
            if op[1] < minB { minB = op[1] }
        }
        return minA * minB
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxCount(m: Int, n: Int, ops: Array<IntArray>): Int {
        var minA = m
        var minB = n
        for (op in ops) {
            if (op[0] < minA) minA = op[0]
            if (op[1] < minB) minB = op[1]
        }
        return minA * minB
    }
}
```

## Dart

```dart
class Solution {
  int maxCount(int m, int n, List<List<int>> ops) {
    if (ops.isEmpty) return m * n;
    int minRow = m;
    int minCol = n;
    for (var op in ops) {
      int a = op[0];
      int b = op[1];
      if (a < minRow) minRow = a;
      if (b < minCol) minCol = b;
    }
    return minRow * minCol;
  }
}
```

## Golang

```go
func maxCount(m int, n int, ops [][]int) int {
	if len(ops) == 0 {
		return m * n
	}
	minA, minB := m, n
	for _, op := range ops {
		if op[0] < minA {
			minA = op[0]
		}
		if op[1] < minB {
			minB = op[1]
		}
	}
	return minA * minB
}
```

## Ruby

```ruby
def max_count(m, n, ops)
  return m * n if ops.empty?
  min_a = m
  min_b = n
  ops.each do |a, b|
    min_a = a if a < min_a
    min_b = b if b < min_b
  end
  min_a * min_b
end
```

## Scala

```scala
object Solution {
    def maxCount(m: Int, n: Int, ops: Array[Array[Int]]): Int = {
        if (ops == null || ops.isEmpty) return m * n
        var minRow = m
        var minCol = n
        var i = 0
        while (i < ops.length) {
            val op = ops(i)
            if (op(0) < minRow) minRow = op(0)
            if (op(1) < minCol) minCol = op(1)
            i += 1
        }
        minRow * minCol
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_count(m: i32, n: i32, ops: Vec<Vec<i32>>) -> i32 {
        let mut min_m = m;
        let mut min_n = n;
        for op in ops.iter() {
            if !op.is_empty() {
                min_m = std::cmp::min(min_m, op[0]);
                min_n = std::cmp::min(min_n, op[1]);
            }
        }
        min_m * min_n
    }
}
```

## Racket

```racket
(define/contract (max-count m n ops)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let loop ((remaining ops) (min-a m) (min-b n))
    (if (null? remaining)
        (* min-a min-b)
        (let* ((op (car remaining))
               (a (first op))
               (b (second op))
               (new-min-a (if (< a min-a) a min-a))
               (new-min-b (if (< b min-b) b min-b)))
          (loop (cdr remaining) new-min-a new-min-b)))))
```

## Erlang

```erlang
-spec max_count(M :: integer(), N :: integer(), Ops :: [[integer()]]) -> integer().
max_count(M, N, Ops) ->
    case Ops of
        [] -> M * N;
        _ ->
            {MinA, MinB} = lists:foldl(
                fun([Ai, Bi], {CurA, CurB}) ->
                    {erlang:min(CurA, Ai), erlang:min(CurB, Bi)}
                end,
                {M, N},
                Ops),
            MinA * MinB
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_count(m :: integer, n :: integer, ops :: [[integer]]) :: integer
  def max_count(m, n, ops) do
    if ops == [] do
      m * n
    else
      {min_a, min_b} =
        Enum.reduce(ops, {m, n}, fn [a, b], {cur_a, cur_b} ->
          {
            if a < cur_a, do: a, else: cur_a,
            if b < cur_b, do: b, else: cur_b
          }
        end)

      min_a * min_b
    end
  end
end
```
