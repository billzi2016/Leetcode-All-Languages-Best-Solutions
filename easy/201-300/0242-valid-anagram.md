# 0242. Valid Anagram

## Cpp

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        int cnt[26] = {0};
        for (char c : s) ++cnt[c - 'a'];
        for (char c : t) {
            if (--cnt[c - 'a'] < 0) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int c : count) {
            if (c != 0) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for ch in t:
            idx = ord(ch) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False
        return True
```

## Python3

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        for ch in t:
            idx = ord(ch) - ord('a')
            counts[idx] -= 1
            if counts[idx] < 0:
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool isAnagram(char* s, char* t) {
    size_t len_s = strlen(s);
    size_t len_t = strlen(t);
    if (len_s != len_t) return false;

    int count[26] = {0};
    for (size_t i = 0; i < len_s; ++i) {
        count[s[i] - 'a']++;
        count[t[i] - 'a']--;
    }

    for (int i = 0; i < 26; ++i) {
        if (count[i] != 0) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;
        int[] count = new int[26];
        foreach (char c in s) {
            count[c - 'a']++;
        }
        foreach (char c in t) {
            if (--count[c - 'a'] < 0) return false;
        }
        return true;
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
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    const counts = new Array(26).fill(0);
    const aCode = 'a'.charCodeAt(0);
    
    for (let i = 0; i < s.length; ++i) {
        counts[s.charCodeAt(i) - aCode]++;
    }
    for (let i = 0; i < t.length; ++i) {
        const idx = t.charCodeAt(i) - aCode;
        if (--counts[idx] < 0) return false;
    }
    return true;
};
```

## Typescript

```typescript
function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        cnt[s.charCodeAt(i) - 97]++;
        cnt[t.charCodeAt(i) - 97]--;
    }
    for (const v of cnt) if (v !== 0) return false;
    return true;
};
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isAnagram($s, $t) {
        if (strlen($s) !== strlen($t)) {
            return false;
        }

        $counts = [];

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (!isset($counts[$c])) {
                $counts[$c] = 0;
            }
            $counts[$c]++;
        }

        $len = strlen($t);
        for ($i = 0; $i < $len; $i++) {
            $c = $t[$i];
            if (!isset($counts[$c])) {
                return false;
            }
            $counts[$c]--;
            if ($counts[$c] < 0) {
                return false;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        if s.count != t.count { return false }
        var counts = [Int](repeating: 0, count: 26)
        let aValue = UnicodeScalar("a").value
        for scalar in s.unicodeScalars {
            let idx = Int(scalar.value - aValue)
            counts[idx] += 1
        }
        for scalar in t.unicodeScalars {
            let idx = Int(scalar.value - aValue)
            counts[idx] -= 1
            if counts[idx] < 0 { return false }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        if (s.length != t.length) return false
        val count = IntArray(26)
        for (c in s) {
            count[c - 'a']++
        }
        for (c in t) {
            val idx = c - 'a'
            count[idx]--
            if (count[idx] < 0) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isAnagram(String s, String t) {
    if (s.length != t.length) return false;
    const int aCode = 97; // 'a'.codeUnitAt(0)
    List<int> count = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      count[s.codeUnitAt(i) - aCode]++;
      count[t.codeUnitAt(i) - aCode]--;
    }
    for (int c in count) {
      if (c != 0) return false;
    }
    return true;
  }
}
```

## Golang

```go
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	var count [26]int
	for i := 0; i < len(s); i++ {
		count[s[i]-'a']++
		count[t[i]-'a']--
	}
	for _, v := range count {
		if v != 0 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def is_anagram(s, t)
  return false unless s.length == t.length
  counts = Array.new(26, 0)
  s.each_byte { |b| counts[b - 97] += 1 }
  t.each_byte { |b| counts[b - 97] -= 1 }
  counts.all?(&:zero?)
end
```

## Scala

```scala
object Solution {
    def isAnagram(s: String, t: String): Boolean = {
        if (s.length != t.length) return false
        val count = new Array[Int](26)
        var i = 0
        while (i < s.length) {
            count(s.charAt(i) - 'a') += 1
            count(t.charAt(i) - 'a') -= 1
            i += 1
        }
        var j = 0
        while (j < 26) {
            if (count(j) != 0) return false
            j += 1
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut cnt = [0i32; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        for b in t.bytes() {
            cnt[(b - b'a') as usize] -= 1;
        }
        cnt.iter().all(|&x| x == 0)
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (is-anagram s t)
  (-> string? string? boolean?)
  (if (= (string-length s) (string-length t))
      (let* ([sorted-s (list->string (sort (string->list s) char<?))]
             [sorted-t (list->string (sort (string->list t) char<?))])
        (equal? sorted-s sorted-t))
      #false))
```

## Erlang

```erlang
-module(solution).
-export([is_anagram/2]).

-spec is_anagram(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> boolean().
is_anagram(S, T) ->
    if byte_size(S) =/= byte_size(T) ->
            false;
       true ->
            CountMap = count_chars(S, #{}),
            check_anagram(T, CountMap)
    end.

count_chars(<<>>, Map) ->
    Map;
count_chars(<<C/utf8, Rest/binary>>, Map) ->
    NewMap = maps:update_with(C,
                              fun(V) -> V + 1 end,
                              1,
                              Map),
    count_chars(Rest, NewMap).

check_anagram(<<>>, Map) ->
    maps:size(Map) =:= 0;
check_anagram(<<C/utf8, Rest/binary>>, Map) ->
    case maps:find(C, Map) of
        error ->
            false;
        {ok, 1} ->
            NewMap = maps:remove(C, Map),
            check_anagram(Rest, NewMap);
        {ok, V} when V > 1 ->
            NewMap = maps:put(C, V - 1, Map),
            check_anagram(Rest, NewMap)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_anagram(s :: String.t(), t :: String.t()) :: boolean()
  def is_anagram(s, t) do
    if byte_size(s) != byte_size(t), do: false, else
      count_chars(s) == count_chars(t)
    end
  end

  defp count_chars(str) do
    str
    |> String.to_charlist()
    |> Enum.reduce(%{}, fn cp, acc ->
         Map.update(acc, cp, 1, &(&1 + 1))
       end)
  end
end
```
