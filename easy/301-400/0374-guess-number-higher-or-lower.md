# 0374. Guess Number Higher or Lower

## Cpp

```cpp
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        long long low = 1, high = n;
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            int res = guess(static_cast<int>(mid));
            if (res == 0) return static_cast<int>(mid);
            else if (res == -1) high = mid - 1; // pick is lower
            else low = mid + 1;                 // pick is higher
        }
        return -1; // should never reach here
    }
};
```

## Java

```java
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int low = 1, high = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int res = guess(mid);
            if (res == 0) {
                return mid;
            } else if (res < 0) { // guessed too high
                high = mid - 1;
            } else { // res > 0, guessed too low
                low = mid + 1;
            }
        }
        return -1; // should never reach here
    }
}
```

## Python

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 0:   # guess is higher than pick
                high = mid - 1
            else:         # guess is lower than pick
                low = mid + 1
        return -1  # should never reach here
```

## Python3

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res < 0:   # guessed number is higher than pick
                high = mid - 1
            else:           # guessed number is lower than pick
                low = mid + 1
        return -1  # should never reach here
```

## C

```c
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

int guessNumber(int n){
    int low = 1, high = n;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        int res = guess(mid);
        if (res == 0) return mid;
        else if (res == -1) high = mid - 1; // pick is lower
        else low = mid + 1;                 // pick is higher
    }
    return -1; // should never reach here
}
```

## Csharp

```csharp
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution : GuessGame {
    public int GuessNumber(int n) {
        int low = 1, high = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int res = guess(mid);
            if (res == 0) return mid;
            else if (res < 0) // guessed number is higher than pick
                high = mid - 1;
            else // guessed number is lower than pick
                low = mid + 1;
        }
        return -1; // should never reach here
    }
}
```

## Javascript

```javascript
/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function(n) {
    let low = 1, high = n;
    while (low <= high) {
        const mid = Math.floor(low + (high - low) / 2);
        const res = guess(mid);
        if (res === 0) return mid;
        if (res === -1) {
            high = mid - 1;
        } else { // res === 1
            low = mid + 1;
        }
    }
    return -1; // should never reach here
};
```

## Typescript

```typescript
/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */
function guessNumber(n: number): number {
    let low = 1, high = n;
    while (low <= high) {
        const mid = Math.floor(low + (high - low) / 2);
        const res = guess(mid);
        if (res === 0) return mid;
        else if (res === -1) high = mid - 1;
        else low = mid + 1;
    }
    return -1;
}
```

## Php

```php
/ ** 
 * The API guess is defined in the parent class.
 * @param  num   your guess
 * @return       -1 if num is higher than the picked number
 *               1 if num is lower than the picked number
 *               otherwise return 0
 * public function guess($num){}
 */
class Solution extends GuessGame {
    /**
     * @param Integer $n
     * @return Integer
     */
    function guessNumber($n) {
        $low = 1;
        $high = $n;
        while ($low <= $high) {
            $mid = $low + intdiv($high - $low, 2);
            $res = $this->guess($mid);
            if ($res == 0) {
                return $mid;
            } elseif ($res < 0) { // guess is higher than pick
                $high = $mid - 1;
            } else { // res > 0, guess is lower than pick
                $low = $mid + 1;
            }
        }
        return -1; // should never reach here
    }
}
```

## Swift

```swift
/ ** 
 * Forward declaration of guess API.
 * @param  num -> your guess number
 * @return      -1 if num is higher than the picked number
 *               1 if num is lower than the picked number
 *               otherwise return 0 
 * func guess(_ num: Int) -> Int 
 */

class Solution : GuessGame {
    func guessNumber(_ n: Int) -> Int {
        var low = 1
        var high = n
        while low <= high {
            let mid = low + (high - low) / 2
            let res = guess(mid)
            if res == 0 {
                return mid
            } else if res < 0 { // guessed too high
                high = mid - 1
            } else { // res > 0, guessed too low
                low = mid + 1
            }
        }
        return -1 // should never reach here
    }
}
```

## Kotlin

```kotlin
/** 
 * The API guess is defined in the parent class.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * fun guess(num:Int):Int {}
 */

class Solution : GuessGame() {
    override fun guessNumber(n: Int): Int {
        var low = 1
        var high = n
        while (low <= high) {
            val mid = low + ((high - low) ushr 1)
            when (guess(mid)) {
                0 -> return mid
                -1 -> high = mid - 1   // guess is higher than pick
                1 -> low = mid + 1    // guess is lower than pick
            }
        }
        return -1 // should never reach here
    }
}
```

## Golang

```go
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
	low, high := 1, n
	for low <= high {
		mid := low + (high-low)/2
		res := guess(mid)
		if res == 0 {
			return mid
		} else if res < 0 { // guessed too high
			high = mid - 1
		} else { // guessed too low
			low = mid + 1
		}
	}
	return -1
}
```

## Ruby

```ruby
def guessNumber(n)
  left = 1
  right = n
  while left <= right
    mid = left + ((right - left) >> 1)
    res = guess(mid)
    return mid if res == 0
    if res < 0
      right = mid - 1
    else
      left = mid + 1
    end
  end
  -1
end
```

## Scala

```scala
/** 
 * The API guess is defined in the parent class.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * def guess(num: Int): Int = {}
 */

class Solution extends GuessGame {
    def guessNumber(n: Int): Int = {
        var low = 1
        var high = n
        while (low <= high) {
            val mid = low + ((high - low) >>> 1)
            guess(mid) match {
                case 0 => return mid
                case -1 => high = mid - 1
                case 1 => low = mid + 1
            }
        }
        -1 // should never reach here
    }
}
```

## Rust

```rust
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * unsafe fn guess(num: i32) -> i32 {}
 */

impl Solution {
    unsafe fn guessNumber(n: i32) -> i32 {
        let mut left = 1i32;
        let mut right = n;
        while left <= right {
            let mid = left + ((right - left) >> 1);
            let res = unsafe { guess(mid) };
            if res == 0 {
                return mid;
            } else if res < 0 {
                // pick is lower than mid
                right = mid - 1;
            } else {
                // pick is higher than mid
                left = mid + 1;
            }
        }
        -1
    }
}
```
