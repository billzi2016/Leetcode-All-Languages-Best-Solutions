# 0521. Longest Uncommon Subsequence I

## Cpp

```cpp
class Solution {
public:
    int findLUSlength(string a, string b) {
        if (a == b) return -1;
        return max((int)a.size(), (int)b.size());
    }
};
```

## Java

```java
class Solution {
    public int findLUSlength(String a, String b) {
        if (a.equals(b)) {
            return -1;
        }
        return Math.max(a.length(), b.length());
    }
}
```

## Python

```python
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))
```

## Python3

```python
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))
```

## C

```c
#include <string.h>

int findLUSlength(char* a, char* b) {
    if (strcmp(a, b) == 0) {
        return -1;
    }
    int lenA = strlen(a);
    int lenB = strlen(b);
    return lenA > lenB ? lenA : lenB;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindLUSlength(string a, string b)
    {
        if (a == b) return -1;
        return Math.Max(a.Length, b.Length);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var findLUSlength = function(a, b) {
    if (a === b) return -1;
    return Math.max(a.length, b.length);
};
```

## Typescript

```typescript
function findLUSlength(a: string, b: string): number {
    if (a === b) return -1;
    return Math.max(a.length, b.length);
}
```

## Php

```php
class Solution {
    /**
     * @param String $a
     * @param String $b
     * @return Integer
     */
    function findLUSlength($a, $b) {
        if ($a === $b) {
            return -1;
        }
        $lenA = strlen($a);
        $lenB = strlen($b);
        return $lenA > $lenB ? $lenA : $lenB;
    }
}
```

## Swift

```swift
class Solution {
    func findLUSlength(_ a: String, _ b: String) -> Int {
        if a == b {
            return -1
        }
        return max(a.count, b.count)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLUSlength(a: String, b: String): Int {
        return if (a == b) -1 else maxOf(a.length, b.length)
    }
}
```

## Dart

```dart
class Solution {
  int findLUSlength(String a, String b) {
    if (a == b) return -1;
    return a.length > b.length ? a.length : b.length;
  }
}
```

## Golang

```go
func findLUSlength(a string, b string) int {
	if a == b {
		return -1
	}
	if len(a) > len(b) {
		return len(a)
	}
	return len(b)
}
```

## Ruby

```ruby
# @param {String} a
# @param {String} b
# @return {Integer}
def find_lu_slength(a, b)
  return -1 if a == b
  [a.length, b.length].max
end
```

## Scala

```scala
object Solution {
    def findLUSlength(a: String, b: String): Int = {
        if (a == b) -1 else math.max(a.length, b.length)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_lu_slength(a: String, b: String) -> i32 {
        if a == b {
            -1
        } else {
            std::cmp::max(a.len(), b.len()) as i32
        }
    }
}
```

## Racket

```racket
(define/contract (find-lu-slength a b)
  (-> string? string? exact-integer?)
  (if (string=? a b)
      -1
      (max (string-length a) (string-length b))))
```

## Erlang

```erlang
-spec find_lu_slength(A :: unicode:unicode_binary(), B :: unicode:unicode_binary()) -> integer().
find_lu_slength(A, B) ->
    case A =:= B of
        true -> -1;
        false -> erlang:max(byte_size(A), byte_size(B))
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_lu_slength(a :: String.t(), b :: String.t()) :: integer()
  def find_lu_slength(a, b) do
    if a == b do
      -1
    else
      max(String.length(a), String.length(b))
    end
  end
end
```
