# 0004. Median of Two Sorted Arrays

## Cpp

```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        if (m > n) {
            swap(nums1, nums2);
            swap(m, n);
        }
        int left = 0, right = m;
        while (left <= right) {
            int i = (left + right) / 2;                 // partition in nums1
            int j = (m + n + 1) / 2 - i;                // partition in nums2

            int maxLeftA = (i == 0) ? INT_MIN : nums1[i - 1];
            int minRightA = (i == m) ? INT_MAX : nums1[i];

            int maxLeftB = (j == 0) ? INT_MIN : nums2[j - 1];
            int minRightB = (j == n) ? INT_MAX : nums2[j];

            if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
                if ((m + n) % 2 == 0) {
                    return ((double)max(maxLeftA, maxLeftB) + (double)min(minRightA, minRightB)) / 2.0;
                } else {
                    return (double)max(maxLeftA, maxLeftB);
                }
            } else if (maxLeftA > minRightB) {
                right = i - 1;
            } else {
                left = i + 1;
            }
        }
        return 0.0; // Should never be reached
    }
};
```

## Java

```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is the smaller array
        if (nums1.length > nums2.length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
        int m = nums1.length;
        int n = nums2.length;
        int totalLeft = (m + n + 1) / 2;
        int left = 0, right = m;

        while (left <= right) {
            int i = (left + right) >>> 1; // partition of nums1
            int j = totalLeft - i;         // partition of nums2

            int maxLeftA = (i == 0) ? Integer.MIN_VALUE : nums1[i - 1];
            int minRightA = (i == m) ? Integer.MAX_VALUE : nums1[i];

            int maxLeftB = (j == 0) ? Integer.MIN_VALUE : nums2[j - 1];
            int minRightB = (j == n) ? Integer.MAX_VALUE : nums2[j];

            if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
                if ((m + n) % 2 == 0) {
                    return ((double)Math.max(maxLeftA, maxLeftB) + Math.min(minRightA, minRightB)) / 2.0;
                } else {
                    return (double)Math.max(maxLeftA, maxLeftB);
                }
            } else if (maxLeftA > minRightB) {
                right = i - 1;
            } else {
                left = i + 1;
            }
        }

        // Should never reach here for valid input
        throw new IllegalArgumentException("Input arrays are not sorted or invalid.");
    }
}
```

## Python

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to get O(log(min(m,n))) time.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2          # partition of nums1
            j = total_left - i               # partition of nums2

            max_left_a = nums1[i - 1] if i > 0 else float('-inf')
            min_right_a = nums1[i] if i < m else float('inf')

            max_left_b = nums2[j - 1] if j > 0 else float('-inf')
            min_right_b = nums2[j] if j < n else float('inf')

            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                if (m + n) % 2 == 1:
                    return float(max(max_left_a, max_left_b))
                else:
                    left_max = max(max_left_a, max_left_b)
                    right_min = min(min_right_a, min_right_b)
                    return (left_max + right_min) / 2.0
            elif max_left_a > min_right_b:
                right = i - 1
            else:
                left = i + 1

        # Should never reach here if input arrays are valid.
        raise ValueError("Input arrays are not sorted or invalid.")
```

## Python3

```python
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2

        while True:
            i = (left + right) // 2          # partition of nums1
            j = half_len - i                 # complementary partition in nums2

            max_left_a = nums1[i - 1] if i > 0 else float('-inf')
            min_right_a = nums1[i] if i < m else float('inf')

            max_left_b = nums2[j - 1] if j > 0 else float('-inf')
            min_right_b = nums2[j] if j < n else float('inf')

            # Correct partition found
            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                if (m + n) % 2 == 0:
                    return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2.0
                else:
                    return float(max(max_left_a, max_left_b))
            # Need to move partition i left
            elif max_left_a > min_right_b:
                right = i - 1
            # Need to move partition i right
            else:
                left = i + 1
