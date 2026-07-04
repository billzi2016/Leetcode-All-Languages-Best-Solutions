# 0409. Longest Palindrome

## Cpp

```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        vector<int> cnt(128, 0);
        for (char c : s) cnt[(int)c]++;
        int ans = 0;
        bool hasOdd = false;
        for (int v : cnt) {
            ans += (v / 2) * 2;
            if (v % 2) hasOdd = true;
        }
        if (hasOdd) ++ans;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestPalindrome(String s) {
        int[] freq = new int[128];
        for (char c : s.toCharArray()) {
            freq[c]++;
        }
        int length = 0;
        boolean hasOdd = false;
        for (int count : freq) {
            if ((count & 1) == 0) {
                length += count;
            } else {
                length += count - 1;
                hasOdd = true;
            }
        }
        return hasOdd ? length + 1 : length;
    }
}
```

## Python

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd_chars = set()
        length = 0
        for ch in s:
            if ch in odd_chars:
                odd_chars.remove(ch)
                length += 2
            else:
                odd_chars.add(ch)
        if odd_chars:
            length += 1
        return length
```

## Python3

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        length = 0
        for ch in s:
            if ch in seen:
                seen.remove(ch)
                length += 2
            else:
                seen.add(ch)
        if seen:
            length += 1
        return length
```

## C

```c
int longestPalindrome(char* s) {
    int res = 0;
    int odd[128] = {0};
    for (char *p = s; *p != '\0'; ++p) {
        unsigned char c = (unsigned char)*p;
        if (odd[c]) {
            odd[c] = 0;
            res += 2;
        } else {
            odd[c] = 1;
        }
    }
    for (int i = 0; i < 128; ++i) {
        if (odd[i]) {
            return res + 1;
        }
    }
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestPalindrome(string s)
    {
        var unmatched = new HashSet<char>();
        int length = 0;
        foreach (char c in s)
        {
            if (!unmatched.Add(c))
            {
                unmatched.Remove(c);
                length += 2;
            }
        }
        if (unmatched.Count > 0)
            length++;
        return length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    const unmatched = new Set();
    let length = 0;
    for (const ch of s) {
        if (unmatched.has(ch)) {
            unmatched.delete(ch);
            length += 2;
        } else {
            unmatched.add(ch);
        }
    }
    if (unmatched.size > 0) {
        length += 1;
    }
    return length;
};
```

## Typescript

```typescript
function longestPalindrome(s: string): number {
    const unmatched = new Set<string>();
    let length = 0;
    for (const ch of s) {
        if (unmatched.has(ch)) {
            unmatched.delete(ch);
            length += 2;
        } else {
            unmatched.add(ch);
        }
    }
    if (unmatched.size > 0) {
        length += 1;
    }
    return length;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function longestPalindrome($s) {
        $set = [];
        $len = 0;
        $chars = str_split($s);
        foreach ($chars as $c) {
            if (isset($set[$c])) {
                unset($set[$c]);
                $len += 2;
            } else {
                $set[$c] = true;
            }
        }
        if (!empty($set)) {
            $len += 1;
        }
        return $len;
    }
}
```

## Swift

```swift
class Solution {
    func longestPalindrome(_ s: String) -> Int {
        var unmatched = Set<Character>()
        var length = 0
        for ch in s {
            if unmatched.contains(ch) {
                unmatched.remove(ch)
                length += 2
            } else {
                unmatched.insert(ch)
            }
        }
        if !unmatched.isEmpty {
            length += 1
        }
        return length
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestPalindrome(s: String): Int {
        val unmatched = HashSet<Char>()
        var length = 0
        for (c in s) {
            if (!unmatched.add(c)) {
                unmatched.remove(c)
                length += 2
            }
        }
        return if (unmatched.isNotEmpty()) length + 1 else length
    }
}
```

## Dart

```dart
class Solution {
  int longestPalindrome(String s) {
    final Set<String> unmatched = {};
    int length = 0;
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      if (unmatched.contains(ch)) {
        unmatched.remove(ch);
        length += 2;
      } else {
        unmatched.add(ch);
      }
    }
    if (unmatched.isNotEmpty) {
      length += 1;
    }
    return length;
  }
}
```

## Golang

```go
func longestPalindrome(s string) int {
    var freq [128]int
    for i := 0; i < len(s); i++ {
        freq[s[i]]++
    }
    length, hasOdd := 0, false
    for _, f := range freq {
        if f%2 == 0 {
            length += f
        } else {
            length += f - 1
            hasOdd = true
        }
    }
    if hasOdd {
        length++
    }
    return length
}
```

## Ruby

```ruby
require 'set'

def longest_palindrome(s)
  seen = Set.new
  length = 0
  s.each_char do |c|
    if seen.include?(c)
      seen.delete(c)
      length += 2
    else
      seen.add(c)
    end
  end
  length + (seen.empty? ? 0 : 1)
end
```

## Scala

```scala
object Solution {
    def longestPalindrome(s: String): Int = {
        val unmatched = scala.collection.mutable.HashSet[Char]()
        var length = 0
        for (c <- s) {
            if (unmatched.contains(c)) {
                unmatched.remove(c)
                length += 2
            } else {
                unmatched.add(c)
            }
        }
        if (unmatched.nonEmpty) length + 1 else length
    }
}
```

## Rust

```rust
use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut set: HashSet<char> = HashSet::new();
        let mut length = 0;
        for ch in s.chars() {
            if set.contains(&ch) {
                set.remove(&ch);
                length += 2;
            } else {
                set.insert(ch);
            }
        }
        if !set.is_empty() {
            length + 1
        } else {
            length
        } as i32
    }
}
```

## Racket

```racket
(define/contract (longest-palindrome s)
  (-> string? exact-integer?)
  (let* ([seen (make-hash)]
         [n (string-length s)])
    (let loop ((i 0) (res 0))
      (if (= i n)
          (if (> (hash-count seen) 0) (+ res 1) res)
          (let ((c (string-ref s i)))
            (if (hash-has-key? seen c)
                (begin
                  (hash-remove! seen c)
                  (loop (+ i 1) (+ res 2)))
                (begin
                  (hash-set! seen c #t)
                  (loop (+ i 1) res))))))))
```

## Erlang

```erlang
-spec longest_palindrome(S :: unicode:unicode_binary()) -> integer().
longest_palindrome(S) ->
    longest_palindrome(S, #{}, 0).

longest_palindrome(<<>>, Set, Res) ->
    case maps:size(Set) of
        0 -> Res;
        _ -> Res + 1
    end;
longest_palindrome(<<C, Rest/binary>>, Set, Res) ->
    case maps:is_key(C, Set) of
        true ->
            longest_palindrome(Rest, maps:remove(C, Set), Res + 2);
        false ->
            longest_palindrome(Rest, maps:put(C, true, Set), Res)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_palindrome(s :: String.t()) :: integer()
  def longest_palindrome(s) do
    {len, odd_set} =
      String.graphemes(s)
      |> Enum.reduce({0, MapSet.new()}, fn ch, {acc, set} ->
        if MapSet.member?(set, ch) do
          {acc + 2, MapSet.delete(set, ch)}
        else
          {acc, MapSet.put(set, ch)}
        end
      end)

    if MapSet.size(odd_set) > 0, do: len + 1, else: len
  end
end
```
