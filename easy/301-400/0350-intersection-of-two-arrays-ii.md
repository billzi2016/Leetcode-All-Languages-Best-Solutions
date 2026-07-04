# 0350. Intersection of Two Arrays II

## Cpp

```cpp
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        vector<int> res;
        int i = 0, j = 0;
        while (i < (int)nums1.size() && j < (int)nums2.size()) {
            if (nums1[i] == nums2[j]) {
                res.push_back(nums1[i]);
                ++i; ++j;
            } else if (nums1[i] < nums2[j]) {
                ++i;
            } else {
                ++j;
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        int[] count = new int[1001];
        for (int num : nums1) {
            count[num]++;
        }
        int[] temp = new int[Math.min(nums1.length, nums2.length)];
        int idx = 0;
        for (int num : nums2) {
            if (count[num] > 0) {
                temp[idx++] = num;
                count[num]--;
            }
        }
        return java.util.Arrays.copyOf(temp, idx);
    }
}
```

## Python

```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Ensure nums1 is the smaller array for less memory usage
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        count = {}
        for num in nums1:
            count[num] = count.get(num, 0) + 1

        result = []
        for num in nums2:
            if count.get(num, 0) > 0:
                result.append(num)
                count[num] -= 1
        return result
```

## Python3

```python
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Ensure we build the counter on the smaller array to save space.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        result = []
        for num in nums2:
            cnt = freq.get(num, 0)
            if cnt > 0:
                result.append(num)
                freq[num] = cnt - 1
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    const int MAX_VAL = 1000;
    int freq[MAX_VAL + 1];
    memset(freq, 0, sizeof(freq));
    
    for (int i = 0; i < nums1Size; ++i) {
        if (nums1[i] >= 0 && nums1[i] <= MAX_VAL)
            ++freq[nums1[i]];
    }
    
    int maxResSize = nums1Size < nums2Size ? nums1Size : nums2Size;
    int* result = (int*)malloc(sizeof(int) * maxResSize);
    if (!result) {
        *returnSize = 0;
        return NULL;
    }
    
    int idx = 0;
    for (int i = 0; i < nums2Size; ++i) {
        int val = nums2[i];
        if (val >= 0 && val <= MAX_VAL && freq[val] > 0) {
            result[idx++] = val;
            --freq[val];
        }
    }
    
    *returnSize = idx;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] Intersect(int[] nums1, int[] nums2)
    {
        // Ensure we iterate over the smaller array for building the frequency map
        if (nums1.Length > nums2.Length)
        {
            var temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        var freq = new Dictionary<int, int>();
        foreach (var num in nums1)
        {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        var result = new List<int>();
        foreach (var num in nums2)
        {
            if (freq.TryGetValue(num, out int count) && count > 0)
            {
                result.Add(num);
                freq[num] = count - 1;
            }
        }

        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    if (nums1.length > nums2.length) return intersect(nums2, nums1);
    const count = new Map();
    for (const n of nums1) {
        count.set(n, (count.get(n) || 0) + 1);
    }
    const result = [];
    for (const n of nums2) {
        const c = count.get(n);
        if (c > 0) {
            result.push(n);
            if (c === 1) count.delete(n);
            else count.set(n, c - 1);
        }
    }
    return result;
};
```

## Typescript

```typescript
function intersect(nums1: number[], nums2: number[]): number[] {
    if (nums1.length > nums2.length) return intersect(nums2, nums1);
    const count = new Map<number, number>();
    for (const n of nums1) {
        count.set(n, (count.get(n) ?? 0) + 1);
    }
    const result: number[] = [];
    for (const n of nums2) {
        const c = count.get(n);
        if (c && c > 0) {
            result.push(n);
            if (c === 1) count.delete(n);
            else count.set(n, c - 1);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function intersect($nums1, $nums2) {
        // Ensure we iterate over the smaller array for counting
        if (count($nums1) > count($nums2)) {
            $tmp = $nums1;
            $nums1 = $nums2;
            $nums2 = $tmp;
        }

        $counts = [];
        foreach ($nums1 as $num) {
            if (!isset($counts[$num])) {
                $counts[$num] = 0;
            }
            $counts[$num]++;
        }

        $result = [];
        foreach ($nums2 as $num) {
            if (isset($counts[$num]) && $counts[$num] > 0) {
                $result[] = $num;
                $counts[$num]--;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func intersect(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var counts = [Int: Int]()
        let (small, large) = nums1.count < nums2.count ? (nums1, nums2) : (nums2, nums1)
        for num in small {
            counts[num, default: 0] += 1
        }
        var result = [Int]()
        for num in large {
            if let c = counts[num], c > 0 {
                result.append(num)
                counts[num] = c - 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun intersect(nums1: IntArray, nums2: IntArray): IntArray {
        val count = IntArray(1001)
        for (num in nums1) {
            count[num]++
        }
        val result = mutableListOf<Int>()
        for (num in nums2) {
            if (count[num] > 0) {
                result.add(num)
                count[num]--
            }
        }
        return result.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> intersect(List<int> nums1, List<int> nums2) {
    if (nums1.length > nums2.length) {
      return intersect(nums2, nums1);
    }
    final Map<int, int> counts = {};
    for (final num in nums1) {
      counts[num] = (counts[num] ?? 0) + 1;
    }
    final List<int> result = [];
    for (final num in nums2) {
      final cnt = counts[num];
      if (cnt != null && cnt > 0) {
        result.add(num);
        if (cnt == 1) {
          counts.remove(num);
        } else {
          counts[num] = cnt - 1;
        }
      }
    }
    return result;
  }
}
```

