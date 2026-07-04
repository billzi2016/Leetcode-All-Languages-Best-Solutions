# 0268. Missing Number

## Cpp

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int missing = n;
        for (int i = 0; i < n; ++i) {
            missing ^= i ^ nums[i];
        }
        return missing;
    }
};
```

## Java

```java
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int xor = n;
        for (int i = 0; i < n; i++) {
            xor ^= i ^ nums[i];
        }
        return xor;
    }
}
```

## Python

```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        miss = n
        for i, num in enumerate(nums):
            miss ^= i ^ num
        return miss
```

## Python3

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        miss = n
        for i, num in enumerate(nums):
            miss ^= i ^ num
        return miss
```

## C

```c
int missingNumber(int* nums, int numsSize) {
    int result = numsSize;
    for (int i = 0; i < numsSize; ++i) {
        result ^= i ^ nums[i];
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MissingNumber(int[] nums) {
        int n = nums.Length;
        int missing = n; // include the number n in the xor
        for (int i = 0; i < n; i++) {
            missing ^= i ^ nums[i];
        }
        return missing;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const n = nums.length;
    let expectedSum = n * (n + 1) / 2;
    for (const num of nums) {
        expectedSum -= num;
    }
    return expectedSum;
};
```

## Typescript

```typescript
function missingNumber(nums: number[]): number {
    const n = nums.length;
    let missing = n;
    for (let i = 0; i < n; i++) {
        missing ^= i ^ nums[i];
    }
    return missing;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function missingNumber($nums) {
        $n = count($nums);
        $expected = $n * ($n + 1) / 2;
        $actual = 0;
        foreach ($nums as $num) {
            $actual += $num;
        }
        return $expected - $actual;
    }
}
```

## Swift

```swift
class Solution {
    func missingNumber(_ nums: [Int]) -> Int {
        var missing = nums.count
        for (i, num) in nums.enumerated() {
            missing ^= i ^ num
        }
        return missing
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun missingNumber(nums: IntArray): Int {
        var missing = nums.size
        for (i in nums.indices) {
            missing = missing xor i xor nums[i]
        }
        return missing
    }
}
```

## Dart

```dart
class Solution {
  int missingNumber(List<int> nums) {
    int n = nums.length;
    int total = n * (n + 1) ~/ 2;
    int sum = 0;
    for (int num in nums) {
      sum += num;
    }
    return total - sum;
  }
}
```

## Golang

```go
func missingNumber(nums []int) int {
    n := len(nums)
    miss := n
    for i, v := range nums {
        miss ^= i ^ v
    }
    return miss
}
```

## Ruby

```ruby
def missing_number(nums)
  n = nums.length
  missing = n
  nums.each_with_index do |num, i|
    missing ^= i ^ num
  end
  missing
end
```

## Scala

```scala
object Solution {
    def missingNumber(nums: Array[Int]): Int = {
        var result = nums.length
        var i = 0
        while (i < nums.length) {
            result ^= i ^ nums(i)
            i += 1
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut result = n; // include the extra number n in XOR
        for (i, &num) in nums.iter().enumerate() {
            result ^= i as i32 ^ num;
        }
        result
    }
}
```

## Racket

```racket
(define/contract (missing-number nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (xor-range
          (for/fold ([acc 0]) ([i (in-range 0 (+ n 1))])
            (bitwise-xor acc i)))
         (missing
          (for/fold ([acc xor-range]) ([x (in-list nums)])
            (bitwise-xor acc x))))
    missing))
```

## Erlang

```erlang
-spec missing_number(Nums :: [integer()]) -> integer().
missing_number(Nums) ->
    N = length(Nums),
    Expected = N * (N + 1) div 2,
    Actual = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Nums),
    Expected - Actual.
```

## Elixir

```elixir
defmodule Solution do
  @spec missing_number(nums :: [integer]) :: integer
  def missing_number(nums) do
    n = length(nums)
    expected_sum = div(n * (n + 1), 2)
    actual_sum = Enum.sum(nums)
    expected_sum - actual_sum
  end
end
```
