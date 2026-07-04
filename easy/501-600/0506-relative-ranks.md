# 0506. Relative Ranks

## Cpp

```cpp
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        int n = score.size();
        vector<pair<int,int>> v;
        v.reserve(n);
        for (int i = 0; i < n; ++i) v.emplace_back(score[i], i);
        sort(v.begin(), v.end(), [](const auto& a, const auto& b){ return a.first > b.first; });
        vector<string> ans(n);
        const string medals[3] = {"Gold Medal", "Silver Medal", "Bronze Medal"};
        for (int rank = 0; rank < n; ++rank) {
            int idx = v[rank].second;
            if (rank < 3) ans[idx] = medals[rank];
            else ans[idx] = to_string(rank + 1);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public String[] findRelativeRanks(int[] score) {
        int n = score.length;
        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }
        Arrays.sort(indices, (a, b) -> Integer.compare(score[b], score[a]));
        
        String[] result = new String[n];
        String[] medals = {"Gold Medal", "Silver Medal", "Bronze Medal"};
        for (int rank = 0; rank < n; rank++) {
            int idx = indices[rank];
            if (rank < 3) {
                result[idx] = medals[rank];
            } else {
                result[idx] = Integer.toString(rank + 1);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Map each score to its original index
        idx_map = {s: i for i, s in enumerate(score)}
        # Sort scores descendingly
        sorted_scores = sorted(score, reverse=True)
        # Prepare result list
        res = [""] * len(score)
        # Assign ranks/medals
        for rank, s in enumerate(sorted_scores):
            i = idx_map[s]
            if rank == 0:
                res[i] = "Gold Medal"
            elif rank == 1:
                res[i] = "Silver Medal"
            elif rank == 2:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank + 1)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Sort indices by descending scores
        sorted_indices = sorted(range(len(score)), key=lambda i: -score[i])
        result = [""] * len(score)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for rank, idx in enumerate(sorted_indices):
            if rank < 3:
                result[idx] = medals[rank]
            else:
                result[idx] = str(rank + 1)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct {
    int score;
    int idx;
} Pair;

static int cmpDesc(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    return pb->score - pa->score; // descending
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findRelativeRanks(int* score, int scoreSize, int* returnSize) {
    if (scoreSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    Pair *arr = (Pair *)malloc(scoreSize * sizeof(Pair));
    for (int i = 0; i < scoreSize; ++i) {
        arr[i].score = score[i];
        arr[i].idx   = i;
    }
    
    qsort(arr, scoreSize, sizeof(Pair), cmpDesc);
    
    const char *medals[3] = {"Gold Medal", "Silver Medal", "Bronze Medal"};
    char **res = (char **)malloc(scoreSize * sizeof(char *));
    
    for (int i = 0; i < scoreSize; ++i) {
        int originalIdx = arr[i].idx;
        if (i < 3) {
            size_t len = strlen(medals[i]) + 1;
            res[originalIdx] = (char *)malloc(len);
            memcpy(res[originalIdx], medals[i], len);
        } else {
            char buf[12];
            sprintf(buf, "%d", i + 1);
            size_t len = strlen(buf) + 1;
            res[originalIdx] = (char *)malloc(len);
            memcpy(res[originalIdx], buf, len);
        }
    }
    
    free(arr);
    *returnSize = scoreSize;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string[] FindRelativeRanks(int[] score)
    {
        int n = score.Length;
        string[] result = new string[n];
        int[] indices = new int[n];
        for (int i = 0; i < n; i++) indices[i] = i;

        System.Array.Sort(indices, (a, b) => score[b].CompareTo(score[a]));

        for (int rank = 0; rank < n; rank++)
        {
            int idx = indices[rank];
            if (rank == 0)
                result[idx] = "Gold Medal";
            else if (rank == 1)
                result[idx] = "Silver Medal";
            else if (rank == 2)
                result[idx] = "Bronze Medal";
            else
                result[idx] = (rank + 1).ToString();
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} score
 * @return {string[]}
 */
var findRelativeRanks = function(score) {
    const n = score.length;
    const paired = score.map((s, i) => [s, i]);
    paired.sort((a, b) => b[0] - a[0]); // descending by score
    
    const result = new Array(n);
    for (let rank = 0; rank < n; rank++) {
        const idx = paired[rank][1];
        if (rank === 0) result[idx] = "Gold Medal";
        else if (rank === 1) result[idx] = "Silver Medal";
        else if (rank === 2) result[idx] = "Bronze Medal";
        else result[idx] = String(rank + 1);
    }
    return result;
};
```

