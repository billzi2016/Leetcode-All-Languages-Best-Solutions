# 0482. License Key Formatting

## Cpp

```cpp
class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        string ans;
        ans.reserve(s.size());
        int cnt = 0;
        for (int i = (int)s.size() - 1; i >= 0; --i) {
            char c = s[i];
            if (c == '-') continue;
            ans.push_back(toupper(c));
            ++cnt;
            if (cnt == k) {
                ans.push_back('-');
                cnt = 0;
            }
        }
        if (!ans.empty() && ans.back() == '-')
            ans.pop_back();
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String licenseKeyFormatting(String s, int k) {
        StringBuilder sb = new StringBuilder();
        int count = 0;
        for (int i = s.length() - 1; i >= 0; --i) {
            char c = s.charAt(i);
            if (c == '-') continue;
            sb.append(Character.toUpperCase(c));
            count++;
            if (count == k) {
                sb.append('-');
                count = 0;
            }
        }
        if (sb.length() > 0 && sb.charAt(sb.length() - 1) == '-') {
            sb.setLength(sb.length() - 1);
        }
        return sb.reverse().toString();
    }
}
```

## Python

```python
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []
        count = 0
        for ch in reversed(s):
            if ch == '-':
                continue
            result.append(ch.upper())
            count += 1
            if count == k:
                result.append('-')
                count = 0
        if result and result[-1] == '-':
            result.pop()
        return ''.join(reversed(result))
```

## Python3

```python
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        parts = []
        count = 0
        for ch in reversed(s):
            if ch == '-':
                continue
            parts.append(ch.upper())
            count += 1
            if count == k:
                parts.append('-')
                count = 0
        if parts and parts[-1] == '-':
            parts.pop()
        return ''.join(reversed(parts))
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* licenseKeyFormatting(char* s, int k) {
    if (!s) return NULL;
    int n = strlen(s);
    int totalChars = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] != '-') totalChars++;
    }
    if (totalChars == 0) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    int dashNeeded = (totalChars - 1) / k;               // number of dashes to insert
    int outLen = totalChars + dashNeeded;                // final length without null terminator

    char *ans = (char*)malloc(outLen + 1);
    ans[outLen] = '\0';

    int idx = outLen;
    int count = 0;
    int insertedDash = 0;

    for (int i = n - 1; i >= 0; --i) {
        char c = s[i];
        if (c == '-') continue;
        if (c >= 'a' && c <= 'z') c = c - 'a' + 'A';
        ans[--idx] = c;
        count++;
        if (count == k && insertedDash < dashNeeded) {
            ans[--idx] = '-';
            insertedDash++;
            count = 0;
        }
    }

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Text;
using System.Linq;

public class Solution {
    public string LicenseKeyFormatting(string s, int k) {
        var sb = new StringBuilder();
        int count = 0;
        for (int i = s.Length - 1; i >= 0; i--) {
            char c = s[i];
            if (c == '-') continue;
            sb.Append(char.ToUpperInvariant(c));
            count++;
            if (count == k) {
                sb.Append('-');
                count = 0;
            }
        }
        if (sb.Length > 0 && sb[sb.Length - 1] == '-')
            sb.Length--; // remove trailing dash
        return new string(sb.ToString().Reverse().ToArray());
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var licenseKeyFormatting = function(s, k) {
    const result = [];
    let count = 0;
    for (let i = s.length - 1; i >= 0; --i) {
        const ch = s[i];
        if (ch === '-') continue;
        result.push(ch.toUpperCase());
        count++;
        if (count === k) {
            result.push('-');
            count = 0;
        }
    }
    if (result.length && result[result.length - 1] === '-') {
        result.pop();
    }
    return result.reverse().join('');
};
```

## Typescript

```typescript
function licenseKeyFormatting(s: string, k: number): string {
    const res: string[] = [];
    let count = 0;
    for (let i = s.length - 1; i >= 0; --i) {
        const ch = s[i];
        if (ch === '-') continue;
        res.push(ch.toUpperCase());
        count++;
        if (count === k) {
            res.push('-');
            count = 0;
        }
    }
    // Remove trailing dash if present
    if (res.length && res[res.length - 1] === '-') {
        res.pop();
    }
    return res.reverse().join('');
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function licenseKeyFormatting($s, $k) {
        $n = strlen($s);
        $ans = '';
        $count = 0;
        for ($i = $n - 1; $i >= 0; --$i) {
            $c = $s[$i];
            if ($c === '-') {
                continue;
            }
            $c = strtoupper($c);
            $ans .= $c;
            $count++;
            if ($count == $k) {
                $ans .= '-';
                $count = 0;
            }
        }
        if ($ans !== '' && $ans[strlen($ans) - 1] === '-') {
            $ans = substr($ans, 0, -1);
        }
        return strrev($ans);
    }
}
```

## Swift

```swift
class Solution {
    func licenseKeyFormatting(_ s: String, _ k: Int) -> String {
        var result = [Character]()
        var count = 0
        for ch in s.reversed() {
            if ch == "-" { continue }
            let upperChar = Character(String(ch).uppercased())
            result.append(upperChar)
            count += 1
            if count == k {
                result.append("-")
                count = 0
            }
        }
        if let last = result.last, last == "-" {
            result.removeLast()
        }
        return String(result.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun licenseKeyFormatting(s: String, k: Int): String {
        val sb = StringBuilder()
        var count = 0
        for (i in s.length - 1 downTo 0) {
            val ch = s[i]
            if (ch == '-') continue
            sb.append(ch.uppercaseChar())
            count++
            if (count == k) {
                sb.append('-')
                count = 0
            }
        }
        if (sb.isNotEmpty() && sb[sb.length - 1] == '-') {
            sb.setLength(sb.length - 1)
        }
        return sb.reverse().toString()
    }
}
```

