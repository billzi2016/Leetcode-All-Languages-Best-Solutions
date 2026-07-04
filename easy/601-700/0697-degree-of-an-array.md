# 0697. Degree of an Array

## Cpp

```cpp
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        const int MAXV = 50001;
        vector<int> left(MAXV, -1), right(MAXV, 0), cnt(MAXV, 0);
        int degree = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            int x = nums[i];
            if (left[x] == -1) left[x] = i;
            right[x] = i;
            cnt[x]++;
            if (cnt[x] > degree) degree = cnt[x];
        }
        int ans = nums.size();
        for (int v = 0; v < MAXV; ++v) {
            if (cnt[v] == degree) {
                ans = min(ans, right[v] - left[v] + 1);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findShortestSubArray(int[] nums) {
        java.util.Map<Integer, Integer> left = new java.util.HashMap<>();
        java.util.Map<Integer, Integer> right = new java.util.HashMap<>();
        java.util.Map<Integer, Integer> count = new java.util.HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            left.putIfAbsent(x, i);
            right.put(x, i);
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        int degree = 0;
        for (int v : count.values()) {
            if (v > degree) degree = v;
        }

        int ans = nums.length;
        for (java.util.Map.Entry<Integer, Integer> entry : count.entrySet()) {
            if (entry.getValue() == degree) {
                int x = entry.getKey();
                int len = right.get(x) - left.get(x) + 1;
                if (len < ans) ans = len;
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        degree = max(count.values())
        ans = len(nums)
        for x, c in count.items():
            if c == degree:
                length = right[x] - left[x] + 1
                if length < ans:
                    ans = length
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {}
        right = {}
        count = {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        degree = max(count.values())
        ans = len(nums)
        for x, c in count.items():
            if c == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans
```

## C

