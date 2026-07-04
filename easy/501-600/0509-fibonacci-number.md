# 0509. Fibonacci Number

## Cpp

```cpp
class Solution {
public:
    int fib(int n) {
        if (n < 2) return n;
        int a = 0, b = 1;
        for (int i = 2; i <= n; ++i) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
};
```

## Java

```java
class Solution {
    public int fib(int n) {
        if (n <= 1) return n;
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
```

## Python

```python
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
```

## Python3

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
```

## C

```c
int fib(int n) {
    if (n < 2) return n;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; ++i) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

## Csharp

```csharp
public class Solution {
    public int Fib(int n) {
        if (n <= 1) return n;
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if (n < 2) return n;
    let a = 0, b = 1;
    for (let i = 2; i <= n; i++) {
        const c = a + b;
        a = b;
        b = c;
    }
    return b;
};
```

## Typescript

```typescript
function fib(n: number): number {
    if (n < 2) return n;
    let a = 0, b = 1;
    for (let i = 2; i <= n; i++) {
        const c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function fib($n) {
        if ($n < 2) {
            return $n;
        }
        $a = 0;
        $b = 1;
        for ($i = 2; $i <= $n; $i++) {
            $c = $a + $b;
            $a = $b;
            $b = $c;
        }
        return $b;
    }
}
```

## Swift

```swift
class Solution {
    func fib(_ n: Int) -> Int {
        if n < 2 { return n }
        var a = 0
        var b = 1
        for _ in 2...n {
            let c = a + b
            a = b
            b = c
        }
        return b
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun fib(n: Int): Int {
        if (n < 2) return n
        var a = 0
        var b = 1
        for (i in 2..n) {
            val c = a + b
            a = b
            b = c
        }
        return b
    }
}
```

## Golang

```go
func fib(n int) int {
	if n < 2 {
		return n
	}
	a, b := 0, 1
	for i := 2; i <= n; i++ {
		a, b = b, a+b
	}
	return b
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def fib(n)
  return n if n < 2
  a, b = 0, 1
  (2..n).each do
    a, b = b, a + b
  end
  b
end
```

## Scala

```scala
object Solution {
    def fib(n: Int): Int = {
        if (n <= 1) return n
        var a = 0
        var b = 1
        for (_ <- 2 to n) {
            val c = a + b
            a = b
            b = c
        }
        b
    }
}
```

## Rust

```rust
impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n <= 1 {
            return n;
        }
        let mut a = 0;
        let mut b = 1;
        for _ in 2..=n {
            let c = a + b;
            a = b;
            b = c;
        }
        b
    }
}
```