```

## C

```c
#include <limits.h>
#include <stddef.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // Ensure nums1 is the smaller array
    if (nums1Size > nums2Size) {
        // swap pointers and sizes
        int *tmpPtr = nums1;
        nums1 = nums2;
        nums2 = tmpPtr;
        int tmpSize = nums1Size;
        nums1Size = nums2Size;
        nums2Size = tmpSize;
    }

    int m = nums1Size;
    int n = nums2Size;
    int left = 0, right = m;

    while (left <= right) {
        int partitionA = (left + right) / 2;
        int partitionB = (m + n + 1) / 2 - partitionA;

        int maxLeftA = (partitionA == 0) ? INT_MIN : nums1[partitionA - 1];
        int minRightA = (partitionA == m) ? INT_MAX : nums1[partitionA];

        int maxLeftB = (partitionB == 0) ? INT_MIN : nums2[partitionB - 1];
        int minRightB = (partitionB == n) ? INT_MAX : nums2[partitionB];

        if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
            // Correct partition
            if ((m + n) % 2 == 0) {
                int leftMax = (maxLeftA > maxLeftB) ? maxLeftA : maxLeftB;
                int rightMin = (minRightA < minRightB) ? minRightA : minRightB;
                return ((double)leftMax + (double)rightMin) / 2.0;
            } else {
                int leftMax = (maxLeftA > maxLeftB) ? maxLeftA : maxLeftB;
                return (double)leftMax;
            }
        } else if (maxLeftA > minRightB) {
            // Move towards left in nums1
            right = partitionA - 1;
        } else {
            // Move towards right in nums1
            left = partitionA + 1;
        }
    }

    // Should never reach here if input arrays are valid
    return 0.0;
}
```

## Csharp

```csharp
public class Solution
{
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        // Ensure nums1 is the smaller array to get O(log(min(m,n))) time.
        if (nums1.Length > nums2.Length)
        {
            var temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        int m = nums1.Length;
        int n = nums2.Length;
        int left = 0, right = m;

        while (left <= right)
        {
            int partitionX = (left + right) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;

            int maxLeftX = (partitionX == 0) ? int.MinValue : nums1[partitionX - 1];
            int minRightX = (partitionX == m) ? int.MaxValue : nums1[partitionX];

            int maxLeftY = (partitionY == 0) ? int.MinValue : nums2[partitionY - 1];
            int minRightY = (partitionY == n) ? int.MaxValue : nums2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX)
            {
                // Correct partition found.
                if ((m + n) % 2 == 0)
                {
                    double leftMax = Math.Max(maxLeftX, maxLeftY);
                    double rightMin = Math.Min(minRightX, minRightY);
                    return (leftMax + rightMin) / 2.0;
                }
                else
                {
                    return (double)Math.Max(maxLeftX, maxLeftY);
                }
            }
            else if (maxLeftX > minRightY)
            {
                // Move towards left in nums1.
                right = partitionX - 1;
            }
            else
            {
                // Move towards right in nums1.
                left = partitionX + 1;
            }
        }

        // Should never reach here if input arrays are valid.
        throw new System.ArgumentException("Input arrays are not sorted or invalid.");
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    // Ensure nums1 is the smaller array for binary search efficiency
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    const m = nums1.length;
    const n = nums2.length;
    let left = 0, right = m;
    const totalLeft = Math.floor((m + n + 1) / 2); // number of elements in left partition

