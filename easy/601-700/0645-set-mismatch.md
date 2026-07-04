# 0645. Set Mismatch

## Cpp

```cpp
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int duplicate = -1, missing = -1;
        for (int i = 0; i < n; ++i) {
            int val = abs(nums[i]);
            if (nums[val - 1] < 0) {
                duplicate = val;
            } else {
                nums[val - 1] = -nums[val - 1];
            }
        }
        for (int i = 0; i < n; ++i) {
            if (nums[i] > 0) {
                missing = i + 1;
                break;
            }
        }
        return {duplicate, missing};
    }
};
```

## Java

```java
class Solution {
    public int[] findErrorNums(int[] nums) {
        int duplicate = -1;
        int missing = -1;
        for (int i = 0; i < nums.length; i++) {
            int idx = Math.abs(nums[i]) - 1;
            if (nums[idx] < 0) {
                duplicate = Math.abs(nums[i]);
            } else {
                nums[idx] = -nums[idx];
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                missing = i + 1;
                break;
            }
        }
        return new int[]{duplicate, missing};
    }
}
```

## Python

```python
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup = -1
        n = len(nums)
        for i in range(n):
            val = abs(nums[i])
            if nums[val - 1] < 0:
                dup = val
            else:
                nums[val - 1] *= -1

        missing = -1
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
                break

        return [dup, missing]
```

## Python3

```python
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        n = len(nums)
        for i in range(n):
            val = abs(nums[i])
            if nums[val - 1] < 0:
                dup = val
            else:
                nums[val - 1] *= -1
        miss = -1
        for i in range(n):
            if nums[i] > 0:
                miss = i + 1
                break
        return [dup, miss]
```

## C

```c
#include <stdlib.h>

int* findErrorNums(int* nums, int numsSize, int* returnSize) {
    *returnSize = 2;
    int* ans = (int*)malloc(2 * sizeof(int));
    int dup = -1, miss = -1;

    for (int i = 0; i < numsSize; ++i) {
        int val = abs(nums[i]);
        if (nums[val - 1] < 0) {
            dup = val;
        } else {
            nums[val - 1] = -nums[val - 1];
        }
    }

    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > 0) {
            miss = i + 1;
            break;
        }
    }

    ans[0] = dup;
    ans[1] = miss;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] FindErrorNums(int[] nums)
    {
        int duplicate = -1;
        for (int i = 0; i < nums.Length; i++)
        {
            int val = Math.Abs(nums[i]);
            int idx = val - 1;
            if (nums[idx] < 0)
                duplicate = val;
            else
                nums[idx] = -nums[idx];
        }

        int missing = -1;
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] > 0)
            {
                missing = i + 1;
                break;
            }
        }

        return new int[] { duplicate, missing };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    let duplicate = -1;
    for (let i = 0; i < nums.length; i++) {
        const val = Math.abs(nums[i]);
        const idx = val - 1;
        if (nums[idx] < 0) {
            duplicate = val;
        } else {
            nums[idx] = -nums[idx];
        }
    }
    let missing = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0) {
            missing = i + 1;
            break;
        }
    }
    return [duplicate, missing];
};
```

## Typescript

```typescript
function findErrorNums(nums: number[]): number[] {
    const n = nums.length;
    let dup = -1, miss = -1;
    for (let i = 0; i < n; i++) {
        const val = Math.abs(nums[i]);
        if (nums[val - 1] < 0) {
            dup = val;
        } else {
            nums[val - 1] = -nums[val - 1];
        }
    }
    for (let i = 0; i < n; i++) {
        if (nums[i] > 0) {
            miss = i + 1;
            break;
        }
    }
    return [dup, miss];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findErrorNums($nums) {
        $n = count($nums);
        $sum = array_sum($nums);
        $expectedSum = intdiv($n * ($n + 1), 2);
        $diff = $sum - $expectedSum; // duplicate - missing

        $sqSum = 0;
        foreach ($nums as $v) {
            $sqSum += $v * $v;
        }
        $expectedSq = intdiv($n * ($n + 1) * (2 * $n + 1), 6);
        $diffSq = $sqSum - $expectedSq; // duplicate^2 - missing^2

        $sumDupMiss = intdiv($diffSq, $diff); // duplicate + missing

        $duplicate = intdiv($diff + $sumDupMiss, 2);
        $missing = $sumDupMiss - $duplicate;

        return [$duplicate, $missing];
    }
}
```

## Swift

```swift
class Solution {
    func findErrorNums(_ nums: [Int]) -> [Int] {
        var seen = Set<Int>()
        var duplicate = 0
        var total = 0
        for num in nums {
            if seen.contains(num) {
                duplicate = num
            } else {
                seen.insert(num)
            }
            total += num
        }
        let n = nums.count
        let expectedSum = n * (n + 1) / 2
        let missing = expectedSum - (total - duplicate)
        return [duplicate, missing]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findErrorNums(nums: IntArray): IntArray {
        var duplicate = -1
        for (i in nums.indices) {
            val index = kotlin.math.abs(nums[i]) - 1
            if (nums[index] < 0) {
                duplicate = index + 1
            } else {
                nums[index] = -nums[index]
            }
        }
        var missing = -1
        for (i in nums.indices) {
            if (nums[i] > 0) {
                missing = i + 1
                break
            }
        }
        return intArrayOf(duplicate, missing)
    }
}
```

