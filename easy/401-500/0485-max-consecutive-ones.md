# 0485. Max Consecutive Ones

## Cpp

```cpp
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCount = 0, current = 0;
        for (int num : nums) {
            if (num == 1) {
                ++current;
                if (current > maxCount) maxCount = current;
            } else {
                current = 0;
            }
        }
        return maxCount;
    }
};
```

## Java

```java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0, current = 0;
        for (int num : nums) {
            if (num == 1) {
                current++;
            } else {
                if (current > max) {
                    max = current;
                }
                current = 0;
            }
        }
        return Math.max(max, current);
    }
}
```

## Python

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                if current > max_count:
                    max_count = current
            else:
                current = 0
        return max_count
```

## Python3

```python
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                if current > max_count:
                    max_count = current
            else:
                current = 0
        return max_count
```

## C

```c
int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int maxCount = 0;
    int current = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) {
            ++current;
            if (current > maxCount) {
                maxCount = current;
            }
        } else {
            current = 0;
        }
    }
    return maxCount;
}
```

## Csharp

```csharp
public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int max = 0, current = 0;
        foreach (int num in nums) {
            if (num == 1) {
                current++;
                if (current > max) max = current;
            } else {
                current = 0;
            }
        }
        return max;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let max = 0, cur = 0;
    for (const n of nums) {
        if (n === 1) {
            cur++;
            if (cur > max) max = cur;
        } else {
            cur = 0;
        }
    }
    return max;
};
```

## Typescript

```typescript
function findMaxConsecutiveOnes(nums: number[]): number {
    let maxCount = 0;
    let current = 0;
    for (const num of nums) {
        if (num === 1) {
            current++;
            if (current > maxCount) maxCount = current;
        } else {
            current = 0;
        }
    }
    return maxCount;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaxConsecutiveOnes($nums) {
        $max = 0;
        $curr = 0;
        foreach ($nums as $num) {
            if ($num == 1) {
                $curr++;
                if ($curr > $max) {
                    $max = $curr;
                }
            } else {
                $curr = 0;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func findMaxConsecutiveOnes(_ nums: [Int]) -> Int {
        var maxCount = 0
        var current = 0
        for num in nums {
            if num == 1 {
                current += 1
                if current > maxCount {
                    maxCount = current
                }
            } else {
                current = 0
            }
        }
        return maxCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaxConsecutiveOnes(nums: IntArray): Int {
        var maxCount = 0
        var current = 0
        for (num in nums) {
            if (num == 1) {
                current++
                if (current > maxCount) maxCount = current
            } else {
                current = 0
            }
        }
        return maxCount
    }
}
```

## Dart

```dart
class Solution {
  int findMaxConsecutiveOnes(List<int> nums) {
    int maxCount = 0;
    int current = 0;
    for (int num in nums) {
      if (num == 1) {
        current++;
        if (current > maxCount) {
          maxCount = current;
        }
      } else {
        current = 0;
      }
    }
    return maxCount;
  }
}
```

## Golang

```go
func findMaxConsecutiveOnes(nums []int) int {
    maxCount, cur := 0, 0
    for _, v := range nums {
        if v == 1 {
            cur++
            if cur > maxCount {
                maxCount = cur
            }
        } else {
            cur = 0
        }
    }
    return maxCount
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_max_consecutive_ones(nums)
  max_count = 0
  current = 0
  nums.each do |num|
    if num == 1
      current += 1
    else
      max_count = [max_count, current].max
      current = 0
    end
  end
  [max_count, current].max
end
```

## Scala

```scala
object Solution {
    def findMaxConsecutiveOnes(nums: Array[Int]): Int = {
        var maxCount = 0
        var current = 0
        for (n <- nums) {
            if (n == 1) {
                current += 1
                if (current > maxCount) maxCount = current
            } else {
                current = 0
            }
        }
        maxCount
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut max_cnt = 0;
        let mut cur_cnt = 0;
        for n in nums {
            if n == 1 {
                cur_cnt += 1;
                if cur_cnt > max_cnt {
                    max_cnt = cur_cnt;
                }
            } else {
                cur_cnt = 0;
            }
        }
        max_cnt
    }
}
```

## Racket

```racket
(define/contract (find-max-consecutive-ones nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (cur 0) (best 0))
    (cond
      [(null? lst) best]
      [else (if (= (car lst) 1)
                (let ([new-cur (+ cur 1)])
                  (loop (cdr lst) new-cur (max best new-cur)))
                (loop (cdr lst) 0 best))])))
```

## Erlang

```erlang
-spec find_max_consecutive_ones(Nums :: [integer()]) -> integer().
find_max_consecutive_ones(Nums) ->
    find_max_consecutive_ones(Nums, 0, 0).

find_max_consecutive_ones([], _Curr, Max) ->
    Max;
find_max_consecutive_ones([1|Rest], Curr, Max) ->
    NewCurr = Curr + 1,
    NewMax = erlang:max(NewCurr, Max),
    find_max_consecutive_ones(Rest, NewCurr, NewMax);
find_max_consecutive_ones([0|Rest], _Curr, Max) ->
    find_max_consecutive_ones(Rest, 0, Max).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_max_consecutive_ones(nums :: [integer]) :: integer
  def find_max_consecutive_ones(nums) do
    {max_len, _} =
      Enum.reduce(nums, {0, 0}, fn
        1, {max_acc, cur_acc} ->
          new_cur = cur_acc + 1
          {if(new_cur > max_acc, do: new_cur, else: max_acc), new_cur}

        0, {max_acc, _cur_acc} ->
          {max_acc, 0}
      end)

    max_len
  end
end
```