    while (left <= right) {
        const partitionA = Math.floor((left + right) / 2);
        const partitionB = totalLeft - partitionA;

        const maxLeftA = (partitionA === 0) ? -Infinity : nums1[partitionA - 1];
        const minRightA = (partitionA === m) ? Infinity : nums1[partitionA];

        const maxLeftB = (partitionB === 0) ? -Infinity : nums2[partitionB - 1];
        const minRightB = (partitionB === n) ? Infinity : nums2[partitionB];

        if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
            // Correct partition found
            if ((m + n) % 2 === 1) {
                return Math.max(maxLeftA, maxLeftB);
            } else {
                const leftMax = Math.max(maxLeftA, maxLeftB);
                const rightMin = Math.min(minRightA, minRightB);
                return (leftMax + rightMin) / 2;
            }
        } else if (maxLeftA > minRightB) {
            // Move partitionA to the left
            right = partitionA - 1;
        } else {
            // Move partitionA to the right
            left = partitionA + 1;
        }
    }

    // Should never reach here if input arrays are valid per problem constraints
    return 0;
};
```

## Typescript

```typescript
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    // Ensure nums1 is the smaller array
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    const m = nums1.length;
    const n = nums2.length;
    let left = 0;
    let right = m;

    while (left <= right) {
        const partitionA = Math.floor((left + right) / 2);
        const partitionB = Math.floor((m + n + 1) / 2) - partitionA;

        const maxLeftA = partitionA === 0 ? Number.NEGATIVE_INFINITY : nums1[partitionA - 1];
        const minRightA = partitionA === m ? Number.POSITIVE_INFINITY : nums1[partitionA];

        const maxLeftB = partitionB === 0 ? Number.NEGATIVE_INFINITY : nums2[partitionB - 1];
        const minRightB = partitionB === n ? Number.POSITIVE_INFINITY : nums2[partitionB];

        if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
            if ((m + n) % 2 === 0) {
                return (Math.max(maxLeftA, maxLeftB) + Math.min(minRightA, minRightB)) / 2;
            } else {
                return Math.max(maxLeftA, maxLeftB);
            }
        } else if (maxLeftA > minRightB) {
            right = partitionA - 1;
        } else {
            left = partitionA + 1;
        }
    }

    // Should never reach here if input constraints are satisfied
    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Float
     */
    function findMedianSortedArrays($nums1, $nums2) {
        // Ensure nums1 is the smaller array
        if (count($nums1) > count($nums2)) {
            $tmp = $nums1;
            $nums1 = $nums2;
            $nums2 = $tmp;
        }

        $m = count($nums1);
        $n = count($nums2);
        $totalLeft = intdiv($m + $n + 1, 2);

        $left = 0;
        $right = $m;

        while ($left <= $right) {
            $i = intdiv($left + $right, 2); // partition of nums1
            $j = $totalLeft - $i;           // partition of nums2

            $maxLeftA  = ($i == 0) ? -INF : $nums1[$i - 1];
            $minRightA = ($i == $m) ? INF : $nums1[$i];

            $maxLeftB  = ($j == 0) ? -INF : $nums2[$j - 1];
            $minRightB = ($j == $n) ? INF : $nums2[$j];

            if ($maxLeftA <= $minRightB && $maxLeftB <= $minRightA) {
                // Correct partition found
                if ((($m + $n) % 2) == 1) {
                    return max($maxLeftA, $maxLeftB);
                } else {
                    $leftMax = max($maxLeftA, $maxLeftB);
                    $rightMin = min($minRightA, $minRightB);
                    return ($leftMax + $rightMin) / 2.0;
                }
            } elseif ($maxLeftA > $minRightB) {
                // Move partition A left
                $right = $i - 1;
            } else {
                // Move partition A right
                $left = $i + 1;
            }
        }

        // Should never reach here if input arrays are valid
        return 0.0;
    }
}
```

## Swift

```swift
class Solution {
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        var A = nums1
        var B = nums2
        if A.count > B.count {
            swap(&A, &B)
        }
        let m = A.count
        let n = B.count
        var left = 0
        var right = m
        