## Typescript

```typescript
function findRelativeRanks(score: number[]): string[] {
    const n = score.length;
    const indices = Array.from({ length: n }, (_, i) => i);
    indices.sort((a, b) => score[b] - score[a]); // descending scores

    const result = new Array<string>(n);
    for (let i = 0; i < n; i++) {
        let rank: string;
        if (i === 0) rank = "Gold Medal";
        else if (i === 1) rank = "Silver Medal";
        else if (i === 2) rank = "Bronze Medal";
        else rank = (i + 1).toString();
        result[indices[i]] = rank;
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $score
     * @return String[]
     */
    function findRelativeRanks($score) {
        $n = count($score);
        if ($n === 0) return [];

        // indices sorted by descending score
        $indices = range(0, $n - 1);
        usort($indices, function($a, $b) use ($score) {
            return $score[$b] <=> $score[$a];
        });

        $result = array_fill(0, $n, "");
        foreach ($indices as $rank => $idx) {
            if ($rank == 0) {
                $result[$idx] = "Gold Medal";
            } elseif ($rank == 1) {
                $result[$idx] = "Silver Medal";
            } elseif ($rank == 2) {
                $result[$idx] = "Bronze Medal";
            } else {
                $result[$idx] = strval($rank + 1);
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findRelativeRanks(_ score: [Int]) -> [String] {
        let n = score.count
        var indexed = [(value: Int, index: Int)]()
        indexed.reserveCapacity(n)
        for (i, v) in score.enumerated() {
            indexed.append((v, i))
        }
        indexed.sort { $0.value > $1.value }  // descending order
        
        var result = Array(repeating: "", count: n)
        let medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        for (place, item) in indexed.enumerated() {
            if place < 3 {
                result[item.index] = medals[place]
            } else {
                result[item.index] = String(place + 1)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findRelativeRanks(score: IntArray): Array<String> {
        val n = score.size
        val order = (0 until n).sortedWith(compareByDescending<Int> { score[it] })
        val result = Array(n) { "" }
        for ((rank, idx) in order.withIndex()) {
            result[idx] = when (rank) {
                0 -> "Gold Medal"
                1 -> "Silver Medal"
                2 -> "Bronze Medal"
                else -> (rank + 1).toString()
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> findRelativeRanks(List<int> score) {
    int n = score.length;
    List<int> indices = List<int>.generate(n, (i) => i);
    indices.sort((a, b) => score[b].compareTo(score[a]));
    List<String> result = List<String>.filled(n, '');
    for (int i = 0; i < n; i++) {
      String rank;
      if (i == 0) {
        rank = "Gold Medal";
      } else if (i == 1) {
        rank = "Silver Medal";
      } else if (i == 2) {
        rank = "Bronze Medal";
      } else {
        rank = (i + 1).toString();
      }
      result[indices[i]] = rank;
    }
    return result;
  }
}
```

## Golang

```go
package main

import (
	"sort"
	"strconv"
)

func findRelativeRanks(score []int) []string {
	n := len(score)
	type pair struct{ val, idx int }
	pairs := make([]pair, n)
	for i, v := range score {
		pairs[i] = pair{v, i}
	}
	sort.Slice(pairs, func(i, j int) bool { return pairs[i].val > pairs[j].val })
	res := make([]string, n)
	medals := []string{"Gold Medal", "Silver Medal", "Bronze Medal"}
	for i, p := range pairs {
		if i < 3 {
			res[p.idx] = medals[i]
		} else {
			res[p.idx] = strconv.Itoa(i + 1)
		}
	}
	return res
}
```

## Ruby