## Golang

```go
func intersect(nums1 []int, nums2 []int) []int {
	counts := make([]int, 1001)
	for _, v := range nums1 {
		counts[v]++
	}
	result := make([]int, 0)
	for _, v := range nums2 {
		if counts[v] > 0 {
			result = append(result, v)
			counts[v]--
		}
	}
	return result
}
```

## Ruby

```ruby
def intersect(nums1, nums2)
  counts = Hash.new(0)
  nums1.each { |num| counts[num] += 1 }
  result = []
  nums2.each do |num|
    if counts[num] > 0
      result << num
      counts[num] -= 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def intersect(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
        val a = nums1.sorted
        val b = nums2.sorted
        var i = 0
        var j = 0
        val res = scala.collection.mutable.ArrayBuffer[Int]()
        while (i < a.length && j < b.length) {
            if (a(i) == b(j)) {
                res += a(i)
                i += 1
                j += 1
            } else if (a(i) < b(j)) {
                i += 1
            } else {
                j += 1
            }
        }
        res.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn intersect(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> Vec<i32> {
        nums1.sort_unstable();
        nums2.sort_unstable();
        let (mut i, mut j) = (0usize, 0usize);
        let mut res = Vec::new();
        while i < nums1.len() && j < nums2.len() {
            if nums1[i] == nums2[j] {
                res.push(nums1[i]);
                i += 1;
                j += 1;
            } else if nums1[i] < nums2[j] {
                i += 1;
            } else {
                j += 1;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (intersect nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((counts (make-vector 1001 0))
         (result '()))
    (for ([x nums1])
      (vector-set! counts x (+ (vector-ref counts x) 1)))
    (for ([y nums2])
      (when (> (vector-ref counts y) 0)
        (set! result (cons y result))
        (vector-set! counts y (- (vector-ref counts y) 1))))
    (reverse result)))
```

## Erlang

```erlang
-module(solution).
-export([intersect/2]).

-spec intersect(Nums1 :: [integer()], Nums2 :: [integer()]) -> [integer()].
intersect(Nums1, Nums2) ->
    Sorted1 = lists:sort(Nums1),
    Sorted2 = lists:sort(Nums2),
    intersect_sorted(Sorted1, Sorted2).

-spec intersect_sorted([integer()], [integer()]) -> [integer()].
intersect_sorted([], _) -> [];
intersect_sorted(_, []) -> [];
intersect_sorted([H1|T1]=L1, [H2|T2]=L2) ->
    if
        H1 =:= H2 -> [H1 | intersect_sorted(T1, T2)];
        H1 < H2  -> intersect_sorted(T1, L2);
        true     -> intersect_sorted(L1, T2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec intersect(nums1 :: [integer], nums2 :: [integer]) :: [integer]
  def intersect(nums1, nums2) do
    {small, large} =
      if length(nums1) <= length(nums2), do: {nums1, nums2}, else: {nums2, nums1}

    freq =
      Enum.reduce(small, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    {result, _} =
      Enum.reduce(large, {[], freq}, fn x, {res, map} ->
        case Map.get(map, x) do
          nil -> {res, map}
          count when count > 0 ->
            new_map = Map.put(map, x, count - 1)
            {[x | res], new_map}
        end
      end)

    Enum.reverse(result)
  end
end
```
