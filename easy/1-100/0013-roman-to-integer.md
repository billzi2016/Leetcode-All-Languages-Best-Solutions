# 0013. Roman to Integer

## Cpp

```cpp
class Solution {
public:
    int romanToInt(string s) {
        static const unordered_map<char,int> val = {
            {'I',1},{'V',5},{'X',10},{'L',50},
            {'C',100},{'D',500},{'M',1000}
        };
        int total = 0;
        int maxSeen = 0;
        for (int i = s.size() - 1; i >= 0; --i) {
            int cur = val.at(s[i]);
            if (cur < maxSeen)
                total -= cur;
            else {
                total += cur;
                maxSeen = cur;
            }
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public int romanToInt(String s) {
        int total = 0;
        int prevValue = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            int value;
            switch (s.charAt(i)) {
                case 'I': value = 1; break;
                case 'V': value = 5; break;
                case 'X': value = 10; break;
                case 'L': value = 50; break;
                case 'C': value = 100; break;
                case 'D': value = 500; break;
                default:  value = 1000; // 'M'
            }
            if (value < prevValue) {
                total -= value;
            } else {
                total += value;
                prevValue = value;
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for ch in reversed(s):
            cur = vals[ch]
            if cur < prev:
                total -= cur
            else:
                total += cur
                prev = cur
        return total
```

## Python3

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        total = 0
        max_seen = 0
        for ch in reversed(s):
            val = values[ch]
            if val < max_seen:
                total -= val
            else:
                total += val
                max_seen = val
        return total
```

## C

```c
#include <string.h>

static int value(char c) {
    switch (c) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
    }
    return 0;
}

