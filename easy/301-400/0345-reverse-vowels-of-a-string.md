# 0345. Reverse Vowels of a String

## Cpp

```cpp
class Solution {
public:
    string reverseVowels(string s) {
        auto isVowel = [](char c) -> bool {
            switch (c) {
                case 'a': case 'e': case 'i': case 'o': case 'u':
                case 'A': case 'E': case 'I': case 'O': case 'U':
                    return true;
                default:
                    return false;
            }
        };
        int i = 0, j = (int)s.size() - 1;
        while (i < j) {
            while (i < j && !isVowel(s[i])) ++i;
            while (i < j && !isVowel(s[j])) --j;
            if (i < j) {
                swap(s[i], s[j]);
                ++i;
                --j;
            }
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        int i = 0, j = chars.length - 1;
        while (i < j) {
            while (i < j && !isVowel(chars[i])) i++;
            while (i < j && !isVowel(chars[j])) j--;
            if (i < j) {
                char tmp = chars[i];
                chars[i] = chars[j];
                chars[j] = tmp;
                i++;
                j--;
            }
        }
        return new String(chars);
    }

    private boolean isVowel(char c) {
        switch (Character.toLowerCase(c)) {
            case 'a': case 'e': case 'i': case 'o': case 'u':
                return true;
            default:
                return false;
        }
    }
}
```

## Python

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        chars = list(s)
        i, j = 0, len(chars) - 1
        while i < j:
            while i < j and chars[i] not in vowels:
                i += 1
            while i < j and chars[j] not in vowels:
                j -= 1
            if i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return ''.join(chars)
```

## Python3

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        chars = list(s)
        i, j = 0, len(chars) - 1
        while i < j:
            while i < j and chars[i] not in vowels:
                i += 1
            while i < j and chars[j] not in vowels:
                j -= 1
            if i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return ''.join(chars)
```

## C

```c
#include <string.h>
#include <stdbool.h>

static bool isVowel(char c) {
    switch (c) {
        case 'a': case 'e': case 'i': case 'o': case 'u':
        case 'A': case 'E': case 'I': case 'O': case 'U':
            return true;
        default:
            return false;
    }
}

char* reverseVowels(char* s) {
    if (!s) return s;
    int left = 0;
    int right = (int)strlen(s) - 1;
    while (left < right) {
        while (left < right && !isVowel(s[left])) left++;
        while (left < right && !isVowel(s[right])) right--;
        if (left < right) {
            char tmp = s[left];
            s[left] = s[right];
            s[right] = tmp;
            left++;
            right--;
        }
    }
    return s;
}
```

## Csharp

```csharp
public class Solution {
    public string ReverseVowels(string s) {
        if (string.IsNullOrEmpty(s)) return s;
        var vowels = new HashSet<char>{'a','e','i','o','u','A','E','I','O','U'};
        char[] chars = s.ToCharArray();
        int left = 0, right = chars.Length - 1;
        while (left < right) {
            while (left < right && !vowels.Contains(chars[left])) left++;
            while (left < right && !vowels.Contains(chars[right])) right--;
            if (left < right) {
                char temp = chars[left];
                chars[left] = chars[right];
                chars[right] = temp;
                left++;
                right--;
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
var reverseVowels = function(s) {
    const vowels = new Set(['a','e','i','o','u','A','E','I','O','U']);
    const arr = s.split('');
    let i = 0, j = arr.length - 1;
    while (i < j) {
        while (i < j && !vowels.has(arr[i])) i++;
        while (i < j && !vowels.has(arr[j])) j--;
        if (i < j) {
            const tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
    }
    return arr.join('');
};
```

## Typescript

```typescript
function reverseVowels(s: string): string {
    const vowels = new Set(['a','e','i','o','u','A','E','I','O','U']);
    const chars = s.split('');
    let i = 0, j = chars.length - 1;
    while (i < j) {
        while (i < j && !vowels.has(chars[i])) i++;
        while (i < j && !vowels.has(chars[j])) j--;
        if (i < j) {
            const temp = chars[i];
            chars[i] = chars[j];
            chars[j] = temp;
            i++;
            j--;
        }
    }
    return chars.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reverseVowels($s) {
        $vowels = [
            'a'=>true, 'e'=>true, 'i'=>true, 'o'=>true, 'u'=>true,
            'A'=>true, 'E'=>true, 'I'=>true, 'O'=>true, 'U'=>true
        ];
        $chars = str_split($s);
        $left = 0;
        $right = count($chars) - 1;

        while ($left < $right) {
            while ($left < $right && !isset($vowels[$chars[$left]])) {
                $left++;
            }
            while ($left < $right && !isset($vowels[$chars[$right]])) {
                $right--;
            }
            if ($left < $right) {
                $tmp = $chars[$left];
                $chars[$left] = $chars[$right];
                $chars[$right] = $tmp;
                $left++;
                $right--;
            }
        }

        return implode('', $chars);
    }
}
```

## Swift

```swift
class Solution {
    func reverseVowels(_ s: String) -> String {
        var chars = Array(s)
        let vowels: Set<Character> = ["a","e","i","o","u","A","E","I","O","U"]
        var left = 0
        var right = chars.count - 1
        
        while left < right {
            while left < right && !vowels.contains(chars[left]) {
                left += 1
            }
            while left < right && !vowels.contains(chars[right]) {
                right -= 1
            }
            if left < right {
                chars.swapAt(left, right)
                left += 1
                right -= 1
            }
        }
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reverseVowels(s: String): String {
        val vowels = setOf('a','e','i','o','u','A','E','I','O','U')
        val chars = s.toCharArray()
        var i = 0
        var j = chars.lastIndex
        while (i < j) {
            while (i < j && chars[i] !in vowels) i++
            while (i < j && chars[j] !in vowels) j--
            if (i < j) {
                val tmp = chars[i]
                chars[i] = chars[j]
                chars[j] = tmp
                i++; j--
            }
        }
        return String(chars)
    }
}
```

