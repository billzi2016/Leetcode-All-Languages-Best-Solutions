# 0303. Range Sum Query - Immutable

## Cpp

```cpp
class NumArray {
private:
    std::vector<long long> pref;
public:
    NumArray(std::vector<int>& nums) {
        int n = nums.size();
        pref.resize(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        return static_cast<int>(pref[right + 1] - pref[left]);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
```

## Java

```java
class NumArray {
    private final int[] prefix;

    public NumArray(int[] nums) {
        int n = nums.length;
        prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
    }

    public int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */
```

## Python

```python
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right + 1] - self.prefix[left]
```

## Python3

```python
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *prefix;
    int size;
} NumArray;

NumArray* numArrayCreate(int* nums, int numsSize) {
    NumArray *obj = (NumArray *)malloc(sizeof(NumArray));
    if (!obj) return NULL;
    obj->size = numsSize;
    obj->prefix = (int *)malloc((numsSize + 1) * sizeof(int));
    if (!obj->prefix) {
        free(obj);
        return NULL;
    }
    obj->prefix[0] = 0;
    for (int i = 0; i < numsSize; ++i) {
        obj->prefix[i + 1] = obj->prefix[i] + nums[i];
    }
    return obj;
}

int numArraySumRange(NumArray* obj, int left, int right) {
    if (!obj) return 0;
    return obj->prefix[right + 1] - obj->prefix[left];
}

void numArrayFree(NumArray* obj) {
    if (obj) {
        free(obj->prefix);
        free(obj);
    }
}
```

## Csharp

```csharp
public class NumArray
{
    private readonly int[] _prefix;

    public NumArray(int[] nums)
    {
        if (nums == null) nums = new int[0];
        _prefix = new int[nums.Length + 1];
        for (int i = 0; i < nums.Length; i++)
        {
            _prefix[i + 1] = _prefix[i] + nums[i];
        }
    }

    public int SumRange(int left, int right)
    {
        return _prefix[right + 1] - _prefix[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.SumRange(left,right);
 */
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.prefix = new Array(nums.length + 1);
    this.prefix[0] = 0;
    for (let i = 0; i < nums.length; i++) {
        this.prefix[i + 1] = this.prefix[i] + nums[i];
    }
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function(left, right) {
    return this.prefix[right + 1] - this.prefix[left];
};
```

## Typescript

```typescript
class NumArray {
    private prefix: number[];

    constructor(nums: number[]) {
        this.prefix = new Array(nums.length + 1);
        this.prefix[0] = 0;
        for (let i = 0; i < nums.length; i++) {
            this.prefix[i + 1] = this.prefix[i] + nums[i];
        }
    }

    sumRange(left: number, right: number): number {
        return this.prefix[right + 1] - this.prefix[left];
    }
}
```

## Php

```php
class NumArray {
    private $prefix = [];

    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
        $this->prefix = array_fill(0, count($nums) + 1, 0);
        for ($i = 0; $i < count($nums); $i++) {
            $this->prefix[$i + 1] = $this->prefix[$i] + $nums[$i];
        }
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function sumRange($left, $right) {
        return $this->prefix[$right + 1] - $this->prefix[$left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * $obj = new NumArray($nums);
 * $ret_1 = $obj->sumRange($left, $right);
 */
```

## Swift

```swift
class NumArray {
    private var prefix: [Int]

    init(_ nums: [Int]) {
        let n = nums.count
        prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + nums[i]
        }
    }

    func sumRange(_ left: Int, _ right: Int) -> Int {
        return prefix[right + 1] - prefix[left]
    }
}
```

## Kotlin

```kotlin
class NumArray(nums: IntArray) {
    private val prefix: IntArray = IntArray(nums.size + 1)

    init {
        for (i in nums.indices) {
            prefix[i + 1] = prefix[i] + nums[i]
        }
    }

    fun sumRange(left: Int, right: Int): Int {
        return prefix[right + 1] - prefix[left]
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */
```

## Dart

