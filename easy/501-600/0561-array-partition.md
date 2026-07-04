# 0561. Array Partition

## Cpp

```cpp
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int sum = 0;
        for (int i = 0; i < nums.size(); i += 2) {
            sum += nums[i];
        }
        return sum;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        for (int i = 0; i < nums.length; i += 2) {
            sum += nums[i];
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])
```

## Python3

```python
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int arrayPairSum(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int sum = 0;
    for (int i = 0; i < numsSize; i += 2) {
        sum += nums[i];
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public int ArrayPairSum(int[] nums) {
        System.Array.Sort(nums);
        int sum = 0;
        for (int i = 0; i < nums.Length; i += 2) {
            sum += nums[i];
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    nums.sort((a, b) => a - b);
    let sum = 0;
    for (let i = 0; i < nums.length; i += 2) {
        sum += nums[i];
    }
    return sum;
};
```

## Typescript

```typescript
function arrayPairSum(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let sum = 0;
    for (let i = 0; i < nums.length; i += 2) {
        sum += nums[i];
    }
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function arrayPairSum($nums) {
        sort($nums, SORT_NUMERIC);
        $sum = 0;
        $len = count($nums);
        for ($i = 0; $i < $len; $i += 2) {
            $sum += $nums[$i];
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func arrayPairSum(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        var result = 0
        var i = 0
        while i < sorted.count {
            result += sorted[i]
            i += 2
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun arrayPairSum(nums: IntArray): Int {
        nums.sort()
        var sum = 0
        var i = 0
        while (i < nums.size) {
            sum += nums[i]
            i += 2
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int arrayPairSum(List<int> nums) {
    nums.sort();
    int sum = 0;
    for (int i = 0; i < nums.length; i += 2) {
      sum += nums[i];
    }
    return sum;
  }
}
```

## Golang

```go
package main

import "sort"

func arrayPairSum(nums []int) int {
	sort.Ints(nums)
	sum := 0
	for i := 0; i < len(nums); i += 2 {
		sum += nums[i]
	}
	return sum
}
```

## Ruby

```ruby
def array_pair_sum(nums)
  nums.sort!
  sum = 0
  i = 0
  while i < nums.length
    sum += nums[i]
    i += 2
  end
  sum
end
```

## Scala

```scala
object Solution {
    def arrayPairSum(nums: Array[Int]): Int = {
        java.util.Arrays.sort(nums)
        var sum = 0
        var i = 0
        while (i < nums.length) {
            sum += nums(i)
            i += 2
        }
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn array_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut sum = 0;
        for i in (0..nums.len()).step_by(2) {
            sum += nums[i];
        }
        sum
    }
}
```

## Racket

```racket
(define/contract (array-pair-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <))
         (len (length sorted)))
    (let loop ((i 0) (acc 0))
      (if (>= i len)
          acc
          (loop (+ i 2) (+ acc (list-ref sorted i)))))))
```

## Erlang

```erlang
-spec array_pair_sum(Nums :: [integer()]) -> integer().
array_pair_sum(Nums) ->
    Sorted = lists:sort(Nums),
    sum_even(Sorted, 0).

sum_even([], Acc) -> 
    Acc;
sum_even([_], Acc) -> 
    Acc;
sum_even([X,_Y|Rest], Acc) -> 
    sum_even(Rest, Acc + X).
```

## Elixir

```elixir
defmodule Solution do
  @spec array_pair_sum(nums :: [integer]) :: integer
  def array_pair_sum(nums) do
    nums
    |> Enum.sort()
    |> Enum.take_every(2)
    |> Enum.sum()
  end
end
```