## Dart

```dart
class Solution {
  String reverseVowels(String s) {
    const vowels = {'a','e','i','o','u','A','E','I','O','U'};
    List<String> chars = s.split('');
    int i = 0, j = chars.length - 1;
    while (i < j) {
      while (i < j && !vowels.contains(chars[i])) i++;
      while (i < j && !vowels.contains(chars[j])) j--;
      if (i < j) {
        String tmp = chars[i];
        chars[i] = chars[j];
        chars[j] = tmp;
        i++;
        j--;
      }
    }
    return chars.join();
  }
}
```

## Golang

```go
func reverseVowels(s string) string {
	b := []byte(s)
	isVowel := func(c byte) bool {
		switch c {
		case 'a', 'e', 'i', 'o', 'u',
			'A', 'E', 'I', 'O', 'U':
			return true
		}
		return false
	}
	i, j := 0, len(b)-1
	for i < j {
		for i < j && !isVowel(b[i]) {
			i++
		}
		for i < j && !isVowel(b[j]) {
			j--
		}
		if i < j {
			b[i], b[j] = b[j], b[i]
			i++
			j--
		}
	}
	return string(b)
}
```

## Ruby

```ruby
def reverse_vowels(s)
  vowels = "aeiouAEIOU"
  chars = s.chars
  i = 0
  j = chars.length - 1

  while i < j
    i += 1 until i >= j || vowels.include?(chars[i])
    j -= 1 until i >= j || vowels.include?(chars[j])
    break if i >= j
    chars[i], chars[j] = chars[j], chars[i]
    i += 1
    j -= 1
  end

  chars.join
end
```

## Scala

```scala
object Solution {
    def reverseVowels(s: String): String = {
        val vowels = Set('a','e','i','o','u','A','E','I','O','U')
        val chars = s.toCharArray
        var i = 0
        var j = chars.length - 1
        while (i < j) {
            while (i < j && !vowels.contains(chars(i))) i += 1
            while (i < j && !vowels.contains(chars(j))) j -= 1
            if (i < j) {
                val tmp = chars(i)
                chars(i) = chars(j)
                chars(j) = tmp
                i += 1
                j -= 1
            }
        }
        new String(chars)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        fn is_vowel(b: u8) -> bool {
            matches!(b,
                b'a' | b'e' | b'i' | b'o' | b'u' |
                b'A' | b'E' | b'I' | b'O' | b'U')
        }

        let mut bytes = s.into_bytes();
        let (mut i, mut j) = (0usize, bytes.len().saturating_sub(1));
        while i < j {
            while i < j && !is_vowel(bytes[i]) {
                i += 1;
            }
            while i < j && !is_vowel(bytes[j]) {
                if j == 0 { break; } // avoid underflow, though condition prevents it
                j -= 1;
            }
            if i < j {
                bytes.swap(i, j);
                i += 1;
                if j > 0 { j -= 1; }
            }
        }
        String::from_utf8(bytes).unwrap()
    }
}
```

## Racket

```racket
(define (vowel? ch)
  (let ([lc (char-downcase ch)])
    (or (char=? lc #\a)
        (char=? lc #\e)
        (char=? lc #\i)
        (char=? lc #\o)
        (char=? lc #\u))))

(define/contract (reverse-vowels s)
  (-> string? string?)
  (let* ([len (string-length s)]
         [vec (list->vector (string->list s))])
    (let loop ([i 0] [j (- len 1)])
      (when (< i j)
        (cond
          [(not (vowel? (vector-ref vec i))) (loop (+ i 1) j)]
          [(not (vowel? (vector-ref vec j))) (loop i (- j 1))]
          [else
           (let ([tmp (vector-ref vec i)])
             (vector-set! vec i (vector-ref vec j))
             (vector-set! vec j tmp)
             (loop (+ i 1) (- j 1)))])))
    (list->string (vector->list vec))))
```

## Erlang

```erlang
-spec reverse_vowels(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reverse_vowels(S) ->
    Vowels = "aeiouAEIOU",
    CharList = unicode:characters_to_list(S),
    VowelChars = [C || C <- CharList, lists:member(C, Vowels)],
    RevVowelChars = lists:reverse(VowelChars),
    NewCharList = replace(CharList, RevVowelChars, Vowels),
    unicode:characters_to_binary(NewCharList).

replace([], _, _) -> [];
replace([H|T], Rev, V) ->
    case lists:member(H, V) of
        true ->
            [hd(Rev) | replace(T, tl(Rev), V)];
        false ->
            [H | replace(T, Rev, V)]
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_vowels(s :: String.t) :: String.t
  def reverse_vowels(s) do
    vowel_set = MapSet.new(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
    chars = String.graphemes(s)

    rev_vowels =
      chars
      |> Enum.filter(&MapSet.member?(vowel_set, &1))
      |> Enum.reverse()

    {new_chars, _} =
      Enum.map_reduce(chars, rev_vowels, fn ch, acc_rev ->
        if MapSet.member?(vowel_set, ch) do
          [new_ch | rest] = acc_rev
          {new_ch, rest}
        else
          {ch, acc_rev}
        end
      end)

    Enum.join(new_chars)
  end
end
```
