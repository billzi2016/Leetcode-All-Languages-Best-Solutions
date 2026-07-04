# 0292. Nim Game

## Cpp

```cpp
class Solution {
public:
    bool canWinNim(int n) {
        return n % 4 != 0;
    }
};
```

## Java

```java
class Solution {
    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }
}
```

## Python

```python
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
```

## Python3

```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
```

## C

```c
#include <stdbool.h>

bool canWinNim(int n) {
    return n % 4 != 0;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanWinNim(int n)
    {
        return n % 4 != 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var canWinNim = function(n) {
    return n % 4 !== 0;
};
```

## Typescript

```typescript
function canWinNim(n: number): boolean {
    return n % 4 !== 0;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function canWinNim($n) {
        return $n % 4 !== 0;
    }
}
?>
```

## Swift

```swift
class Solution {
    func canWinNim(_ n: Int) -> Bool {
        return n % 4 != 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canWinNim(n: Int): Boolean {
        return n % 4 != 0
    }
}
```

## Dart

```dart
class Solution {
  bool canWinNim(int n) {
    return n % 4 != 0;
  }
}
```

## Golang

```go
func canWinNim(n int) bool {
    return n%4 != 0
}
```

## Ruby

```ruby
def can_win_nim(n)
  n % 4 != 0
end
```

## Scala

```scala
object Solution {
    def canWinNim(n: Int): Boolean = {
        n % 4 != 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_win_nim(n: i32) -> bool {
        n % 4 != 0
    }
}
```

## Racket

```racket
(define/contract (can-win-nim n)
  (-> exact-integer? boolean?)
  (not (= (modulo n 4) 0)))
```

## Erlang

```erlang
-module(solution).
-export([can_win_nim/1]).

-spec can_win_nim(N :: integer()) -> boolean().
can_win_nim(N) ->
    N rem 4 =/= 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_win_nim(n :: integer) :: boolean
  def can_win_nim(n) do
    rem(n, 4) != 0
  end
end
```
