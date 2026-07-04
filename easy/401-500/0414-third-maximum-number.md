# 0414. Third Maximum Number

## Cpp

```cpp
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long long first = LLONG_MIN, second = LLONG_MIN, third = LLONG_MIN;
        for (int x : nums) {
            if (x == first || x == second || x == third) continue;
            if (x > first) {
                third = second;
                second = first;
                first = x;
            } else if (x > second) {
                third = second;
                second = x;
            } else if (x > third) {
                third = x;
            }
        }
        return third == LLONG_MIN ? static_cast<int>(first) : static_cast<int>(third);
    }
};
```

## Java

```java
class Solution {
    public int thirdMax(int[] nums) {
        long first = Long.MIN_VALUE;
        long second = Long.MIN_VALUE;
        long third = Long.MIN_VALUE;

        for (int n : nums) {
            if (n == first || n == second || n == third) continue;

            if (n > first) {
                third = second;
                second = first;
                first = n;
            } else if (n > second) {
                third = second;
                second = n;
            } else if (n > third) {
                third = n;
            }
        }

        return third == Long.MIN_VALUE ? (int)first : (int)third;
    }
}
```

## Python

```python
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = None
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num
        return third if third is not None else first
```

## Python3

```python
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None
        for n in nums:
            if n == first or n == second or n == third:
                continue
            if first is None or n > first:
                third = second
                second = first
                first = n
            elif second is None or n > second:
                third = second
                second = n
            elif third is None or n > third:
                third = n
        return third if third is not None else first
```

## C

```c
#include <limits.h>

int thirdMax(int* nums, int numsSize) {
    long long first = LLONG_MIN, second = LLONG_MIN, third = LLONG_MIN;
    for (int i = 0; i < numsSize; ++i) {
        long long cur = nums[i];
        if (cur == first || cur == second || cur == third) continue;
        if (cur > first) {
            third = second;
            second = first;
            first = cur;
        } else if (cur > second) {
            third = second;
            second = cur;
        } else if (cur > third) {
            third = cur;
        }
    }
    return (third == LLONG_MIN) ? (int)first : (int)third;
}
```

## Csharp

```csharp
public class Solution {
    public int ThirdMax(int[] nums) {
        long first = long.MinValue;
        long second = long.MinValue;
        long third = long.MinValue;

        foreach (int n in nums) {
            long val = n;
            if (val == first || val == second || val == third) continue;
            if (val > first) {
                third = second;
                second = first;
                first = val;
            } else if (val > second) {
                third = second;
                second = val;
            } else if (val > third) {
                third = val;
            }
        }

        return third == long.MinValue ? (int)first : (int)third;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    let first = -Infinity, second = -Infinity, third = -Infinity;
    for (const n of nums) {
        if (n === first || n === second || n === third) continue;
        if (n > first) {
            third = second;
            second = first;
            first = n;
        } else if (n > second) {
            third = second;
            second = n;
        } else if (n > third) {
            third = n;
        }
    }
    return third === -Infinity ? first : third;
};
```

## Typescript

```typescript
function thirdMax(nums: number[]): number {
    let first: number | null = null;
    let second: number | null = null;
    let third: number | null = null;

    for (const n of nums) {
        if (n === first || n === second || n === third) continue;

        if (first === null || n > first) {
            third = second;
            second = first;
            first = n;
        } else if (second === null || n > second) {
            third = second;
            second = n;
        } else if (third === null || n > third) {
            third = n;
        }
    }

    return third === null ? (first as number) : (third as number);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function thirdMax($nums) {
        $first = null;
        $second = null;
        $third = null;

        foreach ($nums as $num) {
            if ($num === $first || $num === $second || $num === $third) {
                continue;
            }

            if ($first === null || $num > $first) {
                $third = $second;
                $second = $first;
                $first = $num;
            } elseif ($second === null || $num > $second) {
                $third = $second;
                $second = $num;
            } elseif ($third === null || $num > $third) {
                $third = $num;
            }
        }

        return $third === null ? $first : $third;
    }
}
```

## Swift

```swift
class Solution {
    func thirdMax(_ nums: [Int]) -> Int {
        var unique = Set<Int>()
        for num in nums {
            unique.insert(num)
        }
        let sorted = unique.sorted(by: >)
        return sorted.count >= 3 ? sorted[2] : sorted[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun thirdMax(nums: IntArray): Int {
        var first: Long? = null
        var second: Long? = null
        var third: Long? = null

        for (num in nums) {
            val v = num.toLong()
            if (v == first || v == second || v == third) continue
            if (first == null || v > first) {
                third = second
                second = first
                first = v
            } else if (second == null || v > second) {
                third = second
                second = v
            } else if (third == null || v > third) {
                third = v
            }
        }

        return (third ?: first)!!.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int thirdMax(List<int> nums) {
    int? firstMax;
    int? secondMax;
    int? thirdMax;

    for (var num in nums) {
      if (num == firstMax || num == secondMax || num == thirdMax) continue;

      if (firstMax == null || num > firstMax) {
        thirdMax = secondMax;
        secondMax = firstMax;
        firstMax = num;
      } else if (secondMax == null || num > secondMax) {
        thirdMax = secondMax;
        secondMax = num;
      } else if (thirdMax == null || num > thirdMax) {
        thirdMax = num;
      }
    }

    return thirdMax ?? firstMax!;
  }
}
```

