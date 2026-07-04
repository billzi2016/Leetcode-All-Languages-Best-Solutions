# 0680. Valid Palindrome II

## Cpp

```cpp
class Solution {
public:
    bool validPalindrome(string s) {
        int left = 0, right = (int)s.size() - 1;
        while (left < right && s[left] == s[right]) {
            ++left;
            --right;
        }
        if (left >= right) return true;
        auto isPal = [&](int l, int r) -> bool {
            while (l < r) {
                if (s[l++] != s[r--]) return false;
            }
            return true;
        };
        return isPal(left + 1, right) || isPal(left, right - 1);
    }
};
```

## Java

```java
class Solution {
    public boolean validPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) == s.charAt(j)) {
                i++;
                j--;
            } else {
                return isPal(s, i + 1, j) || isPal(s, i, j - 1);
            }
        }
        return true;
    }

    private boolean isPal(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1

        if left >= right:
            return True
        return is_pal(left + 1, right) or is_pal(left, right - 1)
```

## Python3

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        return is_pal(left + 1, right) or is_pal(left, right - 1)
```

## C

```c
#include <stdbool.h>
#include <string.h>

static bool isPalindrome(const char *s, int left, int right) {
    while (left < right) {
        if (s[left] != s[right]) return false;
        ++left;
        --right;
    }
    return true;
}

bool validPalindrome(char* s) {
    int n = strlen(s);
    int i = 0, j = n - 1;
    while (i < j && s[i] == s[j]) {
        ++i;
        --j;
    }
    if (i >= j) return true;
    return isPalindrome(s, i + 1, j) || isPalindrome(s, i, j - 1);
}
```

## Csharp

```csharp
public class Solution
{
    public bool ValidPalindrome(string s)
    {
        int left = 0;
        int right = s.Length - 1;

        while (left < right && s[left] == s[right])
        {
            left++;
            right--;
        }

        if (left >= right) return true;

        return IsPalindrome(s, left + 1, right) || IsPalindrome(s, left, right - 1);
    }

