# 0389. Find the Difference

## Cpp

```cpp
class Solution {
public:
    char findTheDifference(string s, string t) {
        char diff = 0;
        for (char c : s) diff ^= c;
        for (char c : t) diff ^= c;
        return diff;
    }
};
```

## Java

```java
class Solution {
    public char findTheDifference(String s, String t) {
        int diff = 0;
        for (int i = 0; i < s.length(); i++) {
            diff ^= s.charAt(i);
        }
        for (int i = 0; i < t.length(); i++) {
            diff ^= t.charAt(i);
        }
        return (char) diff;
    }
}
```

## Python

```python
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        diff = 0
        for ch in s:
            diff ^= ord(ch)
        for ch in t:
            diff ^= ord(ch)
        return chr(diff)
```

## Python3

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for ch in s:
            diff ^= ord(ch)
        for ch in t:
            diff ^= ord(ch)
        return chr(diff)
```

## C

```c
char findTheDifference(char* s, char* t) {
    char diff = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        diff ^= s[i];
    }
    for (int i = 0; t[i] != '\0'; ++i) {
        diff ^= t[i];
    }
    return diff;
}
```

## Csharp

```csharp
public class Solution
{
    public char FindTheDifference(string s, string t)
    {
        int diff = 0;
        foreach (char c in s) diff ^= c;
        foreach (char c in t) diff ^= c;
        return (char)diff;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    let diff = 0;
    for (let i = 0; i < s.length; i++) {
        diff ^= s.charCodeAt(i);
    }
    for (let i = 0; i < t.length; i++) {
        diff ^= t.charCodeAt(i);
    }
    return String.fromCharCode(diff);
};
```

## Typescript

```typescript
function findTheDifference(s: string, t: string): string {
    let xor = 0;
    for (const ch of s) xor ^= ch.charCodeAt(0);
    for (const ch of t) xor ^= ch.charCodeAt(0);
    return String.fromCharCode(xor);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return String
     */
    function findTheDifference($s, $t) {
        $xor = 0;
        $lenS = strlen($s);
        for ($i = 0; $i < $lenS; $i++) {
            $xor ^= ord($s[$i]);
        }
        $lenT = strlen($t);
        for ($i = 0; $i < $lenT; $i++) {
            $xor ^= ord($t[$i]);
        }
        return chr($xor);
    }
}
```

## Swift

```swift
class Solution {
    func findTheDifference(_ s: String, _ t: String) -> Character {
        var xorValue: UInt32 = 0
        for scalar in s.unicodeScalars {
            xorValue ^= scalar.value
        }
        for scalar in t.unicodeScalars {
            xorValue ^= scalar.value
        }
        return Character(UnicodeScalar(xorValue)!)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findTheDifference(s: String, t: String): Char {
        var diff = 0
        for (c in s) diff = diff xor c.code
        for (c in t) diff = diff xor c.code
        return diff.toChar()
    }
}
```

## Dart

```dart
class Solution {
  String findTheDifference(String s, String t) {
    int diff = 0;
    for (int i = 0; i < s.length; i++) {
      diff ^= s.codeUnitAt(i);
    }
    for (int i = 0; i < t.length; i++) {
      diff ^= t.codeUnitAt(i);
    }
    return String.fromCharCode(diff);
  }
}
```

## Golang

```go
func findTheDifference(s string, t string) byte {
	var diff byte = 0
	for i := 0; i < len(s); i++ {
		diff ^= s[i]
	}
	for i := 0; i < len(t); i++ {
		diff ^= t[i]
	}
	return diff
}
```

## Ruby

```ruby
def find_the_difference(s, t)
  xor = 0
  s.each_byte { |b| xor ^= b }
  t.each_byte { |b| xor ^= b }
  xor.chr
end
```

## Scala

```scala
object Solution {
    def findTheDifference(s: String, t: String): Char = {
        var xorSum = 0
        for (c <- s) xorSum ^= c.toInt
        for (c <- t) xorSum ^= c.toInt
        xorSum.toChar
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        let mut diff = 0u8;
        for b in s.bytes() {
            diff ^= b;
        }
        for b in t.bytes() {
            diff ^= b;
        }
        diff as char
    }
}
```

## Racket

```racket
(define/contract (find-the-difference s t)
  (-> string? string? char?)
  (let loop-s ((i 0) (acc 0))
    (if (= i (string-length s))
        (let loop-t ((j 0) (acc2 acc))
          (if (= j (string-length t))
              (integer->char acc2)
              (loop-t (+ j 1)
                      (bitwise-xor acc2
                                   (char->integer (string-ref t j))))))
        (loop-s (+ i 1)
                (bitwise-xor acc
                             (char->integer (string-ref s i)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_the_difference/2]).

-spec find_the_difference(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> char().
find_the_difference(S, T) ->
    Xor = fun(List) -> lists:foldl(fun(C, Acc) -> C bxor Acc end, 0, List) end,
    Result = Xor(binary_to_list(T)) bxor Xor(binary_to_list(S)),
    Result.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_the_difference(s :: String.t(), t :: String.t()) :: String.t()
  def find_the_difference(s, t) do
    s_list = :binary.bin_to_list(s)
    t_list = :binary.bin_to_list(t)

    xor =
      Enum.reduce(s_list ++ t_list, 0, fn c, acc ->
        Bitwise.bxor(acc, c)
      end)

    <<xor>>
  end
end
```
