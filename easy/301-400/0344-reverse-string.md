# 0344. Reverse String

## Cpp

```cpp
class Solution {
public:
    void reverseString(std::vector<char>& s) {
        int i = 0, j = static_cast<int>(s.size()) - 1;
        while (i < j) {
            std::swap(s[i], s[j]);
            ++i;
            --j;
        }
    }
};
```

## Java

```java
class Solution {
    public void reverseString(char[] s) {
        int left = 0, right = s.length - 1;
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
}
```

## Python

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

## Python3

```python
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

## C

```c
void reverseString(char* s, int sSize) {
    int left = 0;
    int right = sSize - 1;
    while (left < right) {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }
}
```

## Csharp

```csharp
public class Solution {
    public void ReverseString(char[] s) {
        int left = 0, right = s.Length - 1;
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let i = 0, j = s.length - 1;
    while (i < j) {
        const temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        i++;
        j--;
    }
};
```

## Typescript

```typescript
/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        const temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $s
     * @return NULL
     */
    function reverseString(&$s) {
        $i = 0;
        $j = count($s) - 1;
        while ($i < $j) {
            $tmp = $s[$i];
            $s[$i] = $s[$j];
            $s[$j] = $tmp;
            $i++;
            $j--;
        }
    }
}
```

## Swift

```swift
class Solution {
    func reverseString(_ s: inout [Character]) {
        var left = 0
        var right = s.count - 1
        while left < right {
            s.swapAt(left, right)
            left += 1
            right -= 1
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reverseString(s: CharArray): Unit {
        var left = 0
        var right = s.size - 1
        while (left < right) {
            val tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left++
            right--
        }
    }
}
```

## Dart

```dart
class Solution {
  void reverseString(List<String> s) {
    int left = 0;
    int right = s.length - 1;
    while (left < right) {
      String temp = s[left];
      s[left] = s[right];
      s[right] = temp;
      left++;
      right--;
    }
  }
}
```

## Golang

```go
func reverseString(s []byte) {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}
```

## Ruby

```ruby
# @param {Character[]} s
# @return {Void} Do not return anything, modify s in-place instead.
def reverse_string(s)
  left = 0
  right = s.length - 1
  while left < right
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
  end
end
```

## Scala

```scala
object Solution {
    def reverseString(s: Array[Char]): Unit = {
        var left = 0
        var right = s.length - 1
        while (left < right) {
            val tmp = s(left)
            s(left) = s(right)
            s(right) = tmp
            left += 1
            right -= 1
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let mut i = 0usize;
        let mut j = s.len().saturating_sub(1);
        while i < j {
            s.swap(i, j);
            i += 1;
            j -= 1;
        }
    }
}
```
