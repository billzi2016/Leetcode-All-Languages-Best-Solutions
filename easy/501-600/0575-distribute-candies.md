# 0575. Distribute Candies

## Cpp

```cpp
class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_set<int> types;
        for (int c : candyType) types.insert(c);
        return min((int)types.size(), (int)candyType.size() / 2);
    }
};
```

## Java

```java
class Solution {
    public int distributeCandies(int[] candyType) {
        java.util.HashSet<Integer> set = new java.util.HashSet<>();
        for (int type : candyType) {
            set.add(type);
        }
        return Math.min(set.size(), candyType.length / 2);
    }
}
```

## Python

```python
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        distinct = len(set(candyType))
        return min(distinct, len(candyType) // 2)
```

## Python3

```python
from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        distinct = len(set(candyType))
        limit = len(candyType) // 2
        return distinct if distinct < limit else limit
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    return (ia > ib) - (ia < ib);
}

int distributeCandies(int* candyType, int candyTypeSize) {
    if (candyTypeSize == 0) return 0;
    qsort(candyType, candyTypeSize, sizeof(int), cmp_int);
    
    int distinct = 1;
    for (int i = 1; i < candyTypeSize; ++i) {
        if (candyType[i] != candyType[i - 1]) {
            ++distinct;
        }
    }
    
    int limit = candyTypeSize / 2;
    return distinct < limit ? distinct : limit;
}
```

## Csharp

```csharp
public class Solution
{
    public int DistributeCandies(int[] candyType)
    {
        var set = new System.Collections.Generic.HashSet<int>();
        foreach (int type in candyType)
        {
            set.Add(type);
        }
        int distinct = set.Count;
        int limit = candyType.Length / 2;
        return distinct < limit ? distinct : limit;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    const unique = new Set();
    for (const c of candyType) {
        unique.add(c);
    }
    return Math.min(unique.size, candyType.length / 2);
};
```

## Typescript

```typescript
function distributeCandies(candyType: number[]): number {
    const types = new Set<number>();
    for (const c of candyType) {
        types.add(c);
    }
    return Math.min(types.size, candyType.length / 2);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $candyType
     * @return Integer
     */
    function distributeCandies($candyType) {
        $unique = [];
        foreach ($candyType as $type) {
            $unique[$type] = true;
        }
        $distinct = count($unique);
        $limit = intdiv(count($candyType), 2);
        return min($distinct, $limit);
    }
}
```

## Swift

```swift
class Solution {
    func distributeCandies(_ candyType: [Int]) -> Int {
        let uniqueTypes = Set(candyType)
        return min(uniqueTypes.count, candyType.count / 2)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distributeCandies(candyType: IntArray): Int {
        val distinct = mutableSetOf<Int>()
        for (c in candyType) {
            distinct.add(c)
        }
        return minOf(distinct.size, candyType.size / 2)
    }
}
```

## Dart

```dart
class Solution {
  int distributeCandies(List<int> candyType) {
    final distinct = <int>{};
    for (var type in candyType) {
      distinct.add(type);
    }
    return distinct.length < candyType.length ~/ 2
        ? distinct.length
        : candyType.length ~/ 2;
  }
}
```

## Golang

```go
func distributeCandies(candyType []int) int {
    unique := make(map[int]struct{})
    for _, c := range candyType {
        unique[c] = struct{}{}
    }
    maxEat := len(candyType) / 2
    if len(unique) < maxEat {
        return len(unique)
    }
    return maxEat
}
```

## Ruby

```ruby
require 'set'

# @param {Integer[]} candy_type
# @return {Integer}
def distribute_candies(candy_type)
  distinct = Set.new(candy_type).size
  [distinct, candy_type.length / 2].min
end
```

## Scala

```scala
object Solution {
    def distributeCandies(candyType: Array[Int]): Int = {
        val distinct = candyType.toSet.size
        math.min(distinct, candyType.length / 2)
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn distribute_candies(candy_type: Vec<i32>) -> i32 {
        let unique_kinds = candy_type.iter().cloned().collect::<HashSet<_>>().len() as i32;
        let limit = (candy_type.len() / 2) as i32;
        std::cmp::min(unique_kinds, limit)
    }
}
```

## Racket

```racket
(define/contract (distribute-candies candyType)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((tbl (make-hash))
         (_   (for-each (lambda (x) (hash-set! tbl x #t)) candyType))
         (unique-count (hash-count tbl))
         (limit (/ (length candyType) 2)))
    (min unique-count limit)))
```

## Erlang

```erlang
-module(solution).
-export([distribute_candies/1]).

-spec distribute_candies(CandyType :: [integer()]) -> integer().
distribute_candies(CandyType) ->
    UniqueCount = sets:size(sets:from_list(CandyType)),
    Limit = length(CandyType) div 2,
    erlang:min(UniqueCount, Limit).
```

## Elixir

```elixir
defmodule Solution do
  @spec distribute_candies(candy_type :: [integer]) :: integer
  def distribute_candies(candy_type) do
    distinct = candy_type |> MapSet.new() |> MapSet.size()
    half = div(length(candy_type), 2)
    if distinct < half, do: distinct, else: half
  end
end
```
