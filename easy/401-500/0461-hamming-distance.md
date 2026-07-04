# 0461. Hamming Distance

## Cpp

```cpp
class Solution {
public:
    int hammingDistance(int x, int y) {
        return __builtin_popcount(static_cast<unsigned int>(x ^ y));
    }
};
```

## Java

```java
class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}
```

## Python

```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
```

## Python3

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()
```

## C

```c
int hammingDistance(int x, int y) {
    unsigned int v = (unsigned int)(x ^ y);
    int cnt = 0;
    while (v) {
        v &= v - 1;
        cnt++;
    }
    return cnt;
}
```

## Csharp

```csharp
public class Solution {
    public int HammingDistance(int x, int y) {
        int diff = x ^ y;
        int count = 0;
        while (diff != 0) {
            count++;
            diff &= diff - 1; // clear the lowest set bit
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
    let xor = x ^ y;
    let count = 0;
    while (xor) {
        xor &= xor - 1;
        count++;
    }
    return count;
};
```

## Typescript

```typescript
function hammingDistance(x: number, y: number): number {
    let xor = x ^ y;
    let count = 0;
    while (xor) {
        count++;
        xor &= xor - 1;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function hammingDistance($x, $y) {
        $xor = $x ^ $y;
        $count = 0;
        while ($xor) {
            $xor &= ($xor - 1);
            $count++;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func hammingDistance(_ x: Int, _ y: Int) -> Int {
        return (x ^ y).nonzeroBitCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hammingDistance(x: Int, y: Int): Int {
        return Integer.bitCount(x xor y)
    }
}
```

## Dart

```dart
class Solution {
  int hammingDistance(int x, int y) {
    int xor = x ^ y;
    int count = 0;
    while (xor != 0) {
      xor &= xor - 1;
      count++;
    }
    return count;
  }
}
```

## Golang

```go
package main

import "math/bits"

func hammingDistance(x int, y int) int {
	return bits.OnesCount(uint(x ^ y))
}
```

## Ruby

```ruby
def hamming_distance(x, y)
  xor = x ^ y
  count = 0
  while xor != 0
    count += xor & 1
    xor >>= 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def hammingDistance(x: Int, y: Int): Int = {
        Integer.bitCount(x ^ y)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn hamming_distance(x: i32, y: i32) -> i32 {
        (x ^ y).count_ones() as i32
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define/contract (hamming-distance x y)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((n (bitwise-xor x y)) (cnt 0))
    (if (= n 0)
        cnt
        (loop (bitwise-and n (sub1 n)) (+ cnt 1)))))
```

## Erlang

```erlang
-module(solution).
-export([hamming_distance/2]).

-spec hamming_distance(X :: integer(), Y :: integer()) -> integer().
hamming_distance(X, Y) ->
    count_bits(X bxor Y).

count_bits(N) -> count_bits(N, 0).

count_bits(0, Acc) -> Acc;
count_bits(N, Acc) ->
    count_bits(N bsr 1, Acc + (N band 1)).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec hamming_distance(x :: integer, y :: integer) :: integer
  def hamming_distance(x, y) do
    xor = x ^^^ y
    count_bits(xor)
  end

  defp count_bits(0), do: 0
  defp count_bits(n) do
    (n &&& 1) + count_bits(bsr(n, 1))
  end
end
```