```c
int findShortestSubArray(int* nums, int numsSize) {
    const int MAXV = 50000;
    static int left[50000];
    static int right[50000];
    static int cnt[50000];

    for (int i = 0; i < MAXV; ++i) {
        left[i] = -1;
        cnt[i] = 0;
    }

    int degree = 0;
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        if (left[v] == -1) left[v] = i;
        right[v] = i;
        cnt[v]++;
        if (cnt[v] > degree) degree = cnt[v];
    }

    int ans = numsSize;
    for (int v = 0; v < MAXV; ++v) {
        if (cnt[v] == degree) {
            int len = right[v] - left[v] + 1;
            if (len < ans) ans = len;
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindShortestSubArray(int[] nums)
    {
        var left = new Dictionary<int, int>();
        var right = new Dictionary<int, int>();
        var count = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            int x = nums[i];
            if (!left.ContainsKey(x))
                left[x] = i;
            right[x] = i;

            if (count.ContainsKey(x))
                count[x]++;
            else
                count[x] = 1;
        }

        int degree = 0;
        foreach (var kvp in count)
            if (kvp.Value > degree)
                degree = kvp.Value;

        int ans = nums.Length;
        foreach (var kvp in count)
        {
            if (kvp.Value == degree)
            {
                int len = right[kvp.Key] - left[kvp.Key] + 1;
                if (len < ans)
                    ans = len;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
var findShortestSubArray = function(nums) {
    const left = {};
    const right = {};
    const count = {};

    for (let i = 0; i < nums.length; ++i) {
        const x = nums[i];
        if (!(x in left)) left[x] = i;
        right[x] = i;
        count[x] = (count[x] || 0) + 1;
    }

    let degree = 0;
    for (const k in count) {
        if (count[k] > degree) degree = count[k];
    }

    let ans = nums.length;
    for (const k in count) {
        if (count[k] === degree) {
            const len = right[k] - left[k] + 1;
            if (len < ans) ans = len;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function findShortestSubArray(nums: number[]): number {
    const left = new Map<number, number>();
    const right = new Map<number, number>();
    const cnt = new Map<number, number>();

    for (let i = 0; i < nums.length; ++i) {
        const x = nums[i];
        if (!left.has(x)) left.set(x, i);
        right.set(x, i);
        cnt.set(x, (cnt.get(x) ?? 0) + 1);
    }

    let degree = 0;
    for (const v of cnt.values()) {
        if (v > degree) degree = v;
    }

    let ans = nums.length;
    for (const [x, c] of cnt.entries()) {
        if (c === degree) {
            const len = right.get(x)! - left.get(x)! + 1;
            if (len < ans) ans = len;
        }
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
    function findShortestSubArray($nums) {
        $left = [];
        $right = [];
        $count = [];

        foreach ($nums as $i => $x) {
            if (!array_key_exists($x, $left)) {
                $left[$x] = $i;
            }
            $right[$x] = $i;
            if (isset($count[$x])) {
                $count[$x]++;
            } else {
                $count[$x] = 1;
            }
        }

        $degree = max($count);
        $ans = count($nums);

        foreach ($count as $x => $c) {
            if ($c == $degree) {
                $len = $right[$x] - $left[$x] + 1;
                if ($len < $ans) {
                    $ans = $len;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findShortestSubArray(_ nums: [Int]) -> Int {
        var left = [Int:Int]()
        var right = [Int:Int]()
        var count = [Int:Int]()
        
        for (i, x) in nums.enumerated() {
            if left[x] == nil {
                left[x] = i
            }
            right[x] = i
            count[x] = (count[x] ?? 0) + 1
        }
        
        guard let degree = count.values.max() else { return 0 }
        var ans = nums.count
        
        for (num, cnt) in count where cnt == degree {
            if let l = left[num], let r = right[num] {
                ans = min(ans, r - l + 1)
            }
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findShortestSubArray(nums: IntArray): Int {
        val left = HashMap<Int, Int>()
        val right = HashMap<Int, Int>()
        val count = HashMap<Int, Int>()
        for (i in nums.indices) {
            val x = nums[i]
            if (!left.containsKey(x)) {
                left[x] = i
            }
            right[x] = i
            count[x] = (count[x] ?: 0) + 1
        }
        var degree = 0
        for (v in count.values) {
            if (v > degree) degree = v
        }
        var ans = nums.size
        for ((num, cnt) in count) {
            if (cnt == degree) {
                val length = right[num]!! - left[num]!! + 1
                if (length < ans) ans = length
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int findShortestSubArray(List<int> nums) {
    final Map<int, int> left = {};
    final Map<int, int> right = {};
    final Map<int, int> count = {};

    for (int i = 0; i < nums.length; i++) {
      final int x = nums[i];
      if (!left.containsKey(x)) {
        left[x] = i;
      }
      right[x] = i;
      count[x] = (count[x] ?? 0) + 1;
    }

    int degree = 0;
    for (final c in count.values) {
      if (c > degree) degree = c;
    }

    int ans = nums.length;
    for (final entry in count.entries) {
      if (entry.value == degree) {
        final int len = right[entry.key]! - left[entry.key]! + 1;
        if (len < ans) ans = len;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func findShortestSubArray(nums []int) int {
    left := make(map[int]int)
    right := make(map[int]int)
    count := make(map[int]int)

    for i, x := range nums {
        if _, ok := left[x]; !ok {
            left[x] = i
        }
        right[x] = i
        count[x]++
    }

    degree := 0
    for _, c := range count {
        if c > degree {
            degree = c
        }
    }

    ans := len(nums)
    for x, c := range count {
        if c == degree {
            length := right[x] - left[x] + 1
            if length < ans {
                ans = length
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def find_shortest_sub_array(nums)
  left = {}
  right = {}
  count = Hash.new(0)

  nums.each_with_index do |x, i|
    left[x] ||= i
    right[x] = i
    count[x] += 1
  end

  degree = count.values.max
  ans = nums.length

  count.each do |x, c|
    if c == degree
      length = right[x] - left[x] + 1
      ans = length if length < ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def findShortestSubArray(nums: Array[Int]): Int = {
    val left = scala.collection.mutable.Map[Int, Int]()
    val right = scala.collection.mutable.Map[Int, Int]()
    val count = scala.collection.mutable.Map[Int, Int]()

    for ((x, i) <- nums.zipWithIndex) {
      if (!left.contains(x)) left(x) = i
      right(x) = i
      count(x) = count.getOrElse(x, 0) + 1
    }

    val degree = count.values.max
    var ans = nums.length

    for ((x, c) <- count) {
      if (c == degree) {
        val len = right(x) - left(x) + 1
        if (len < ans) ans = len
      }
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_shortest_sub_array(nums: Vec<i32>) -> i32 {
        const MAX_VAL: usize = 50000;
        let n = nums.len();
        let mut left = vec![usize::MAX; MAX_VAL + 1];
        let mut right = vec![0usize; MAX_VAL + 1];
        let mut count = vec![0i32; MAX_VAL + 1];

        for (i, &num) in nums.iter().enumerate() {
            let idx = num as usize;
            if left[idx] == usize::MAX {
                left[idx] = i;
            }
            right[idx] = i;
            count[idx] += 1;
        }

        let mut degree = 0i32;
        for &c in &count {
            if c > degree {
                degree = c;
            }
        }

        let mut ans = n as i32;
        for v in 0..=MAX_VAL {
            if count[v] == degree {
                let len = (right[v] - left[v] + 1) as i32;
                if len < ans {
                    ans = len;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
#lang racket

(provide find-shortest-sub-array)

(define/contract (find-shortest-sub-array nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((left (make-hash))
        (right (make-hash))
        (cnt (make-hash)))
    ;; record first index, last index and count for each value
    (for ([x nums] [i (in-naturals)])
      (unless (hash-has-key? left x)
        (hash-set! left x i))
      (hash-set! right x i)
      (hash-set! cnt x (+ 1 (hash-ref cnt x 0))))
    ;; degree of the whole array
    (define degree (apply max (hash-values cnt)))
    (define ans (length nums))
    ;; find minimal length among elements achieving the degree
    (for ([k (in-hash-keys cnt)])
      (when (= (hash-ref cnt k) degree)
        (let ((len (+ 1 (- (hash-ref right k) (hash-ref left k)))))
          (set! ans (min ans len)))))
    ans))
```

