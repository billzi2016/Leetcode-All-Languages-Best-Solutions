# 0476. Number Complement

## Cpp

```cpp
class Solution {
public:
    int findComplement(int num) {
        int mask = 0, t = num;
        while (t) {
            mask = (mask << 1) | 1;
            t >>= 1;
        }
        return num ^ mask;
    }
};
```

## Java

```java
class Solution {
    public int findComplement(int num) {
        // Find the mask with all bits set to 1 up to the highest bit of num
        int mask = Integer.highestOneBit(num);
        // If num is exactly a power of two, highestOneBit returns that bit,
        // we need a mask covering that bit as well.
        mask = (mask << 1) - 1;
        return mask ^ num;
    }
}
```

## Python

```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 1
        mask = (1 << num.bit_length()) - 1
        return mask ^ num
```

## Python3

```python
class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        mask = (1 << num.bit_length()) - 1
        return mask ^ num
```

## C

```c
int findComplement(int num) {
    int mask = 1;
    while (mask < num) {
        mask = (mask << 1) | 1;
    }
    return num ^ mask;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindComplement(int num)
    {
        if (num == 0) return 1;
        int mask = 1;
        while (mask < num)
        {
            mask <<= 1;
        }
        mask -= 1;
        return num ^ mask;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    let mask = 0;
    while (mask < num) {
        mask = (mask << 1) | 1;
    }
    return num ^ mask;
};
```

## Typescript

```typescript
function findComplement(num: number): number {
    let mask = 0;
    let temp = num;
    while (temp > 0) {
        mask = (mask << 1) | 1;
        temp >>= 1;
    }
    return mask ^ num;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function findComplement($num) {
        if ($num == 0) {
            return 1;
        }
        $mask = 1;
        while ($mask < $num) {
            $mask = ($mask << 1) | 1;
        }
        return $mask ^ $num;
    }
}
```

## Swift

```swift
class Solution {
    func findComplement(_ num: Int) -> Int {
        var mask = 0
        var n = num
        while n > 0 {
            mask = (mask << 1) | 1
            n >>= 1
        }
        return mask ^ num
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findComplement(num: Int): Int {
        var mask = 0
        var n = num
        while (n > 0) {
            mask = (mask shl 1) or 1
            n = n shr 1
        }
        return mask xor num
    }
}
```

## Dart

```dart
class Solution {
  int findComplement(int num) {
    if (num == 0) return 1;
    int mask = 1;
    while (mask < num) {
      mask = (mask << 1) | 1;
    }
    return mask ^ num;
  }
}
```

## Golang

```go
func findComplement(num int) int {
	if num == 0 {
		return 1
	}
	mask := 1
	for mask < num {
		mask = (mask << 1) | 1
	}
	return mask ^ num
}
```

## Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def find_complement(num)
  return 1 if num == 0
  mask = (1 << num.bit_length) - 1
  mask ^ num
end
```

## Scala

```scala
object Solution {
    def findComplement(num: Int): Int = {
        if (num == 0) return 1
        var mask = 0
        while (mask < num) {
            mask = (mask << 1) | 1
        }
        mask ^ num
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_complement(num: i32) -> i32 {
        if num == 0 {
            return 1;
        }
        let mut mask = 0i32;
        let mut n = num;
        while n > 0 {
            mask = (mask << 1) | 1;
            n >>= 1;
        }
        (!num) & mask
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define/contract (find-complement num)
  (-> exact-integer? exact-integer?)
  (if (= num 0)
      1
      (let loop ((mask 1))
        (if (< mask num)
            (loop (+ (arithmetic-shift mask 1) 1))
            (bitwise-xor mask num)))))
```

## Erlang

```erlang
-module(solution).
-export([find_complement/1]).

-spec find_complement(Num :: integer()) -> integer().
find_complement(Num) ->
    Mask = build_mask(Num, 0),
    Num bxor Mask.

build_mask(0, Acc) -> Acc;
build_mask(N, Acc) ->
    NewAcc = (Acc bsl 1) bor 1,
    build_mask(N bsr 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_complement(num :: integer) :: integer
  def find_complement(0), do: 1
  def find_complement(num) when num > 0 do
    mask = build_mask(num, 1)
    Bitwise.bxor(mask, num)
  end

  defp build_mask(num, mask) when mask >= num, do: mask
  defp build_mask(num, mask), do: build_mask(num, (mask <<< 1) + 1)
end
```
