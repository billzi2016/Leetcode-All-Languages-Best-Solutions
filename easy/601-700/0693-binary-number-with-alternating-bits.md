# 0693. Binary Number with Alternating Bits

## Cpp

```cpp
class Solution {
public:
    bool hasAlternatingBits(int n) {
        int prev = n & 1;
        n >>= 1;
        while (n) {
            int cur = n & 1;
            if (cur == prev) return false;
            prev = cur;
            n >>= 1;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean hasAlternatingBits(int n) {
        int x = n ^ (n >> 1);
        return (x & (x + 1)) == 0;
    }
}
```

## Python

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
```

## Python3

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
```

## C

```c
#include <stdbool.h>

bool hasAlternatingBits(int n) {
    unsigned int x = (unsigned int)n ^ ((unsigned int)n >> 1);
    return (x & (x + 1)) == 0;
}
```

## Csharp

```csharp
public class Solution {
    public bool HasAlternatingBits(int n) {
        int prev = n & 1;
        n >>= 1;
        while (n > 0) {
            int cur = n & 1;
            if (cur == prev) return false;
            prev = cur;
            n >>= 1;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var hasAlternatingBits = function(n) {
    let prev = n & 1;
    n >>= 1;
    while (n !== 0) {
        const cur = n & 1;
        if (cur === prev) return false;
        prev = cur;
        n >>= 1;
    }
    return true;
};
```

## Typescript

```typescript
function hasAlternatingBits(n: number): boolean {
    const x = n ^ (n >> 1);
    return (x & (x + 1)) === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function hasAlternatingBits($n) {
        $prev = -1;
        while ($n > 0) {
            $cur = $n & 1;
            if ($prev !== -1 && $cur === $prev) {
                return false;
            }
            $prev = $cur;
            $n >>= 1;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func hasAlternatingBits(_ n: Int) -> Bool {
        var prev = n & 1
        var m = n >> 1
        while m > 0 {
            let cur = m & 1
            if cur == prev { return false }
            prev = cur
            m >>= 1
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hasAlternatingBits(n: Int): Boolean {
        val x = n xor (n shr 1)
        return (x and (x + 1)) == 0
    }
}
```

## Dart

```dart
class Solution {
  bool hasAlternatingBits(int n) {
    int prev = n & 1;
    n >>= 1;
    while (n > 0) {
      int cur = n & 1;
      if (cur == prev) return false;
      prev = cur;
      n >>= 1;
    }
    return true;
  }
}
```

## Golang

```go
func hasAlternatingBits(n int) bool {
	prev := -1
	for n > 0 {
		cur := n & 1
		if prev != -1 && cur == prev {
			return false
		}
		prev = cur
		n >>= 1
	}
	return true
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def has_alternating_bits(n)
  x = n ^ (n >> 1)
  ((x + 1) & x).zero?
end
```

## Scala

```scala
object Solution {
    def hasAlternatingBits(n: Int): Boolean = {
        var num = n
        var prev = -1
        while (num > 0) {
            val cur = num & 1
            if (prev != -1 && cur == prev) return false
            prev = cur
            num >>= 1
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn has_alternating_bits(n: i32) -> bool {
        let n = n as u32;
        let x = n ^ (n >> 1);
        (x & (x + 1)) == 0
    }
}
```

## Racket

```racket
(define/contract (has-alternating-bits n)
  (-> exact-integer? boolean?)
  (let loop ((prev (bitwise-and n 1))
             (m (arithmetic-shift n -1)))
    (if (= m 0)
        #t
        (let ((cur (bitwise-and m 1)))
          (if (= cur prev)
              #f
              (loop cur (arithmetic-shift m -1)))))))
```

## Erlang

```erlang
-spec has_alternating_bits(N :: integer()) -> boolean().
has_alternating_bits(N) ->
    First = N band 1,
    check(N bsr 1, First).

check(0, _Prev) -> true;
check(N, Prev) ->
    Cur = N band 1,
    if Cur == Prev -> false;
       true -> check(N bsr 1, Cur)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec has_alternating_bits(n :: integer) :: boolean
  def has_alternating_bits(n) do
    x = Bitwise.bxor(n, Bitwise.bsr(n, 1))
    Bitwise.band(x, x + 1) == 0
  end
end
```
