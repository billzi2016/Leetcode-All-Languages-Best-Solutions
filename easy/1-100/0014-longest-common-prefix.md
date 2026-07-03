# 0014. Longest Common Prefix

## Cpp

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string prefix = strs[0];
        for (size_t i = 1; i < strs.size(); ++i) {
            while (strs[i].rfind(prefix, 0) != 0) { // prefix not at start
                prefix.pop_back();
                if (prefix.empty()) return "";
            }
        }
        return prefix;
    }
};
```

## Java

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        // Find the length of the shortest string
        int minLen = Integer.MAX_VALUE;
        for (String s : strs) {
            if (s == null) return "";
            minLen = Math.min(minLen, s.length());
        }
        if (minLen == 0) return "";
        // Compare characters column by column
        for (int i = 0; i < minLen; i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (strs[j].charAt(i) != c) {
                    return strs[0].substring(0, i);
                }
            }
        }
        return strs[0].substring(0, minLen);
    }
}
```

## Python

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
```

## Python3

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # Find the shortest string to limit comparisons
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for s in strs:
                if s[i] != ch:
                    return shortest[:i]
        return shortest
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) {
        char *res = (char*)malloc(1);
        res[0] = '\0';
        return res;
    }
    
    int minLen = INT_MAX;
    for (int i = 0; i < strsSize; ++i) {
        int len = strlen(strs[i]);
        if (len < minLen) minLen = len;
    }
    
    int prefixLen = 0;
    for (int idx = 0; idx < minLen; ++idx) {
        char c = strs[0][idx];
        int j;
        for (j = 1; j < strsSize; ++j) {
            if (strs[j][idx] != c) break;
        }
        if (j == strsSize) {
            ++prefixLen;
        } else {
            break;
        }
    }
    
    char *res = (char*)malloc(prefixLen + 1);
    if (prefixLen > 0) memcpy(res, strs[0], prefixLen);
    res[prefixLen] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        if (strs == null || strs.Length == 0) return "";
        // Use the first string as reference
        for (int i = 0; i < strs[0].Length; i++)
        {
            char c = strs[0][i];
            for (int j = 1; j < strs.Length; j++)
            {
                if (i >= strs[j].Length || strs[j][i] != c)
                    return strs[0].Substring(0, i);
            }
        }
        return strs[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (!strs || strs.length === 0) return "";
    let prefix = strs[0];
    for (let i = 1; i < strs.length; i++) {
        while (!strs[i].startsWith(prefix)) {
            prefix = prefix.slice(0, -1);
            if (prefix === "") return "";
        }
    }
    return prefix;
};
```

## Typescript

```typescript
function longestCommonPrefix(strs: string[]): string {
    if (strs.length === 0) return "";
    let prefix = strs[0];
    for (let i = 1; i < strs.length; i++) {
        while (!strs[i].startsWith(prefix)) {
            prefix = prefix.slice(0, -1);
            if (prefix === "") return "";
        }
    }
    return prefix;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        if (empty($strs)) {
            return "";
        }
        $prefix = $strs[0];
        foreach ($strs as $word) {
            while (strpos($word, $prefix) !== 0) {
                $prefix = substr($prefix, 0, -1);
                if ($prefix === "") {
                    return "";
                }
            }
        }
        return $prefix;
    }
}
```

## Swift

```swift
class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        guard var prefix = strs.first else { return "" }
        for i in 1..<strs.count {
            while !strs[i].hasPrefix(prefix) {
                if prefix.isEmpty { return "" }
                prefix.removeLast()
            }
        }
        return prefix
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        if (strs.isEmpty()) return ""
        var prefix = strs[0]
        for (i in 1 until strs.size) {
            while (!strs[i].startsWith(prefix)) {
                if (prefix.isEmpty()) return ""
                prefix = prefix.substring(0, prefix.length - 1)
            }
        }
        return prefix
    }
}
```

## Dart

```dart
class Solution {
  String longestCommonPrefix(List<String> strs) {
    if (strs.isEmpty) return "";
    String prefix = strs[0];
    for (int i = 1; i < strs.length; i++) {
      while (!strs[i].startsWith(prefix)) {
        if (prefix.isEmpty) return "";
        prefix = prefix.substring(0, prefix.length - 1);
      }
    }
    return prefix;
  }
}
```

## Golang