## Dart

```dart
class Solution {
  List<int> findErrorNums(List<int> nums) {
    int dup = -1;
    for (int i = 0; i < nums.length; i++) {
      int val = nums[i].abs();
      int idx = val - 1;
      if (nums[idx] < 0) {
        dup = val;
      } else {
        nums[idx] = -nums[idx];
      }
    }
    int missing = -1;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] > 0) {
        missing = i + 1;
        break;
      }
    }
    return [dup, missing];
  }
}
```

## Golang

```go
func findErrorNums(nums []int) []int {
    dup := -1
    n := len(nums)
    for i := 0; i < n; i++ {
        val := nums[i]
        if val < 0 {
            val = -val
        }
        idx := val - 1
        if nums[idx] < 0 {
            dup = val
        } else {
            nums[idx] = -nums[idx]
        }
    }
    missing := -1
    for i := 0; i < n; i++ {
        if nums[i] > 0 {
            missing = i + 1
            break
        }
    }
    return []int{dup, missing}
}
```

## Ruby

```ruby
def find_error_nums(nums)
  duplicate = nil
  nums.each do |num|
    idx = num.abs - 1
    if nums[idx] < 0
      duplicate = idx + 1
    else
      nums[idx] = -nums[idx]
    end
  end

  missing = nil
  nums.each_with_index do |val, i|
    if val > 0
      missing = i + 1
      break
    end
  end

  [duplicate, missing]
end
```

## Scala

```scala
object Solution {
    def findErrorNums(nums: Array[Int]): Array[Int] = {
        var dup = -1
        for (i <- nums.indices) {
            val v = Math.abs(nums(i))
            val idx = v - 1
            if (nums(idx) < 0) dup = v
            else nums(idx) = -nums(idx)
        }
        var missing = -1
        for (i <- nums.indices) {
            if (nums(i) > 0) missing = i + 1
        }
        Array(dup, missing)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len() as i32;
        let mut seen = vec![false; (n + 1) as usize];
        let mut duplicate = 0i32;

        for &num in &nums {
            let idx = num as usize;
            if seen[idx] {
                duplicate = num;
            } else {
                seen[idx] = true;
            }
        }

        let mut missing = 0i32;
        for i in 1..=n {
            if !seen[i as usize] {
                missing = i;
                break;
            }
        }

        vec![duplicate, missing]
    }
}
```

## Racket

```racket
(define/contract (find-error-nums nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (expected-sum (/ (* n (+ n 1)) 2))
         (expected-sumsq (/ (* n (+ n 1) (+ (* 2 n) 1)) 6))
         (s (foldl + 0 nums))
         (sq (foldl (lambda (x acc) (+ acc (* x x))) 0 nums))
         (diff (- s expected-sum))                ; duplicate - missing
         (diff2 (- sq expected-sumsq))            ; duplicate^2 - missing^2
         (sumdup-miss (quotient diff2 diff))     ; duplicate + missing
         (duplicate (quotient (+ diff sumdup-miss) 2))
         (missing (- duplicate diff)))
    (list duplicate missing)))
```

## Erlang

```erlang
-module(solution).
-export([find_error_nums/1]).

-spec find_error_nums(Nums :: [integer()]) -> [integer()].
find_error_nums(Nums) ->
    N = length(Nums),
    {Sum, Sq} = lists:foldl(
        fun(X, {AccS, AccQ}) -> {AccS + X, AccQ + X * X} end,
        {0, 0},
        Nums
    ),
    ExpectedSum = N * (N + 1) div 2,
    ExpectedSq = N * (N + 1) * (2 * N + 1) div 6,
    Diff = Sum - ExpectedSum,
    DiffSq = Sq - ExpectedSq,
    SumDupMiss = DiffSq div Diff,
    Duplicate = (Diff + SumDupMiss) div 2,
    Missing = SumDupMiss - Duplicate,
    [Duplicate, Missing].
```

## Elixir

```elixir
defmodule Solution do
  @spec find_error_nums(nums :: [integer]) :: [integer]
  def find_error_nums(nums) do
    n = length(nums)
    expected_sum = div(n * (n + 1), 2)
    sum_nums = Enum.reduce(nums, 0, &+/2)

    {duplicate, _} =
      Enum.reduce_while(nums, {nil, MapSet.new()}, fn x, {_dup, set} ->
        if MapSet.member?(set, x) do
          {:halt, {x, set}}
        else
          {:cont, {nil, MapSet.put(set, x)}}
        end
      end)

    diff = sum_nums - expected_sum
    missing = duplicate - diff
    [duplicate, missing]
  end
end
```