int romanToInt(char* s) {
    int total = 0, prev = 0;
    int len = strlen(s);
    for (int i = len - 1; i >= 0; --i) {
        int cur = value(s[i]);
        if (cur < prev)
            total -= cur;
        else {
            total += cur;
            prev = cur;
        }
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int RomanToInt(string s) {
        var values = new Dictionary<char, int> {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int total = 0;
        int prev = 0;
        for (int i = s.Length - 1; i >= 0; i--) {
            int cur = values[s[i]];
            if (cur < prev) {
                total -= cur;
            } else {
                total += cur;
                prev = cur;
            }
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };
    let total = 0;
    let prev = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        const cur = map[s[i]];
        if (cur < prev) {
            total -= cur;
        } else {
            total += cur;
        }
        prev = cur;
    }
    return total;
};
```

## Typescript

```typescript
function romanToInt(s: string): number {
    const valueMap: { [key: string]: number } = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    };
    let total = 0;
    for (let i = 0; i < s.length; i++) {
        const cur = valueMap[s[i]];
        const next = i + 1 < s.length ? valueMap[s[i + 1]] : 0;
        if (cur < next) {
            total -= cur;
        } else {
            total += cur;
        }
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function romanToInt($s) {
        $map = [
            'I' => 1,
            'V' => 5,
            'X' => 10,
            'L' => 50,
            'C' => 100,
            'D' => 500,
            'M' => 1000
        ];
        $total = 0;
        $prev = 0;
        for ($i = strlen($s) - 1; $i >= 0; $i--) {
            $curr = $map[$s[$i]];
            if ($curr < $prev) {
                $total -= $curr;
            } else {
                $total += $curr;
            }
            $prev = $curr;
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func romanToInt(_ s: String) -> Int {
        let values: [Character: Int] = ["I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000]
        var total = 0
        let chars = Array(s)
        for i in 0..<chars.count {
            let cur = values[chars[i]]!
            if i + 1 < chars.count, let next = values[chars[i + 1]], cur < next {
                total -= cur
            } else {
                total += cur
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun romanToInt(s: String): Int {
        val values = mapOf(
            'I' to 1,
            'V' to 5,
            'X' to 10,
            'L' to 50,
            'C' to 100,
            'D' to 500,
            'M' to 1000
        )
        var total = 0
        var prev = 0
        for (i in s.length - 1 downTo 0) {
            val cur = values[s[i]] ?: 0
            if (cur < prev) {
                total -= cur
            } else {
                total += cur
                prev = cur
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int romanToInt(String s) {
    const Map<String, int> values = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
    };
    int total = 0;
    int prev = 0;
    for (int i = s.length - 1; i >= 0; --i) {
      int cur = values[s[i]]!;
      if (cur < prev) {
        total -= cur;
      } else {
        total += cur;
        if (cur > prev) prev = cur;
      }
    }
    return total;
  }
}
```

## Golang

```go
func romanToInt(s string) int {
	values := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	total, prev := 0, 0
	for i := len(s) - 1; i >= 0; i-- {
		v := values[s[i]]
		if v < prev {
			total -= v
		} else {
			total += v
			prev = v
		}
	}
	return total
}
```

## Ruby

```ruby
def roman_to_int(s)
  values = {
    'I' => 1,
    'V' => 5,
    'X' => 10,
    'L' => 50,
    'C' => 100,
    'D' => 500,
    'M' => 1000
  }
  total = 0
  prev = 0
  s.chars.reverse_each do |ch|
    cur = values[ch]
    if cur < prev
      total -= cur
    else
      total += cur
      prev = cur
    end
  end
  total
end
```

## Scala

```scala
object Solution {
    def romanToInt(s: String): Int = {
        val values = Map(
            'I' -> 1,
            'V' -> 5,
            'X' -> 10,
            'L' -> 50,
            'C' -> 100,
            'D' -> 500,
            'M' -> 1000
        )
        var total = 0
        var prev = 0
        for (i <- s.length - 1 to 0 by -1) {
            val cur = values(s.charAt(i))
            if (cur < prev) total -= cur else total += cur
            prev = cur
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut total = 0i32;
        let mut prev = 0i32;
        for ch in s.chars().rev() {
            let val = match ch {
                'I' => 1,
                'V' => 5,
                'X' => 10,
                'L' => 50,
                'C' => 100,
                'D' => 500,
                'M' => 1000,
                _ => 0,
            };
            if val < prev {
                total -= val;
            } else {
                total += val;
                if val > prev {
                    prev = val;
                }
            }
        }
        total
    }
}
```

## Racket

```racket
(define/contract (roman-to-int s)
  (-> string? exact-integer?)
  (let ([chars (reverse (string->list s))])
    (let loop ((lst chars) (prev 0) (total 0))
      (if (null? lst)
          total
          (let* ([c (car lst)]
                 [v (case c
                      [(#\I) 1]
                      [(#\V) 5]
                      [(#\X) 10]
                      [(#\L) 50]
                      [(#\C) 100]
                      [(#\D) 500]
                      [(#\M) 1000])])
            (if (< v prev)
                (loop (cdr lst) prev (- total v))
                (loop (cdr lst) v (+ total v))))))))
```

## Erlang

```erlang
-module(solution).
-export([roman_to_int/1]).

-spec roman_to_int(S :: unicode:unicode_binary()) -> integer().
roman_to_int(S) ->
    CharMap = #{ $I => 1,
                $V => 5,
                $X => 10,
                $L => 50,
                $C => 100,
                $D => 500,
                $M => 1000 },
    Chars = unicode:characters_to_list(S),
    RevChars = lists:reverse(Chars),
    process(RevChars, CharMap, 0, 0).

process([], _CharMap, _Prev, Acc) ->
    Acc;
process([H|T], CharMap, Prev, Acc) ->
    Val = maps:get(H, CharMap),
    if
        Val < Prev ->
            process(T, CharMap, Prev, Acc - Val);
        true ->
            process(T, CharMap, Val, Acc + Val)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec roman_to_int(String.t()) :: integer()
  def roman_to_int(s) do
    values = %{
      "I" => 1,
      "V" => 5,
      "X" => 10,
      "L" => 50,
      "C" => 100,
      "D" => 500,
      "M" => 1000
    }

    {result, _} =
      s
      |> String.graphemes()
      |> Enum.reverse()
      |> Enum.reduce({0, 0}, fn ch, {total, last_val} ->
        cur = Map.fetch!(values, ch)

        if cur < last_val do
          {total - cur, last_val}
        else
          {total + cur, cur}
        end
      end)

    result
  end
end
```
