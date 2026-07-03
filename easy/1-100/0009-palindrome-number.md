# 0009. Palindrome Number

## Cpp

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        // Negative numbers and numbers ending with 0 (but not zero itself) cannot be palindromes
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        
        int reversedHalf = 0;
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }
        // For odd length numbers, discard the middle digit by reversedHalf/10
        return x == reversedHalf || x == reversedHalf / 10;
    }
};
```

## Java

```java
class Solution {
    public boolean isPalindrome(int x) {
        // Negative numbers are not palindrome
        if (x < 0) return false;
        // Numbers ending with 0 that are not zero itself cannot be palindrome
        if (x != 0 && x % 10 == 0) return false;

        int reversedHalf = 0;
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }
        // For odd length numbers, discard the middle digit by reversedHalf/10
        return x == reversedHalf || x == reversedHalf / 10;
    }
}
```

## Python

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
```

## Python3

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False
        # Numbers ending with 0 (but not 0 itself) cannot be palindrome
        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even length numbers, x should equal reversed_half.
        # For odd length, ignore the middle digit by reversed_half//10.
        return x == reversed_half or x == reversed_half // 10
```

## C

```c
#include <stdbool.h>

bool isPalindrome(int x) {
    if (x < 0) return false;
    int reverted = 0;
    while (x > reverted) {
        reverted = reverted * 10 + x % 10;
        x /= 10;
    }
    return x == reverted || x == reverted / 10;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;

        int reversedHalf = 0;
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }

        // For numbers with odd number of digits, discard the middle digit before comparison
        return x == reversedHalf || x == reversedHalf / 10;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0 || (x % 10 === 0 && x !== 0)) return false;
    let reverted = 0;
    while (x > reverted) {
        reverted = reverted * 10 + (x % 10);
        x = Math.floor(x / 10);
    }
    return x === reverted || x === Math.floor(reverted / 10);
};
```

## Typescript

```typescript
function isPalindrome(x: number): boolean {
    if (x < 0 || (x % 10 === 0 && x !== 0)) return false;
    let rev = 0;
    while (x > rev) {
        rev = rev * 10 + (x % 10);
        x = Math.trunc(x / 10);
    }
    return x === rev || x === Math.trunc(rev / 10);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        if ($x < 0 || ($x % 10 == 0 && $x != 0)) {
            return false;
        }
        $reverted = 0;
        while ($x > $reverted) {
            $reverted = $reverted * 10 + $x % 10;
            $x = intdiv($x, 10);
        }
        return $x == $reverted || $x == intdiv($reverted, 10);
    }
}
```

## Swift

```swift
class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        // Negative numbers and numbers ending with 0 (but not zero itself) cannot be palindromes
        if x < 0 || (x % 10 == 0 && x != 0) {
            return false
        }
        
        var original = x
        var reversedHalf = 0
        
        // Build the reversed number only for half of the digits
        while original > reversedHalf {
            reversedHalf = reversedHalf * 10 + original % 10
            original /= 10
        }
        
        // For even length numbers, original == reversedHalf
        // For odd length numbers, ignore the middle digit by reversedHalf/10
        return original == reversedHalf || original == reversedHalf / 10
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPalindrome(x: Int): Boolean {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false
        var reverted = 0
        var n = x
        while (n > reverted) {
            reverted = reverted * 10 + n % 10
            n /= 10
        }
        return n == reverted || n == reverted / 10
    }
}
```

## Dart

```dart
class Solution {
  bool isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) return false;
    int reverted = 0;
    while (x > reverted) {
      reverted = reverted * 10 + x % 10;
      x ~/= 10;
    }
    return x == reverted || x == reverted ~/ 10;
  }
}
```

## Golang

```go
func isPalindrome(x int) bool {
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}
	reversed := 0
	for x > reversed {
		reversed = reversed*10 + x%10
		x /= 10
	}
	return x == reversed || x == reversed/10
}
```

## Ruby

```ruby
def is_palindrome(x)
  return false if x < 0
  s = x.to_s
  s == s.reverse
end
```

## Scala

```scala
object Solution {
    def isPalindrome(x: Int): Boolean = {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false
        var original = x
        var rev = 0
        while (original > rev) {
            rev = rev * 10 + original % 10
            original /= 10
        }
        original == rev || original == rev / 10
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 || (x % 10 == 0 && x != 0) {
            return false;
        }
        let mut n = x;
        let mut rev = 0i32;
        while n > rev {
            rev = rev * 10 + n % 10;
            n /= 10;
        }
        n == rev || n == rev / 10
    }
}
```

## Racket

```racket
(define/contract (is-palindrome x)
  (-> exact-integer? boolean?)
  (cond
    [(negative? x) #false]
    [(= x 0) #true]
    [(and (= (modulo x 10) 0) (not (= x 0))) #false]
    [else
     (let loop ((n x) (rev 0))
       (if (> rev n)
           (or (= rev n) (= (quotient rev 10) n))
           (loop (quotient n 10)
                 (+ (* rev 10) (modulo n 10)))))]))
```

## Erlang

```erlang
-spec is_palindrome(X :: integer()) -> boolean().
is_palindrome(X) when X < 0 ->
    false;
is_palindrome(X) ->
    List = integer_to_list(X),
    List =:= lists:reverse(List).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_palindrome(x :: integer) :: boolean
  def is_palindrome(x) when x < 0, do: false
  def is_palindrome(x) do
    s = Integer.to_string(x)
    s == String.reverse(s)
  end
end
```