        while left <= right {
            let i = (left + right) / 2
            let j = (m + n + 1) / 2 - i
            
            let maxLeftA = (i == 0) ? Int.min : A[i - 1]
            let minRightA = (i == m) ? Int.max : A[i]
            
            let maxLeftB = (j == 0) ? Int.min : B[j - 1]
            let minRightB = (j == n) ? Int.max : B[j]
            
            if maxLeftA <= minRightB && maxLeftB <= minRightA {
                if (m + n) % 2 == 0 {
                    let leftMax = max(maxLeftA, maxLeftB)
                    let rightMin = min(minRightA, minRightB)
                    return Double(leftMax + rightMin) / 2.0
                } else {
                    return Double(max(maxLeftA, maxLeftB))
                }
            } else if maxLeftA > minRightB {
                right = i - 1
            } else {
                left = i + 1
            }
        }
        return 0.0 // Should never be reached given problem constraints
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
        var a = nums1
        var b = nums2
        if (a.size > b.size) {
            val tmp = a
            a = b
            b = tmp
        }
        val m = a.size
        val n = b.size
        var left = 0
        var right = m
        while (left <= right) {
            val partitionA = (left + right) / 2
            val partitionB = (m + n + 1) / 2 - partitionA

            val maxLeftA = if (partitionA == 0) Int.MIN_VALUE else a[partitionA - 1]
            val minRightA = if (partitionA == m) Int.MAX_VALUE else a[partitionA]

            val maxLeftB = if (partitionB == 0) Int.MIN_VALUE else b[partitionB - 1]
            val minRightB = if (partitionB == n) Int.MAX_VALUE else b[partitionB]

            if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
                return if ((m + n) % 2 == 0) {
                    (kotlin.math.max(maxLeftA, maxLeftB).toDouble() +
                            kotlin.math.min(minRightA, minRightB).toDouble()) / 2.0
                } else {
                    kotlin.math.max(maxLeftA, maxLeftB).toDouble()
                }
            } else if (maxLeftA > minRightB) {
                right = partitionA - 1
            } else {
                left = partitionA + 1
            }
        }
        return 0.0
    }
}
```

## Dart

```dart
class Solution {
  double findMedianSortedArrays(List<int> nums1, List<int> nums2) {
    if (nums1.length > nums2.length) {
      return findMedianSortedArrays(nums2, nums1);
    }
    int m = nums1.length;
    int n = nums2.length;
    int left = 0;
    int right = m;

    while (true) {
      int partitionA = ((left + right) ~/ 2);
      int partitionB = ((m + n + 1) ~/ 2) - partitionA;

      double maxLeftA = partitionA == 0
          ? double.negativeInfinity
          : nums1[partitionA - 1].toDouble();
      double minRightA = partitionA == m
          ? double.infinity
          : nums1[partitionA].toDouble();

      double maxLeftB = partitionB == 0
          ? double.negativeInfinity
          : nums2[partitionB - 1].toDouble();
      double minRightB = partitionB == n
          ? double.infinity
          : nums2[partitionB].toDouble();

      if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
        if ((m + n) % 2 == 0) {
          double leftMax = maxLeftA > maxLeftB ? maxLeftA : maxLeftB;
          double rightMin = minRightA < minRightB ? minRightA : minRightB;
          return (leftMax + rightMin) / 2.0;
        } else {
          return maxLeftA > maxLeftB ? maxLeftA : maxLeftB;
        }
      } else if (maxLeftA > minRightB) {
        right = partitionA - 1;
      } else {
        left = partitionA + 1;
      }
    }
  }
}
```

## Golang

```go
package main

import (
	"math"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// Ensure nums1 is the smaller array.
	if len(nums1) > len(nums2) {
		nums1, nums2 = nums2, nums1
	}
	m, n := len(nums1), len(nums2)
	left, right := 0, m
	halfLen := (m + n + 1) / 2

	for left <= right {
		i := (left + right) / 2          // partition of nums1
		j := halfLen - i                 // partition of nums2

		var maxLeftA int
		if i == 0 {
			maxLeftA = math.MinInt64
		} else {
			maxLeftA = nums1[i-1]
		}
		var minRightA int
		if i == m {
			minRightA = math.MaxInt64
		} else {
			minRightA = nums1[i]
		}

		var maxLeftB int
		if j == 0 {
			maxLeftB = math.MinInt64
		} else {
			maxLeftB = nums2[j-1]
		}
		var minRightB int
		if j == n {
			minRightB = math.MaxInt64
		} else {
			minRightB = nums2[j]
		}

		if maxLeftA <= minRightB && maxLeftB <= minRightA {
			if (m+n)%2 == 1 {
				return float64(max(maxLeftA, maxLeftB))
			}
			return float64(max(maxLeftA, maxLeftB)+min(minRightA, minRightB)) / 2.0
		} else if maxLeftA > minRightB {
			right = i - 1
		} else {
			left = i + 1
		}
	}
	// Should never reach here.
	return 0.0
}
```

## Ruby

```ruby
def find_median_sorted_arrays(nums1, nums2)
  m = nums1.length
  n = nums2.length
  if m > n
    return find_median_sorted_arrays(nums2, nums1)
  end

  left = 0
  right = m
  half = (m + n + 1) / 2

  while left <= right
    partition_a = (left + right) / 2
    partition_b = half - partition_a

    max_left_a = partition_a == 0 ? -Float::INFINITY : nums1[partition_a - 1]
    min_right_a = partition_a == m ? Float::INFINITY : nums1[partition_a]

    max_left_b = partition_b == 0 ? -Float::INFINITY : nums2[partition_b - 1]
    min_right_b = partition_b == n ? Float::INFINITY : nums2[partition_b]

    if max_left_a <= min_right_b && max_left_b <= min_right_a
      if (m + n).odd?
        return [max_left_a, max_left_b].max.to_f
      else
        left_max = [max_left_a, max_left_b].max
        right_min = [min_right_a, min_right_b].min
        return (left_max + right_min) / 2.0
      end
    elsif max_left_a > min_right_b
      right = partition_a - 1
    else
      left = partition_a + 1
    end
  end