## Dart

```dart
class Solution {
  String licenseKeyFormatting(String s, int k) {
    StringBuffer sb = StringBuffer();
    int count = 0;
    for (int i = s.length - 1; i >= 0; --i) {
      var ch = s[i];
      if (ch == '-') continue;
      sb.write(ch.toUpperCase());
      count++;
      if (count == k) {
        sb.write('-');
        count = 0;
      }
    }
    String res = sb.toString();
    if (res.isNotEmpty && res.endsWith('-')) {
      res = res.substring(0, res.length - 1);
    }
    return res.split('').reversed.join('');
  }
}
```

## Golang

```go
func licenseKeyFormatting(s string, k int) string {
    var res []byte
    count := 0
    for i := len(s) - 1; i >= 0; i-- {
        c := s[i]
        if c == '-' {
            continue
        }
        if c >= 'a' && c <= 'z' {
            c = c - ('a' - 'A')
        }
        res = append(res, c)
        count++
        if count == k {
            res = append(res, '-')
            count = 0
        }
    }
    if len(res) > 0 && res[len(res)-1] == '-' {
        res = res[:len(res)-1]
    }
    for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
        res[i], res[j] = res[j], res[i]
    }
    return string(res)
}
```

## Ruby

```ruby
def license_key_formatting(s, k)
  count = 0
  res = +''
  s.reverse.each_char do |ch|
    next if ch == '-'
    res << ch.upcase
    count += 1
    if count == k
      res << '-'
      count = 0
    end
  end
  res.chop! if res[-1] == '-'
  res.reverse!
end
```

## Scala

```scala
object Solution {
    def licenseKeyFormatting(s: String, k: Int): String = {
        val sb = new StringBuilder
        var cnt = 0
        var i = s.length - 1
        while (i >= 0) {
            val ch = s.charAt(i)
            if (ch != '-') {
                sb.append(ch.toUpper)
                cnt += 1
                if (cnt == k) {
                    sb.append('-')
                    cnt = 0
                }
            }
            i -= 1
        }
        if (sb.nonEmpty && sb.last == '-') {
            sb.setLength(sb.length - 1)
        }
        sb.reverse.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn license_key_formatting(s: String, k: i32) -> String {
        let k = k as usize;
        let mut count = 0usize;
        let mut rev = String::new();

        for ch in s.chars().rev() {
            if ch == '-' {
                continue;
            }
            rev.push(ch.to_ascii_uppercase());
            count += 1;
            if count == k {
                rev.push('-');
                count = 0;
            }
        }

        // Remove trailing dash if present
        if rev.ends_with('-') {
            rev.pop();
        }

        let mut chars: Vec<char> = rev.chars().collect();
        chars.reverse();
        chars.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (license-key-formatting s k)
  (-> string? exact-integer? string?)
  (let* ((len (string-length s))
         (rev '())
         (count 0))
    (for ([i (in-range (sub1 len) -1 -1)])
      (let ((c (string-ref s i)))
        (when (not (char=? c #\-))
          (set! rev (cons (char-upcase c) rev))
          (set! count (+ count 1))
          (when (= count k)
            (set! rev (cons #\- rev))
            (set! count 0)))))
    (when (and (pair? rev) (char=? (car rev) #\-))
      (set! rev (cdr rev)))
    (list->string rev)))
```

## Erlang

```erlang
-module(solution).
-export([license_key_formatting/2]).

-spec license_key_formatting(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
license_key_formatting(S, K) ->
    CleanRev = clean_rev(S, []),
    FormedRev = group_rev(CleanRev, K, 0, []),
    ResultList = lists:reverse(FormedRev),
    list_to_binary(ResultList).

clean_rev(<<>>, Acc) -> Acc;
clean_rev(<<C, Rest/binary>>, Acc) ->
    case C of
        $- -> clean_rev(Rest, Acc);
        _ when $a =< C, C =< $z -> clean_rev(Rest, [(C - 32) | Acc]);
        _ -> clean_rev(Rest, [C | Acc])
    end.

group_rev([], _, _, Out) -> Out;
group_rev([C|Rest], K, Count, Out) ->
    NewOut = [C | Out],
    NewCount = Count + 1,
    case {NewCount, Rest} of
        {K, []} ->
            group_rev(Rest, K, 0, NewOut);
        {K, _} ->
            group_rev(Rest, K, 0, [$- | NewOut]);
        _ ->
            group_rev(Rest, K, NewCount, NewOut)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec license_key_formatting(s :: String.t(), k :: integer) :: String.t()
  def license_key_formatting(s, k) do
    clean = s |> String.replace("-", "") |> String.upcase()
    len = String.length(clean)

    if len == 0 do
      ""
    else
      first_len = rem(len, k)
      chars = String.graphemes(clean)

      groups =
        if first_len == 0 do
          Enum.chunk_every(chars, k)
        else
          {first, rest} = Enum.split(chars, first_len)
          [first | Enum.chunk_every(rest, k)]
        end

      groups
      |> Enum.map(&Enum.join/1)
      |> Enum.join("-")
    end
  end
end
```
