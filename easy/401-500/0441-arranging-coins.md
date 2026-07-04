# 0441. Arranging Coins

## Cpp

```cpp
class Solution {
public:
    int arrangeCoins(int n) {
        long long left = 0, right = n;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            long long sum = mid * (mid + 1) / 2;
            if (sum == n) return static_cast<int>(mid);
            if (sum < n) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return static_cast<int>(right);
    }
};
```

## Java

```java
class Solution {
    public int arrangeCoins(int n) {
        long left = 0, right = n;
        while (left <= right) {
            long mid = (left + right) >>> 1;
            long sum = mid * (mid + 1) / 2;
            if (sum == n) {
                return (int) mid;
            } else if (sum < n) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return (int) right;
    }
}
```

## Python

```python
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return (math.isqrt(1 + 8 * n) - 1) // 2
```

## Python3

```python
import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        d = math.isqrt(1 + 8 * n)
        return (d - 1) // 2
```

## C

```c
int arrangeCoins(int n) {
    long long left = 0, right = n;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        long long sum = mid * (mid + 1) / 2;
        if (sum == n) return (int)mid;
        if (sum < n)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return (int)right;
}
```

## Csharp

```csharp
public class Solution {
    public int ArrangeCoins(int n) {
        long left = 0, right = n;
        while (left <= right) {
            long mid = (left + right) / 2;
            long sum = mid * (mid + 1) / 2;
            if (sum == n) return (int)mid;
            if (sum < n) left = mid + 1;
            else right = mid - 1;
        }
        return (int)right;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function(n) {
    return Math.floor((Math.sqrt(8 * n + 1) - 1) / 2);
};
```

## Typescript

```typescript
function arrangeCoins(n: number): number {
    const discriminant = 1 + 8 * n;
    return Math.floor((Math.sqrt(discriminant) - 1) / 2);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function arrangeCoins($n) {
        $low = 0;
        $high = $n;
        $ans = 0;
        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            $curr = $mid * ($mid + 1) / 2;
            if ($curr == $n) {
                return $mid;
            } elseif ($curr < $n) {
                $ans = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func arrangeCoins(_ n: Int) -> Int {
        var left = 0
        var right = n
        var result = 0
        let target = Int64(n)
        while left <= right {
            let mid = left + (right - left) / 2
            let sum = Int64(mid) * Int64(mid + 1) / 2
            if sum == target {
                return mid
            } else if sum < target {
                result = mid
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun arrangeCoins(n: Int): Int {
        var left = 0L
        var right = n.toLong()
        var ans = 0L
        val target = n.toLong()
        while (left <= right) {
            val mid = left + (right - left) / 2
            val sum = mid * (mid + 1) / 2
            if (sum == target) return mid.toInt()
            if (sum < target) {
                ans = mid
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int arrangeCoins(int n) {
    int left = 0;
    int right = n;
    while (left <= right) {
      int mid = left + ((right - left) >> 1);
      int curr = mid * (mid + 1) ~/ 2;
      if (curr == n) return mid;
      if (curr < n) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return right;
  }
}
```

## Golang

```go
func arrangeCoins(n int) int {
    N := int64(n)
    var left, right int64 = 0, N
    var ans int64 = 0
    for left <= right {
        mid := (left + right) / 2
        sum := mid * (mid + 1) / 2
        if sum == N {
            return int(mid)
        } else if sum < N {
            ans = mid
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return int(ans)
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def arrange_coins(n)
  ((Math.sqrt(8 * n + 1) - 1) / 2).floor
end
```

## Scala

```scala
object Solution {
    def arrangeCoins(n: Int): Int = {
        var left = 0L
        var right = n.toLong
        val target = n.toLong
        while (left <= right) {
            val mid = left + (right - left) / 2
            val sum = mid * (mid + 1) / 2
            if (sum == target) return mid.toInt
            else if (sum < target) left = mid + 1
            else right = mid - 1
        }
        right.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn arrange_coins(n: i32) -> i32 {
        let mut left: i64 = 0;
        let mut right: i64 = n as i64;
        let mut ans: i64 = 0;
        while left <= right {
            let mid = (left + right) / 2;
            let sum = mid * (mid + 1) / 2;
            if sum == n as i64 {
                return mid as i32;
            } else if sum < n as i64 {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (arrange-coins n)
  (-> exact-integer? exact-integer?)
  (let* ((target (* 2 n))
         (max-k
          (let loop ((low 0) (high n))
            (if (> low high)
                low
                (let* ((mid (quotient (+ low high) 2))
                       (sum (* mid (+ mid 1))))
                  (if (<= sum target)
                      (loop (+ mid 1) high)
                      (loop low (- mid 1))))))))
    (- max-k 1)))
```

## Erlang

```erlang
-spec arrange_coins(N :: integer()) -> integer().
arrange_coins(N) ->
    trunc((math:sqrt(8 * N + 1) - 1) / 2).
```

## Elixir

```elixir
defmodule Solution do
  @spec arrange_coins(n :: integer) :: integer
  def arrange_coins(n) do
    binary_search(0, n, n, 0)
  end

  defp binary_search(low, high, target, ans) when low > high, do: ans

  defp binary_search(low, high, target, _ans) do
    mid = div(low + high, 2)
    sum = div(mid * (mid + 1), 2)

    cond do
      sum == target ->
        mid

      sum < target ->
        binary_search(mid + 1, high, target, mid)

      true ->
        binary_search(low, mid - 1, target, 0)
    end
  end
end
```
