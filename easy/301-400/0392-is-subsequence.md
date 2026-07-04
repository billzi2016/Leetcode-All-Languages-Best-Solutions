# 0392. Is Subsequence

## Cpp

```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        while (i < (int)s.size() && j < (int)t.size()) {
            if (s[i] == t[j]) ++i;
            ++j;
        }
        return i == (int)s.size();
    }
};
```

## Java

```java
class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0, j = 0;
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++;
        }
        return i == s.length();
    }
}
```

## Python

```python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        ls = len(s)
        if ls == 0:
            return True
        for ch in t:
            if ch == s[i]:
                i += 1
                if i == ls:
                    return True
        return False
```

## Python3

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i == len(s):
                break
            if ch == s[i]:
                i += 1
        return i == len(s)
```

## C

```c
#include <stdbool.h>

bool isSubsequence(char* s, char* t) {
    while (*s && *t) {
        if (*s == *t) {
            ++s;
        }
        ++t;
    }
    return *s == '\0';
}
```

## Csharp

```csharp
public class Solution {
    public bool IsSubsequence(string s, string t) {
        int i = 0, j = 0;
        while (i < s.Length && j < t.Length) {
            if (s[i] == t[j]) i++;
            j++;
        }
        return i == s.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let i = 0, j = 0;
    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) i++;
        j++;
    }
    return i === s.length;
};
```

## Typescript

```typescript
function isSubsequence(s: string, t: string): boolean {
    let i = 0, j = 0;
    const m = s.length, n = t.length;
    while (i < m && j < n) {
        if (s.charAt(i) === t.charAt(j)) i++;
        j++;
    }
    return i === m;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isSubsequence($s, $t) {
        $i = 0;
        $lenS = strlen($s);
        $lenT = strlen($t);
        if ($lenS === 0) {
            return true;
        }
        for ($j = 0; $j < $lenT && $i < $lenS; $j++) {
            if ($s[$i] === $t[$j]) {
                $i++;
            }
        }
        return $i === $lenS;
    }
}
```

## Swift

```swift
class Solution {
    func isSubsequence(_ s: String, _ t: String) -> Bool {
        var i = s.startIndex
        var j = t.startIndex
        
        while i != s.endIndex && j != t.endIndex {
            if s[i] == t[j] {
                i = s.index(after: i)
            }
            j = t.index(after: j)
        }
        
        return i == s.endIndex
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isSubsequence(s: String, t: String): Boolean {
        var i = 0
        var j = 0
        while (i < s.length && j < t.length) {
            if (s[i] == t[j]) i++
            j++
        }
        return i == s.length
    }
}
```

## Dart

```dart
class Solution {
  bool isSubsequence(String s, String t) {
    int i = 0;
    int j = 0;
    while (i < s.length && j < t.length) {
      if (s[i] == t[j]) {
        i++;
      }
      j++;
    }
    return i == s.length;
  }
}
```

## Golang

```go
func isSubsequence(s string, t string) bool {
	si, ti := 0, 0
	for si < len(s) && ti < len(t) {
		if s[si] == t[ti] {
			si++
		}
		ti++
	}
	return si == len(s)
}
```

## Ruby

```ruby
def is_subsequence(s, t)
  i = 0
  s_len = s.length
  return true if s_len == 0
  t.each_char do |ch|
    if ch == s[i]
      i += 1
      return true if i == s_len
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def isSubsequence(s: String, t: String): Boolean = {
        var i = 0
        var j = 0
        val n = s.length
        val m = t.length
        while (i < n && j < m) {
            if (s.charAt(i) == t.charAt(j)) i += 1
            j += 1
        }
        i == n
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let s_bytes = s.as_bytes();
        let mut i = 0usize;
        if s_bytes.is_empty() {
            return true;
        }
        for &c in t.as_bytes() {
            if c == s_bytes[i] {
                i += 1;
                if i == s_bytes.len() {
                    break;
                }
            }
        }
        i == s_bytes.len()
    }
}
```

## Racket

```racket
(define/contract (is-subsequence s t)
  (-> string? string? boolean?)
  (let* ((len-s (string-length s))
         (len-t (string-length t)))
    (if (= len-s 0)
        #t
        (let loop ((i 0) (j 0))
          (cond
            [(= i len-s) #t]
            [(= j len-t) #f]
            [else (if (char=? (string-ref s i) (string-ref t j))
                      (loop (+ i 1) (+ j 1))
                      (loop i (+ j 1)))])))))
```

## Erlang

```erlang
-spec is_subsequence(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> boolean().
is_subsequence(S, T) ->
    Sub = unicode:characters_to_list(S),
    Txt = unicode:characters_to_list(T),
    sub(Sub, Txt).

sub([], _) -> true;
sub(_, []) -> false;
sub([H|RestS], [H|RestT]) ->
    sub(RestS, RestT);
sub(S, [_|RestT]) ->
    sub(S, RestT).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_subsequence(s :: String.t(), t :: String.t()) :: boolean()
  def is_subsequence(s, t) do
    check(s, t)
  end

  defp check(<<>>, _), do: true
  defp check(_, <<>>), do: false
  defp check(<<c1::utf8, rest_s::binary>>, <<c2::utf8, rest_t::binary>>) when c1 == c2 do
    check(rest_s, rest_t)
  end
  defp check(s, <<_::utf8, rest_t::binary>>) do
    check(s, rest_t)
  end
end
```
