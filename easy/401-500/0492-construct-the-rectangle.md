# 0492. Construct the Rectangle

## Cpp

```cpp
class Solution {
public:
    vector<int> constructRectangle(int area) {
        int w = static_cast<int>(sqrt(area));
        for (int i = w; i >= 1; --i) {
            if (area % i == 0) {
                return {area / i, i};
            }
        }
        // Fallback, should never reach here because 1 always divides area
        return {area, 1};
    }
};
```

## Java

```java
class Solution {
    public int[] constructRectangle(int area) {
        int w = (int)Math.sqrt(area);
        while (w > 0 && area % w != 0) {
            w--;
        }
        int l = area / w;
        return new int[]{l, w};
    }
}
```

## Python

```python
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        w = int(math.isqrt(area))
        while w > 0:
            if area % w == 0:
                return [area // w, w]
            w -= 1
        # Fallback (should never reach here because w=1 always works)
        return [area, 1]
```

## Python3

```python
from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(math.isqrt(area))
        while w > 0:
            if area % w == 0:
                return [area // w, w]
            w -= 1
```

## C

```c
#include <stdlib.h>
#include <math.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructRectangle(int area, int* returnSize) {
    int i = (int)sqrt((double)area);
    while (i > 0 && area % i != 0) {
        --i;
    }
    int *res = (int *)malloc(2 * sizeof(int));
    res[0] = area / i; // length L >= width W
    res[1] = i;
    *returnSize = 2;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ConstructRectangle(int area) {
        int w = (int)Math.Sqrt(area);
        for (int i = w; i >= 1; i--) {
            if (area % i == 0) {
                return new int[] { area / i, i };
            }
        }
        // Fallback, though loop always finds at least i=1
        return new int[] { area, 1 };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} area
 * @return {number[]}
 */
var constructRectangle = function(area) {
    let w = Math.floor(Math.sqrt(area));
    while (w > 0) {
        if (area % w === 0) {
            return [area / w, w];
        }
        w--;
    }
    // Fallback, though for area >=1 this line is never reached
    return [area, 1];
};
```

## Typescript

```typescript
function constructRectangle(area: number): number[] {
    let w = Math.floor(Math.sqrt(area));
    while (w > 0 && area % w !== 0) {
        w--;
    }
    return [area / w, w];
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer $area
     * @return Integer[]
     */
    function constructRectangle($area) {
        $i = (int)floor(sqrt($area));
        while ($area % $i !== 0) {
            $i--;
        }
        return [intdiv($area, $i), $i];
    }
}
?>
```

## Swift

```swift
import Foundation

class Solution {
    func constructRectangle(_ area: Int) -> [Int] {
        var w = Int(Double(area).squareRoot())
        while w > 0 {
            if area % w == 0 {
                let l = area / w
                return [l, w]
            }
            w -= 1
        }
        return [area, 1]
    }
}
```

## Kotlin

```kotlin
import kotlin.math.sqrt

class Solution {
    fun constructRectangle(area: Int): IntArray {
        var w = sqrt(area.toDouble()).toInt()
        while (w >= 1) {
            if (area % w == 0) {
                val l = area / w
                return intArrayOf(l, w)
            }
            w--
        }
        return intArrayOf(area, 1)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  List<int> constructRectangle(int area) {
    int w = sqrt(area).floor();
    while (area % w != 0) {
      w--;
    }
    return [area ~/ w, w];
  }
}
```

## Golang

```go
import "math"

func constructRectangle(area int) []int {
	for i := int(math.Sqrt(float64(area))); i >= 1; i-- {
		if area%i == 0 {
			return []int{area / i, i}
		}
	}
	return []int{}
}
```

## Ruby

```ruby
def construct_rectangle(area)
  w = Math.sqrt(area).to_i
  while w > 0
    if area % w == 0
      return [area / w, w]
    end
    w -= 1
  end
end
```

## Scala

```scala
object Solution {
    def constructRectangle(area: Int): Array[Int] = {
        var w = Math.sqrt(area).toInt
        while (w > 0 && area % w != 0) {
            w -= 1
        }
        val l = area / w
        Array(l, w)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn construct_rectangle(area: i32) -> Vec<i32> {
        let mut w = (area as f64).sqrt() as i32;
        while area % w != 0 {
            w -= 1;
        }
        vec![area / w, w]
    }
}
```

## Racket

```racket
(define/contract (construct-rectangle area)
  (-> exact-integer? (listof exact-integer?))
  (let* ((s (inexact->exact
             (floor (sqrt (exact->inexact area))))))
    (let loop ((w s))
      (if (= (remainder area w) 0)
          (list (/ area w) w)
          (loop (- w 1))))))
```

## Erlang

```erlang
-module(solution).
-export([construct_rectangle/1]).

-spec construct_rectangle(Area :: integer()) -> [integer()].
construct_rectangle(Area) ->
    Max = trunc(math:sqrt(Area)),
    find_pair(Max, Area).

find_pair(I, Area) when I > 0, Area rem I == 0 ->
    [Area div I, I];
find_pair(I, Area) ->
    find_pair(I - 1, Area).
```

## Elixir

```elixir
defmodule Solution do
  @spec construct_rectangle(area :: integer) :: [integer]
  def construct_rectangle(area) do
    w = find_width(:math.sqrt(area) |> trunc, area)
    [div(area, w), w]
  end

  defp find_width(0, _area), do: 1
  defp find_width(w, area) when rem(area, w) == 0, do: w
  defp find_width(w, area), do: find_width(w - 1, area)
end
```
