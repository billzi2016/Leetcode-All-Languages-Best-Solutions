# 0342. Power of Four

## Cpp

```cpp
class Solution {
public:
    bool isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0x55555555);
    }
};
```

## Java

```java
class Solution {
    public boolean isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0x55555555) != 0;
    }
}
```

## Python

```python
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
```

## Python3

```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
```

## C

```c
bool isPowerOfFour(int n) {
    return n > 0 && (n & (n - 1)) == 0 && (n & 0x55555555) != 0;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsPowerOfFour(int n)
    {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0x55555555) != 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    return n > 0 && (n & (n - 1)) === 0 && (n & 0x55555555) !== 0;
};
```

## Typescript

```typescript
function isPowerOfFour(n: number): boolean {
    return n > 0 && (n & (n - 1)) === 0 && (n & 0x55555555) !== 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isPowerOfFour($n) {
        if ($n <= 0) {
            return false;
        }
        // Must be a power of two: only one bit set
        if (($n & ($n - 1)) != 0) {
            return false;
        }
        // The single set bit must be at an even position (mask 0x55555555)
        return ($n & 0x55555555) != 0;
    }
}
```

## Swift

```swift
class Solution {
    func isPowerOfFour(_ n: Int) -> Bool {
        if n <= 0 { return false }
        if (n & (n - 1)) != 0 { return false }
        let mask = 0x55555555
        return (n & mask) == n
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPowerOfFour(n: Int): Boolean {
        if (n <= 0) return false
        // Check that n has only one bit set.
        if ((n and (n - 1)) != 0) return false
        // The single set bit must be at an even position.
        val mask = 0x55555555.toInt() // binary: 010101...
        return (n and mask) != 0
    }
}
```

## Dart

```dart
class Solution {
  bool isPowerOfFour(int n) {
    if (n <= 0) return false;
    if ((n & (n - 1)) != 0) return false;
    const int mask = 0x55555555;
    return (n & mask) != 0;
  }
}
```

## Golang

```go
func isPowerOfFour(n int) bool {
	if n <= 0 {
		return false
	}
	// Check that only one bit is set.
	if n&(n-1) != 0 {
		return false
	}
	// Mask with bits set at positions 0,2,4,... (i.e., powers of four).
	const mask = 0x55555555
	return n&mask != 0
}
```

## Ruby

```ruby
def is_power_of_four(n)
  return false if n <= 0
  (n & (n - 1)) == 0 && (n & 0x55555555) != 0
end
```

## Scala

```scala
object Solution {
    def isPowerOfFour(n: Int): Boolean = {
        n > 0 && ((n & (n - 1)) == 0) && ((n & 0x55555555) != 0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_power_of_four(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        (n & (n - 1)) == 0 && (n & 0x5555_5555) != 0
    }
}
```

## Racket

```racket
(define/contract (is-power-of-four n)
  (-> exact-integer? boolean?)
  (and (> n 0)
       (= (bitwise-and n (- n 1)) 0)
       (= (bitwise-and n #x55555555) n)))
```

## Erlang

```erlang
-module(solution).
-export([is_power_of_four/1]).

-spec is_power_of_four(N :: integer()) -> boolean().
is_power_of_four(N) when N > 0 ->
    is_pow_four(N);
is_power_of_four(_)-> false.

is_pow_four(1) -> true;
is_pow_four(N) when N rem 4 =:= 0 ->
    is_pow_four(N div 4);
is_pow_four(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_power_of_four(n :: integer) :: boolean
  def is_power_of_four(n) when n > 0 do
    import Bitwise
    (n &&& (n - 1)) == 0 and (n &&& 0x55555555) != 0
  end

  def is_power_of_four(_), do: false
end
```