## Golang

```go
package main

import "math"

func thirdMax(nums []int) int {
	var max1, max2, max3 int64 = math.MinInt64, math.MinInt64, math.MinInt64
	for _, n := range nums {
		val := int64(n)
		if val == max1 || val == max2 || val == max3 {
			continue
		}
		if val > max1 {
			max3 = max2
			max2 = max1
			max1 = val
		} else if val > max2 {
			max3 = max2
			max2 = val
		} else if val > max3 {
			max3 = val
		}
	}
	if max3 == math.MinInt64 {
		return int(max1)
	}
	return int(max3)
}
```

## Ruby

```ruby
def third_max(nums)
  first = second = third = nil
  nums.each do |num|
    next if num == first || num == second || num == third
    if first.nil? || num > first
      third = second
      second = first
      first = num
    elsif second.nil? || num > second
      third = second
      second = num
    elsif third.nil? || num > third
      third = num
    end
  end
  third.nil? ? first : third
end
```

## Scala

```scala
object Solution {
    def thirdMax(nums: Array[Int]): Int = {
        var first: Long = Long.MinValue
        var second: Long = Long.MinValue
        var third: Long = Long.MinValue

        for (num <- nums) {
            val n = num.toLong
            if (n == first || n == second || n == third) {
                // duplicate, ignore
            } else if (n > first) {
                third = second
                second = first
                first = n
            } else if (n > second) {
                third = second
                second = n
            } else if (n > third) {
                third = n
            }
        }

        if (third == Long.MinValue) first.toInt else third.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn third_max(nums: Vec<i32>) -> i32 {
        let mut first: i64 = i64::MIN;
        let mut second: i64 = i64::MIN;
        let mut third: i64 = i64::MIN;

        for &n in nums.iter() {
            let val = n as i64;
            if val == first || val == second || val == third {
                continue;
            }
            if val > first {
                third = second;
                second = first;
                first = val;
            } else if val > second {
                third = second;
                second = val;
            } else if val > third {
                third = val;
            }
        }

        if third == i64::MIN {
            first as i32
        } else {
            third as i32
        }
    }
}
```

## Racket

```racket
(define/contract (third-max nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (first #f) (second #f) (third #f))
    (if (null? lst)
        (if third third first)
        (let ((n (car lst)))
          (cond
            [(and first (= n first)) (loop (cdr lst) first second third)]
            [(and second (= n second)) (loop (cdr lst) first second third)]
            [(and third (= n third)) (loop (cdr lst) first second third)]
            [(or (not first) (> n first))
             (loop (cdr lst) n first second)]
            [(or (not second) (> n second))
             (loop (cdr lst) first n third)]
            [(or (not third) (> n third))
             (loop (cdr lst) first second n)]
            [else
             (loop (cdr lst) first second third)])))))
```

## Erlang

```erlang
-module(solution).
-export([third_max/1]).

-spec third_max(Nums :: [integer()]) -> integer().
third_max(Nums) ->
    {M1, M2, M3} = lists:foldl(fun update/2,
                               {undefined, undefined, undefined},
                               Nums),
    case M3 of
        undefined -> M1;
        _ -> M3
    end.

update(N, {M1, M2, M3}) ->
    case {M1, M2, M3} of
        {undefined, _, _} ->
            {N, undefined, undefined};
        _ when N =:= M1; N =:= M2; N =:= M3 ->
            {M1, M2, M3};
        _ when (M1 =:= undefined) orelse (N > M1) ->
            {N, M1, M2};
        _ when (M2 =:= undefined) orelse (N > M2) ->
            {M1, N, M2};
        _ when (M3 =:= undefined) orelse (N > M3) ->
            {M1, M2, N};
        _ ->
            {M1, M2, M3}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec third_max(nums :: [integer]) :: integer
  def third_max(nums) do
    {first, second, third} =
      Enum.reduce(nums, {nil, nil, nil}, fn x, {f, s, t} = acc ->
        cond do
          x == f or x == s or x == t ->
            acc

          f == nil or x > f ->
            {x, f, s}

          s == nil or x > s ->
            {f, x, s}

          t == nil or x > t ->
            {f, s, x}

          true ->
            acc
        end
      end)

    if third != nil, do: third, else: first
  end
end
```
