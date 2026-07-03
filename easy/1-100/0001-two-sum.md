# 0001. Two Sum

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> idx;
        for (int i = 0; i < (int)nums.size(); ++i) {
            int complement = target - nums[i];
            auto it = idx.find(complement);
            if (it != idx.end()) {
                return {it->second, i};
            }
            idx[nums[i]] = i;
        }
        return {};
    }
};
```

## Java

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        return new int[0]; // Should never be reached as per problem constraints
    }
}
```

## Python

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
```

## Python3

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int cap = numsSize * 2;
    if (cap == 0) cap = 1;

    int *keys = (int*)malloc(sizeof(int) * cap);
    int *vals = (int*)malloc(sizeof(int) * cap);
    char *used = (char*)calloc(cap, sizeof(char));

    for (int i = 0; i < numsSize; ++i) {
        int complement = target - nums[i];
        int h = ((complement % cap) + cap) % cap;
        while (used[h]) {
            if (keys[h] == complement) {
                int *res = (int*)malloc(sizeof(int) * 2);
                res[0] = vals[h];
                res[1] = i;
                *returnSize = 2;
                free(keys);
                free(vals);
                free(used);
                return res;
            }
            h = (h + 1) % cap;
        }

        int key = nums[i];
        int idx = ((key % cap) + cap) % cap;
        while (used[idx]) {
            idx = (idx + 1) % cap;
        }
        used[idx] = 1;
        keys[idx] = key;
        vals[idx] = i;
    }

    *returnSize = 0;
    free(keys);
    free(vals);
    free(used);
    return NULL;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        var map = new System.Collections.Generic.Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++)
        {
            int complement = target - nums[i];
            if (map.TryGetValue(complement, out int index))
            {
                return new int[] { index, i };
            }
            // Store the first occurrence of each number
            if (!map.ContainsKey(nums[i]))
            {
                map[nums[i]] = i;
            }
        }
        // According to problem constraints, this line should never be reached.
        return new int[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }
        seen.set(nums[i], i);
    }
};
```

## Typescript

```typescript
function twoSum(nums: number[], target: number): number[] {
    const indexMap = new Map<number, number>();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (indexMap.has(complement)) {
            return [indexMap.get(complement)!, i];
        }
        indexMap.set(nums[i], i);
    }
    return [];
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $map = [];
        foreach ($nums as $i => $num) {
            $complement = $target - $num;
            if (array_key_exists($complement, $map)) {
                return [$map[$complement], $i];
            }
            $map[$num] = $i;
        }
        return [];
    }
}
?>
```

## Swift

```swift
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var indexMap = [Int: Int]()
        for (i, num) in nums.enumerated() {
            let complement = target - num
            if let j = indexMap[complement] {
                return [j, i]
            }
            indexMap[num] = i
        }
        return []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = HashMap<Int, Int>()
        for (i in nums.indices) {
            val complement = target - nums[i]
            if (map.containsKey(complement)) {
                return intArrayOf(map[complement]!!, i)
            }
            map[nums[i]] = i
        }
        return intArrayOf()
    }
}
```

## Dart

```dart
class Solution {
  List<int> twoSum(List<int> nums, int target) {
    final Map<int, int> indexMap = {};
    for (int i = 0; i < nums.length; i++) {
      int complement = target - nums[i];
      if (indexMap.containsKey(complement)) {
        return [indexMap[complement]!, i];
      }
      indexMap[nums[i]] = i;
    }
    return [];
  }
}
```

## Golang

```go
func twoSum(nums []int, target int) []int {
    m := make(map[int]int, len(nums))
    for i, num := range nums {
        if j, ok := m[target-num]; ok {
            return []int{j, i}
        }
        m[num] = i
    }
    return nil
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  index_map = {}
  nums.each_with_index do |num, i|
    complement = target - num
    if index_map.key?(complement)
      return [index_map[complement], i]
    end
    index_map[num] = i
  end
  []
end
```

## Scala

```scala
object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    val seen = scala.collection.mutable.HashMap[Int, Int]()
    for (i <- nums.indices) {
      val complement = target - nums(i)
      if (seen.contains(complement)) {
        return Array(seen(complement), i)
      }
      seen(nums(i)) = i
    }
    Array.emptyIntArray
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::with_capacity(nums.len());
        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&j) = map.get(&complement) {
                return vec![j as i32, i as i32];
            }
            map.insert(num, i);
        }
        Vec::new()
    }
}
```

## Racket

```racket
(define/contract (two-sum nums target)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let ((ht (make-hash)))
    (let loop ((lst nums) (idx 0))
      (if (null? lst)
          (error "No solution found")
          (let* ((val (car lst))
                 (comp (- target val)))
            (if (hash-has-key? ht comp)
                (list (hash-ref ht comp) idx)
                (begin
                  (hash-set! ht val idx)
                  (loop (cdr lst) (+ idx 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([two_sum/2]).

-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].
two_sum(Nums, Target) ->
    two_sum_loop(Nums, Target, 0, #{}).

two_sum_loop([], _Target, _Idx, _Map) ->
    [];
two_sum_loop([X|Rest], Target, Idx, Map) ->
    Complement = Target - X,
    case maps:find(Complement, Map) of
        {ok, CompIdx} -> [CompIdx, Idx];
        error ->
            NewMap = maps:put(X, Idx, Map),
            two_sum_loop(Rest, Target, Idx + 1, NewMap)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    Enum.reduce_while(Enum.with_index(nums), %{}, fn {num, idx}, map ->
      comp = target - num

      case Map.fetch(map, comp) do
        {:ok, comp_idx} -> {:halt, [comp_idx, idx]}
        :error -> {:cont, Map.put(map, num, idx)}
      end
    end)
  end
end
```
