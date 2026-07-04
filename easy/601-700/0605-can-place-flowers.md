# 0605. Can Place Flowers

## Cpp

```cpp
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
        int m = flowerbed.size();
        for (int i = 0; i < m && count < n; ++i) {
            if (flowerbed[i] == 0) {
                bool emptyLeft = (i == 0) || (flowerbed[i - 1] == 0);
                bool emptyRight = (i == m - 1) || (flowerbed[i + 1] == 0);
                if (emptyLeft && emptyRight) {
                    flowerbed[i] = 1;
                    ++count;
                }
            }
        }
        return count >= n;
    }
};
```

## Java

```java
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) return true;
        int count = 0;
        int len = flowerbed.length;
        for (int i = 0; i < len && count < n; i++) {
            if (flowerbed[i] == 0) {
                boolean emptyLeft = (i == 0) || (flowerbed[i - 1] == 0);
                boolean emptyRight = (i == len - 1) || (flowerbed[i + 1] == 0);
                if (emptyLeft && emptyRight) {
                    flowerbed[i] = 1;
                    count++;
                }
            }
        }
        return count >= n;
    }
}
```

## Python

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)
        i = 0
        while i < length:
            if flowerbed[i] == 0:
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
            i += 1
        return count >= n
```

## Python3

```python
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n
```

## C

```c
#include <stdbool.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    int placed = 0;
    for (int i = 0; i < flowerbedSize && placed < n; ++i) {
        if (flowerbed[i] == 0) {
            bool emptyPrev = (i == 0) || (flowerbed[i - 1] == 0);
            bool emptyNext = (i == flowerbedSize - 1) || (flowerbed[i + 1] == 0);
            if (emptyPrev && emptyNext) {
                flowerbed[i] = 1;
                ++placed;
            }
        }
    }
    return placed >= n;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        for (int i = 0; i < flowerbed.Length && count < n; i++) {
            if (flowerbed[i] == 0) {
                bool emptyLeft = (i == 0) || (flowerbed[i - 1] == 0);
                bool emptyRight = (i == flowerbed.Length - 1) || (flowerbed[i + 1] == 0);
                if (emptyLeft && emptyRight) {
                    flowerbed[i] = 1;
                    count++;
                }
            }
        }
        return count >= n;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let placed = 0;
    const len = flowerbed.length;
    for (let i = 0; i < len && placed < n; i++) {
        if (flowerbed[i] === 0) {
            const prev = i === 0 ? 0 : flowerbed[i - 1];
            const next = i === len - 1 ? 0 : flowerbed[i + 1];
            if (prev === 0 && next === 0) {
                flowerbed[i] = 1;
                placed++;
            }
        }
    }
    return placed >= n;
};
```

## Typescript

```typescript
function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    let placed = 0;
    const len = flowerbed.length;
    for (let i = 0; i < len && placed < n; i++) {
        if (flowerbed[i] === 0) {
            const emptyLeft = i === 0 || flowerbed[i - 1] === 0;
            const emptyRight = i === len - 1 || flowerbed[i + 1] === 0;
            if (emptyLeft && emptyRight) {
                flowerbed[i] = 1; // plant a flower
                placed++;
            }
        }
    }
    return placed >= n;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $flowerbed
     * @param Integer $n
     * @return Boolean
     */
    function canPlaceFlowers($flowerbed, $n) {
        $count = 0;
        $len = count($flowerbed);
        for ($i = 0; $i < $len; $i++) {
            if ($flowerbed[$i] == 0) {
                $prev = ($i == 0) ? 0 : $flowerbed[$i - 1];
                $next = ($i == $len - 1) ? 0 : $flowerbed[$i + 1];
                if ($prev == 0 && $next == 0) {
                    $flowerbed[$i] = 1;
                    $count++;
                    if ($count >= $n) {
                        return true;
                    }
                }
            }
        }
        return $count >= $n;
    }
}
```

## Swift

```swift
class Solution {
    func canPlaceFlowers(_ flowerbed: [Int], _ n: Int) -> Bool {
        if n == 0 { return true }
        var count = 0
        var i = 0
        let m = flowerbed.count
        while i < m {
            if flowerbed[i] == 0 {
                let leftEmpty = (i == 0) || (flowerbed[i - 1] == 0)
                let rightEmpty = (i == m - 1) || (flowerbed[i + 1] == 0)
                if leftEmpty && rightEmpty {
                    count += 1
                    if count >= n { return true }
                    i += 2
                    continue
                }
            }
            i += 1
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        var placed = 0
        val len = flowerbed.size
        var i = 0
        while (i < len) {
            if (flowerbed[i] == 0 &&
                (i == 0 || flowerbed[i - 1] == 0) &&
                (i == len - 1 || flowerbed[i + 1] == 0)
            ) {
                flowerbed[i] = 1
                placed++
                if (placed >= n) return true
            }
            i++
        }
        return placed >= n
    }
}
```

## Dart

```dart
class Solution {
  bool canPlaceFlowers(List<int> flowerbed, int n) {
    int placed = 0;
    for (int i = 0; i < flowerbed.length && placed < n; i++) {
      if (flowerbed[i] == 0) {
        bool emptyPrev = i == 0 || flowerbed[i - 1] == 0;
        bool emptyNext = i == flowerbed.length - 1 || flowerbed[i + 1] == 0;
        if (emptyPrev && emptyNext) {
          placed++;
          flowerbed[i] = 1; // mark as planted
        }
      }
    }
    return placed >= n;
  }
}
```

## Golang

```go
func canPlaceFlowers(flowerbed []int, n int) bool {
	count := 0
	m := len(flowerbed)
	for i := 0; i < m && count < n; i++ {
		if flowerbed[i] == 0 {
			leftEmpty := i == 0 || flowerbed[i-1] == 0
			rightEmpty := i == m-1 || flowerbed[i+1] == 0
			if leftEmpty && rightEmpty {
				flowerbed[i] = 1
				count++
			}
		}
	}
	return count >= n
}
```

## Ruby

```ruby
def can_place_flowers(flowerbed, n)
  return true if n <= 0
  count = 0
  len = flowerbed.length
  i = 0
  while i < len
    if flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == len - 1 || flowerbed[i + 1] == 0)
      flowerbed[i] = 1
      count += 1
      return true if count >= n
    end
    i += 1
  end
  false
