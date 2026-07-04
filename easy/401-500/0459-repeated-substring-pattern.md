# 0459. Repeated Substring Pattern

## Cpp

```cpp
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.size();
        vector<int> lps(n, 0);
        for (int i = 1; i < n; ++i) {
            int len = lps[i - 1];
            while (len > 0 && s[i] != s[len]) {
                len = lps[len - 1];
            }
            if (s[i] == s[len]) {
                ++len;
            }
            lps[i] = len;
        }
        int longest = lps[n - 1];
        return longest > 0 && n % (n - longest) == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int n = s.length();
        int[] lps = new int[n];
        for (int i = 1, len = 0; i < n;) {
            if (s.charAt(i) == s.charAt(len)) {
                lps[i++] = ++len;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i++] = 0;
                }
            }
        }
        int longest = lps[n - 1];
        return longest > 0 && n % (n - longest) == 0;
    }
}
```

## Python

```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s + s)[1:-1].find(s) != -1
```

## Python3

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1:-1].find(s) != -1
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool repeatedSubstringPattern(char* s) {
    int n = strlen(s);
    if (n == 0) return false;

    int *lps = (int *)malloc(n * sizeof(int));
    if (!lps) return false; // allocation failure, treat as false

    lps[0] = 0;
    int len = 0;
    for (int i = 1; i < n; ++i) {
        while (len > 0 && s[i] != s[len]) {
            len = lps[len - 1];
        }
        if (s[i] == s[len]) {
            ++len;
        }
        lps[i] = len;
    }

    int longest = lps[n - 1];
    bool result = (longest > 0 && n % (n - longest) == 0);
    free(lps);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public bool RepeatedSubstringPattern(string s) {
        int n = s.Length;
        if (n == 0) return false;
        int[] lps = new int[n];
        for (int i = 1, len = 0; i < n; i++) {
            while (len > 0 && s[i] != s[len]) {
                len = lps[len - 1];
            }
            if (s[i] == s[len]) {
                len++;
                lps[i] = len;
            } else {
                lps[i] = 0;
            }
        }
        int longestPrefixSuffix = lps[n - 1];
        return longestPrefixSuffix > 0 && n % (n - longestPrefixSuffix) == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var repeatedSubstringPattern = function(s) {
    const doubled = s + s;
    const trimmed = doubled.slice(1, -1);
    return trimmed.includes(s);
};
```

## Typescript

```typescript
function repeatedSubstringPattern(s: string): boolean {
    const doubled = s + s;
    return doubled.slice(1, -1).includes(s);
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function repeatedSubstringPattern($s) {
        $double = $s . $s;
        $sub = substr($double, 1, -1);
        return strpos($sub, $s) !== false;
    }
}
?>
```

## Swift

```swift
class Solution {
    func repeatedSubstringPattern(_ s: String) -> Bool {
        let chars = Array(s)
        let n = chars.count
        if n == 0 { return false }
        var lps = [Int](repeating: 0, count: n)
        var length = 0
        var i = 1
        while i < n {
            if chars[i] == chars[length] {
                length += 1
                lps[i] = length
                i += 1
            } else {
                if length != 0 {
                    length = lps[length - 1]
                } else {
                    lps[i] = 0
                    i += 1
                }
            }
        }
        let len = lps[n - 1]
        return len > 0 && n % (n - len) == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun repeatedSubstringPattern(s: String): Boolean {
        val n = s.length
        if (n == 0) return false
        val lps = IntArray(n)
        var len = 0
        var i = 1
        while (i < n) {
            if (s[i] == s[len]) {
                len++
                lps[i] = len
                i++
            } else {
                if (len != 0) {
                    len = lps[len - 1]
                } else {
                    lps[i] = 0
                    i++
                }
            }
        }
        val longestPrefixSuffix = lps[n - 1]
        return longestPrefixSuffix > 0 && n % (n - longestPrefixSuffix) == 0
    }
}
```

## Dart

```dart
class Solution {
  bool repeatedSubstringPattern(String s) {
    if (s.isEmpty) return false;
    String doubled = s + s;
    String sub = doubled.substring(1, doubled.length - 1);
    return sub.contains(s);
  }
}
```

## Golang

```go
import "strings"

func repeatedSubstringPattern(s string) bool {
	if len(s) == 0 {
		return false
	}
	t := s + s
	sub := t[1 : len(t)-1]
	return strings.Contains(sub, s)
}
```

## Ruby

```ruby
# @param {String} s
# @return {Boolean}
def repeated_substring_pattern(s)
  doubled = s + s
  sub = doubled[1...-1]
  sub.include?(s)
end
```

## Scala

```scala
object Solution {
    def repeatedSubstringPattern(s: String): Boolean = {
        val n = s.length
        if (n == 0) return false
        val doubled = s + s
        val sub = doubled.substring(1, doubled.length - 1)
        sub.contains(s)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn repeated_substring_pattern(s: String) -> bool {
        let n = s.len();
        if n == 0 {
            return false;
        }
        let bytes = s.as_bytes();
        let mut lps = vec![0usize; n];
        for i in 1..n {
            let mut len = lps[i - 1];
            while len > 0 && bytes[i] != bytes[len] {
                len = lps[len - 1];
            }
            if bytes[i] == bytes[len] {
                len += 1;
            }
            lps[i] = len;
        }
        let longest = lps[n - 1];
        longest > 0 && n % (n - longest) == 0
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (repeated-substring-pattern s)
  (-> string? boolean?)
  (let* ((doubled (string-append s s))
         (inner (substring doubled 1 (- (string-length doubled) 1))))
    (and (> (string-length s) 0)
         (string-contains? inner s))))
```

## Erlang

```erlang
-module(solution).
-export([repeated_substring_pattern/1]).

-spec repeated_substring_pattern(unicode:unicode_binary()) -> boolean().
repeated_substring_pattern(S) ->
    N = byte_size(S),
    check(N, S, 1).

check(N, S, I) when I =< N div 2 ->
    case N rem I of
        0 ->
            Sub = binary:part(S, {0, I}),
            if is_repeat(Sub, S) -> true;
               true -> check(N, S, I + 1)
            end;
        _ -> check(N, S, I + 1)
    end;
check(_, _, _) -> false.

is_repeat(Sub, Bin) ->
    Sz = byte_size(Sub),
    case Bin of
        <<Sub:Sz/binary, Rest/binary>> -> is_repeat(Sub, Rest);
        <<>> -> true;
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec repeated_substring_pattern(s :: String.t) :: boolean
  def repeated_substring_pattern(s) do
    double = s <> s
    trimmed = binary_part(double, 1, byte_size(double) - 2)
    String.contains?(trimmed, s)
  end
end
```
