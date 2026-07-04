# 0599. Minimum Index Sum of Two Lists

## Cpp

```cpp
class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string,int> idx;
        for (int i = 0; i < (int)list1.size(); ++i) {
            idx[list1[i]] = i;
        }
        int minSum = INT_MAX;
        vector<string> res;
        for (int j = 0; j < (int)list2.size(); ++j) {
            auto it = idx.find(list2[j]);
            if (it != idx.end()) {
                int sum = it->second + j;
                if (sum < minSum) {
                    minSum = sum;
                    res.clear();
                    res.push_back(list2[j]);
                } else if (sum == minSum) {
                    res.push_back(list2[j]);
                }
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        java.util.Map<String, Integer> indexMap = new java.util.HashMap<>();
        for (int i = 0; i < list1.length; i++) {
            indexMap.put(list1[i], i);
        }
        int minSum = Integer.MAX_VALUE;
        java.util.List<String> result = new java.util.ArrayList<>();
        for (int j = 0; j < list2.length; j++) {
            Integer i = indexMap.get(list2[j]);
            if (i != null) {
                int sum = i + j;
                if (sum < minSum) {
                    minSum = sum;
                    result.clear();
                    result.add(list2[j]);
                } else if (sum == minSum) {
                    result.add(list2[j]);
                }
            }
        }
        return result.toArray(new String[0]);
    }
}
```

## Python

```python
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {s: i for i, s in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for j, s in enumerate(list2):
            if s in index_map:
                total = index_map[s] + j
                if total < min_sum:
                    min_sum = total
                    result = [s]
                elif total == min_sum:
                    result.append(s)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx_map = {name: i for i, name in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for j, name in enumerate(list2):
            if name in idx_map:
                s = idx_map[name] + j
                if s < min_sum:
                    min_sum = s
                    result = [name]
                elif s == min_sum:
                    result.append(name)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include "uthash.h"

/* Hash table entry for strings from list1 */
typedef struct {
    const char *key;   /* string (pointer) */
    int idx;           /* index in list1 */
    UT_hash_handle hh;
} Entry;

char** findRestaurant(char** list1, int list1Size, char** list2, int list2Size, int* returnSize) {
    Entry *map = NULL, *e;
    
    /* Build hash map from list1 */
    for (int i = 0; i < list1Size; ++i) {
        e = (Entry *)malloc(sizeof(Entry));
        e->key = list1[i];
        e->idx = i;
        HASH_ADD_KEYPTR(hh, map, e->key, strlen(e->key), e);
    }
    
    int minSum = INT_MAX;
    int count = 0;
    char **tempRes = (char **)malloc(sizeof(char *) * (list1Size < list2Size ? list1Size : list2Size));
    
    for (int j = 0; j < list2Size; ++j) {
        HASH_FIND_STR(map, list2[j], e);
        if (e) {
            int sum = e->idx + j;
            if (sum < minSum) {
                minSum = sum;
                count = 0;
                tempRes[count++] = (char *)list2[j];
            } else if (sum == minSum) {
                tempRes[count++] = (char *)list2[j];
            }
        }
    }
    
    /* Prepare output */
    char **result = (char **)malloc(sizeof(char *) * count);
    for (int i = 0; i < count; ++i) {
        result[i] = strdup(tempRes[i]);
    }
    *returnSize = count;
    
    free(tempRes);
    
    /* Clean up hash map */
    Entry *cur, *tmp;
    HASH_ITER(hh, map, cur, tmp) {
        HASH_DEL(map, cur);
        free(cur);
    }
    
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public string[] FindRestaurant(string[] list1, string[] list2) {
        var indexMap = new Dictionary<string, int>();
        for (int i = 0; i < list1.Length; i++) {
            indexMap[list1[i]] = i;
        }

        var result = new List<string>();
        int minSum = int.MaxValue;

        for (int j = 0; j < list2.Length; j++) {
            if (indexMap.TryGetValue(list2[j], out int i)) {
                int sum = i + j;
                if (sum < minSum) {
                    minSum = sum;
                    result.Clear();
                    result.Add(list2[j]);
                } else if (sum == minSum) {
                    result.Add(list2[j]);
                }
            }
        }

        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    const indexMap = new Map();
    for (let i = 0; i < list1.length; i++) {
        indexMap.set(list1[i], i);
    }
    let minSum = Infinity;
    const result = [];
    for (let j = 0; j < list2.length; j++) {
        const name = list2[j];
        if (indexMap.has(name)) {
            const sum = indexMap.get(name) + j;
            if (sum < minSum) {
                minSum = sum;
                result.length = 0;
                result.push(name);
            } else if (sum === minSum) {
                result.push(name);
            }
        }
    }
    return result;
};
```

