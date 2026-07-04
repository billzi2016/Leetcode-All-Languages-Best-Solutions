# 0496. Next Greater Element I

## Cpp

```cpp
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> nxt;
        stack<int> st;
        for (int x : nums2) {
            while (!st.empty() && x > st.top()) {
                nxt[st.top()] = x;
                st.pop();
            }
            st.push(x);
        }
        while (!st.empty()) {
            nxt[st.top()] = -1;
            st.pop();
        }
        vector<int> ans;
        ans.reserve(nums1.size());
        for (int v : nums1) {
            ans.push_back(nxt[v]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        java.util.Map<Integer, Integer> nextGreaterMap = new java.util.HashMap<>();
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();

        for (int num : nums2) {
            while (!stack.isEmpty() && num > stack.peek()) {
                nextGreaterMap.put(stack.pop(), num);
            }
            stack.push(num);
        }

        // Remaining elements have no greater element
        while (!stack.isEmpty()) {
            nextGreaterMap.put(stack.pop(), -1);
        }

        int[] result = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            result[i] = nextGreaterMap.getOrDefault(nums1[i], -1);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nxt = {}
        stack = []
        for x in nums2:
            while stack and x > stack[-1]:
                prev = stack.pop()
                nxt[prev] = x
            stack.append(x)
        while stack:
            nxt[stack.pop()] = -1
        return [nxt[x] for x in nums1]
```

## Python3

```python
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nxt = {}
        for x in nums2:
            while stack and x > stack[-1]:
                prev = stack.pop()
                nxt[prev] = x
            stack.append(x)
        return [nxt.get(num, -1) for num in nums1]
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nextGreaterElement(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    // Maximum possible value according to constraints
    const int MAX_VAL = 10000;
    int *next = (int *)malloc((MAX_VAL + 1) * sizeof(int));
    for (int i = 0; i <= MAX_VAL; ++i) next[i] = -1;

    // Monotonic decreasing stack
    int *stack = (int *)malloc(nums2Size * sizeof(int));
    int top = -1;
    for (int i = 0; i < nums2Size; ++i) {
        int cur = nums2[i];
        while (top >= 0 && cur > stack[top]) {
            int val = stack[top--];
            next[val] = cur;
        }
        stack[++top] = cur;
    }

    free(stack);

    int *ans = (int *)malloc(nums1Size * sizeof(int));
    for (int i = 0; i < nums1Size; ++i) {
        ans[i] = next[nums1[i]];
    }

    free(next);
    *returnSize = nums1Size;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] NextGreaterElement(int[] nums1, int[] nums2) {
        var nextGreater = new Dictionary<int, int>();
        var stack = new Stack<int>();

        foreach (var num in nums2) {
            while (stack.Count > 0 && num > stack.Peek()) {
                int smaller = stack.Pop();
                nextGreater[smaller] = num;
            }
            stack.Push(num);
        }

        // Remaining elements have no greater element
        while (stack.Count > 0) {
            int remaining = stack.Pop();
            nextGreater[remaining] = -1;
        }

        var result = new int[nums1.Length];
        for (int i = 0; i < nums1.Length; i++) {
            result[i] = nextGreater[nums1[i]];
        }
        return result;
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
var nextGreaterElement = function(nums1, nums2) {
    const nge = new Map();
    const stack = [];
    for (const num of nums2) {
        while (stack.length && num > stack[stack.length - 1]) {
            const prev = stack.pop();
            nge.set(prev, num);
        }
        stack.push(num);
    }
    while (stack.length) {
        const val = stack.pop();
        nge.set(val, -1);
    }
    return nums1.map(v => nge.get(v));
};
```

## Typescript

```typescript
function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    const next = new Map<number, number>();
    const stack: number[] = [];
    for (const x of nums2) {
        while (stack.length && stack[stack.length - 1] < x) {
            const prev = stack.pop()!;
            next.set(prev, x);
        }
        stack.push(x);
    }
    while (stack.length) {
        const v = stack.pop()!;
        next.set(v, -1);
    }
    return nums1.map(v => next.get(v)!);
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
    function nextGreaterElement($nums1, $nums2) {
        $next = [];
        $stack = [];

        foreach ($nums2 as $num) {
            while (!empty($stack) && end($stack) < $num) {
                $prev = array_pop($stack);
                $next[$prev] = $num;
            }
            $stack[] = $num;
        }

        foreach ($stack as $rem) {
            $next[$rem] = -1;
        }

        $result = [];
        foreach ($nums1 as $val) {
            $result[] = $next[$val];
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func nextGreaterElement(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var nextMap = [Int: Int]()
        var stack = [Int]()
        
        for val in nums2 {
            while let last = stack.last, val > last {
                stack.removeLast()
                nextMap[last] = val
            }
            stack.append(val)
        }
        
        var result = [Int]()
        for num in nums1 {
            if let ng = nextMap[num] {
                result.append(ng)
            } else {
                result.append(-1)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
        val nextMap = HashMap<Int, Int>()
        val stack = java.util.ArrayDeque<Int>()

        for (num in nums2) {
            while (!stack.isEmpty() && num > stack.peek()) {
                val prev = stack.pop()
                nextMap[prev] = num
            }
            stack.push(num)
        }

        while (!stack.isEmpty()) {
            nextMap[stack.pop()] = -1
        }

        return IntArray(nums1.size) { idx -> nextMap.getOrDefault(nums1[idx], -1) }
    }
}
```

