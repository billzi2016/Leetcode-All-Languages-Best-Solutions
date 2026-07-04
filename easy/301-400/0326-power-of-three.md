# 0326. Power of Three

## Cpp

```cpp
class Solution {
public:
    bool isPowerOfThree(int n) {
        const int maxPower = 1162261467; // 3^19, largest power of three within 32-bit signed int
        return n > 0 && maxPower % n == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean isPowerOfThree(int n) {
        if (n <= 0) return false;
        while (n % 3 == 0) {
            n /= 3;
        }
        return n == 1;
    }
}
```

## Python

```python
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0
```

## Python3

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
```

## C

```c
#include <stdbool.h>

bool isPowerOfThree(int n) {
    if (n <= 0) return false;
    while (n % 3 == 0) {
        n /= 3;
    }
    return n == 1;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsPowerOfThree(int n) {
        const int maxPowerOfThree = 1162261467; // 3^19, largest power of three within 32-bit signed int
        return n > 0 && maxPowerOfThree % n == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
    const maxPowerOfThree = 1162261467; // 3^19, largest power of three within 32-bit signed int
    return n > 0 && maxPowerOfThree % n === 0;
};
```

## Typescript

```typescript
function isPowerOfThree(n: number): boolean {
    const maxPower = 1162261467; // 3^19, largest power of three within 32-bit signed int
    return n > 0 && maxPower % n === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isPowerOfThree($n) {
        // Maximum power of three that fits in a 32-bit signed integer: 3^19 = 1162261467
        return ($n > 0 && 1162261467 % $n == 0);
    }
}
```

## Swift

```swift
class Solution {
    func isPowerOfThree(_ n: Int) -> Bool {
        if n <= 0 { return false }
        let maxPower = 1162261467 // 3^19, largest power of three within 32-bit signed int
        return maxPower % n == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPowerOfThree(n: Int): Boolean {
        // Maximum power of three that fits in a 32-bit signed integer: 3^19 = 1162261467
        return n > 0 && 1162261467 % n == 0
    }
}
```

## Dart

```dart
class Solution {
  bool isPowerOfThree(int n) {
    return n > 0 && 1162261467 % n == 0;
  }
}
```

## Golang

```go
func isPowerOfThree(n int) bool {
    if n <= 0 {
        return false
    }
    const maxPower = 1162261467 // 3^19, the largest power of three within 32-bit signed integer range
    return maxPower%n == 0
}
```

## Ruby

```ruby
def is_power_of_three(n)
  n > 0 && 1_162_261_467 % n == 0
end
```

## Scala

```scala
object Solution {
    def isPowerOfThree(n: Int): Boolean = {
        n > 0 && 1162261467 % n == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        const MAX_POWER_OF_THREE: i32 = 1_162_261_467; // 3^19, largest power of three fitting in i32
        n > 0 && MAX_POWER_OF_THREE % n == 0
    }
}
```

## Racket

```racket
(define/contract (is-power-of-three n)
  (-> exact-integer? boolean?)
  (if (<= n 0)
      #false
      (let loop ((x n))
        (cond [(= x 1) #true]
              [(zero? (remainder x 3)) (loop (/ x 3))]
              [else #false]))))
```

## Erlang

```erlang
-spec is_power_of_three(N :: integer()) -> boolean().
is_power_of_three(N) when N > 0 ->
    case N of
        1 -> true;
        _ when N rem 3 =:= 0 -> is_power_of_three(N div 3);
        _ -> false
    end;
is_power_of_three(_)->false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_power_of_three(n :: integer) :: boolean
  def is_power_of_three(n) when n > 0 do
    max_pow = 1_162_261_467
    rem(max_pow, n) == 0
  end

  def is_power_of_three(_), do: false
end
```
