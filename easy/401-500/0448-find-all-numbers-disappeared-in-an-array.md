# 0448. Find All Numbers Disappeared in an Array

## Cpp

```cpp
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            int idx = abs(nums[i]) - 1;
            if (nums[idx] > 0) nums[idx] = -nums[idx];
        }
        vector<int> result;
        for (int i = 0; i < n; ++i) {
            if (nums[i] > 0) result.push_back(i + 1);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int idx = Math.abs(nums[i]) - 1;
            if (nums[idx] > 0) {
                nums[idx] = -nums[idx];
            }
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                result.add(i + 1);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        return [i + 1 for i, v in enumerate(nums) if v > 0]
```

## Python3

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        return res
```

## C

```c
#include <stdlib.h>

int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    for (int i = 0; i < numsSize; ++i) {
        int val = abs(nums[i]);
        int idx = val - 1;
        if (nums[idx] > 0)
            nums[idx] = -nums[idx];
    }
    
    int *result = (int *)malloc(numsSize * sizeof(int));
    int cnt = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > 0) {
            result[cnt++] = i + 1;
        }
    }
    
    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> FindDisappearedNumbers(int[] nums) {
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            int idx = Math.Abs(nums[i]) - 1;
            if (nums[idx] > 0) nums[idx] = -nums[idx];
        }
        List<int> result = new List<int>();
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) result.Add(i + 1);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const idx = Math.abs(nums[i]) - 1;
        if (nums[idx] > 0) {
            nums[idx] = -nums[idx];
        }
    }
    const result = [];
    for (let i = 0; i < n; i++) {
        if (nums[i] > 0) {
            result.push(i + 1);
        }
    }
    return result;
};
```

## Typescript

```typescript
function findDisappearedNumbers(nums: number[]): number[] {
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const idx = Math.abs(nums[i]) - 1;
        if (nums[idx] > 0) {
            nums[idx] = -nums[idx];
        }
    }
    const result: number[] = [];
    for (let i = 0; i < n; i++) {
        if (nums[i] > 0) {
            result.push(i + 1);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findDisappearedNumbers($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $idx = abs($nums[$i]) - 1;
            if ($nums[$idx] > 0) {
                $nums[$idx] = -$nums[$idx];
            }
        }

        $result = [];
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] > 0) {
                $result[] = $i + 1;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findDisappearedNumbers(_ nums: [Int]) -> [Int] {
        var arr = nums
        for i in 0..<arr.count {
            let idx = abs(arr[i]) - 1
            if arr[idx] > 0 {
                arr[idx] = -arr[idx]
            }
        }
        var result = [Int]()
        for i in 0..<arr.count where arr[i] > 0 {
            result.append(i + 1)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findDisappearedNumbers(nums: IntArray): List<Int> {
        for (i in nums.indices) {
            val idx = kotlin.math.abs(nums[i]) - 1
            if (nums[idx] > 0) {
                nums[idx] = -nums[idx]
            }
        }
        val result = mutableListOf<Int>()
        for (i in nums.indices) {
            if (nums[i] > 0) {
                result.add(i + 1)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findDisappearedNumbers(List<int> nums) {
    for (int i = 0; i < nums.length; i++) {
      int idx = nums[i].abs() - 1;
      if (nums[idx] > 0) {
        nums[idx] = -nums[idx];
      }
    }
    List<int> result = [];
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] > 0) {
        result.add(i + 1);
      }
    }
    return result;
  }
}
```

## Golang

```go
func findDisappearedNumbers(nums []int) []int {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	for _, v := range nums {
		idx := abs(v) - 1
		if nums[idx] > 0 {
			nums[idx] = -nums[idx]
		}
	}
	res := []int{}
	for i, v := range nums {
		if v > 0 {
			res = append(res, i+1)
		}
	}
	return res
}
```

## Ruby

```ruby
def find_disappeared_numbers(nums)
  nums.each do |num|
    idx = num.abs - 1
    nums[idx] = -nums[idx].abs if nums[idx] > 0
  end
  result = []
  nums.each_with_index do |num, i|
    result << i + 1 if num > 0
  end
  result
end
```

## Scala

```scala
object Solution {
    def findDisappearedNumbers(nums: Array[Int]): List[Int] = {
        val n = nums.length
        var i = 0
        while (i < n) {
            val idx = math.abs(nums(i)) - 1
            if (nums(idx) > 0) nums(idx) = -nums(idx)
            i += 1
        }
        val res = scala.collection.mutable.ListBuffer[Int]()
        var j = 0
        while (j < n) {
            if (nums(j) > 0) res += (j + 1)
            j += 1
        }
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_disappeared_numbers(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        for i in 0..n {
            let idx = (nums[i].abs() - 1) as usize;
            if nums[idx] > 0 {
                nums[idx] = -nums[idx];
            }
        }
        let mut result = Vec::new();
        for i in 0..n {
            if nums[i] > 0 {
                result.push((i + 1) as i32);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (find-disappeared-numbers nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (present (make-vector n #f)))
    (for-each (lambda (x) (vector-set! present (- x 1) #t)) nums)
    (let loop ((i 0) (acc '()))
      (if (= i n)
          (reverse acc)
          (loop (+ i 1)
                (if (not (vector-ref present i))
                    (cons (+ i 1) acc)
                    acc))))))
```

## Erlang

```erlang
-spec find_disappeared_numbers(Nums :: [integer()]) -> [integer()].
find_disappeared_numbers(Nums) ->
    Set = lists:foldl(fun(X, Acc) -> sets:add_element(X, Acc) end,
                      sets:new(),
                      Nums),
    N = length(Nums),
    [I || I <- lists:seq(1, N), not sets:is_element(I, Set)].
```

## Elixir

```elixir
defmodule Solution do
  @spec find_disappeared_numbers(nums :: [integer]) :: [integer]
  def find_disappeared_numbers(nums) do
    n = length(nums)

    present =
      Enum.reduce(nums, MapSet.new(), fn x, acc ->
        MapSet.put(acc, x)
      end)

    1..n
    |> Enum.filter(fn i -> not MapSet.member?(present, i) end)
    |> Enum.to_list()
  end
end
```