end
```

## Scala

```scala
object Solution {
  def findMedianSortedArrays(nums1: Array[Int], nums2: Array[Int]): Double = {
    var A = nums1
    var B = nums2
    if (A.length > B.length) {
      val tmp = A; A = B; B = tmp
    }
    val m = A.length
    val n = B.length
    var left = 0
    var right = m

    while (left <= right) {
      val partitionA = (left + right) / 2
      val partitionB = (m + n + 1) / 2 - partitionA

      val maxLeftA = if (partitionA == 0) Int.MinValue else A(partitionA - 1)
      val minRightA = if (partitionA == m) Int.MaxValue else A(partitionA)

      val maxLeftB = if (partitionB == 0) Int.MinValue else B(partitionB - 1)
      val minRightB = if (partitionB == n) Int.MaxValue else B(partitionB)

      if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
        if ((m + n) % 2 == 0) {
          return (Math.max(maxLeftA, maxLeftB).toDouble + Math.min(minRightA, minRightB).toDouble) / 2.0
        } else {
          return Math.max(maxLeftA, maxLeftB).toDouble
        }
      } else if (maxLeftA > minRightB) {
        right = partitionA - 1
      } else {
        left = partitionA + 1
      }
    }
    0.0 // unreachable
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        // Ensure the first array is the smaller one
        let (a, b) = if nums1.len() <= nums2.len() {
            (nums1, nums2)
        } else {
            (nums2, nums1)
        };
        let m = a.len();
        let n = b.len();

        let mut left = 0usize;
        let mut right = m;

        while left <= right {
            let partition_a = (left + right) / 2;
            let partition_b = (m + n + 1) / 2 - partition_a;

            let max_left_a = if partition_a == 0 { i32::MIN } else { a[partition_a - 1] };
            let min_right_a = if partition_a == m { i32::MAX } else { a[partition_a] };

            let max_left_b = if partition_b == 0 { i32::MIN } else { b[partition_b - 1] };
            let min_right_b = if partition_b == n { i32::MAX } else { b[partition_b] };

            if max_left_a > min_right_b {
                // Move towards left in a
                right = partition_a.saturating_sub(1);
            } else if max_left_b > min_right_a {
                // Move towards right in a
                left = partition_a + 1;
            } else {
                // Correct partition found
                let max_of_left = std::cmp::max(max_left_a, max_left_b) as f64;
                if (m + n) % 2 == 1 {
                    return max_of_left;
                }
                let min_of_right = std::cmp::min(min_right_a, min_right_b) as f64;
                return (max_of_left + min_of_right) / 2.0;
            }
        }

        // The problem guarantees that input arrays are non‑empty in total,
        // so this line should never be reached.
        0.0
    }
}
```

## Racket

```racket
(define/contract (find-median-sorted-arrays nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) flonum?)
  (let* ((v1 (list->vector nums1))
         (v2 (list->vector nums2))
         (len1 (vector-length v1))
         (len2 (vector-length v2)))
    (define (median a b m n) ; a is smaller vector, length m; b length n
      (let loop ((left 0) (right m))
        (define partitionA (quotient (+ left right) 2))
        (define partitionB (- (quotient (+ m n 1) 2) partitionA))
        (define maxLeftA (if (= partitionA 0) -inf.0 (vector-ref a (- partitionA 1))))
        (define minRightA (if (= partitionA m) +inf.0 (vector-ref a partitionA)))
        (define maxLeftB (if (= partitionB 0) -inf.0 (vector-ref b (- partitionB 1))))
        (define minRightB (if (= partitionB n) +inf.0 (vector-ref b partitionB)))
        (cond
          [(> maxLeftA minRightB)
           (loop left (- partitionA 1))]
          [(> maxLeftB minRightA)
           (loop (+ partitionA 1) right)]
          [else
           (let ((total (+ m n))
                 (med (if (= (modulo total 2) 1)
                          (max maxLeftA maxLeftB)
                          (/ (+ (max maxLeftA maxLeftB) (min minRightA minRightB)) 2.0))))
             (+ 0.0 med))])))
    (if (> len1 len2)
        (median v2 v1 len2 len1)
        (median v1 v2 len1 len2))))
