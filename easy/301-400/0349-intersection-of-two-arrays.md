# 0349. Intersection of Two Arrays

## Cpp

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        vector<int> result;
        for (int x : nums2) {
            if (set1.erase(x)) {
                result.push_back(x);
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        java.util.HashSet<Integer> set = new java.util.HashSet<>();
        for (int num : nums1) {
            set.add(num);
        }
        java.util.HashSet<Integer> resultSet = new java.util.HashSet<>();
        for (int num : nums2) {
            if (set.contains(num)) {
                resultSet.add(num);
            }
        }
        int[] result = new int[resultSet.size()];
        int i = 0;
        for (int val : resultSet) {
            result[i++] = val;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
```

## Python3

```python
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    // Values are in the range [0, 1000]
    char present[1001] = {0};
    
    for (int i = 0; i < nums1Size; ++i) {
        present[nums1[i]] = 1;
    }
    
    int maxRes = nums1Size < nums2Size ? nums1Size : nums2Size;
    int *result = (int *)malloc(maxRes * sizeof(int));
    int idx = 0;
    
    for (int i = 0; i < nums2Size; ++i) {
        int val = nums2[i];
        if (present[val]) {
            result[idx++] = val;
            present[val] = 0; // ensure uniqueness in output
        }
    }
    
    *returnSize = idx;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] Intersection(int[] nums1, int[] nums2) {
        var set = new HashSet<int>(nums1);
        var result = new List<int>();
        foreach (var num in nums2) {
            if (set.Contains(num)) {
                result.Add(num);
                set.Remove(num); // ensure each element is added only once
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
var intersection = function(nums1, nums2) {
    const set1 = new Set(nums1);
    const set2 = new Set(nums2);
    const result = [];
    for (const val of set1) {
        if (set2.has(val)) {
            result.push(val);
        }
    }
    return result;
};
```

## Typescript

```typescript
function intersection(nums1: number[], nums2: number[]): number[] {
    const set = new Set<number>(nums1);
    const result: number[] = [];
    for (const num of nums2) {
        if (set.has(num)) {
            result.push(num);
            set.delete(num); // ensure uniqueness
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
    function intersection($nums1, $nums2) {
        // Build a hash set from the first array
        $set = [];
        foreach ($nums1 as $num) {
            $set[$num] = true;
        }

        $result = [];
        foreach ($nums2 as $num) {
            if (isset($set[$num])) {
                $result[] = $num;
                // Ensure each element appears only once in the result
                unset($set[$num]);
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func intersection(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        let set1 = Set(nums1)
        let set2 = Set(nums2)
        return Array(set1.intersection(set2))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        val set1 = HashSet<Int>()
        for (num in nums1) {
            set1.add(num)
        }
        val result = HashSet<Int>()
        for (num in nums2) {
            if (set1.contains(num)) {
                result.add(num)
            }
        }
        return result.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> intersection(List<int> nums1, List<int> nums2) {
    final set1 = nums1.toSet();
    final set2 = nums2.toSet();
    return set1.intersection(set2).toList();
  }
}
```

## Golang

```go
func intersection(nums1 []int, nums2 []int) []int {
    m := make(map[int]struct{})
    for _, v := range nums1 {
        m[v] = struct{}{}
    }
    var result []int
    for _, v := range nums2 {
        if _, ok := m[v]; ok {
            result = append(result, v)
            delete(m, v)
        }
    }
    return result
}
```

## Ruby

```ruby
def intersection(nums1, nums2)
  nums1 & nums2
end
```

## Scala

```scala
object Solution {
    def intersection(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
        val set1 = nums1.toSet
        val set2 = nums2.toSet
        (set1 intersect set2).toArray
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let set1: HashSet<i32> = nums1.into_iter().collect();
        let set2: HashSet<i32> = nums2.into_iter().collect();

        if set1.len() < set2.len() {
            set1.intersection(&set2).cloned().collect()
        } else {
            set2.intersection(&set1).cloned().collect()
        }
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (intersection nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ([set1 (list->set nums1)]
         [set2 (list->set nums2)])
    (set->list (set-intersect set1 set2))))
```

## Erlang

```erlang
-spec intersection(Nums1 :: [integer()], Nums2 :: [integer()]) -> [integer()].
intersection(Nums1, Nums2) ->
    Set1 = lists:foldl(fun(X, Acc) -> maps:put(X, true, Acc) end, #{}, Nums1),
    InterMap = lists:foldl(
        fun(X, Acc) ->
            case maps:is_key(X, Set1) of
                true  -> maps:put(X, true, Acc);
                false -> Acc
            end
        end,
        #{},
        Nums2),
    maps:keys(InterMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec intersection(nums1 :: [integer], nums2 :: [integer]) :: [integer]
  def intersection(nums1, nums2) do
    set1 = MapSet.new(nums1)
    set2 = MapSet.new(nums2)
    MapSet.to_list(MapSet.intersection(set1, set2))
  end
end
```
