# 0258. Add Digits

## Cpp

```cpp
class Solution {
public:
    int addDigits(int num) {
        if (num == 0) return 0;
        return 1 + (num - 1) % 9;
    }
};
```

## Java

```java
class Solution {
    public int addDigits(int num) {
        if (num == 0) return 0;
        return 1 + (num - 1) % 9;
    }
}
```

## Python

```python
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return (num - 1) % 9 + 1
```

## Python3

```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return (num - 1) % 9 + 1
```

## C

```c
int addDigits(int num) {
    if (num == 0) return 0;
    return 1 + (num - 1) % 9;
}
```

## Csharp

```csharp
public class Solution {
    public int AddDigits(int num) {
        if (num == 0) return 0;
        return 1 + (num - 1) % 9;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    if (num === 0) return 0;
    return 1 + ((num - 1) % 9);
};
```

## Typescript

```typescript
function addDigits(num: number): number {
    if (num === 0) return 0;
    return ((num - 1) % 9) + 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function addDigits($num) {
        if ($num == 0) {
            return 0;
        }
        return 1 + ($num - 1) % 9;
    }
}
```

## Swift

```swift
class Solution {
    func addDigits(_ num: Int) -> Int {
        if num == 0 { return 0 }
        return (num - 1) % 9 + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun addDigits(num: Int): Int {
        return if (num == 0) 0 else (num - 1) % 9 + 1
    }
}
```

## Dart

```dart
class Solution {
  int addDigits(int num) {
    if (num == 0) return 0;
    return (num - 1) % 9 + 1;
  }
}
```

## Golang

```go
func addDigits(num int) int {
	if num == 0 {
		return 0
	}
	return 1 + (num-1)%9
}
```

## Ruby

```ruby
def add_digits(num)
  return 0 if num == 0
  1 + (num - 1) % 9
end
```

## Scala

```scala
object Solution {
    def addDigits(num: Int): Int = {
        if (num == 0) 0 else ((num - 1) % 9) + 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn add_digits(num: i32) -> i32 {
        if num == 0 {
            0
        } else {
            (num - 1) % 9 + 1
        }
    }
}
```

## Racket

```racket
(define/contract (add-digits num)
  (-> exact-integer? exact-integer?)
  (if (= num 0)
      0
      (+ 1 (modulo (- num 1) 9))))
```

## Erlang

```erlang
-module(solution).
-export([add_digits/1]).

-spec add_digits(Num :: integer()) -> integer().
add_digits(0) ->
    0;
add_digits(Num) ->
    ((Num - 1) rem 9) + 1.
```

## Elixir

```elixir
defmodule Solution do
  @spec add_digits(num :: integer) :: integer
  def add_digits(num) do
    if num == 0 do
      0
    else
      rem(num - 1, 9) + 1
    end
  end
end
```
