# 0401. Binary Watch

## Cpp

```cpp
class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> result;
        for (int h = 0; h < 12; ++h) {
            for (int m = 0; m < 60; ++m) {
                if (__builtin_popcount(h) + __builtin_popcount(m) == turnedOn) {
                    string time = to_string(h) + ":";
                    if (m < 10) time += "0";
                    time += to_string(m);
                    result.push_back(time);
                }
            }
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> readBinaryWatch(int turnedOn) {
        List<String> result = new ArrayList<>();
        if (turnedOn < 0 || turnedOn > 8) return result;
        for (int hour = 0; hour < 12; hour++) {
            int hourBits = Integer.bitCount(hour);
            for (int minute = 0; minute < 60; minute++) {
                if (hourBits + Integer.bitCount(minute) == turnedOn) {
                    result.add(hour + ":" + (minute < 10 ? "0" + minute : minute));
                }
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []
        for h in range(12):
            hour_bits = bin(h).count('1')
            if hour_bits > turnedOn:
                continue
            for m in range(60):
                minute_bits = bin(m).count('1')
                if hour_bits + minute_bits == turnedOn:
                    result.append(f"{h}:{m:02d}")
        return result
```

## Python3

```python
from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

char** readBinaryWatch(int turnedOn, int* returnSize) {
    const int maxTimes = 12 * 60; // 720
    char **result = (char **)malloc(maxTimes * sizeof(char *));
    int count = 0;
    
    for (int h = 0; h < 12; ++h) {
        for (int m = 0; m < 60; ++m) {
            if (__builtin_popcount((unsigned)h) + __builtin_popcount((unsigned)m) == turnedOn) {
                char *timeStr = (char *)malloc(6); // "hh:mm\0"
                sprintf(timeStr, "%d:%02d", h, m);
                result[count++] = timeStr;
            }
        }
    }
    
    *returnSize = count;
    if (count == 0) {
        free(result);
        return NULL;
    }
    result = (char **)realloc(result, count * sizeof(char *));
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<string> ReadBinaryWatch(int turnedOn)
    {
        var result = new List<string>();
        if (turnedOn < 0 || turnedOn > 8) return result;

        for (int h = 0; h < 12; h++)
        {
            int hourBits = CountBits(h);
            for (int m = 0; m < 60; m++)
            {
                if (hourBits + CountBits(m) == turnedOn)
                {
                    result.Add($"{h}:{m:D2}");
                }
            }
        }

        return result;
    }

    private static int CountBits(int x)
    {
        int cnt = 0;
        while (x > 0)
        {
            cnt += x & 1;
            x >>= 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} turnedOn
 * @return {string[]}
 */
var readBinaryWatch = function(turnedOn) {
    const res = [];
    const bitCount = (n) => {
        let cnt = 0;
        while (n) {
            cnt += n & 1;
            n >>= 1;
        }
        return cnt;
    };
    for (let h = 0; h < 12; ++h) {
        const hb = bitCount(h);
        if (hb > turnedOn) continue;
        for (let m = 0; m < 60; ++m) {
            if (hb + bitCount(m) === turnedOn) {
                res.push(`${h}:${m < 10 ? '0' : ''}${m}`);
            }
        }
    }
    return res;
};
```

## Typescript

```typescript
function readBinaryWatch(turnedOn: number): string[] {
    const result: string[] = [];
    
    const bitCount = (n: number): number => {
        let count = 0;
        while (n) {
            count += n & 1;
            n >>= 1;
        }
        return count;
    };
    
    for (let hour = 0; hour < 12; ++hour) {
        const hourBits = bitCount(hour);
        for (let minute = 0; minute < 60; ++minute) {
            if (hourBits + bitCount(minute) === turnedOn) {
                const minuteStr = minute < 10 ? '0' + minute : '' + minute;
                result.push(`${hour}:${minuteStr}`);
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
     * @param Integer $turnedOn
     * @return String[]
     */
    function readBinaryWatch($turnedOn) {
        $result = [];
        for ($h = 0; $h < 12; $h++) {
            $hourBits = $this->bitCount($h);
            for ($m = 0; $m < 60; $m++) {
                if ($hourBits + $this->bitCount($m) === $turnedOn) {
                    $result[] = sprintf("%d:%02d", $h, $m);
                }
            }
        }
        return $result;
    }

    private function bitCount($n) {
        $count = 0;
        while ($n > 0) {
            $n &= ($n - 1);
            $count++;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func readBinaryWatch(_ turnedOn: Int) -> [String] {
        var result = [String]()
        for hour in 0..<12 {
            for minute in 0..<60 {
                if hour.nonzeroBitCount + minute.nonzeroBitCount == turnedOn {
                    let time = String(format: "%d:%02d", hour, minute)
                    result.append(time)
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
    fun readBinaryWatch(turnedOn: Int): List<String> {
        val result = mutableListOf<String>()
        for (hour in 0..11) {
            for (minute in 0..59) {
                if (Integer.bitCount(hour) + Integer.bitCount(minute) == turnedOn) {
                    val minuteStr = if (minute < 10) "0$minute" else "$minute"
                    result.add("$hour:$minuteStr")
                }
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> readBinaryWatch(int turnedOn) {
    List<String> result = [];
    for (int h = 0; h < 12; ++h) {
      int hourBits = _popCount(h);
      for (int m = 0; m < 60; ++m) {
        if (hourBits + _popCount(m) == turnedOn) {
          String minuteStr = m < 10 ? '0$m' : '$m';
          result.add('$h:$minuteStr');
        }
      }
    }
    return result;
  }

  int _popCount(int n) {
    int count = 0;
    while (n > 0) {
      count += n & 1;
      n >>= 1;
    }
    return count;
  }
}
```

