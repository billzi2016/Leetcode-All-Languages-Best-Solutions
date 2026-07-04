# 0643. Maximum Average Subarray I

## Cpp

```cpp
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        long long window_sum = 0;
        for (int i = 0; i < k; ++i) {
            window_sum += nums[i];
        }
        long long max_sum = window_sum;
        for (int i = k; i < (int)nums.size(); ++i) {
            window_sum += nums[i] - nums[i - k];
            if (window_sum > max_sum) max_sum = window_sum;
        }
        return static_cast<double>(max_sum) / k;
    }
};
```

## Java

```java
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        long sum = 0;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        long maxSum = sum;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            if (sum > maxSum) {
                maxSum = sum;
            }
        }
        return (double) maxSum / k;
    }
}
```

## Python

```python
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum
        return max_sum / float(k)
```

## Python3

```python
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum
        return max_sum / k
```

## C

```c
double findMaxAverage(int* nums, int numsSize, int k) {
    long long sum = 0;
    for (int i = 0; i < k; ++i) {
        sum += nums[i];
    }
    long long maxSum = sum;
    for (int i = k; i < numsSize; ++i) {
        sum += nums[i];
        sum -= nums[i - k];
        if (sum > maxSum) {
            maxSum = sum;
        }
    }
    return (double)maxSum / k;
}
```

## Csharp

```csharp
public class Solution {
    public double FindMaxAverage(int[] nums, int k) {
        long windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }
        long maxSum = windowSum;
        for (int i = k; i < nums.Length; i++) {
            windowSum += nums[i] - nums[i - k];
            if (windowSum > maxSum) {
                maxSum = windowSum;
            }
        }
        return (double)maxSum / k;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let sum = 0;
    for (let i = 0; i < k; ++i) {
        sum += nums[i];
    }
    let maxSum = sum;
    for (let i = k; i < nums.length; ++i) {
        sum += nums[i] - nums[i - k];
        if (sum > maxSum) maxSum = sum;
    }
    return maxSum / k;
};
```

## Typescript

```typescript
function findMaxAverage(nums: number[], k: number): number {
    let sum = 0;
    for (let i = 0; i < k; i++) {
        sum += nums[i];
    }
    let maxSum = sum;
    for (let i = k; i < nums.length; i++) {
        sum += nums[i] - nums[i - k];
        if (sum > maxSum) {
            maxSum = sum;
        }
    }
    return maxSum / k;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Float
     */
    function findMaxAverage($nums, $k) {
        $n = count($nums);
        $sum = 0;
        for ($i = 0; $i < $k; $i++) {
            $sum += $nums[$i];
        }
        $maxSum = $sum;
        for ($i = $k; $i < $n; $i++) {
            $sum += $nums[$i] - $nums[$i - $k];
            if ($sum > $maxSum) {
                $maxSum = $sum;
            }
        }
        return $maxSum / $k;
    }
}
```

## Swift

```swift
class Solution {
    func findMaxAverage(_ nums: [Int], _ k: Int) -> Double {
        var windowSum: Int64 = 0
        for i in 0..<k {
            windowSum += Int64(nums[i])
        }
        var maxSum = windowSum
        let n = nums.count
        if k < n {
            for i in k..<n {
                windowSum += Int64(nums[i])
                windowSum -= Int64(nums[i - k])
                if windowSum > maxSum {
                    maxSum = windowSum
                }
            }
        }
        return Double(maxSum) / Double(k)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaxAverage(nums: IntArray, k: Int): Double {
        var sum = 0L
        for (i in 0 until k) {
            sum += nums[i].toLong()
        }
        var maxSum = sum
        for (i in k until nums.size) {
            sum += nums[i].toLong()
            sum -= nums[i - k].toLong()
            if (sum > maxSum) maxSum = sum
        }
        return maxSum.toDouble() / k
    }
}
```

## Dart

```dart
class Solution {
  double findMaxAverage(List<int> nums, int k) {
    int n = nums.length;
    int sum = 0;
    for (int i = 0; i < k; ++i) {
      sum += nums[i];
    }
    int maxSum = sum;
    for (int i = k; i < n; ++i) {
      sum += nums[i] - nums[i - k];
      if (sum > maxSum) {
        maxSum = sum;
      }
    }
    return maxSum / k;
  }
}
```

