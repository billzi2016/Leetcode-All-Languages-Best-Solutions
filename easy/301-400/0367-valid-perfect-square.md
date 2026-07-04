# 0367. Valid Perfect Square

## Cpp

```cpp
class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num < 2) return true;
        long long left = 1, right = num / 2;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            long long sq = mid * mid;
            if (sq == num) return true;
            if (sq < num) left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean isPerfectSquare(int num) {
        if (num < 2) return true;
        long left = 1, right = num / 2L + 1;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            long sq = mid * mid;
            if (sq == num) return true;
            if (sq < num) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        left, right = 1, num // 2 + 1
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
```

## Python3

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 1, num // 2
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == num:
                return True
            if sq < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
```

## C

```c
#include <stdbool.h>

bool isPerfectSquare(int num) {
    if (num < 2) return true;
    long long left = 2, right = num / 2;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        long long sq = mid * mid;
        if (sq == num) return true;
        if (sq < num)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsPerfectSquare(int num) {
        if (num < 2) return true;
        long left = 1, right = num;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            long sq = mid * mid;
            if (sq == num) return true;
            if (sq < num) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    if (num === 1) return true;
    let left = 1, right = Math.floor(num / 2);
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const div = Math.floor(num / mid);
        if (mid === div && mid * mid === num) return true;
        if (mid > div) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return false;
};
```

## Typescript

```typescript
function isPerfectSquare(num: number): boolean {
    if (num < 2) return true;
    let left = 2;
    let right = Math.floor(num / 2);
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const sq = mid * mid;
        if (sq === num) return true;
        if (sq < num) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Boolean
     */
    function isPerfectSquare($num) {
        if ($num < 2) {
            return true;
        }
        $left = 1;
        $right = intval($num / 2);
        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            $sq = $mid * $mid;
            if ($sq == $num) {
                return true;
            } elseif ($sq < $num) {
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isPerfectSquare(_ num: Int) -> Bool {
        if num < 2 { return true }
        var left = 1
        var right = num / 2
        let target = Int64(num)
        while left <= right {
            let mid = left + (right - left) / 2
            let sq = Int64(mid) * Int64(mid)
            if sq == target {
                return true
            } else if sq < target {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPerfectSquare(num: Int): Boolean {
        if (num < 2) return true
        var left = 1L
        var right = num.toLong() / 2 + 1
        while (left <= right) {
            val mid = (left + right) ushr 1
            val sq = mid * mid
            when {
                sq == num.toLong() -> return true
                sq < num -> left = mid + 1
                else -> right = mid - 1
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool isPerfectSquare(int num) {
    if (num < 2) return true;
    int left = 1, right = num ~/ 2;
    while (left <= right) {
      int mid = left + ((right - left) >> 1);
      int sq = mid * mid;
      if (sq == num) return true;
      if (sq < num) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return false;
  }
}
```

## Golang

```go
func isPerfectSquare(num int) bool {
	if num < 2 {
		return true
	}
	left, right := 1, num/2
	target := int64(num)
	for left <= right {
		mid := left + (right-left)/2
		sq := int64(mid) * int64(mid)
		if sq == target {
			return true
		} else if sq < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return false
}
```

## Ruby

```ruby
# @param {Integer} num
# @return {Boolean}
def is_perfect_square(num)
  left = 0
  right = num

  while left <= right
    mid = (left + right) / 2
    square = mid * mid

    if square == num
      return true
    elsif square < num
      left = mid + 1
    else
      right = mid - 1
    end
  end

  false
end
```

## Scala

```scala
object Solution {
    def isPerfectSquare(num: Int): Boolean = {
        if (num < 2) return true
        var left: Long = 1L
        var right: Long = num / 2L
        while (left <= right) {
            val mid = left + (right - left) / 2
            val sq = mid * mid
            if (sq == num) return true
            else if (sq < num) left = mid + 1
            else right = mid - 1
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        if num < 2 {
            return true;
        }
        let target = num as i64;
        let mut left: i64 = 1;
        let mut right: i64 = target / 2;
        while left <= right {
            let mid = left + (right - left) / 2;
            let sq = mid * mid;
            if sq == target {
                return true;
            } else if sq < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (is-perfect-square num)
  (-> exact-integer? boolean?)
  (if (= num 1)
      #t
      (let loop ((low 1) (high (quotient num 2)))
        (cond [(> low high) #f]
              [else
               (let* ([mid (+ low (quotient (- high low) 2))]
                      [sq (* mid mid)])
                 (cond [(= sq num) #t]
                       [(< sq num) (loop (+ mid 1) high)]
                       [else (loop low (- mid 1))]))]))) )
```

## Erlang

```erlang
-spec is_perfect_square(Num :: integer()) -> boolean().
is_perfect_square(Num) when Num >= 1 ->
    is_perf_sq(1, Num, Num).

is_perf_sq(Low, High, Target) when Low > High ->
    false;
is_perf_sq(Low, High, Target) ->
    Mid = (Low + High) div 2,
    Prod = Mid * Mid,
    case Prod of
        P when P == Target -> true;
        P when P < Target -> is_perf_sq(Mid + 1, High, Target);
        _ -> is_perf_sq(Low, Mid - 1, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_perfect_square(num :: integer) :: boolean
  def is_perfect_square(num) when num < 2, do: true

  def is_perfect_square(num) do
    binary_search(1, div(num, 2), num)
  end

  defp binary_search(low, high, target) when low > high, do: false

  defp binary_search(low, high, target) do
    mid = div(low + high, 2)
    sq = mid * mid

    cond do
      sq == target -> true
      sq < target -> binary_search(mid + 1, high, target)
      true -> binary_search(low, mid - 1, target)
    end
  end
end
```
