# 0628. Maximum Product of Three Numbers

## Cpp

```cpp
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        long long prod1 = 1LL * nums[n - 1] * nums[n - 2] * nums[n - 3];
        long long prod2 = 1LL * nums[0] * nums[1] * nums[n - 1];
        return static_cast<int>(max(prod1, prod2));
    }
};
```

## Java

```java
class Solution {
    public int maximumProduct(int[] nums) {
        int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE, max3 = Integer.MIN_VALUE;
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        for (int n : nums) {
            if (n > max1) {
                max3 = max2;
                max2 = max1;
                max1 = n;
            } else if (n > max2) {
                max3 = max2;
                max2 = n;
            } else if (n > max3) {
                max3 = n;
            }
            
            if (n < min1) {
                min2 = min1;
                min1 = n;
            } else if (n < min2) {
                min2 = n;
            }
        }
        return Math.max(max1 * max2 * max3, max1 * min1 * min2);
    }
}
```

## Python

```python
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
```

## Python3

```python
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
```

## C

```c
#include <limits.h>

int maximumProduct(int* nums, int numsSize) {
    int max1 = INT_MIN, max2 = INT_MIN, max3 = INT_MIN;
    int min1 = INT_MAX, min2 = INT_MAX;

    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];

        // Update max values
        if (x > max1) {
            max3 = max2;
            max2 = max1;
            max1 = x;
        } else if (x > max2) {
            max3 = max2;
            max2 = x;
        } else if (x > max3) {
            max3 = x;
        }

        // Update min values
        if (x < min1) {
            min2 = min1;
            min1 = x;
        } else if (x < min2) {
            min2 = x;
        }
    }

    int product1 = max1 * max2 * max3;
    int product2 = max1 * min1 * min2;

    return product1 > product2 ? product1 : product2;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumProduct(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        long product1 = (long)nums[n - 1] * nums[n - 2] * nums[n - 3];
        long product2 = (long)nums[0] * nums[1] * nums[n - 1];
        long result = Math.Max(product1, product2);
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {
    let max1 = -Infinity, max2 = -Infinity, max3 = -Infinity;
    let min1 = Infinity, min2 = Infinity;
    
    for (const n of nums) {
        // Update max values
        if (n > max1) {
            max3 = max2;
            max2 = max1;
            max1 = n;
        } else if (n > max2) {
            max3 = max2;
            max2 = n;
        } else if (n > max3) {
            max3 = n;
        }
        
        // Update min values
        if (n < min1) {
            min2 = min1;
            min1 = n;
        } else if (n < min2) {
            min2 = n;
        }
    }
    
    return Math.max(max1 * max2 * max3, max1 * min1 * min2);
};
```

## Typescript

```typescript
function maximumProduct(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const prod1 = nums[n - 1] * nums[n - 2] * nums[n - 3];
    const prod2 = nums[0] * nums[1] * nums[n - 1];
    return Math.max(prod1, prod2);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumProduct($nums) {
        sort($nums);
        $n = count($nums);
        $product1 = $nums[$n - 1] * $nums[$n - 2] * $nums[$n - 3];
        $product2 = $nums[0] * $nums[1] * $nums[$n - 1];
        return max($product1, $product2);
    }
}
```

## Swift