## Dart

```dart
class Solution {
  List<int> nextGreaterElement(List<int> nums1, List<int> nums2) {
    final Map<int, int> next = {};
    final List<int> stack = [];

    for (final int num in nums2) {
      while (stack.isNotEmpty && num > stack.last) {
        next[stack.removeLast()] = num;
      }
      stack.add(num);
    }

    return List<int>.generate(
      nums1.length,
      (i) => next[nums1[i]] ?? -1,
    );
  }
}
```

## Golang

```go
func nextGreaterElement(nums1 []int, nums2 []int) []int {
	// Map each element in nums2 to its next greater element.
	nge := make(map[int]int)
	stack := []int{}

	for _, v := range nums2 {
		// Resolve elements smaller than current value.
		for len(stack) > 0 && v > stack[len(stack)-1] {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			nge[top] = v
		}
		stack = append(stack, v)
	}

	// Build result for nums1 using the map.
	res := make([]int, len(nums1))
	for i, v := range nums1 {
		if val, ok := nge[v]; ok {
			res[i] = val
		} else {
			res[i] = -1
		}
	}
	return res
}
```

## Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def next_greater_element(nums1, nums2)
  next_greater = {}
  stack = []
  nums2.each do |num|
    while !stack.empty? && num > stack[-1]
      prev = stack.pop
      next_greater[prev] = num
    end
    stack << num
  end
  while !stack.empty?
    prev = stack.pop
    next_greater[prev] = -1
  end
  nums1.map { |x| next_greater[x] }
end
```

## Scala

```scala
object Solution {
    def nextGreaterElement(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
        import scala.collection.mutable
        val next = mutable.Map[Int, Int]()
        val stack = mutable.Stack[Int]()
        for (num <- nums2) {
            while (stack.nonEmpty && num > stack.top) {
                val prev = stack.pop()
                next(prev) = num
            }
            stack.push(num)
        }
        while (stack.nonEmpty) {
            val v = stack.pop()
            next(v) = -1
        }
        nums1.map(x => next.getOrElse(x, -1))
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut next_map: HashMap<i32, i32> = HashMap::new();
        let mut stack: Vec<i32> = Vec::new();

        for &val in nums2.iter() {
            while let Some(&top) = stack.last() {
                if val > top {
                    stack.pop();
                    next_map.insert(top, val);
                } else {
                    break;
                }
            }
            stack.push(val);
        }

        nums1
            .iter()
            .map(|&x| *next_map.get(&x).unwrap_or(&-1))
            .collect()
    }
}
```

## Racket

```racket
(define/contract (next-greater-element nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let ((next (make-hash)))
    (let ((stack '()))
      (for ([x nums2])
        (let loop ()
          (when (and (pair? stack) (> x (car stack)))
            (hash-set! next (car stack) x)
            (set! stack (cdr stack))
            (loop)))
        (set! stack (cons x stack)))
      (for ([v stack])
        (hash-set! next v -1))
      (map (lambda (v) (hash-ref next v)) nums1))))
```

## Erlang

```erlang
-module(solution).
-export([next_greater_element/2]).

-spec next_greater_element(Nums1 :: [integer()], Nums2 :: [integer()]) -> [integer()].
next_greater_element(Nums1, Nums2) ->
    Map = build_map(Nums2),
    [maps:get(N, Map) || N <- Nums1].

build_map(List) ->
    process(List, [], #{}).

process([], Stack, Map) ->
    lists:foldl(fun(X, Acc) -> maps:put(X, -1, Acc) end, Map, Stack);
process([H|T], Stack, Map) ->
    {NewStack, NewMap} = pop_and_set(H, Stack, Map),
    process(T, [H|NewStack], NewMap).

pop_and_set(_Cur, [], Map) ->
    {[], Map};
pop_and_set(Cur, [Top|Rest]=Stack, Map) when Cur > Top ->
    UpdatedMap = maps:put(Top, Cur, Map),
    pop_and_set(Cur, Rest, UpdatedMap);
pop_and_set(_Cur, Stack, Map) ->
    {Stack, Map}.
```

## Elixir

```elixir
defmodule Solution do
  @spec next_greater_element(nums1 :: [integer], nums2 :: [integer]) :: [integer]
  def next_greater_element(nums1, nums2) do
    {stack, map} =
      Enum.reduce(nums2, {[], %{}}, fn cur, {stk, mp} ->
        {new_stk, new_mp} = pop_and_set(cur, stk, mp)
        {[cur | new_stk], new_mp}
      end)

    final_map = Enum.reduce(stack, map, fn val, acc -> Map.put(acc, val, -1) end)

    Enum.map(nums1, fn x -> Map.get(final_map, x, -1) end)
  end

  defp pop_and_set(_cur, [], mp), do: {[], mp}
  defp pop_and_set(cur, [top | rest] = stk, mp) when cur > top do
    pop_and_set(cur, rest, Map.put(mp, top, cur))
  end
  defp pop_and_set(_cur, stk, mp), do: {stk, mp}
end
```