## Erlang

```erlang
-spec find_shortest_sub_array(Nums :: [integer()]) -> integer().
find_shortest_sub_array(Nums) ->
    {Left, Right, Count} = build_maps(Nums, 0, #{}, #{}, #{}),
    Degree = lists:max(maps:values(Count)),
    Len = length(Nums),
    MinLen = maps:fold(
        fun(Key, Cnt, Acc) ->
            if Cnt == Degree ->
                    L = maps:get(Key, Left),
                    R = maps:get(Key, Right),
                    Cand = R - L + 1,
                    case Cand < Acc of
                        true -> Cand;
                        false -> Acc
                    end;
               true -> Acc
            end
        end,
        Len,
        Count),
    MinLen.

build_maps([], _Idx, Left, Right, Count) ->
    {Left, Right, Count};
build_maps([X|Rest], Idx, Left, Right, Count) ->
    NewLeft = case maps:is_key(X, Left) of
                 true -> Left;
                 false -> maps:put(X, Idx, Left)
              end,
    NewRight = maps:put(X, Idx, Right),
    PrevCnt = maps:get(X, Count, 0),
    NewCount = maps:put(X, PrevCnt + 1, Count),
    build_maps(Rest, Idx + 1, NewLeft, NewRight, NewCount).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_shortest_sub_array(nums :: [integer]) :: integer
  def find_shortest_sub_array(nums) do
    {left, right, count} =
      Enum.reduce(Enum.with_index(nums), {%{}, %{}, %{}}, fn {x, i}, {l, r, c} ->
        l = if Map.has_key?(l, x), do: l, else: Map.put(l, x, i)
        r = Map.put(r, x, i)
        c = Map.update(c, x, 1, &(&1 + 1))
        {l, r, c}
      end)

    degree = count |> Map.values() |> Enum.max()

    Enum.reduce(count, length(nums), fn {x, cnt}, acc ->
      if cnt == degree do
        len = right[x] - left[x] + 1
        min(acc, len)
      else
        acc
      end
    end)
  end
end
```
