# 0674. Longest Continuous Increasing Subsequence

## Cpp

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.empty()) return 0;
        int ans = 0, anchor = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (i > 0 && nums[i - 1] >= nums[i]) {
                anchor = i;
            }
            ans = max(ans, i - anchor + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int ans = 0;
        int anchor = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i - 1] >= nums[i]) {
                anchor = i;
            }
            ans = Math.max(ans, i - anchor + 1);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = 1
        anchor = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        anchor = 0
        ans = 1
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
```

## C

```c
int findLengthOfLCIS(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int ans = 1;
    int anchor = 0;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i - 1] >= nums[i]) {
            anchor = i;
        }
        int len = i - anchor + 1;
        if (len > ans) ans = len;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int FindLengthOfLCIS(int[] nums) {
        if (nums == null || nums.Length == 0) return 0;
        int ans = 0;
        int anchor = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (i > 0 && nums[i] <= nums[i - 1]) {
                anchor = i;
            }
            ans = Math.Max(ans, i - anchor + 1);
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findLengthOfLCIS = function(nums) {
    if (nums.length === 0) return 0;
    let ans = 1, anchor = 0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i - 1] >= nums[i]) {
            anchor = i;
        }
        const len = i - anchor + 1;
        if (len > ans) ans = len;
    }
    return ans;
};
```

## Typescript

```typescript
function findLengthOfLCIS(nums: number[]): number {
    let ans = 0;
    let anchor = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i - 1] >= nums[i]) {
            anchor = i;
        }
        const len = i - anchor + 1;
        if (len > ans) ans = len;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findLengthOfLCIS($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        $anchor = 0;
        $ans = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i - 1] >= $nums[$i]) {
                $anchor = $i;
            }
            $len = $i - $anchor + 1;
            if ($len > $ans) {
                $ans = $len;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findLengthOfLCIS(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        var ans = 1
        var anchor = 0
        for i in 1..<nums.count {
            if nums[i - 1] >= nums[i] {
                anchor = i
            }
            let length = i - anchor + 1
            if length > ans {
                ans = length
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLengthOfLCIS(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        var ans = 1
        var anchor = 0
        for (i in 1 until nums.size) {
            if (nums[i - 1] >= nums[i]) {
                anchor = i
            }
            val length = i - anchor + 1
            if (length > ans) ans = length
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int findLengthOfLCIS(List<int> nums) {
    if (nums.isEmpty) return 0;
    int ans = 1;
    int anchor = 0;
    for (int i = 1; i < nums.length; ++i) {
      if (nums[i - 1] >= nums[i]) {
        anchor = i;
      }
      ans = max(ans, i - anchor + 1);
    }
    return ans;
  }
}
```

## Golang

```go
func findLengthOfLCIS(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	ans, anchor := 1, 0
	for i := 1; i < len(nums); i++ {
		if nums[i-1] >= nums[i] {
			anchor = i
		}
		if cur := i - anchor + 1; cur > ans {
			ans = cur
		}
	}
	return ans
}
```

## Ruby

```ruby
def find_length_of_lcis(nums)
  return 0 if nums.empty?
  anchor = 0
  ans = 1
  (1...nums.length).each do |i|
    anchor = i if nums[i] <= nums[i - 1]
    len = i - anchor + 1
    ans = len if len > ans
  end
  ans
end
```

## Scala

```scala
object Solution {
    def findLengthOfLCIS(nums: Array[Int]): Int = {
        if (nums.isEmpty) return 0
        var ans = 0
        var anchor = 0
        for (i <- nums.indices) {
            if (i > 0 && nums(i - 1) >= nums(i)) {
                anchor = i
            }
            val len = i - anchor + 1
            if (len > ans) ans = len
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_length_of_lcis(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut ans = 1i32;
        let mut anchor = 0usize;
        for i in 1..n {
            if nums[i - 1] >= nums[i] {
                anchor = i;
            }
            let len = (i - anchor + 1) as i32;
            if len > ans {
                ans = len;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-length-of-lcis nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (prev #f) (cur 0) (ans 0))
    (if (null? lst)
        ans
        (let* ((x (car lst))
               (new-cur (if (and (not (eq? prev #f)) (< prev x))
                            (+ cur 1)
                            1))
               (new-ans (max ans new-cur)))
          (loop (cdr lst) x new-cur new-ans)))))
```

## Erlang

```erlang
-spec find_length_of_lcis(Nums :: [integer()]) -> integer().
find_length_of_lcis([]) ->
    0;
find_length_of_lcis([H|T]) ->
    find_len(T, H, 1, 1).

-spec find_len(list(), integer(), integer(), integer()) -> integer().
find_len([], _Prev, _Curr, Max) ->
    Max;
find_len([X|Rest], Prev, Curr, Max) ->
    NewCurr = if X > Prev -> Curr + 1; true -> 1 end,
    NewMax = case NewCurr > Max of
                true -> NewCurr;
                false -> Max
             end,
    find_len(Rest, X, NewCurr, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_length_of_lcis(nums :: [integer]) :: integer
  def find_length_of_lcis([]), do: 0

  def find_length_of_lcis([head | tail]) do
    {max_len, _, _} =
      Enum.reduce(tail, {1, 1, head}, fn x, {max_len, cur_len, prev} ->
        if x > prev do
          new_cur = cur_len + 1
          {max(max_len, new_cur), new_cur, x}
        else
          {max_len, 1, x}
        end
      end)

    max_len
  end
end
```
