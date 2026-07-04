# 0434. Number of Segments in a String

## Cpp

```cpp
class Solution {
public:
    int countSegments(string s) {
        int cnt = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            if (s[i] != ' ' && (i == 0 || s[i - 1] == ' '))
                ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countSegments(String s) {
        s = s.trim();
        if (s.isEmpty()) {
            return 0;
        }
        return s.split("\\s+").length;
    }
}
```

## Python

```python
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
```

## Python3

```python
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
```

## C

```c
int countSegments(char* s) {
    int cnt = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] != ' ' && (i == 0 || s[i - 1] == ' '))
            ++cnt;
    }
    return cnt;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountSegments(string s)
    {
        int count = 0;
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] != ' ' && (i == 0 || s[i - 1] == ' '))
                count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
    let count = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== ' ' && (i === 0 || s[i - 1] === ' ')) {
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function countSegments(s: string): number {
    let count = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== ' ' && (i === 0 || s[i - 1] === ' ')) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countSegments($s) {
        $n = strlen($s);
        $count = 0;
        $i = 0;
        while ($i < $n) {
            // Skip leading spaces
            while ($i < $n && $s[$i] === ' ') {
                $i++;
            }
            if ($i < $n) {
                $count++;
                // Skip the current segment
                while ($i < $n && $s[$i] !== ' ') {
                    $i++;
                }
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countSegments(_ s: String) -> Int {
        return s.split(separator: " ", omittingEmptySubsequences: true).count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSegments(s: String): Int {
        var count = 0
        var i = 0
        val n = s.length
        while (i < n) {
            while (i < n && s[i] == ' ') i++
            if (i < n) {
                count++
                while (i < n && s[i] != ' ') i++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countSegments(String s) {
    s = s.trim();
    if (s.isEmpty) return 0;
    return s.split(RegExp(r'\s+')).length;
  }
}
```

## Golang

```go
func countSegments(s string) int {
    cnt := 0
    n := len(s)
    for i := 0; i < n; i++ {
        if s[i] != ' ' && (i == 0 || s[i-1] == ' ') {
            cnt++
        }
    }
    return cnt
}
```

## Ruby

```ruby
def count_segments(s)
  s.split.size
end
```

## Scala

```scala
object Solution {
    def countSegments(s: String): Int = {
        val trimmed = s.trim
        if (trimmed.isEmpty) 0 else trimmed.split("\\s+").length
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_segments(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut count = 0;
        for (i, &b) in bytes.iter().enumerate() {
            if b != b' ' && (i == 0 || bytes[i - 1] == b' ') {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (count-segments s)
  (-> string? exact-integer?)
  (let* ((len (string-length s))
         (cnt
          (let loop ((i 0) (c 0))
            (if (>= i len)
                c
                (let ((ch (string-ref s i)))
                  (if (and (not (char=? ch #\space))
                           (or (= i 0)
                               (char=? (string-ref s (- i 1)) #\space)))
                      (loop (+ i 1) (+ c 1))
                      (loop (+ i 1) c)))))))
    cnt))
```

## Erlang

```erlang
-spec count_segments(S :: unicode:unicode_binary()) -> integer().
count_segments(S) ->
    count_segments(S, 0, true).

count_segments(<<>>, Count, _PrevSpace) ->
    Count;
count_segments(<<C/utf8, Rest/binary>>, Count, PrevSpace) ->
    if C =:= $  ->
            count_segments(Rest, Count, true);
       true ->
            NewCount = case PrevSpace of
                true -> Count + 1;
                false -> Count
            end,
            count_segments(Rest, NewCount, false)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_segments(s :: String.t()) :: integer
  def count_segments(s) do
    s
    |> String.split()
    |> length()
  end
end
```