```swift
class Solution {
    func maximumProduct(_ nums: [Int]) -> Int {
        var max1 = Int.min, max2 = Int.min, max3 = Int.min
        var min1 = Int.max, min2 = Int.max
        
        for v in nums {
            if v > max1 {
                max3 = max2
                max2 = max1
                max1 = v
            } else if v > max2 {
                max3 = max2
                max2 = v
            } else if v > max3 {
                max3 = v
            }
            
            if v < min1 {
                min2 = min1
                min1 = v
            } else if v < min2 {
                min2 = v
            }
        }
        
        return max(max1 * max2 * max3, min1 * min2 * max1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumProduct(nums: IntArray): Int {
        var max1 = Int.MIN_VALUE
        var max2 = Int.MIN_VALUE
        var max3 = Int.MIN_VALUE
        var min1 = Int.MAX_VALUE
        var min2 = Int.MAX_VALUE

        for (n in nums) {
            if (n > max1) {
                max3 = max2
                max2 = max1
                max1 = n
            } else if (n > max2) {
                max3 = max2
                max2 = n
            } else if (n > max3) {
                max3 = n
            }

            if (n < min1) {
                min2 = min1
                min1 = n
            } else if (n < min2) {
                min2 = n
            }
        }

        val product1 = max1.toLong() * max2 * max3
        val product2 = min1.toLong() * min2 * max1
        return kotlin.math.max(product1, product2).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maximumProduct(List<int> nums) {
    int max1 = -10000000, max2 = -10000000, max3 = -10000000;
    int min1 = 10000000, min2 = 10000000;

    for (int n in nums) {
      if (n > max1) {
        max3 = max2;
        max2 = max1;
        max1 = n;
      } else if (n > max2) {
        max3 = max2;
        max2 = n;
      } else if (n > max3) {
        max3 = n;
      }

      if (n < min1) {
        min2 = min1;
        min1 = n;
      } else if (n < min2) {
        min2 = n;
      }
    }

    int product1 = max1 * max2 * max3;
    int product2 = max1 * min1 * min2;

    return product1 > product2 ? product1 : product2;
  }
}
```

## Golang

```go
func maximumProduct(nums []int) int {
    max1, max2, max3 := -1000000000, -1000000000, -1000000000
    min1, min2 := 1000000000, 1000000000

    for _, n := range nums {
        if n > max1 {
            max3 = max2
            max2 = max1
            max1 = n
        } else if n > max2 {
            max3 = max2
            max2 = n
        } else if n > max3 {
            max3 = n
        }

        if n < min1 {
            min2 = min1
            min1 = n
        } else if n < min2 {
            min2 = n
        }
    }

    prod1 := max1 * max2 * max3
    prod2 := max1 * min1 * min2

    if prod1 > prod2 {
        return prod1
    }
    return prod2
}
```

## Ruby

```ruby
def maximum_product(nums)
  nums.sort!
  [nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1]].max
end
```

## Scala

```scala
object Solution {
    def maximumProduct(nums: Array[Int]): Int = {
        val sorted = nums.sorted
        val n = sorted.length
        val prod1 = sorted(n - 1) * sorted(n - 2) * sorted(n - 3)
        val prod2 = sorted(0) * sorted(1) * sorted(n - 1)
        Math.max(prod1, prod2)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_product(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let n = nums.len();
        let prod1 = nums[n - 1] as i64 * nums[n - 2] as i64 * nums[n - 3] as i64;
        let prod2 = nums[0] as i64 * nums[1] as i64 * nums[n - 1] as i64;
        std::cmp::max(prod1, prod2) as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-product nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([sorted (sort nums <)]
         [n (length sorted)])
    (define (prod . xs) (apply * xs))
    (let* ([a1 (list-ref sorted (- n 3))]
           [a2 (list-ref sorted (- n 2))]
           [a3 (list-ref sorted (- n 1))]
           [b1 (list-ref sorted 0)]
           [b2 (list-ref sorted 1)])
      (max (prod a1 a2 a3)
           (prod b1 b2 a3)))))
```

## Erlang

```erlang
-spec maximum_product(Nums :: [integer()]) -> integer().
maximum_product(Nums) ->
    Sorted = lists:sort(Nums),
    [Small1, Small2 | _] = Sorted,
    Rev = lists:reverse(Sorted),
    [Large1, Large2, Large3 | _] = Rev,
    Prod1 = Large1 * Large2 * Large3,
    Prod2 = Small1 * Small2 * Large1,
    erlang:max(Prod1, Prod2).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_product(nums :: [integer]) :: integer
  def maximum_product(nums) do
    sorted = Enum.sort(nums)
    n = length(sorted)

    a = Enum.at(sorted, n - 1)
    b = Enum.at(sorted, n - 2)
    c = Enum.at(sorted, n - 3)

    d = Enum.at(sorted, 0)
    e = Enum.at(sorted, 1)

    product1 = a * b * c
    product2 = d * e * a

    if product1 > product2, do: product1, else: product2
  end
end
```
