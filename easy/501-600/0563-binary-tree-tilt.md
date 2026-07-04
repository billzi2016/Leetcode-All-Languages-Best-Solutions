# 0563. Binary Tree Tilt

## Cpp

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int findTilt(TreeNode* root) {
        long long total = 0;
        std::function<long long(TreeNode*)> dfs = [&](TreeNode* node) -> long long {
            if (!node) return 0;
            long long leftSum = dfs(node->left);
            long long rightSum = dfs(node->right);
            total += std::llabs(leftSum - rightSum);
            return node->val + leftSum + rightSum;
        };
        dfs(root);
        return static_cast<int>(total);
    }
};
```

## Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int totalTilt = 0;

    public int findTilt(TreeNode root) {
        computeSum(root);
        return totalTilt;
    }

    private int computeSum(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftSum = computeSum(node.left);
        int rightSum = computeSum(node.right);
        totalTilt += Math.abs(leftSum - rightSum);
        return node.val + leftSum + rightSum;
    }
}
```

## Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.total_tilt = 0

        def postorder(node):
            if not node:
                return 0
            left_sum = postorder(node.left)
            right_sum = postorder(node.right)
            self.total_tilt += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum

        postorder(root)
        return self.total_tilt
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            self.total += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum

        dfs(root)
        return self.total
```

## C

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <stdlib.h>

static long dfs(struct TreeNode* node, long *totalTilt) {
    if (node == NULL) return 0;
    long leftSum = dfs(node->left, totalTilt);
    long rightSum = dfs(node->right, totalTilt);
    *totalTilt += llabs(leftSum - rightSum);
    return node->val + leftSum + rightSum;
}

int findTilt(struct TreeNode* root) {
    long total = 0;
    dfs(root, &total);
    return (int)total;
}
```

## Csharp

```csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private int totalTilt;

    public int FindTilt(TreeNode root) {
        totalTilt = 0;
        ComputeSum(root);
        return totalTilt;
    }

    private int ComputeSum(TreeNode node) {
        if (node == null) return 0;
        int leftSum = ComputeSum(node.left);
        int rightSum = ComputeSum(node.right);
        totalTilt += System.Math.Abs(leftSum - rightSum);
        return node.val + leftSum + rightSum;
    }
}
```

## Javascript

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var findTilt = function(root) {
    let totalTilt = 0;
    const dfs = (node) => {
        if (!node) return 0;
        const leftSum = dfs(node.left);
        const rightSum = dfs(node.right);
        totalTilt += Math.abs(leftSum - rightSum);
        return node.val + leftSum + rightSum;
    };
    dfs(root);
    return totalTilt;
};
```

## Typescript

```typescript
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function findTilt(root: TreeNode | null): number {
    let totalTilt = 0;
    const dfs = (node: TreeNode | null): number => {
        if (!node) return 0;
        const leftSum = dfs(node.left);
        const rightSum = dfs(node.right);
        totalTilt += Math.abs(leftSum - rightSum);
        return node.val + leftSum + rightSum;
    };
    dfs(root);
    return totalTilt;
}
```

## Php

```php
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {
    private int $totalTilt = 0;

    /**
     * @param TreeNode|null $root
     * @return int
     */
    function findTilt($root) {
        $this->totalTilt = 0;
        $this->postOrderSum($root);
        return $this->totalTilt;
    }

    private function postOrderSum($node): int {
        if ($node === null) {
            return 0;
        }
        $leftSum = $this->postOrderSum($node->left);
        $rightSum = $this->postOrderSum($node->right);
        $this->totalTilt += abs($leftSum - $rightSum);
        return $node->val + $leftSum + $rightSum;
    }
}
```

## Swift

```swift
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func findTilt(_ root: TreeNode?) -> Int {
        var totalTilt = 0
        
        func subtreeSum(_ node: TreeNode?) -> Int {
            guard let n = node else { return 0 }
            let left = subtreeSum(n.left)
            let right = subtreeSum(n.right)
            totalTilt += abs(left - right)
            return n.val + left + right
        }
        
        _ = subtreeSum(root)
        return totalTilt
    }
}
```

## Kotlin

```kotlin
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    private var totalTilt = 0

    fun findTilt(root: TreeNode?): Int {
        totalTilt = 0
        dfs(root)
        return totalTilt
    }

    private fun dfs(node: TreeNode?): Int {
        if (node == null) return 0
        val leftSum = dfs(node.left)
        val rightSum = dfs(node.right)
        totalTilt += kotlin.math.abs(leftSum - rightSum)
        return node.`val` + leftSum + rightSum
    }
}
```

## Dart

```dart
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class Solution {
  int findTilt(TreeNode? root) {
    int totalTilt = 0;

    int subtreeSum(TreeNode? node) {
      if (node == null) return 0;
      int left = subtreeSum(node.left);
      int right = subtreeSum(node.right);
      totalTilt += (left - right).abs();
      return node.val + left + right;
    }

    subtreeSum(root);
    return totalTilt;
  }
}
```

## Golang

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */
func findTilt(root *TreeNode) int {
    var total int
    var dfs func(*TreeNode) int
    dfs = func(node *TreeNode) int {
        if node == nil {
            return 0
        }
        leftSum := dfs(node.Left)
        rightSum := dfs(node.Right)
        diff := leftSum - rightSum
        if diff < 0 {
            diff = -diff
        }
        total += diff
        return node.Val + leftSum + rightSum
    }
    dfs(root)
    return total
}
```

## Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def find_tilt(root)
  @total_tilt = 0
  subtree_sum(root)
  @total_tilt
end

def subtree_sum(node)
  return 0 unless node
  left_sum = subtree_sum(node.left)
  right_sum = subtree_sum(node.right)
  @total_tilt += (left_sum - right_sum).abs
  node.val + left_sum + right_sum
end
```

## Scala

```scala
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def findTilt(root: TreeNode): Int = {
    var totalTilt = 0

    def postOrder(node: TreeNode): Int = {
      if (node == null) return 0
      val leftSum = postOrder(node.left)
      val rightSum = postOrder(node.right)
      totalTilt += math.abs(leftSum - rightSum)
      node.value + leftSum + rightSum
    }

    postOrder(root)
    totalTilt
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }

pub struct Solution;

impl Solution {
    pub fn find_tilt(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, total: &mut i32) -> i32 {
            if let Some(rc) = node {
                let left_sum = dfs(rc.borrow().left.clone(), total);
                let right_sum = dfs(rc.borrow().right.clone(), total);
                *total += (left_sum - right_sum).abs();
                rc.borrow().val + left_sum + right_sum
            } else {
                0
            }
        }

        let mut ans = 0;
        dfs(root, &mut ans);
        ans
    }
}
```

## Racket

```racket
#|
; Definition for a binary tree node.
; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (find-tilt root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ((total 0))
    (define (dfs node)
      (if (not node)
          0
          (let* ((left-sum  (dfs (tree-node-left node)))
                 (right-sum (dfs (tree-node-right node))))
            (set! total (+ total (abs (- left-sum right-sum))))
            (+ (tree-node-val node) left-sum right-sum))))
    (dfs root)
    total))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec find_tilt(Root :: #tree_node{} | null) -> integer().
find_tilt(Root) ->
    {_, Tilt} = tilt_helper(Root),
    Tilt.

tilt_helper(null) ->
    {0, 0};
tilt_helper(#tree_node{val = V, left = L, right = R}) ->
    {SumL, TiltL} = tilt_helper(L),
    {SumR, TiltR} = tilt_helper(R),
    NodeTilt = abs(SumL - SumR),
    {V + SumL + SumR, NodeTilt + TiltL + TiltR}.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_tilt(root :: TreeNode.t() | nil) :: integer
  def find_tilt(root) do
    {_sum, tilt} = dfs(root)
    tilt
  end

  defp dfs(nil), do: {0, 0}

  defp dfs(%TreeNode{val: v, left: l, right: r}) do
    {lsum, ltilt} = dfs(l)
    {rsum, rtilt} = dfs(r)

    node_tilt = abs(lsum - rsum)
    total_sum = v + lsum + rsum
    total_tilt = ltilt + rtilt + node_tilt

    {total_sum, total_tilt}
  end
end
```