## Golang

```go
import (
	"fmt"
	"math/bits"
)

func readBinaryWatch(turnedOn int) []string {
	var result []string
	for h := 0; h < 12; h++ {
		for m := 0; m < 60; m++ {
			if bits.OnesCount(uint(h))+bits.OnesCount(uint(m)) == turnedOn {
				result = append(result, fmt.Sprintf("%d:%02d", h, m))
			}
		}
	}
	return result
}
```

## Ruby

```ruby
def read_binary_watch(turned_on)
  result = []
  (0..11).each do |hour|
    (0..59).each do |minute|
      if hour.to_s(2).count('1') + minute.to_s(2).count('1') == turned_on
        result << "#{hour}:#{format('%02d', minute)}"
      end
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def readBinaryWatch(turnedOn: Int): List[String] = {
        val res = scala.collection.mutable.ListBuffer[String]()
        for (hour <- 0 to 11) {
            for (minute <- 0 to 59) {
                if (Integer.bitCount(hour) + Integer.bitCount(minute) == turnedOn) {
                    val minuteStr = if (minute < 10) s"0$minute" else minute.toString
                    res += s"$hour:$minuteStr"
                }
            }
        }
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        let mut res = Vec::new();
        if turned_on < 0 || turned_on > 10 {
            return res;
        }
        for h in 0..12 {
            for m in 0..60 {
                if (h.count_ones() + m.count_ones()) as i32 == turned_on {
                    res.push(format!("{}:{:02}", h, m));
                }
            }
        }
        res
    }
}
```

## Racket

```racket
#lang racket
(require racket/bitwise)

(define/contract (read-binary-watch turnedOn)
  (-> exact-integer? (listof string?))
  (if (or (< turnedOn 0) (> turnedOn 10))
      '()
      (let loop ((h 0) (acc '()))
        (if (> h 11)
            (reverse acc)
            (let inner ((m 0) (acc2 acc))
              (if (> m 59)
                  (loop (+ h 1) acc2)
                  (if (= turnedOn (+ (bitwise-bit-count h)
                                     (bitwise-bit-count m)))
                      (inner (+ m 1) (cons (format "~a:~02a" h m) acc2))
                      (inner (+ m 1) acc2))))))))
```

## Erlang

```erlang
-module(solution).
-export([read_binary_watch/1]).

-spec read_binary_watch(TurnedOn :: integer()) -> [unicode:unicode_binary()].
read_binary_watch(TurnedOn) ->
    [format_time(H, M) ||
        H <- lists:seq(0, 11),
        M <- lists:seq(0, 59),
        bit_count(H) + bit_count(M) =:= TurnedOn].

bit_count(0) -> 0;
bit_count(N) when N > 0 ->
    (N band 1) + bit_count(N bsr 1).

format_time(H, M) ->
    MinuteStr = if M < 10 -> "0" ++ integer_to_list(M);
                   true   -> integer_to_list(M)
                end,
    list_to_binary(integer_to_list(H) ++ ":" ++ MinuteStr).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec read_binary_watch(turned_on :: integer) :: [String.t()]
  def read_binary_watch(turned_on) do
    for h <- 0..11,
        m <- 0..59,
        bit_count(h) + bit_count(m) == turned_on,
        do: format_time(h, m)
  end

  defp bit_count(0), do: 0

  defp bit_count(n) do
    (n &&& 1) + bit_count(n >>> 1)
  end

  defp format_time(hour, minute) do
    minute_str = if minute < 10, do: "0#{minute}", else: Integer.to_string(minute)
    "#{hour}:#{minute_str}"
  end
end
```