## Typescript

```typescript
function findRestaurant(list1: string[], list2: string[]): string[] {
    const indexMap = new Map<string, number>();
    for (let i = 0; i < list1.length; i++) {
        indexMap.set(list1[i], i);
    }
    let minSum = Infinity;
    const result: string[] = [];
    for (let j = 0; j < list2.length; j++) {
        const name = list2[j];
        if (indexMap.has(name)) {
            const sum = indexMap.get(name)! + j;
            if (sum < minSum) {
                minSum = sum;
                result.length = 0;
                result.push(name);
            } else if (sum === minSum) {
                result.push(name);
            }
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $list1
     * @param String[] $list2
     * @return String[]
     */
    function findRestaurant($list1, $list2) {
        $indexMap = [];
        foreach ($list1 as $i => $restaurant) {
            $indexMap[$restaurant] = $i;
        }

        $minSum = PHP_INT_MAX;
        $result = [];

        foreach ($list2 as $j => $restaurant) {
            if (isset($indexMap[$restaurant])) {
                $sum = $indexMap[$restaurant] + $j;
                if ($sum < $minSum) {
                    $minSum = $sum;
                    $result = [$restaurant];
                } elseif ($sum == $minSum) {
                    $result[] = $restaurant;
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findRestaurant(_ list1: [String], _ list2: [String]) -> [String] {
        var indexMap = [String: Int]()
        for (i, name) in list1.enumerated() {
            indexMap[name] = i
        }
        
        var minSum = Int.max
        var result = [String]()
        
        for (j, name) in list2.enumerated() {
            if let i = indexMap[name] {
                let sum = i + j
                if sum < minSum {
                    minSum = sum
                    result = [name]
                } else if sum == minSum {
                    result.append(name)
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findRestaurant(list1: Array<String>, list2: Array<String>): Array<String> {
        val indexMap = HashMap<String, Int>(list1.size)
        for (i in list1.indices) {
            indexMap[list1[i]] = i
        }
        var minSum = Int.MAX_VALUE
        val result = mutableListOf<String>()
        for (j in list2.indices) {
            val restaurant = list2[j]
            val i = indexMap[restaurant] ?: continue
            val sum = i + j
            when {
                sum < minSum -> {
                    minSum = sum
                    result.clear()
                    result.add(restaurant)
                }
                sum == minSum -> {
                    result.add(restaurant)
                }
            }
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<String> findRestaurant(List<String> list1, List<String> list2) {
    final Map<String, int> indexMap = {};
    for (int i = 0; i < list1.length; i++) {
      indexMap[list1[i]] = i;
    }

    int minSum = 1 << 30;
    final List<String> result = [];

    for (int j = 0; j < list2.length; j++) {
      final String restaurant = list2[j];
      if (indexMap.containsKey(restaurant)) {
        final int sum = indexMap[restaurant]! + j;
        if (sum < minSum) {
          minSum = sum;
          result
            ..clear()
            ..add(restaurant);
        } else if (sum == minSum) {
          result.add(restaurant);
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func findRestaurant(list1 []string, list2 []string) []string {
    idxMap := make(map[string]int, len(list1))
    for i, s := range list1 {
        idxMap[s] = i
    }

    minSum := int(^uint(0) >> 1) // MaxInt
    var result []string

    for j, s := range list2 {
        if i, ok := idxMap[s]; ok {
            sum := i + j
            if sum < minSum {
                minSum = sum
                result = []string{s}
            } else if sum == minSum {
                result = append(result, s)
            }
        }
    }

    return result
}
```

## Ruby