```go
func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	minLen := len(strs[0])
	for _, s := range strs {
		if len(s) < minLen {
			minLen = len(s)
		}
	}
	for i := 0; i < minLen; i++ {
		c := strs[0][i]
		for _, s := range strs {
			if s[i] != c {
				return strs[0][:i]
			}
		}
	}
	return strs[0][:minLen]
}
```

## Ruby

```ruby
def longest_common_prefix(strs)
  return "" if strs.empty?
  shortest = strs.min_by(&:length)
  (0...shortest.length).each do |i|
    ch = shortest[i]
    strs.each do |s|
      return shortest[0...i] if s[i] != ch
    end
  end
  shortest
end
```

## Scala

```scala
object Solution {
  def longestCommonPrefix(strs: Array[String]): String = {
    if (strs == null || strs.isEmpty) return ""
    var prefix = strs(0)
    for (i <- 1 until strs.length) {
      val s = strs(i)
      var j = 0
      val minLen = Math.min(prefix.length, s.length)
      while (j < minLen && prefix.charAt(j) == s.charAt(j)) {
        j += 1
      }
      if (j == 0) return ""
      prefix = prefix.substring(0, j)
    }
    prefix
  }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return "".to_string();
        }
        let first = &strs[0];
        for i in 0..first.len() {
            let c = first.as_bytes()[i];
            for s in strs.iter().skip(1) {
                if i >= s.len() || s.as_bytes()[i] != c {
                    return first[..i].to_string();
                }
            }
        }
        first.clone()
    }
}
```

## Racket

```racket
#lang racket

(require rackunit)

;; Helper: length of longest common prefix between two strings
(define (lcp-length s1 s2)
  (let loop ((i 0)
             (len1 (string-length s1))
             (len2 (string-length s2)))
    (cond [(or (= i len1) (= i len2)) i]
          [(char=? (string-ref s1 i) (string-ref s2 i))
           (loop (+ i 1) len1 len2)]
          [else i])))

;; Main function
(define/contract (longest-common-prefix strs)
  (-> (listof string?) string?)
  (if (null? strs)
      ""
      (let loop ((prefix (car strs)) (rest (cdr strs)))
        (if (null? rest)
            prefix
            (let* ((s (car rest))
                   (len (lcp-length prefix s))
                   (new-prefix (substring prefix 0 len)))
              (if (= len 0)
                  ""
                  (loop new-prefix (cdr rest))))))))

;; Optional tests
(check-equal? (longest-common-prefix '("flower" "flow" "flight")) "fl")
(check-equal? (longest-common-prefix '("dog" "racecar" "car")) "")
(check-equal? (longest-common-prefix '("")) "")
(check-equal? (longest-common-prefix '("single")) "single")
```

## Erlang

```erlang
-module(solution).
-export([longest_common_prefix/1]).

-spec longest_common_prefix([unicode:unicode_binary()]) -> unicode:unicode_binary().
longest_common_prefix(Strs) ->
    case Strs of
        [] -> <<>>;
        [First|Rest] ->
            MinStr = lists:foldl(
                fun(S, Acc) ->
                    if byte_size(S) < byte_size(Acc) -> S; true -> Acc end
                end,
                First,
                Rest),
            MaxLen = byte_size(MinStr),
            PrefixLen = prefix_len(Strs, MaxLen, 0),
            binary:part(MinStr, {0, PrefixLen})
    end.

prefix_len(_Strs, Max, Index) when Index >= Max -> Max;
prefix_len(Strs, Max, Index) ->
    Char = binary:at(lists:nth(1, Strs), Index),
    case lists:all(fun(S) -> binary:at(S, Index) =:= Char end, Strs) of
        true -> prefix_len(Strs, Max, Index + 1);
        false -> Index
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_common_prefix(strs :: [String.t]) :: String.t
  def longest_common_prefix([]), do: ""

  def longest_common_prefix([first | rest]) do
    Enum.reduce(rest, first, fn s, acc -> common_prefix(acc, s) end)
  end

  defp common_prefix(<<>>, _), do: <<>>
  defp common_prefix(_, <<>>), do: <<>>

  defp common_prefix(<<c1, rest1::binary>>, <<c2, rest2::binary>>) when c1 == c2 do
    <<c1>> <> common_prefix(rest1, rest2)
  end

  defp common_prefix(_, _), do: <<>>
end
```