    private bool IsPalindrome(string s, int left, int right)
    {
        while (left < right)
        {
            if (s[left] != s[right]) return false;
            left++;
            right--;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    const isPal = (left, right) => {
        while (left < right) {
            if (s[left] !== s[right]) return false;
            left++;
            right--;
        }
        return true;
    };
    
    let l = 0, r = s.length - 1;
    while (l < r) {
        if (s[l] === s[r]) {
            l++;
            r--;
        } else {
            return isPal(l + 1, r) || isPal(l, r - 1);
        }
    }
    return true;
};
```

## Typescript

```typescript
function validPalindrome(s: string): boolean {
    const n = s.length;
    let i = 0, j = n - 1;
    while (i < j) {
        if (s[i] === s[j]) {
            i++;
            j--;
        } else {
            return isPal(i + 1, j) || isPal(i, j - 1);
        }
    }
    return true;

    function isPal(l: number, r: number): boolean {
        while (l < r) {
            if (s[l] !== s[r]) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function validPalindrome($s) {
        $left = 0;
        $right = strlen($s) - 1;

        while ($left < $right) {
            if ($s[$left] === $s[$right]) {
                $left++;
                $right--;
            } else {
                return $this->isPalindromeRange($s, $left + 1, $right) ||
                       $this->isPalindromeRange($s, $left, $right - 1);
            }
        }

        return true;
    }

    private function isPalindromeRange($s, $i, $j) {
        while ($i < $j) {
            if ($s[$i] !== $s[$j]) {
                return false;
            }
            $i++;
            $j--;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func validPalindrome(_ s: String) -> Bool {
        let chars = Array(s)
        var left = 0
        var right = chars.count - 1
        
        while left < right && chars[left] == chars[right] {
            left += 1
            right -= 1
        }
        if left >= right { return true }
        
        func isPal(_ l: Int, _ r: Int) -> Bool {
            var i = l
            var j = r
            while i < j {
                if chars[i] != chars[j] {
                    return false
                }
                i += 1
                j -= 1
            }
            return true
        }
        
        return isPal(left + 1, right) || isPal(left, right - 1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validPalindrome(s: String): Boolean {
        var left = 0
        var right = s.length - 1
        while (left < right) {
            if (s[left] == s[right]) {
                left++
                right--
            } else {
                return isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1)
            }
        }
        return true
    }

    private fun isPalindrome(s: String, l: Int, r: Int): Boolean {
        var left = l
        var right = r
        while (left < right) {
            if (s[left] != s[right]) return false
            left++
            right--
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool validPalindrome(String s) {
    int left = 0;
    int right = s.length - 1;

    while (left < right && s[left] == s[right]) {
      left++;
      right--;
    }

    if (left >= right) return true;

    return _isPal(s, left + 1, right) || _isPal(s, left, right - 1);
  }

  bool _isPal(String s, int left, int right) {
    while (left < right && s[left] == s[right]) {
      left++;
      right--;
    }
    return left >= right;
  }
}
```

## Golang

```go
func validPalindrome(s string) bool {
    isPal := func(l, r int) bool {
        for l < r {
            if s[l] != s[r] {
                return false
            }
            l++
            r--
        }
        return true
    }

    left, right := 0, len(s)-1
    for left < right {
        if s[left] == s[right] {
            left++
            right--
        } else {
            // Try skipping either left or right character
            return isPal(left+1, right) || isPal(left, right-1)
        }
    }
    return true
}
```

## Ruby

```ruby
def is_palindrome_range?(s, left, right)
  while left < right
    return false if s[left] != s[right]
    left += 1
    right -= 1
  end
  true
end

# @param {String} s
# @return {Boolean}
def valid_palindrome(s)
  i = 0
  j = s.length - 1
  while i < j
    if s[i] == s[j]
      i += 1
      j -= 1
    else
      return is_palindrome_range?(s, i + 1, j) || is_palindrome_range?(s, i, j - 1)
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def validPalindrome(s: String): Boolean = {
        @inline
        def isPal(l: Int, r: Int): Boolean = {
            var i = l
            var j = r
            while (i < j) {
                if (s.charAt(i) != s.charAt(j)) return false
                i += 1
                j -= 1
            }
            true
        }

        var left = 0
        var right = s.length - 1
        while (left < right) {
            if (s.charAt(left) == s.charAt(right)) {
                left += 1
                right -= 1
            } else {
                return isPal(left + 1, right) || isPal(left, right - 1)
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        let bytes = s.as_bytes();
        let mut left = 0usize;
        let mut right = bytes.len().saturating_sub(1);
        while left < right && bytes[left] == bytes[right] {
            left += 1;
            if right == 0 { break; }
            right -= 1;
        }
        if left >= right {
            return true;
        }

        fn is_palindrome_range(b: &[u8], mut i: usize, mut j: usize) -> bool {
            while i < j {
                if b[i] != b[j] {
                    return false;
                }
                i += 1;
                j -= 1;
            }
            true
        }

        is_palindrome_range(bytes, left + 1, right) || is_palindrome_range(bytes, left, right - 1)
    }
}
```

## Racket

```racket
(define/contract (valid-palindrome s)
  (-> string? boolean?)
  (let* ((len (string-length s))
         (is-pal?
          (lambda (i j)
            (let loop ((l i) (r j))
              (if (>= l r)
                  #t
                  (if (char=? (string-ref s l) (string-ref s r))
                      (loop (+ l 1) (- r 1))
                      #f))))))
    (let loop ((i 0) (j (- len 1)))
      (if (>= i j)
          #t
          (if (char=? (string-ref s i) (string-ref s j))
              (loop (+ i 1) (- j 1))
              (or (is-pal? (+ i 1) j) (is-pal? i (- j 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([valid_palindrome/1]).

-spec valid_palindrome(S :: unicode:unicode_binary()) -> boolean().
valid_palindrome(S) ->
    Len = byte_size(S),
    check(S, 0, Len - 1).

%% Checks the whole string allowing at most one deletion.
check(_Bin, L, R) when L >= R -> true;
check(Bin, L, R) ->
    C1 = binary:at(Bin, L),
    C2 = binary:at(Bin, R),
    if
        C1 == C2 ->
            check(Bin, L + 1, R - 1);
        true ->
            is_palindrome_range(Bin, L + 1, R) orelse
            is_palindrome_range(Bin, L, R - 1)
    end.

%% Checks if the substring Bin[L..R] is a palindrome (no deletions allowed).
is_palindrome_range(_Bin, L, R) when L >= R -> true;
is_palindrome_range(Bin, L, R) ->
    C1 = binary:at(Bin, L),
    C2 = binary:at(Bin, R),
    if
        C1 == C2 ->
            is_palindrome_range(Bin, L + 1, R - 1);
        true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_palindrome(s :: String.t) :: boolean
  def valid_palindrome(s) do
    chars = String.to_charlist(s)
    tuple = List.to_tuple(chars)
    n = tuple_size(tuple)

    check(tuple, 0, n - 1)
  end

  defp check(_t, left, right) when left >= right, do: true

  defp check(t, left, right) do
    if :erlang.element(left + 1, t) == :erlang.element(right + 1, t) do
      check(t, left + 1, right - 1)
    else
      palindrome?(t, left + 1, right) or palindrome?(t, left, right - 1)
    end
  end

  defp palindrome?(_t, left, right) when left >= right, do: true

  defp palindrome?(t, left, right) do
    if :erlang.element(left + 1, t) == :erlang.element(right + 1, t) do
      palindrome?(t, left + 1, right - 1)
    else
      false
    end
  end
end
```