```ruby
def find_restaurant(list1, list2)
  index_map = {}
  list1.each_with_index { |name, i| index_map[name] = i }

  min_sum = Float::INFINITY
  result = []

  list2.each_with_index do |name, j|
    if (i = index_map[name])
      sum = i + j
      if sum < min_sum
        min_sum = sum
        result = [name]
      elsif sum == min_sum
        result << name
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def findRestaurant(list1: Array[String], list2: Array[String]): Array[String] = {
        val indexMap = scala.collection.mutable.HashMap[String, Int]()
        for (i <- list1.indices) {
            indexMap(list1(i)) = i
        }
        var minSum = Int.MaxValue
        val result = scala.collection.mutable.ArrayBuffer[String]()
        for (j <- list2.indices) {
            val s = list2(j)
            indexMap.get(s) match {
                case Some(i) =>
                    val sum = i + j
                    if (sum < minSum) {
                        minSum = sum
                        result.clear()
                        result += s
                    } else if (sum == minSum) {
                        result += s
                    }
                case None => // ignore
            }
        }
        result.toArray
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn find_restaurant(list1: Vec<String>, list2: Vec<String>) -> Vec<String> {
        let mut index_map: HashMap<String, usize> = HashMap::new();
        for (i, name) in list1.iter().enumerate() {
            index_map.insert(name.clone(), i);
        }

        let mut min_sum = usize::MAX;
        let mut result: Vec<String> = Vec::new();

        for (j, name) in list2.iter().enumerate() {
            if let Some(&i) = index_map.get(name) {
                let sum = i + j;
                if sum < min_sum {
                    min_sum = sum;
                    result.clear();
                    result.push(name.clone());
                } else if sum == min_sum {
                    result.push(name.clone());
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (find-restaurant list1 list2)
  (-> (listof string?) (listof string?) (listof string?))
  (let* ((h (make-hash)))
    (for ([s list1] [i (in-naturals)])
      (hash-set! h s i))
    (let loop ((lst list2) (j 0) (min-sum (+ (length list1) (length list2))) (res '()))
      (cond
        [(null? lst) (reverse res)]
        [else
         (let ((s (car lst)))
           (if (hash-has-key? h s)
               (let* ((i (hash-ref h s))
                      (sum (+ i j)))
                 (cond
                   [(< sum min-sum) (loop (cdr lst) (add1 j) sum (list s))]
                   [(= sum min-sum) (loop (cdr lst) (add1 j) min-sum (cons s res))]
                   [else (loop (cdr lst) (add1 j) min-sum res)]))
               (loop (cdr lst) (add1 j) min-sum res)))]))))
```

## Erlang

```erlang
-spec find_restaurant(List1 :: [unicode:unicode_binary()], List2 :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
find_restaurant(List1, List2) ->
    Map = maps:from_list(lists:zip(List1, lists:seq(0, length(List1) - 1))),
    {_, Res} =
        lists:foldl(
            fun({Str, J}, {MinSum, Acc}) ->
                case maps:find(Str, Map) of
                    {ok, I} ->
                        Sum = I + J,
                        case MinSum of
                            undefined -> {Sum, [Str]};
                            _ when Sum < MinSum -> {Sum, [Str]};
                            _ when Sum == MinSum -> {MinSum, [Str | Acc]};
                            _ -> {MinSum, Acc}
                        end;
                    error ->
                        {MinSum, Acc}
                end
            end,
            {undefined, []},
            lists:zip(List2, lists:seq(0, length(List2) - 1))
        ),
    Res.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_restaurant(list1 :: [String.t()], list2 :: [String.t()]) :: [String.t()]
  def find_restaurant(list1, list2) do
    idx_map =
      list1
      |> Enum.with_index()
      |> Map.new(fn {s, i} -> {s, i} end)

    {result, _min_sum} =
      list2
      |> Enum.with_index()
      |> Enum.reduce({[], nil}, fn {s, j}, {acc, min_sum} ->
        case Map.fetch(idx_map, s) do
          {:ok, i} ->
            sum = i + j

            cond do
              min_sum == nil or sum < min_sum -> {[s], sum}
              sum == min_sum -> {[s | acc], min_sum}
              true -> {acc, min_sum}
            end

          :error ->
            {acc, min_sum}
        end
      end)

    Enum.reverse(result)
  end
end
```
