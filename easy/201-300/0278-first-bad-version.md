# 0278. First Bad Version

## Cpp

```cpp
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

## Java

```java
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
```

## Python

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

## Python3

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

## C

```c
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    int left = 1, right = n;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (isBadVersion(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

## Csharp

```csharp
/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

public class Solution : VersionControl {
    public int FirstBadVersion(int n) {
        int left = 1, right = n;
        while (left < right) {
            int mid = left + (int)(((long)right - left) / 2);
            if (IsBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
```

## Javascript

```javascript
/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let left = 1, right = n;
        while (left < right) {
            const mid = Math.floor(left + (right - left) / 2);
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    };
};
```

## Typescript

```typescript
/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

var solution = function(isBadVersion: any) {

    return function(n: number): number {
        let left = 1, right = n;
        while (left < right) {
            const mid = Math.floor(left + (right - left) / 2);
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    };
};
```

## Php

```php
/* The isBadVersion API is defined in the parent class VersionControl.
      public function isBadVersion($version){} */

class Solution extends VersionControl {
    /**
     * @param Integer $n
     * @return Integer
     */
    function firstBadVersion($n) {
        $left = 1;
        $right = $n;
        while ($left < $right) {
            $mid = $left + intdiv($right - $left, 2);
            if ($this->isBadVersion($mid)) {
                $right = $mid;
            } else {
                $left = $mid + 1;
            }
        }
        return $left;
    }
}
```

## Swift

```swift
/**
 * The knows API is defined in the parent class VersionControl.
 *     func isBadVersion(_ version: Int) -> Bool{}
 */

class Solution : VersionControl {
    func firstBadVersion(_ n: Int) -> Int {
        var left = 1
        var right = n
        while left < right {
            let mid = left + (right - left) / 2
            if isBadVersion(mid) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
/ * The isBadVersion API is defined in the parent class VersionControl.
      fun isBadVersion(version: Int) : Boolean {} * /

class Solution : VersionControl() {
    override fun firstBadVersion(n: Int): Int {
        var left = 1L
        var right = n.toLong()
        while (left < right) {
            val mid = left + (right - left) / 2
            if (isBadVersion(mid.toInt())) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left.toInt()
    }
}
```

## Golang

```go
/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return           true if current version is bad 
 *                   false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersion(n int) int {
	low, high := 1, n
	for low < high {
		mid := low + (high-low)/2
		if isBadVersion(mid) {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low
}
```

## Ruby

```ruby
# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):

def first_bad_version(n)
  left = 1
  right = n
  while left < right
    mid = left + (right - left) / 2
    if is_bad_version(mid)
      right = mid
    else
      left = mid + 1
    end
  end
  left
end
```

## Scala

```scala
/* The isBadVersion API is defined in the parent class VersionControl.
      def isBadVersion(version: Int): Boolean = {} */

class Solution extends VersionControl {
  def firstBadVersion(n: Int): Int = {
    var left: Long = 1
    var right: Long = n.toLong
    while (left < right) {
      val mid = left + (right - left) / 2
      if (isBadVersion(mid.toInt)) {
        right = mid
      } else {
        left = mid + 1
      }
    }
    left.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn first_bad_version(&self, n: i32) -> i32 {
        let mut left: i64 = 1;
        let mut right: i64 = n as i64;
        while left < right {
            let mid = left + (right - left) / 2;
            if self.isBadVersion(mid as i32) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left as i32
    }
}
```
