# 0557. Reverse Words in a String III

## Cpp

```cpp
class Solution {
public:
    string reverseWords(string s) {
        int n = s.size();
        int start = 0;
        for (int i = 0; i <= n; ++i) {
            if (i == n || s[i] == ' ') {
                int left = start, right = i - 1;
                while (left < right) {
                    char tmp = s[left];
                    s[left++] = s[right];
                    s[right--] = tmp;
                }
                start = i + 1;
            }
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String reverseWords(String s) {
        char[] chars = s.toCharArray();
        int n = chars.length;
        int start = 0;
        for (int i = 0; i <= n; i++) {
            if (i == n || chars[i] == ' ') {
                int left = start, right = i - 1;
                while (left < right) {
                    char tmp = chars[left];
                    chars[left++] = chars[right];
                    chars[right--] = tmp;
                }
                start = i + 1;
            }
        }
        return new String(chars);
    }
}
```

## Python

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(word[::-1] for word in s.split(' '))
```

## Python3

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split(' '))
```

## C

```c
char* reverseWords(char* s) {
    int i = 0;
    while (s[i]) {
        int start = i;
        while (s[i] && s[i] != ' ') {
            i++;
        }
        int left = start, right = i - 1;
        while (left < right) {
            char tmp = s[left];
            s[left] = s[right];
            s[right] = tmp;
            left++;
            right--;
        }
        if (s[i] == ' ') {
            i++;
        }
    }
    return s;
}
```

## Csharp

```csharp
public class Solution {
    public string ReverseWords(string s) {
        char[] chars = s.ToCharArray();
        int n = chars.Length;
        int start = 0;
        for (int i = 0; i <= n; i++) {
            if (i == n || chars[i] == ' ') {
                int left = start, right = i - 1;
                while (left < right) {
                    char temp = chars[left];
                    chars[left++] = chars[right];
                    chars[right--] = temp;
                }
                start = i + 1;
            }
        }
        return new string(chars);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    return s.split(' ').map(word => word.split('').reverse().join('')).join(' ');
};
```

## Typescript

```typescript
function reverseWords(s: string): string {
    return s
        .split(' ')
        .map(word => word.split('').reverse().join(''))
        .join(' ');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reverseWords($s) {
        $words = explode(' ', $s);
        $words = array_map('strrev', $words);
        return implode(' ', $words);
    }
}
```

## Swift

```swift
class Solution {
    func reverseWords(_ s: String) -> String {
        var chars = Array(s)
        let n = chars.count
        var start = 0
        
        for i in 0...n {
            if i == n || chars[i] == " " {
                var left = start
                var right = i - 1
                while left < right {
                    chars.swapAt(left, right)
                    left += 1
                    right -= 1
                }
                start = i + 1
            }
        }
        
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reverseWords(s: String): String {
        val result = StringBuilder()
        var i = 0
        while (i < s.length) {
            var j = i
            while (j < s.length && s[j] != ' ') j++
            for (k in j - 1 downTo i) {
                result.append(s[k])
            }
            if (j < s.length) {
                result.append(' ')
                j++ // skip the space
            }
            i = j
        }
        return result.toString()
    }
}
```

## Dart

```dart
class Solution {
  String reverseWords(String s) {
    List<String> words = s.split(' ');
    for (int i = 0; i < words.length; i++) {
      words[i] = words[i].split('').reversed.join();
    }
    return words.join(' ');
  }
}
```

## Golang

```go
func reverseWords(s string) string {
    b := []byte(s)
    n := len(b)
    start := 0
    for i := 0; i <= n; i++ {
        if i == n || b[i] == ' ' {
            left, right := start, i-1
            for left < right {
                b[left], b[right] = b[right], b[left]
                left++
                right--
            }
            start = i + 1
        }
    }
    return string(b)
}
```

## Ruby

```ruby
# @param {String} s
# @return {String}
def reverse_words(s)
  s.split(' ').map { |word| word.reverse }.join(' ')
end
```

## Scala

```scala
object Solution {
    def reverseWords(s: String): String = {
        val arr = s.toCharArray
        var start = 0
        for (i <- 0 to arr.length) {
            if (i == arr.length || arr(i) == ' ') {
                var left = start
                var right = i - 1
                while (left < right) {
                    val tmp = arr(left)
                    arr(left) = arr(right)
                    arr(right) = tmp
                    left += 1
                    right -= 1
                }
                start = i + 1
            }
        }
        new String(arr)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_words(s: String) -> String {
        let mut bytes = s.into_bytes();
        let n = bytes.len();
        let mut start = 0usize;
        for i in 0..=n {
            if i == n || bytes[i] == b' ' {
                // reverse the word [start, i-1]
                let mut l = start;
                let mut r = i - 1;
                while l < r {
                    bytes.swap(l, r);
                    l += 1;
                    r -= 1;
                }
                start = i + 1;
            }
        }
        // SAFETY: input is valid UTF-8 and we only swapped bytes.
        unsafe { String::from_utf8_unchecked(bytes) }
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)

(define/contract (reverse-words s)
  (-> string? string?)
  (let* ([words (string-split s " ")]
         [rev-words (map (lambda (w) (list->string (reverse (string->list w)))) words)])
    (string-join rev-words " ")))
```

## Erlang

```erlang
-spec reverse_words(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reverse_words(S) ->
    Words = binary:split(S, <<" ">>, [global]),
    RevWords = lists:map(
        fun(W) ->
            unicode:characters_to_binary(lists:reverse(unicode:characters_to_list(W)))
        end,
        Words),
    iolist_to_binary(join_with_space(RevWords)).

join_with_space([]) -> <<>>;
join_with_space([H|T]) ->
    [H | intersperse_spaces(T)].

intersperse_spaces([]) -> [];
intersperse_spaces([H|T]) ->
    [<<" ">>, H | intersperse_spaces(T)].
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_words(s :: String.t) :: String.t
  def reverse_words(s) do
    s
    |> String.split(" ")
    |> Enum.map(&String.reverse/1)
    |> Enum.join(" ")
  end
end
```
