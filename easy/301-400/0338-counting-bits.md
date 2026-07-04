# 0338. Counting Bits

## Cpp

```cpp
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            ans[i] = ans[i >> 1] + (i & 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            ans[i] = ans[i >> 1] + (i & 1);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        bits = [0] * (n + 1)
        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)
        return bits
```

## Python3

```python
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    *returnSize = n + 1;
    int* ans = (int*)malloc(sizeof(int) * (*returnSize));
    if (!ans) return NULL;
    ans[0] = 0;
    for (int i = 1; i <= n; ++i) {
        ans[i] = ans[i >> 1] + (i & 1);
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] CountBits(int n)
    {
        int[] ans = new int[n + 1];
        for (int i = 1; i <= n; i++)
        {
            ans[i] = ans[i >> 1] + (i & 1);
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    const ans = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; ++i) {
        ans[i] = ans[i >> 1] + (i & 1);
    }
    return ans;
};
```

## Typescript

```typescript
function countBits(n: number): number[] {
    const ans = new Array<number>(n + 1);
    ans[0] = 0;
    for (let i = 1; i <= n; i++) {
        ans[i] = ans[i >> 1] + (i & 1);
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function countBits($n) {
        $ans = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $ans[$i] = $ans[$i >> 1] + ($i & 1);
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countBits(_ n: Int) -> [Int] {
        var ans = Array(repeating: 0, count: n + 1)
        if n == 0 { return ans }
        for i in 1...n {
            ans[i] = ans[i >> 1] + (i & 1)
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countBits(n: Int): IntArray {
        val ans = IntArray(n + 1)
        for (i in 1..n) {
            ans[i] = ans[i shr 1] + (i and 1)
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> countBits(int n) {
    List<int> ans = List.filled(n + 1, 0);
    for (int i = 1; i <= n; i++) {
      ans[i] = ans[i >> 1] + (i & 1);
    }
    return ans;
  }
}
```

## Golang

```go
func countBits(n int) []int {
    ans := make([]int, n+1)
    for i := 1; i <= n; i++ {
        ans[i] = ans[i>>1] + (i & 1)
    }
    return ans
}
```

## Ruby

```ruby
def count_bits(n)
  res = Array.new(n + 1, 0)
  i = 1
  while i <= n
    res[i] = res[i >> 1] + (i & 1)
    i += 1
  end
  res
end
```

## Scala

```scala
object Solution {
    def countBits(n: Int): Array[Int] = {
        val ans = new Array[Int](n + 1)
        var i = 1
        while (i <= n) {
            ans(i) = ans(i >> 1) + (i & 1)
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        if n < 0 {
            return Vec::new();
        }
        let n = n as usize;
        let mut ans = vec![0i32; n + 1];
        for i in 1..=n {
            ans[i] = ans[i >> 1] + ((i & 1) as i32);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-bits n)
  (-> exact-integer? (listof exact-integer?))
  (let* ([size (+ n 1)]
         [ans (make-vector size 0)])
    (for ([i (in-range 1 size)])
      (vector-set! ans i
                   (+ (vector-ref ans (quotient i 2))
                      (bitwise-and i 1))))
    (vector->list ans)))
```

## Erlang

```erlang
-spec count_bits(N :: integer()) -> [integer()].
count_bits(N) when N >= 0 ->
    lists:map(fun(I) -> erlang:bcnt(I) end,
              lists:seq(0, N)).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec count_bits(n :: integer) :: [integer]
  def count_bits(n) when n >= 0 do
    Enum.map(0..n, &popcount/1)
  end

  defp popcount(0), do: 0
  defp popcount(x) do
    (x &&& 1) + popcount(x >>> 1)
  end
end
```