```dart
class NumArray {
  late final List<int> _prefix;

  NumArray(List<int> nums) {
    _prefix = List.filled(nums.length + 1, 0);
    for (int i = 0; i < nums.length; i++) {
      _prefix[i + 1] = _prefix[i] + nums[i];
    }
  }

  int sumRange(int left, int right) {
    return _prefix[right + 1] - _prefix[left];
  }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = NumArray(nums);
 * int param1 = obj.sumRange(left,right);
 */
```

## Golang

```go
type NumArray struct {
	prefix []int
}

func Constructor(nums []int) NumArray {
	n := len(nums)
	prefix := make([]int, n+1)
	for i, v := range nums {
		prefix[i+1] = prefix[i] + v
	}
	return NumArray{prefix: prefix}
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.prefix[right+1] - this.prefix[left]
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(left,right);
 */
```

## Ruby

```ruby
class NumArray
  def initialize(nums)
    @prefix = Array.new(nums.length + 1, 0)
    nums.each_with_index do |val, i|
      @prefix[i + 1] = @prefix[i] + val
    end
  end

  def sum_range(left, right)
    @prefix[right + 1] - @prefix[left]
  end
end
```

## Scala

```scala
class NumArray(_nums: Array[Int]) {

  private val prefix: Array[Int] = {
    val n = _nums.length
    val pre = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pre(i + 1) = pre(i) + _nums(i)
      i += 1
    }
    pre
  }

  def sumRange(left: Int, right: Int): Int = {
    prefix(right + 1) - prefix(left)
  }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * val obj = new NumArray(nums)
 * val param_1 = obj.sumRange(left,right)
 */
```

## Rust

```rust
struct NumArray {
    prefix: Vec<i32>,
}

impl NumArray {
    fn new(nums: Vec<i32>) -> Self {
        let mut prefix = Vec::with_capacity(nums.len() + 1);
        prefix.push(0);
        for &num in nums.iter() {
            let last = *prefix.last().unwrap();
            prefix.push(last + num);
        }
        NumArray { prefix }
    }

    fn sum_range(&self, left: i32, right: i32) -> i32 {
        let l = left as usize;
        let r = right as usize;
        self.prefix[r + 1] - self.prefix[l]
    }
}
```

## Racket

```racket
(define num-array%
  (class object%
    (init-field nums)
    ; precompute prefix sums in a vector
    (define prefix
      (let* ((n (length nums))
             (vec (make-vector (+ n 1) 0)))
        (let loop ((i 0) (lst nums))
          (if (null? lst)
              vec
              (begin
                (vector-set! vec (add1 i)
                             (+ (vector-ref vec i) (car lst)))
                (loop (add1 i) (cdr lst)))))))
    (super-new)
    (define/public (sum-range left right)
      (- (vector-ref prefix (add1 right))
         (vector-ref prefix left)))))
```

## Erlang

```erlang
-module(solution).
-export([num_array_init_/1, num_array_sum_range/2]).

-spec num_array_init_(Nums :: [integer()]) -> any().
num_array_init_(Nums) ->
    % Build prefix sums: prefix[0]=0, prefix[i+1]=sum of first i elements
    {_, RevSums} = lists:foldl(
        fun(X, {Acc, List}) ->
            NewAcc = Acc + X,
            {NewAcc, [NewAcc | List]}
        end,
        {0, []},
        Nums),
    PrefixList = [0 | lists:reverse(RevSums)],
    PrefixTuple = list_to_tuple(PrefixList),
    put(num_array_prefix, PrefixTuple).

-spec num_array_sum_range(Left :: integer(), Right :: integer()) -> integer().
num_array_sum_range(Left, Right) ->
    Prefix = get(num_array_prefix),
    element(Right + 2, Prefix) - element(Left + 1, Prefix).
```

## Elixir

```elixir
defmodule NumArray do
  @spec init_(nums :: [integer]) :: :ok
  def init_(nums) do
    prefix =
      Enum.reduce(nums, [0], fn x, acc ->
        [hd(acc) + x | acc]
      end)
      |> Enum.reverse()

    Process.put(:numarray_prefix, prefix)
    :ok
  end

  @spec sum_range(left :: integer, right :: integer) :: integer
  def sum_range(left, right) do
    prefix = Process.get(:numarray_prefix)
    Enum.at(prefix, right + 1) - Enum.at(prefix, left)
  end
end
```