## Golang

```go
func findMaxAverage(nums []int, k int) float64 {
    n := len(nums)
    var sum int64
    for i := 0; i < k; i++ {
        sum += int64(nums[i])
    }
    maxSum := sum
    for i := k; i < n; i++ {
        sum += int64(nums[i]) - int64(nums[i-k])
        if sum > maxSum {
            maxSum = sum
        }
    }
    return float64(maxSum) / float64(k)
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Float}
def find_max_average(nums, k)
  sum = 0
  k.times { |i| sum += nums[i] }
  max_sum = sum

  (k...nums.length).each do |i|
    sum += nums[i]
    sum -= nums[i - k]
    max_sum = sum if sum > max_sum
  end

  max_sum.to_f / k
end
```

## Scala

```scala
object Solution {
    def findMaxAverage(nums: Array[Int], k: Int): Double = {
        var sum: Long = 0L
        for (i <- 0 until k) {
            sum += nums(i).toLong
        }
        var maxSum = sum
        var i = k
        while (i < nums.length) {
            sum += nums(i).toLong - nums(i - k).toLong
            if (sum > maxSum) maxSum = sum
            i += 1
        }
        maxSum.toDouble / k
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let n = nums.len();
        let k_usize = k as usize;
        let mut sum: i64 = 0;
        for i in 0..k_usize {
            sum += nums[i] as i64;
        }
        let mut max_sum = sum;
        for i in k_usize..n {
            sum += nums[i] as i64 - nums[i - k_usize] as i64;
            if sum > max_sum {
                max_sum = sum;
            }
        }
        max_sum as f64 / k as f64
    }
}
```

## Racket

```racket
(define/contract (find-max-average nums k)
  (-> (listof exact-integer?) exact-integer? flonum?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    ;; initial window sum
    (let loop-init ((i 0) (s 0))
      (if (= i k)
          (let loop-slide ((idx k) (curr s) (best s))
            (if (= idx n)
                (/ (exact->inexact best) (exact->inexact k))
                (let* ((out (vector-ref v (- idx k)))
                       (inn (vector-ref v idx))
                       (new-sum (+ (- curr out) inn))
                       (new-best (if (> new-sum best) new-sum best)))
                  (loop-slide (+ idx 1) new-sum new-best))))
          (loop-init (+ i 1) (+ s (vector-ref v i)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_max_average/2]).

-spec find_max_average(Nums :: [integer()], K :: integer()) -> float().
find_max_average(Nums, K) ->
    InitialWindow = lists:sublist(Nums, K),
    CurSum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, InitialWindow),
    MaxSum = CurSum,
    Start = Nums,
    End = lists:nthtail(K, Nums),
    Max = slide(Start, End, CurSum, MaxSum),
    Max / K.

slide(_Start, [], _CurSum, MaxSum) ->
    MaxSum;
slide(Start, End, CurSum, MaxSum) ->
    Leaving = hd(Start),
    Entering = hd(End),
    NewSum = CurSum - Leaving + Entering,
    NewMax = if NewSum > MaxSum -> NewSum; true -> MaxSum end,
    slide(tl(Start), tl(End), NewSum, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_max_average(nums :: [integer], k :: integer) :: float
  def find_max_average(nums, k) do
    {_, max_sum, _} =
      Enum.reduce(nums, {0.0, -1.0e100, :queue.new()}, fn x, {sum, max_sum, q} ->
        new_sum = sum + x
        q1 = :queue.in(x, q)

        if :queue.len(q1) > k do
          {{:value, old}, q2} = :queue.out(q1)
          new_sum2 = new_sum - old
          max_sum2 = if new_sum2 > max_sum, do: new_sum2, else: max_sum
          {new_sum2, max_sum2, q2}
        else
          max_sum2 = if :queue.len(q1) == k and new_sum > max_sum, do: new_sum, else: max_sum
          {new_sum, max_sum2, q1}
        end
      end)

    max_sum / k
  end
end
```
