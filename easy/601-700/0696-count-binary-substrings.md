# 0696. Count Binary Substrings

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countBinarySubstrings(string s) {
        int ans = 0, prev = 0, cur = 1;
        for (int i = 1; i < (int)s.size(); ++i) {
            if (s[i] != s[i - 1]) {
                ans += min(prev, cur);
                prev = cur;
                cur = 1;
            } else {
                ++cur;
            }
        }
        return ans + min(prev, cur);
    }
};
```

## Java

```java
class Solution {
    public int countBinarySubstrings(String s) {
        int ans = 0, prev = 0, cur = 1;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(i - 1)) {
                ans += Math.min(prev, cur);
                prev = cur;
                cur = 1;
            } else {
                cur++;
            }
        }
        ans += Math.min(prev, cur);
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        prev = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return ans + min(prev, cur)
```

## Python3

```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return ans + min(prev, cur)
```

## C

```c
int countBinarySubstrings(char* s) {
    if (!s) return 0;
    int ans = 0, prev = 0, cur = 1;
    for (int i = 1; s[i] != '\0'; ++i) {
        if (s[i] != s[i - 1]) {
            ans += (prev < cur) ? prev : cur;
            prev = cur;
            cur = 1;
        } else {
            ++cur;
        }
    }
    ans += (prev < cur) ? prev : cur;
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    public int CountBinarySubstrings(string s)
    {
        int ans = 0;
        int prev = 0;
        int cur = 1;

        for (int i = 1; i < s.Length; i++)
        {
            if (s[i] != s[i - 1])
            {
                ans += Math.Min(prev, cur);
                prev = cur;
                cur = 1;
            }
            else
            {
                cur++;
            }
        }

        ans += Math.Min(prev, cur);
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countBinarySubstrings = function(s) {
    let ans = 0, prev = 0, cur = 1;
    for (let i = 1; i < s.length; i++) {
        if (s[i] !== s[i - 1]) {
            ans += Math.min(prev, cur);
            prev = cur;
            cur = 1;
        } else {
            cur++;
        }
    }
    return ans + Math.min(prev, cur);
};
```

## Typescript

```typescript
function countBinarySubstrings(s: string): number {
    let ans = 0;
    let prev = 0;
    let cur = 1;
    for (let i = 1; i < s.length; i++) {
        if (s[i] !== s[i - 1]) {
            ans += Math.min(prev, cur);
            prev = cur;
            cur = 1;
        } else {
            cur++;
        }
    }
    ans += Math.min(prev, cur);
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countBinarySubstrings($s) {
        $n = strlen($s);
        if ($n == 0) return 0;
        $prev = 0;
        $cur = 1;
        $ans = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] !== $s[$i - 1]) {
                $ans += min($prev, $cur);
                $prev = $cur;
                $cur = 1;
            } else {
                $cur++;
            }
        }
        return $ans + min($prev, $cur);
    }
}
```

## Swift

```swift
class Solution {
    func countBinarySubstrings(_ s: String) -> Int {
        let chars = Array(s)
        var prev = 0
        var cur = 1
        var ans = 0
        for i in 1..<chars.count {
            if chars[i] != chars[i - 1] {
                ans += min(prev, cur)
                prev = cur
                cur = 1
            } else {
                cur += 1
            }
        }
        ans += min(prev, cur)
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countBinarySubstrings(s: String): Int {
        var ans = 0
        var prev = 0
        var cur = 1
        for (i in 1 until s.length) {
            if (s[i] != s[i - 1]) {
                ans += kotlin.math.min(prev, cur)
                prev = cur
                cur = 1
            } else {
                cur++
            }
        }
        ans += kotlin.math.min(prev, cur)
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countBinarySubstrings(String s) {
    int ans = 0;
    int prev = 0;
    int cur = 1;
    for (int i = 1; i < s.length; i++) {
      if (s[i] != s[i - 1]) {
        ans += prev < cur ? prev : cur;
        prev = cur;
        cur = 1;
      } else {
        cur++;
      }
    }
    ans += prev < cur ? prev : cur;
    return ans;
  }
}
```

## Golang

```go
package main

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func countBinarySubstrings(s string) int {
	ans, prev, cur := 0, 0, 1
	for i := 1; i < len(s); i++ {
		if s[i] != s[i-1] {
			ans += min(prev, cur)
			prev = cur
			cur = 1
		} else {
			cur++
		}
	}
	ans += min(prev, cur)
	return ans
}
```

## Ruby

```ruby
def count_binary_substrings(s)
  ans = 0
  prev = 0
  cur = 1
  (1...s.length).each do |i|
    if s[i] != s[i - 1]
      ans += [prev, cur].min
      prev = cur
      cur = 1
    else
      cur += 1
    end
  end
  ans + [prev, cur].min
end
```

## Scala

```scala
object Solution {
    def countBinarySubstrings(s: String): Int = {
        if (s.isEmpty) return 0
        var ans = 0
        var prev = 0
        var cur = 1
        var i = 1
        while (i < s.length) {
            if (s.charAt(i - 1) != s.charAt(i)) {
                ans += Math.min(prev, cur)
                prev = cur
                cur = 1
            } else {
                cur += 1
            }
            i += 1
        }
        ans + Math.min(prev, cur)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_binary_substrings(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        let mut ans: i32 = 0;
        let mut prev: usize = 0;
        let mut cur: usize = 1;

        for i in 1..n {
            if bytes[i] != bytes[i - 1] {
                ans += std::cmp::min(prev, cur) as i32;
                prev = cur;
                cur = 1;
            } else {
                cur += 1;
            }
        }

        ans + std::cmp::min(prev, cur) as i32
    }
}
```

## Racket

```racket
(define/contract (count-binary-substrings s)
  (-> string? exact-integer?)
  (let ((len (string-length s)))
    (if (= len 0)
        0
        (let loop ((i 1) (ans 0) (prev 0) (cur 1))
          (if (< i len)
              (if (char=? (string-ref s (- i 1)) (string-ref s i))
                  (loop (+ i 1) ans prev (+ cur 1))
                  (let ((new-ans (+ ans (min prev cur))))
                    (loop (+ i 1) new-ans cur 1)))
              (+ ans (min prev cur)))))))
```

## Erlang

```erlang
-module(solution).
-export([count_binary_substrings/1]).

-spec count_binary_substrings(S :: unicode:unicode_binary()) -> integer().
count_binary_substrings(S) ->
    case S of
        <<>> -> 0;
        <<_>> -> 0;
        <<FirstChar:8, Rest/binary>> ->
            loop(Rest, FirstChar, 0, 0, 1)
    end.

loop(<<>>, _PrevChar, Ans, PrevCount, CurCount) ->
    Ans + erlang:min(PrevCount, CurCount);
loop(<<NextChar:8, Rest/binary>>, PrevChar, Ans, PrevCount, CurCount) ->
    if
        NextChar =:= PrevChar ->
            loop(Rest, PrevChar, Ans, PrevCount, CurCount + 1);
        true ->
            NewAns = Ans + erlang:min(PrevCount, CurCount),
            loop(Rest, NextChar, NewAns, CurCount, 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_binary_substrings(s :: String.t()) :: integer()
  def count_binary_substrings(s) do
    chars = String.to_charlist(s)

    case chars do
      [] -> 0
      [first | rest] ->
        helper(rest, first, 0, 1, 0)
    end
  end

  defp helper([], _prev_char, prev_len, cur_len, ans) do
    ans + min(prev_len, cur_len)
  end

  defp helper([c | rest], prev_char, prev_len, cur_len, ans) do
    if c == prev_char do
      helper(rest, prev_char, prev_len, cur_len + 1, ans)
    else
      new_ans = ans + min(prev_len, cur_len)
      helper(rest, c, cur_len, 1, new_ans)
    end
  end
end
```
