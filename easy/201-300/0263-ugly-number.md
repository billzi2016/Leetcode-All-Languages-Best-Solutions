# 0263. Ugly Number

## Cpp

```cpp
class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0) return false;
        while (n % 2 == 0) n /= 2;
        while (n % 3 == 0) n /= 3;
        while (n % 5 == 0) n /= 5;
        return n == 1;
    }
};
```

## Java

```java
class Solution {
    public boolean isUgly(int n) {
        if (n <= 0) return false;
        while (n % 2 == 0) n /= 2;
        while (n % 3 == 0) n /= 3;
        while (n % 5 == 0) n /= 5;
        return n == 1;
    }
}
```

## Python

```python
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        for p in (2, 3, 5):
            while n % p == 0:
                n //= p
        return n == 1
```

## Python3

```python
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for p in (2, 3, 5):
            while n % p == 0:
                n //= p
        return n == 1
```

## C

```c
#include <stdbool.h>

bool isUgly(int n) {
    if (n <= 0) return false;
    while (n % 2 == 0) n /= 2;
    while (n % 3 == 0) n /= 3;
    while (n % 5 == 0) n /= 5;
    return n == 1;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsUgly(int n) {
        if (n <= 0) return false;
        while (n % 2 == 0) n /= 2;
        while (n % 3 == 0) n /= 3;
        while (n % 5 == 0) n /= 5;
        return n == 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isUgly = function(n) {
    if (n <= 0) return false;
    for (const p of [2, 3, 5]) {
        while (n % p === 0) {
            n /= p;
        }
    }
    return n === 1;
};
```

## Typescript

```typescript
function isUgly(n: number): boolean {
    if (n <= 0) return false;
    const factors = [2, 3, 5];
    for (const f of factors) {
        while (n % f === 0) {
            n /= f;
        }
    }
    return n === 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isUgly($n) {
        if ($n <= 0) {
            return false;
        }
        foreach ([2, 3, 5] as $p) {
            while ($n % $p == 0) {
                $n = intdiv($n, $p);
            }
        }
        return $n === 1;
    }
}
```

## Swift

```swift
class Solution {
    func isUgly(_ n: Int) -> Bool {
        if n <= 0 { return false }
        var num = n
        let factors = [2, 3, 5]
        for f in factors {
            while num % f == 0 {
                num /= f
            }
        }
        return num == 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isUgly(n: Int): Boolean {
        if (n <= 0) return false
        var num = n
        val factors = intArrayOf(2, 3, 5)
        for (f in factors) {
            while (num % f == 0) {
                num /= f
            }
        }
        return num == 1
    }
}
```

## Dart

```dart
class Solution {
  bool isUgly(int n) {
    if (n <= 0) return false;
    for (var p in [2, 3, 5]) {
      while (n % p == 0) {
        n ~/= p;
      }
    }
    return n == 1;
  }
}
```

## Golang

```go
func isUgly(n int) bool {
	if n <= 0 {
		return false
	}
	for n%2 == 0 {
		n /= 2
	}
	for n%3 == 0 {
		n /= 3
	}
	for n%5 == 0 {
		n /= 5
	}
	return n == 1
}
```

## Ruby

```ruby
def is_ugly(n)
  return false if n <= 0
  [2, 3, 5].each do |p|
    while (n % p).zero?
      n /= p
    end
  end
  n == 1
end
```

## Scala

```scala
object Solution {
    def isUgly(n: Int): Boolean = {
        if (n <= 0) return false
        var num = n
        val primes = Array(2, 3, 5)
        for (p <- primes) {
            while (num % p == 0) {
                num /= p
            }
        }
        num == 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_ugly(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        let mut x = n;
        for p in [2, 3, 5].iter() {
            while x % *p == 0 {
                x /= *p;
            }
        }
        x == 1
    }
}
```

## Racket

```racket
(define/contract (is-ugly n)
  (-> exact-integer? boolean?)
  (if (<= n 0)
      #f
      (let loop ((m n))
        (cond [(= m 1) #t]
              [(zero? (remainder m 2)) (loop (/ m 2))]
              [(zero? (remainder m 3)) (loop (/ m 3))]
              [(zero? (remainder m 5)) (loop (/ m 5))]
              [else #f]))))
```

## Erlang

```erlang
-module(solution).
-export([is_ugly/1]).

-spec is_ugly(N :: integer()) -> boolean().
is_ugly(N) when N =< 0 ->
    false;
is_ugly(N) ->
    case reduce(N) of
        1 -> true;
        _ -> false
    end.

reduce(N) ->
    N1 = divide(N, 2),
    N2 = divide(N1, 3),
    N3 = divide(N2, 5),
    N3.

divide(X, D) when X rem D =:= 0 ->
    divide(X div D, D);
divide(X, _) -> X.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_ugly(n :: integer) :: boolean
  def is_ugly(n) when n <= 0, do: false
  def is_ugly(1), do: true

  def is_ugly(n) do
    n
    |> divide_by(2)
    |> divide_by(3)
    |> divide_by(5)
    == 1
  end

  defp divide_by(num, factor) when rem(num, factor) == 0,
    do: divide_by(div(num, factor), factor)

  defp divide_by(num, _factor), do: num
end
```
