# 0594. Longest Harmonious Subsequence

## Cpp

```cpp
class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> cnt;
        for (int x : nums) ++cnt[x];
        int ans = 0;
        for (const auto& p : cnt) {
            auto it = cnt.find(p.first + 1);
            if (it != cnt.end()) {
                ans = max(ans, p.second + it->second);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findLHS(int[] nums) {
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        int maxLen = 0;
        for (java.util.Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            int key = entry.getKey();
            if (freq.containsKey(key + 1)) {
                int len = entry.getValue() + freq.get(key + 1);
                if (len > maxLen) {
                    maxLen = len;
                }
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        freq = Counter(nums)
        ans = 0
        for x in freq:
            if x + 1 in freq:
                ans = max(ans, freq[x] + freq[x + 1])
        return ans
```

## Python3

```python
from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        for x in freq:
            if x + 1 in freq:
                ans = max(ans, freq[x] + freq[x + 1])
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int findLHS(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);

    int maxLen = 0;
    int prevVal = 0, prevCount = 0;
    int hasPrev = 0;

    for (int i = 0; i < numsSize;) {
        int val = nums[i];
        int cnt = 0;
        while (i + cnt < numsSize && nums[i + cnt] == val) cnt++;
        if (hasPrev && val == prevVal + 1) {
            int curLen = prevCount + cnt;
            if (curLen > maxLen) maxLen = curLen;
        }
        prevVal = val;
        prevCount = cnt;
        hasPrev = 1;
        i += cnt;
    }

    return maxLen;
}
```

## Csharp

```csharp
public class Solution {
    public int FindLHS(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (var num in nums) {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        int maxLen = 0;
        foreach (var kvp in freq) {
            int key = kvp.Key;
            if (freq.ContainsKey(key + 1)) {
                int len = kvp.Value + freq[key + 1];
                if (len > maxLen) maxLen = len;
            }
        }

        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function(nums) {
    const freq = new Map();
    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }
    let maxLen = 0;
    for (const [key, count] of freq.entries()) {
        if (freq.has(key + 1)) {
            const len = count + freq.get(key + 1);
            if (len > maxLen) maxLen = len;
        }
    }
    return maxLen;
};
```

## Typescript

```typescript
function findLHS(nums: number[]): number {
    const freq = new Map<number, number>();
    for (const n of nums) {
        freq.set(n, (freq.get(n) ?? 0) + 1);
    }
    let maxLen = 0;
    for (const [key, count] of freq.entries()) {
        const nextCount = freq.get(key + 1);
        if (nextCount !== undefined) {
            const len = count + nextCount;
            if (len > maxLen) maxLen = len;
        }
    }
    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findLHS($nums) {
        $freq = [];
        foreach ($nums as $num) {
            if (isset($freq[$num])) {
                $freq[$num]++;
            } else {
                $freq[$num] = 1;
            }
        }

        $maxLen = 0;
        foreach ($freq as $key => $count) {
            $nextKey = $key + 1;
            if (isset($freq[$nextKey])) {
                $len = $count + $freq[$nextKey];
                if ($len > $maxLen) {
                    $maxLen = $len;
                }
            }
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func findLHS(_ nums: [Int]) -> Int {
        var freq = [Int: Int]()
        for num in nums {
            freq[num, default: 0] += 1
        }
        var result = 0
        for (key, count) in freq {
            if let nextCount = freq[key + 1] {
                result = max(result, count + nextCount)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLHS(nums: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (num in nums) {
            freq[num] = (freq[num] ?: 0) + 1
        }
        var ans = 0
        for ((key, count) in freq) {
            val nextCount = freq[key + 1]
            if (nextCount != null) {
                ans = maxOf(ans, count + nextCount)
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int findLHS(List<int> nums) {
    final Map<int, int> freq = {};
    for (var v in nums) {
      freq[v] = (freq[v] ?? 0) + 1;
    }
    int ans = 0;
    freq.forEach((k, v) {
      if (freq.containsKey(k + 1)) {
        final combined = v + freq[k + 1]!;
        if (combined > ans) ans = combined;
      }
    });
    return ans;
  }
}
```

## Golang

```go
func findLHS(nums []int) int {
    freq := make(map[int]int)
    for _, v := range nums {
        freq[v]++
    }
    maxLen := 0
    for val, cnt := range freq {
        if c2, ok := freq[val+1]; ok {
            if cnt+c2 > maxLen {
                maxLen = cnt + c2
            }
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def find_lhs(nums)
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }
  max_len = 0
  freq.each do |val, cnt|
    if freq.key?(val + 1)
      cur = cnt + freq[val + 1]
      max_len = cur if cur > max_len
    end
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def findLHS(nums: Array[Int]): Int = {
        val freq = scala.collection.mutable.Map[Int, Int]()
        for (x <- nums) {
            freq(x) = freq.getOrElse(x, 0) + 1
        }
        var maxLen = 0
        for ((k, v) <- freq) {
            if (freq.contains(k + 1)) {
                val len = v + freq(k + 1)
                if (len > maxLen) maxLen = len
            }
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_lhs(nums: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut freq: HashMap<i32, usize> = HashMap::new();
        for v in nums {
            *freq.entry(v).or_insert(0) += 1;
        }
        let mut best = 0usize;
        for (&k, &cnt) in freq.iter() {
            if let Some(&next_cnt) = freq.get(&(k + 1)) {
                let total = cnt + next_cnt;
                if total > best {
                    best = total;
                }
            }
        }
        best as i32
    }
}
```

## Racket

```racket
(define/contract (find-lhs nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([freq (make-hash)])
    (for-each (lambda (x)
                (hash-set! freq x (+ 1 (hash-ref freq x 0))))
              nums)
    (let ([maxlen 0])
      (for ([k (in-hash-keys freq)])
        (define v (hash-ref freq k))
        (when (hash-has-key? freq (+ k 1))
          (define v2 (hash-ref freq (+ k 1)))
          (set! maxlen (max maxlen (+ v v2)))))
      maxlen)))
```

## Erlang

```erlang
-module(solution).
-export([find_lhs/1]).

-spec find_lhs(Nums :: [integer()]) -> integer().
find_lhs(Nums) ->
    Freq = build_freq(Nums, #{}),
    Lengths = [ maps:get(K, Freq) + maps:get(K+1, Freq)
                || K <- maps:keys(Freq), maps:is_key(K+1, Freq) ],
    case Lengths of
        [] -> 0;
        _  -> lists:max(Lengths)
    end.

build_freq([], Acc) ->
    Acc;
build_freq([H|T], Acc) ->
    NewAcc = case maps:is_key(H, Acc) of
        true  -> maps:update_with(H, fun(C) -> C + 1 end, Acc);
        false -> maps:put(H, 1, Acc)
    end,
    build_freq(T, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_lhs(nums :: [integer]) :: integer
  def find_lhs(nums) do
    freq =
      Enum.reduce(nums, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    Enum.reduce(freq, 0, fn {k, v}, max_len ->
      case Map.get(freq, k + 1) do
        nil -> max_len
        v2 -> max(max_len, v + v2)
      end
    end)
  end
end
```