```ruby
def find_relative_ranks(score)
  index_map = {}
  score.each_with_index { |s, i| index_map[s] = i }

  sorted_scores = score.sort.reverse
  result = Array.new(score.length)

  sorted_scores.each_with_index do |s, rank|
    idx = index_map[s]
    result[idx] = case rank
                  when 0 then "Gold Medal"
                  when 1 then "Silver Medal"
                  when 2 then "Bronze Medal"
                  else (rank + 1).to_s
                  end
  end

  result
end
```

## Scala

```scala
object Solution {
    def findRelativeRanks(score: Array[Int]): Array[String] = {
        val n = score.length
        val result = new Array[String](n)
        val order = (0 until n).toArray.sortWith((i, j) => score(i) > score(j))
        for (rank <- order.indices) {
            val idx = order(rank)
            result(idx) = rank match {
                case 0 => "Gold Medal"
                case 1 => "Silver Medal"
                case 2 => "Bronze Medal"
                case _ => (rank + 1).toString
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_relative_ranks(score: Vec<i32>) -> Vec<String> {
        let n = score.len();
        let mut pairs: Vec<(i32, usize)> = score.into_iter().enumerate().map(|(i, s)| (s as i32, i)).collect();
        pairs.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        let mut res = vec![String::new(); n];
        for (place, &(_, idx)) in pairs.iter().enumerate() {
            let rank = match place {
                0 => "Gold Medal".to_string(),
                1 => "Silver Medal".to_string(),
                2 => "Bronze Medal".to_string(),
                _ => (place + 1).to_string(),
            };
            res[idx] = rank;
        }
        res
    }
}
```

## Racket

```racket
(define/contract (find-relative-ranks score)
  (-> (listof exact-integer?) (listof string?))
  (let* ((n (length score))
         (indexed
           (let loop ((lst score) (i 0) (acc '()))
             (if (null? lst)
                 (reverse acc)
                 (loop (cdr lst) (+ i 1) (cons (list (car lst) i) acc)))))
         (sorted (sort indexed (lambda (a b) (> (first a) (first b)))))
         (res (make-vector n #f)))
    (for ([pair sorted] [place (in-naturals 1)])
      (define idx (second pair))
      (vector-set! res idx
        (cond [(= place 1) "Gold Medal"]
              [(= place 2) "Silver Medal"]
              [(= place 3) "Bronze Medal"]
              [else (number->string place)])))
    (vector->list res)))
```

## Erlang

```erlang
-spec find_relative_ranks(Score :: [integer()]) -> [unicode:unicode_binary()].
find_relative_ranks(Score) ->
    N = length(Score),
    Indices = lists:seq(0, N - 1),
    Pairs = lists:zip(Score, Indices),                     % {Score, Index}
    Sorted = lists:sort(fun({S1,_}, {S2,_}) -> S1 > S2 end, Pairs),
    RankMap = assign_ranks(Sorted, 1, #{}),
    [maps:get(I, RankMap) || I <- Indices].

assign_ranks([], _Pos, Map) ->
    Map;
assign_ranks([{_Score, Idx} | Rest], Pos, Map) ->
    RankBin = case Pos of
        1 -> <<"Gold Medal">>;
        2 -> <<"Silver Medal">>;
        3 -> <<"Bronze Medal">>;
        _ -> integer_to_binary(Pos)
    end,
    assign_ranks(Rest, Pos + 1, maps:put(Idx, RankBin, Map)).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_relative_ranks(score :: [integer]) :: [String.t()]
  def find_relative_ranks(score) do
    # Pair each score with its original index
    indexed = Enum.with_index(score)

    # Sort scores in descending order while keeping indices
    sorted =
      Enum.sort_by(indexed, fn {s, _i} -> s end, :desc)

    # Build a map from original index to rank string
    ranks_map =
      sorted
      |> Enum.with_index(1)
      |> Enum.reduce(%{}, fn {{_score, idx}, rank}, acc ->
        rank_str =
          case rank do
            1 -> "Gold Medal"
            2 -> "Silver Medal"
            3 -> "Bronze Medal"
            _ -> Integer.to_string(rank)
          end

        Map.put(acc, idx, rank_str)
      end)

    # Produce the result list in original order
    Enum.map(0..(length(score) - 1), fn i -> Map.get(ranks_map, i) end)
  end
end
```
