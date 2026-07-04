# 0283. Move Zeroes

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int last = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] != 0) {
                swap(nums[last], nums[i]);
                ++last;
            }
        }
    }
};
```

## Java

```java
class Solution {
    public void moveZeroes(int[] nums) {
        int lastNonZeroFoundAt = 0;
        for (int cur = 0; cur < nums.length; cur++) {
            if (nums[cur] != 0) {
                int temp = nums[lastNonZeroFoundAt];
                nums[lastNonZeroFoundAt] = nums[cur];
                nums[cur] = temp;
                lastNonZeroFoundAt++;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last], nums[i] = nums[i], nums[last]
                last += 1
```

## Python3

```python
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                if cur != last_non_zero:
                    nums[last_non_zero], nums[cur] = nums[cur], 0
                last_non_zero += 1
```

## C

```c
void moveZeroes(int* nums, int numsSize) {
    int last = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != 0) {
            if (i != last) {
                int temp = nums[i];
                nums[i] = nums[last];
                nums[last] = temp;
            }
            ++last;
        }
    }
}
```

## Csharp

```csharp
public class Solution {
    public void MoveZeroes(int[] nums) {
        int lastNonZeroFoundAt = 0;
        for (int cur = 0; cur < nums.Length; cur++) {
            if (nums[cur] != 0) {
                int temp = nums[lastNonZeroFoundAt];
                nums[lastNonZeroFoundAt] = nums[cur];
                nums[cur] = temp;
                lastNonZeroFoundAt++;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let lastNonZeroFoundAt = 0;
    for (let cur = 0; cur < nums.length; cur++) {
        if (nums[cur] !== 0) {
            const temp = nums[lastNonZeroFoundAt];
            nums[lastNonZeroFoundAt] = nums[cur];
            nums[cur] = temp;
            lastNonZeroFoundAt++;
        }
    }
};
```

## Typescript

```typescript
function moveZeroes(nums: number[]): void {
    let lastNonZero = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            const temp = nums[lastNonZero];
            nums[lastNonZero] = nums[i];
            nums[i] = temp;
            lastNonZero++;
        }
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function moveZeroes(&$nums) {
        $last = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] != 0) {
                if ($i !== $last) {
                    $temp = $nums[$i];
                    $nums[$i] = $nums[$last];
                    $nums[$last] = $temp;
                }
                $last++;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        var lastNonZero = 0
        for i in 0..<nums.count {
            if nums[i] != 0 {
                nums.swapAt(i, lastNonZero)
                lastNonZero += 1
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        var lastNonZeroFoundAt = 0
        for (i in nums.indices) {
            if (nums[i] != 0) {
                val temp = nums[lastNonZeroFoundAt]
                nums[lastNonZeroFoundAt] = nums[i]
                nums[i] = temp
                lastNonZeroFoundAt++
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  void moveZeroes(List<int> nums) {
    int lastNonZeroFoundAt = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != 0) {
        int temp = nums[lastNonZeroFoundAt];
        nums[lastNonZeroFoundAt] = nums[i];
        nums[i] = temp;
        lastNonZeroFoundAt++;
      }
    }
  }
}
```

## Golang

```go
func moveZeroes(nums []int) {
    last := 0
    for cur, v := range nums {
        if v != 0 {
            if cur != last {
                nums[last], nums[cur] = nums[cur], nums[last]
            }
            last++
        }
    }
}
```

## Ruby

```ruby
def move_zeroes(nums)
  last_non_zero = 0
  nums.each_with_index do |val, i|
    next if val == 0
    if i != last_non_zero
      nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
    end
    last_non_zero += 1
  end
end
```

## Scala

```scala
object Solution {
    def moveZeroes(nums: Array[Int]): Unit = {
        var lastNonZero = 0
        for (i <- nums.indices) {
            if (nums(i) != 0) {
                val temp = nums(lastNonZero)
                nums(lastNonZero) = nums(i)
                nums(i) = temp
                lastNonZero += 1
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut last_non_zero = 0usize;
        for i in 0..nums.len() {
            if nums[i] != 0 {
                if i != last_non_zero {
                    nums.swap(i, last_non_zero);
                }
                last_non_zero += 1;
            }
        }
    }
}
```