```

## Erlang

```erlang
-spec find_median_sorted_arrays(Nums1 :: [integer()], Nums2 :: [integer()]) -> float().
find_median_sorted_arrays(Nums1, Nums2) ->
    % Ensure the first array is the smaller one
    case length(Nums1) =< length(Nums2) of
        true  -> Small = Nums1, Large = Nums2;
        false -> Small = Nums2, Large = Nums1
    end,
    A = list_to_tuple(Small),
    B = list_to_tuple(Large),
    M = tuple_size(A),
    N = tuple_size(B),
    Total = M + N,
    Half = (Total + 1) div 2,
    binary_search(A, B, M, N, Half, Total, 0, M).

binary_search(_A, _B, _M, _N, _Half, _Total, L, R) when L > R ->
    0.0; % should never happen
binary_search(A, B, M, N, Half, Total, L, R) ->
    PartitionA = (L + R) div 2,
    PartitionB = Half - PartitionA,

    MaxLeftA = if PartitionA == 0 -> -1.0e18;
                  true -> element_at(A, PartitionA - 1)
               end,
    MinRightA = if PartitionA == M -> 1.0e18;
                   true -> element_at(A, PartitionA)
                end,

    MaxLeftB = if PartitionB == 0 -> -1.0e18;
                  true -> element_at(B, PartitionB - 1)
               end,
    MinRightB = if PartitionB == N -> 1.0e18;
                   true -> element_at(B, PartitionB)
                end,

    case (MaxLeftA =< MinRightB) andalso (MaxLeftB =< MinRightA) of
        true ->
            if Total rem 2 =:= 0 ->
                    (erlang:max(MaxLeftA, MaxLeftB) + erlang:min(MinRightA, MinRightB)) / 2.0;
               true ->
                    erlang:max(MaxLeftA, MaxLeftB) * 1.0
            end;
        false ->
            if MaxLeftA > MinRightB ->
                    binary_search(A, B, M, N, Half, Total, L, PartitionA - 1);
               true -> % MaxLeftB > MinRightA
                    binary_search(A, B, M, N, Half, Total, PartitionA + 1, R)
            end
    end.

element_at(Tuple, IndexZero) ->
    erlang:element(IndexZero + 1, Tuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_median_sorted_arrays(nums1 :: [integer], nums2 :: [integer]) :: float
  def find_median_sorted_arrays(nums1, nums2) do
    {a, b} =
      if length(nums1) <= length(nums2) do
        {nums1, nums2}
      else
        {nums2, nums1}
      end

    m = length(a)
    n = length(b)

    median_helper(a, b, m, n, 0, m)
  end

  defp median_helper(a, b, m, n, left, right) do
    partition_a = div(left + right, 2)
    partition_b = div(m + n + 1, 2) - partition_a

    max_left_a =
      if partition_a == 0 do
        -1.0 / 0.0
      else
        Enum.at(a, partition_a - 1)
      end

    min_right_a =
      if partition_a == m do
        1.0 / 0.0
      else
        Enum.at(a, partition_a)
      end

    max_left_b =
      if partition_b == 0 do
        -1.0 / 0.0
      else
        Enum.at(b, partition_b - 1)
      end

    min_right_b =
      if partition_b == n do
        1.0 / 0.0
      else
        Enum.at(b, partition_b)
      end

    cond do
      max_left_a > min_right_b ->
        median_helper(a, b, m, n, left, partition_a - 1)

      max_left_b > min_right_a ->
        median_helper(a, b, m, n, partition_a + 1, right)

      true ->
        if rem(m + n, 2) == 0 do
          (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2.0
        else
          max(max_left_a, max_left_b) * 1.0
        end
    end
  end
end
```
