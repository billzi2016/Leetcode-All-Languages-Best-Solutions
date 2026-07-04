# 0387. First Unique Character in a String

## Cpp

```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        int cnt[26] = {0};
        for (char c : s) ++cnt[c - 'a'];
        for (int i = 0; i < (int)s.size(); ++i) {
            if (cnt[s[i] - 'a'] == 1) return i;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        int n = s.length();
        for (int i = 0; i < n; i++) {
            count[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < n; i++) {
            if (count[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = [0] * 26
        base = ord('a')
        for ch in s:
            counts[ord(ch) - base] += 1
        for i, ch in enumerate(s):
            if counts[ord(ch) - base] == 1:
                return i
        return -1
```

## Python3

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = [0] * 26
        base = ord('a')
        for ch in s:
            counts[ord(ch) - base] += 1
        for i, ch in enumerate(s):
            if counts[ord(ch) - base] == 1:
                return i
        return -1
```

## C

```c
int firstUniqChar(char* s) {
    if (!s) return -1;
    int cnt[26] = {0};
    for (int i = 0; s[i]; ++i) {
        cnt[s[i] - 'a']++;
    }
    for (int i = 0; s[i]; ++i) {
        if (cnt[s[i] - 'a'] == 1) return i;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int FirstUniqChar(string s)
    {
        int[] count = new int[26];
        foreach (char c in s)
        {
            count[c - 'a']++;
        }

        for (int i = 0; i < s.Length; i++)
        {
            if (count[s[i] - 'a'] == 1)
                return i;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const freq = new Array(26).fill(0);
    const aCode = 'a'.charCodeAt(0);
    
    for (let i = 0; i < s.length; i++) {
        freq[s.charCodeAt(i) - aCode]++;
    }
    
    for (let i = 0; i < s.length; i++) {
        if (freq[s.charCodeAt(i) - aCode] === 1) return i;
    }
    return -1;
};
```

## Typescript

```typescript
function firstUniqChar(s: string): number {
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        cnt[s.charCodeAt(i) - 97]++;
    }
    for (let i = 0; i < s.length; ++i) {
        if (cnt[s.charCodeAt(i) - 97] === 1) return i;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function firstUniqChar($s) {
        $len = strlen($s);
        $cnt = array_fill(0, 26, 0);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($s[$i]) - 97;
            $cnt[$idx]++;
        }
        for ($i = 0; $i < $len; $i++) {
            if ($cnt[ord($s[$i]) - 97] === 1) {
                return $i;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func firstUniqChar(_ s: String) -> Int {
        var counts = [Int](repeating: 0, count: 26)
        let chars = Array(s)
        for ch in chars {
            if let val = ch.asciiValue {
                let idx = Int(val - Character("a").asciiValue!)
                counts[idx] += 1
            }
        }
        for (i, ch) in chars.enumerated() {
            if let val = ch.asciiValue {
                let idx = Int(val - Character("a").asciiValue!)
                if counts[idx] == 1 {
                    return i
                }
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun firstUniqChar(s: String): Int {
        val count = IntArray(26)
        for (ch in s) {
            count[ch - 'a']++
        }
        for ((i, ch) in s.withIndex()) {
            if (count[ch - 'a'] == 1) return i
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int firstUniqChar(String s) {
    List<int> count = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      count[s.codeUnitAt(i) - 97]++;
    }
    for (int i = 0; i < s.length; i++) {
      if (count[s.codeUnitAt(i) - 97] == 1) return i;
    }
    return -1;
  }
}
```

## Golang

```go
func firstUniqChar(s string) int {
    var count [26]int
    for i := 0; i < len(s); i++ {
        count[s[i]-'a']++
    }
    for i := 0; i < len(s); i++ {
        if count[s[i]-'a'] == 1 {
            return i
        }
    }
    return -1
}
```

## Ruby

```ruby
def first_uniq_char(s)
  counts = Array.new(26, 0)
  s.each_byte { |b| counts[b - 97] += 1 }
  s.each_byte.with_index do |b, i|
    return i if counts[b - 97] == 1
  end
  -1
end
```

## Scala

```scala
object Solution {
    def firstUniqChar(s: String): Int = {
        val counts = new Array[Int](26)
        for (c <- s) {
            counts(c - 'a') += 1
        }
        for (i <- s.indices) {
            if (counts(s(i) - 'a') == 1) return i
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut cnt = [0usize; 26];
        for &b in bytes {
            cnt[(b - b'a') as usize] += 1;
        }
        for (i, &b) in bytes.iter().enumerate() {
            if cnt[(b - b'a') as usize] == 1 {
                return i as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (first-uniq-char s)
  (-> string? exact-integer?)
  (let* ((len (string-length s))
         (cnt (make-vector 26 0)))
    ;; Count occurrences of each character
    (for ([i (in-range len)])
      (let* ((ch (char->integer (string-ref s i)))
             (idx (- ch (char->integer #\a))))
        (vector-set! cnt idx (+ 1 (vector-ref cnt idx)))))
    ;; Find first unique character
    (let loop ((i 0))
      (if (>= i len)
          -1
          (let* ((ch (char->integer (string-ref s i)))
                 (idx (- ch (char->integer #\a))))
            (if (= 1 (vector-ref cnt idx))
                i
                (loop (+ i 1)))))))
```

## Erlang

```erlang
-spec first_uniq_char(S :: unicode:unicode_binary()) -> integer().
first_uniq_char(S) ->
    List = binary_to_list(S),
    FreqMap = build_freq(List, #{}),
    find_first_unique(List, 0, FreqMap).

build_freq([], M) -> M;
build_freq([C|Rest], M) ->
    Updated = maps:update_with(C,
                               fun(V) -> V + 1 end,
                               1,
                               M),
    build_freq(Rest, Updated).

find_first_unique([], _Idx, _M) -> -1;
find_first_unique([C|Rest], Idx, M) ->
    case maps:get(C, M) of
        1 -> Idx;
        _ -> find_first_unique(Rest, Idx + 1, M)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec first_uniq_char(s :: String.t()) :: integer()
  def first_uniq_char(s) do
    chars = String.to_charlist(s)

    freq =
      Enum.reduce(chars, %{}, fn c, acc ->
        Map.update(acc, c, 1, &(&1 + 1))
      end)

    Enum.with_index(chars)
    |> Enum.find_value(-1, fn {c, idx} -> if Map.get(freq, c) == 1, do: idx, else: nil end)
  end
end
```
