# 0507. Perfect Number

## Cpp

```cpp
class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false;
        long long sum = 1;
        for (int i = 2; i * i <= num; ++i) {
            if (num % i == 0) {
                sum += i;
                int d = num / i;
                if (d != i) sum += d;
            }
        }
        return sum == num;
    }
};
```

## Java

```java
class Solution {
    public boolean checkPerfectNumber(int num) {
        if (num <= 1) return false;
        int sum = 1;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                sum += i;
                int other = num / i;
                if (other != i) sum += other;
            }
        }
        return sum == num;
    }
}
```

## Python

```python
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        total = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                other = num // i
                if other != i:
                    total += other
            i += 1
        return total == num
```

## Python3

```python
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in {6, 28, 496, 8128, 33550336}
```

## C

```c
#include <stdbool.h>

bool checkPerfectNumber(int num) {
    if (num <= 1) return false;
    int sum = 1;
    for (int i = 2; (long long)i * i <= num; ++i) {
        if (num % i == 0) {
            sum += i;
            int other = num / i;
            if (other != i) sum += other;
        }
    }
    return sum == num;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckPerfectNumber(int num) {
        if (num <= 1) return false;
        long sum = 1;
        int limit = (int)Math.Sqrt(num);
        for (int i = 2; i <= limit; i++) {
            if (num % i == 0) {
                int paired = num / i;
                sum += i;
                if (paired != i) sum += paired;
            }
        }
        return sum == num;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {boolean}
 */
var checkPerfectNumber = function(num) {
    const perfectSet = new Set([6, 28, 496, 8128, 33550336]);
    return perfectSet.has(num);
};
```

## Typescript

```typescript
function checkPerfectNumber(num: number): boolean {
    if (num <= 1) return false;
    let sum = 1;
    const limit = Math.sqrt(num);
    for (let i = 2; i <= limit; i++) {
        if (num % i === 0) {
            sum += i;
            const other = num / i;
            if (other !== i) sum += other;
        }
    }
    return sum === num;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Boolean
     */
    function checkPerfectNumber($num) {
        // Known perfect numbers within the given constraints (1 <= num <= 10^8)
        $perfectNumbers = [6, 28, 496, 8128, 33550336];
        return in_array($num, $perfectNumbers, true);
    }
}
```

## Swift

```swift
class Solution {
    func checkPerfectNumber(_ num: Int) -> Bool {
        if num <= 1 { return false }
        var sum = 1
        let sqrtN = Int(Double(num).squareRoot())
        if sqrtN > 1 {
            for i in 2...sqrtN {
                if num % i == 0 {
                    let other = num / i
                    if i == other {
                        sum += i
                    } else {
                        sum += i + other
                    }
                }
            }
        }
        return sum == num
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkPerfectNumber(num: Int): Boolean {
        if (num <= 1) return false
        var sum = 1L
        val n = num.toLong()
        val limit = kotlin.math.sqrt(num.toDouble()).toInt()
        for (i in 2..limit) {
            if (num % i == 0) {
                sum += i
                val other = num / i
                if (other != i) sum += other
            }
        }
        return sum == n
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  bool checkPerfectNumber(int num) {
    if (num <= 1) return false;
    int sum = 1;
    int sqrtN = sqrt(num).toInt();
    for (int i = 2; i <= sqrtN; i++) {
      if (num % i == 0) {
        sum += i;
        int other = num ~/ i;
        if (other != i) sum += other;
      }
      if (sum > num) return false;
    }
    return sum == num;
  }
}
```

## Golang

```go
import "math"

func checkPerfectNumber(num int) bool {
	if num <= 1 {
		return false
	}
	sum := 1
	limit := int(math.Sqrt(float64(num)))
	for i := 2; i <= limit; i++ {
		if num%i == 0 {
			sum += i
			other := num / i
			if other != i {
				sum += other
			}
		}
	}
	return sum == num
}
```

## Ruby

```ruby
def check_perfect_number(num)
  return false if num <= 1
  sum = 1
  i = 2
  while i * i <= num
    if num % i == 0
      sum += i
      other = num / i
      sum += other if other != i
    end
    i += 1
  end
  sum == num
end
```

## Scala

```scala
object Solution {
    def checkPerfectNumber(num: Int): Boolean = {
        if (num <= 1) return false
        var sum: Long = 1L
        val limit = math.sqrt(num.toDouble).toInt
        var i = 2
        while (i <= limit) {
            if (num % i == 0) {
                sum += i
                val other = num / i
                if (other != i) sum += other
            }
            i += 1
        }
        sum == num
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_perfect_number(num: i32) -> bool {
        if num <= 1 {
            return false;
        }
        let mut sum: i64 = 1;
        let n = num as i64;
        let limit = (num as f64).sqrt() as i32;
        for i in 2..=limit {
            if num % i == 0 {
                sum += i as i64;
                let other = num / i;
                if other != i {
                    sum += other as i64;
                }
            }
        }
        sum == n
    }
}
```

## Racket

```racket
(define/contract (check-perfect-number num)
  (-> exact-integer? boolean?)
  (if (< num 2)
      #false
      (let loop ((i 2) (sum 1))
        (cond [(> (* i i) num) (= sum num)]
              [(zero? (remainder num i))
               (let* ([j (/ num i)])
                 (if (= i j)
                     (loop (+ i 1) (+ sum i))
                     (loop (+ i 1) (+ sum i j))))]
              [else (loop (+ i 1) sum)]))))
```

## Erlang

```erlang
-module(solution).
-export([check_perfect_number/1]).

-spec check_perfect_number(Num :: integer()) -> boolean().
check_perfect_number(Num) when Num > 1 ->
    Max = trunc(math:sqrt(Num)),
    Sum = sum_divisors(2, Max, 1, Num),
    Sum == Num;
check_perfect_number(_) ->
    false.

sum_divisors(I, Max, Acc, N) when I =< Max ->
    case N rem I of
        0 ->
            Other = N div I,
            NewAcc = if I == Other -> Acc + I; true -> Acc + I + Other end,
            sum_divisors(I + 1, Max, NewAcc, N);
        _ ->
            sum_divisors(I + 1, Max, Acc, N)
    end;
sum_divisors(_, _, Acc, _) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_perfect_number(num :: integer) :: boolean
  def check_perfect_number(num) when num <= 1, do: false

  def check_perfect_number(num) do
    limit = :math.sqrt(num) |> trunc()
    sum =
      Enum.reduce(2..limit, 1, fn i, acc ->
        if rem(num, i) == 0 do
          other = div(num, i)

          if other == i do
            acc + i
          else
            acc + i + other
          end
        else
          acc
        end
      end)

    sum == num
  end
end
```
