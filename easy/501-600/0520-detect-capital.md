# 0520. Detect Capital

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool detectCapitalUse(string word) {
        int n = word.size();
        if (n == 0) return true;
        
        bool allUpper = true, allLower = true;
        for (char c : word) {
            if (!isupper(c)) allUpper = false;
            if (!islower(c)) allLower = false;
        }
        bool firstUpperRestLower = isupper(word[0]);
        for (int i = 1; i < n && firstUpperRestLower; ++i) {
            if (!islower(word[i])) firstUpperRestLower = false;
        }
        return allUpper || allLower || firstUpperRestLower;
    }
};
```

## Java

```java
class Solution {
    public boolean detectCapitalUse(String word) {
        int upperCount = 0;
        for (int i = 0; i < word.length(); i++) {
            if (Character.isUpperCase(word.charAt(i))) {
                upperCount++;
            }
        }
        int n = word.length();
        return upperCount == n || upperCount == 0 || (upperCount == 1 && Character.isUpperCase(word.charAt(0)));
    }
}
```

## Python

```python
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())
```

## Python3

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())
```

## C

```c
#include <stdbool.h>

bool detectCapitalUse(char* word) {
    bool allUpper = true;
    bool allLower = true;
    bool firstUpperRestLower = true;

    for (int i = 0; word[i] != '\0'; ++i) {
        char c = word[i];
        if (c >= 'A' && c <= 'Z') {
            allLower = false;
            if (i > 0) firstUpperRestLower = false;
        } else { // lowercase
            allUpper = false;
            if (i == 0) firstUpperRestLower = false;
        }
    }

    return allUpper || allLower || firstUpperRestLower;
}
```

## Csharp

```csharp
public class Solution
{
    public bool DetectCapitalUse(string word)
    {
        int n = word.Length;
        int caps = 0;
        foreach (char c in word)
        {
            if (char.IsUpper(c))
                caps++;
        }

        if (caps == n) return true;               // all uppercase
        if (caps == 0) return true;               // all lowercase
        if (caps == 1 && char.IsUpper(word[0]))   // only first letter uppercase
            return true;

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    if (word === word.toUpperCase()) return true;
    if (word === word.toLowerCase()) return true;
    return word[0] === word[0].toUpperCase() && word.slice(1) === word.slice(1).toLowerCase();
};
```

## Typescript

```typescript
function detectCapitalUse(word: string): boolean {
    const allUpper = word === word.toUpperCase();
    const allLower = word === word.toLowerCase();
    const firstUpperRestLower = word[0] === word[0].toUpperCase() && word.slice(1) === word.slice(1).toLowerCase();
    return allUpper || allLower || firstUpperRestLower;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Boolean
     */
    function detectCapitalUse($word) {
        if (preg_match('/^[A-Z]+$/', $word)) {
            return true;
        }
        if (preg_match('/^[a-z]+$/', $word)) {
            return true;
        }
        if (preg_match('/^[A-Z][a-z]*$/', $word)) {
            return true;
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func detectCapitalUse(_ word: String) -> Bool {
        if word == word.uppercased() { return true }
        if word == word.lowercased() { return true }
        let first = word.prefix(1)
        let rest = word.dropFirst()
        return first == first.uppercased() && rest == rest.lowercased()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun detectCapitalUse(word: String): Boolean {
        if (word.all { it.isUpperCase() }) return true
        if (word.all { it.isLowerCase() }) return true
        if (word[0].isUpperCase() && word.drop(1).all { it.isLowerCase() }) return true
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool detectCapitalUse(String word) {
    if (word.isEmpty) return true;
    bool allUpper = word == word.toUpperCase();
    bool allLower = word == word.toLowerCase();
    bool firstUpperRestLower = word[0] == word[0].toUpperCase() &&
        word.substring(1) == word.substring(1).toLowerCase();
    return allUpper || allLower || firstUpperRestLower;
  }
}
```

## Golang

```go
package main

import "unicode"

func detectCapitalUse(word string) bool {
	upperCount := 0
	for _, ch := range word {
		if unicode.IsUpper(ch) {
			upperCount++
		}
	}
	n := len(word)
	if upperCount == n || upperCount == 0 {
		return true
	}
	if upperCount == 1 && unicode.IsUpper(rune(word[0])) {
		return true
	}
	return false
}
```

## Ruby

```ruby
# @param {String} word
# @return {Boolean}
def detect_capital_use(word)
  word == word.upcase ||
    word == word.downcase ||
    (word[0] == word[0].upcase && word[1..-1] == word[1..-1].downcase)
end
```

## Scala

```scala
object Solution {
    def detectCapitalUse(word: String): Boolean = {
        val allUpper = word == word.toUpperCase
        val allLower = word == word.toLowerCase
        val firstUpperRestLower = word.head.isUpper && (word.tail == word.tail.toLowerCase)
        allUpper || allLower || firstUpperRestLower
    }
}
```

## Rust

```rust
impl Solution {
    pub fn detect_capital_use(word: String) -> bool {
        let bytes = word.as_bytes();
        let n = bytes.len();
        let mut upper_cnt = 0;
        for &b in bytes {
            if b.is_ascii_uppercase() {
                upper_cnt += 1;
            }
        }
        if upper_cnt == n || upper_cnt == 0 {
            return true;
        }
        if upper_cnt == 1 && bytes[0].is_ascii_uppercase() {
            return true;
        }
        false
    }
}
```

## Racket

```racket
#lang racket
(require racket/string
         racket/list)

(define/contract (detect-capital-use word)
  (-> string? boolean?)
  (define (uppercase? c) (char=? c (char-upcase c)))
  (define (lowercase? c) (char=? c (char-downcase c)))
  (let ((len (string-length word)))
    (cond
      [(andmap uppercase? (in-string word)) #t]
      [(andmap lowercase? (in-string word)) #t]
      [else
       (and (> len 0)
            (uppercase? (string-ref word 0))
            (let loop ((i 1))
              (or (= i len)
                  (and (lowercase? (string-ref word i))
                       (loop (+ i 1))))))])))
```

## Erlang

```erlang
-spec detect_capital_use(Word :: unicode:unicode_binary()) -> boolean().
detect_capital_use(Word) ->
    L = binary_to_list(Word),
    is_all_upper(L) orelse is_all_lower(L) orelse is_capitalized(L).

is_all_upper([]) -> true;
is_all_upper([C|Rest]) when C >= $A, C =< $Z -> is_all_upper(Rest);
is_all_upper(_) -> false.

is_all_lower([]) -> true;
is_all_lower([C|Rest]) when C >= $a, C =< $z -> is_all_lower(Rest);
is_all_lower(_) -> false.

is_capitalized([First|Rest]) when First >= $A, First =< $Z ->
    is_all_lower(Rest);
is_capitalized(_)-> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec detect_capital_use(word :: String.t()) :: boolean()
  def detect_capital_use(word) do
    up = String.upcase(word)
    down = String.downcase(word)

    cond do
      word == up -> true
      word == down -> true
      first_upper?(word) and rest_lower?(word) -> true
      true -> false
    end
  end

  defp first_upper?(<<first, _rest::binary>>) when first >= ?A and first <= ?Z, do: true
  defp first_upper?(_), do: false

  defp rest_lower?(word) do
    case String.slice(word, 1..-1) do
      "" -> true
      rest ->
        Enum.all?(String.to_charlist(rest), fn c -> c >= ?a and c <= ?z end)
    end
  end
end
```