end
```

## Scala

```scala
object Solution {
    def canPlaceFlowers(flowerbed: Array[Int], n: Int): Boolean = {
        var count = 0
        val len = flowerbed.length
        var i = 0
        while (i < len && count < n) {
            if (flowerbed(i) == 0) {
                val emptyPrev = i == 0 || flowerbed(i - 1) == 0
                val emptyNext = i == len - 1 || flowerbed(i + 1) == 0
                if (emptyPrev && emptyNext) {
                    flowerbed(i) = 1
                    count += 1
                }
            }
            i += 1
        }
        count >= n
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_place_flowers(mut flowerbed: Vec<i32>, n: i32) -> bool {
        if n == 0 {
            return true;
        }
        let len = flowerbed.len();
        let mut placed = 0i32;
        for i in 0..len {
            if flowerbed[i] == 0 {
                let left_empty = i == 0 || flowerbed[i - 1] == 0;
                let right_empty = i + 1 == len || flowerbed[i + 1] == 0;
                if left_empty && right_empty {
                    flowerbed[i] = 1;
                    placed += 1;
                    if placed >= n {
                        return true;
                    }
                }
            }
        }
        placed >= n
    }
}
```

## Racket

```racket
(define/contract (can-place-flowers flowerbed n)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let loop ((prev 0) (lst flowerbed) (need n))
    (cond
      [(<= need 0) #t]
      [(null? lst) #f]
      [else
       (define cur (car lst))
       (define next (if (null? (cdr lst)) 0 (cadr lst)))
       (if (and (= cur 0) (= prev 0) (= next 0))
           (loop 1 (cdr lst) (- need 1))
           (loop cur (cdr lst) need))])))
```

## Erlang

```erlang
-module(solution).
-export([can_place_flowers/2]).

-spec can_place_flowers(Flowerbed :: [integer()], N :: integer()) -> boolean().
can_place_flowers(Flowerbed, N) ->
    can_place_flowers_helper(0, Flowerbed, N).

can_place_flowers_helper(_Prev, _List, N) when N =< 0 ->
    true;
can_place_flowers_helper(_Prev, [], _N) ->
    false;
can_place_flowers_helper(Prev, [Curr|Rest], N) ->
    Next = hd_or_zero(Rest),
    case {Prev, Curr, Next} of
        {0,0,0} ->
            can_place_flowers_helper(1, Rest, N-1);
        _ ->
            can_place_flowers_helper(Curr, Rest, N)
    end.

hd_or_zero([]) -> 0;
hd_or_zero([H|_]) -> H.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_place_flowers(flowerbed :: [integer], n :: integer) :: boolean
  def can_place_flowers(_flowerbed, n) when n <= 0, do: true

  def can_place_flowers(flowerbed, n) do
    # Append a zero to simplify the check for the last plot
    go(flowerbed ++ [0], 0, n)
  end

  defp go([], _prev, need), do: need <= 0

  defp go([h | t] = list, prev, need) do
    cond do
      h == 0 and prev == 0 and (t == [] or hd(t) == 0) ->
        new_need = need - 1
        if new_need <= 0 do
          true
        else
          go(t, 1, new_need)
        end

      true ->
        go(t, h, need)
    end
  end
end
```
