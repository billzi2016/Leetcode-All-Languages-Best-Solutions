# 0495. Teemo Attacking

## Cpp

```cpp
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        if (duration == 0 || timeSeries.empty()) return 0;
        long long total = 0;
        for (size_t i = 0; i + 1 < timeSeries.size(); ++i) {
            total += min(duration, timeSeries[i + 1] - timeSeries[i]);
        }
        total += duration; // last attack
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        if (timeSeries == null || timeSeries.length == 0) {
            return 0;
        }
        int total = 0;
        for (int i = 0; i < timeSeries.length - 1; i++) {
            int interval = timeSeries[i + 1] - timeSeries[i];
            total += Math.min(interval, duration);
        }
        total += duration;
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        total = 0
        for i in range(len(timeSeries) - 1):
            total += min(duration, timeSeries[i + 1] - timeSeries[i])
        return total + duration
```

## Python3

```python
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries or duration == 0:
            return 0
        total = 0
        for i in range(1, len(timeSeries)):
            total += min(duration, timeSeries[i] - timeSeries[i - 1])
        return total + duration
```

## C

```c
int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration) {
    if (timeSeriesSize == 0 || duration == 0) return 0;
    long long total = 0;
    for (int i = 0; i < timeSeriesSize - 1; ++i) {
        int diff = timeSeries[i + 1] - timeSeries[i];
        total += (diff < duration) ? diff : duration;
    }
    total += duration;
    return (int)total;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int FindPoisonedDuration(int[] timeSeries, int duration) {
        if (timeSeries == null || timeSeries.Length == 0) return 0;
        long total = 0;
        for (int i = 0; i < timeSeries.Length - 1; i++) {
            int diff = timeSeries[i + 1] - timeSeries[i];
            total += Math.Min(diff, duration);
        }
        total += duration; // last attack
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    if (duration === 0 || timeSeries.length === 0) return 0;
    let total = 0;
    for (let i = 0; i < timeSeries.length - 1; ++i) {
        const gap = timeSeries[i + 1] - timeSeries[i];
        total += Math.min(gap, duration);
    }
    total += duration; // last attack
    return total;
};
```

## Typescript

```typescript
function findPoisonedDuration(timeSeries: number[], duration: number): number {
    let total = 0;
    for (let i = 1; i < timeSeries.length; ++i) {
        const diff = timeSeries[i] - timeSeries[i - 1];
        total += Math.min(diff, duration);
    }
    if (timeSeries.length > 0) {
        total += duration;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $timeSeries
     * @param Integer $duration
     * @return Integer
     */
    function findPoisonedDuration($timeSeries, $duration) {
        $n = count($timeSeries);
        if ($n == 0 || $duration == 0) {
            return 0;
        }
        $total = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $gap = $timeSeries[$i + 1] - $timeSeries[$i];
            $total += min($duration, $gap);
        }
        $total += $duration; // last attack
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func findPoisonedDuration(_ timeSeries: [Int], _ duration: Int) -> Int {
        guard !timeSeries.isEmpty else { return 0 }
        var total = 0
        for i in 0..<(timeSeries.count - 1) {
            let diff = timeSeries[i + 1] - timeSeries[i]
            total += min(diff, duration)
        }
        total += duration
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findPoisonedDuration(timeSeries: IntArray, duration: Int): Int {
        if (timeSeries.isEmpty() || duration == 0) return 0
        var total = 0
        for (i in 0 until timeSeries.size - 1) {
            val diff = timeSeries[i + 1] - timeSeries[i]
            total += kotlin.math.min(duration, diff)
        }
        total += duration
        return total
    }
}
```

## Dart

```dart
class Solution {
  int findPoisonedDuration(List<int> timeSeries, int duration) {
    if (timeSeries.isEmpty || duration == 0) return 0;
    int total = 0;
    for (int i = 0; i < timeSeries.length - 1; ++i) {
      int diff = timeSeries[i + 1] - timeSeries[i];
      total += diff < duration ? diff : duration;
    }
    total += duration;
    return total;
  }
}
```

## Golang

```go
func findPoisonedDuration(timeSeries []int, duration int) int {
	if len(timeSeries) == 0 || duration == 0 {
		return 0
	}
	total := 0
	for i := 0; i < len(timeSeries)-1; i++ {
		diff := timeSeries[i+1] - timeSeries[i]
		if diff < duration {
			total += diff
		} else {
			total += duration
		}
	}
	total += duration
	return total
}
```

## Ruby

```ruby
def find_poisoned_duration(time_series, duration)
  return 0 if time_series.empty? || duration == 0
  total = 0
  (0...time_series.length - 1).each do |i|
    diff = time_series[i + 1] - time_series[i]
    total += diff < duration ? diff : duration
  end
  total + duration
end
```

## Scala

```scala
object Solution {
    def findPoisonedDuration(timeSeries: Array[Int], duration: Int): Int = {
        if (timeSeries.isEmpty || duration == 0) return 0
        var total: Long = 0L
        val n = timeSeries.length
        var i = 0
        while (i < n - 1) {
            val diff = timeSeries(i + 1) - timeSeries(i)
            total += Math.min(diff, duration).toLong
            i += 1
        }
        (total + duration).toInt
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn find_poisoned_duration(time_series: Vec<i32>, duration: i32) -> i32 {
        let n = time_series.len();
        if n == 0 || duration == 0 {
            return 0;
        }
        let mut total: i64 = 0;
        for i in 0..n - 1 {
            let diff = time_series[i + 1] - time_series[i];
            total += std::cmp::min(diff, duration) as i64;
        }
        total += duration as i64;
        total as i32
    }
}
```

## Racket

```racket
(define/contract (find-poisoned-duration timeSeries duration)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ((lst timeSeries) (total 0))
    (cond
      [(null? lst) total]
      [(null? (cdr lst)) (+ total duration)]
      [else
       (define diff (- (cadr lst) (car lst)))
       (loop (cdr lst) (+ total (min duration diff)))])))
```

## Erlang

```erlang
-module(solution).
-export([find_poisoned_duration/2]).

-spec find_poisoned_duration(TimeSeries :: [integer()], Duration :: integer()) -> integer().
find_poisoned_duration([], _Duration) ->
    0;
find_poisoned_duration([_], Duration) ->
    Duration;
find_poisoned_duration([First | Rest], Duration) ->
    Total = sum_intervals(Rest, First, Duration, 0),
    Total + Duration.

sum_intervals([], _Prev, _Duration, Acc) ->
    Acc;
sum_intervals([Curr | Tail], Prev, Duration, Acc) ->
    Diff = Curr - Prev,
    Add = if Diff < Duration -> Diff; true -> Duration end,
    sum_intervals(Tail, Curr, Duration, Acc + Add).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_poisoned_duration(time_series :: [integer], duration :: integer) :: integer
  def find_poisoned_duration([], _duration), do: 0

  def find_poisoned_duration([_single] = ts, duration), do: duration

  def find_poisoned_duration([first | rest] = time_series, duration) do
    total = helper(first, rest, duration, 0)
    total + duration
  end

  defp helper(_prev, [], _duration, acc), do: acc

  defp helper(prev, [curr | tail], duration, acc) do
    diff = curr - prev
    add = if diff < duration, do: diff, else: duration
    helper(curr, tail, duration, acc + add)
  end
end
```
