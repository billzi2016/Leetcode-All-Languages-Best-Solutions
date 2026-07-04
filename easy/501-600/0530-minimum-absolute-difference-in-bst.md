# 0530. Minimum Absolute Difference in BST

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
    int getMinimumDifference(TreeNode* root) {
        int prev = -1;
        int minDiff = INT_MAX;
        std::function<void(TreeNode*)> inorder = [&](TreeNode* node) {
            if (!node) return;
            inorder(node->left);
            if (prev != -1) {
                minDiff = std::min(minDiff, node->val - prev);
            }
            prev = node->val;
            inorder(node->right);
        };
        inorder(root);
        return minDiff;
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
    private Integer prev = null;
    private int minDiff = Integer.MAX_VALUE;

    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        return minDiff;
    }

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        if (prev != null) {
            minDiff = Math.min(minDiff, node.val - prev);
        }
        prev = node.val;
        inorder(node.right);
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
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev = None
        self.min_diff = float('inf')
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                diff = node.val - self.prev
                if diff < self.min_diff:
                    self.min_diff = diff
            self.prev = node.val
            inorder(node.right)
        
        inorder(root)
        return self.min_diff
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root):
        stack = []
        prev = None
        min_diff = float('inf')
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev is not None:
                diff = node.val - prev
                if diff < min_diff:
                    min_diff = diff
            prev = node.val
            node = node.right
        return min_diff
```

## C

```c
#include <limits.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
static void inorder(struct TreeNode* node, int *prev, int *minDiff) {
    if (!node) return;
    inorder(node->left, prev, minDiff);
    if (*prev != -1) {
        int diff = node->val - *prev;
        if (diff < *minDiff) *minDiff = diff;
    }
    *prev = node->val;
    inorder(node->right, prev, minDiff);
}

int getMinimumDifference(struct TreeNode* root) {
    int prev = -1;
    int minDiff = INT_MAX;
    inorder(root, &prev, &minDiff);
    return minDiff;
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
public class Solution
{
    private int _prev = -1; // sentinel since node values are non‑negative
    private int _minDiff = int.MaxValue;

    public int GetMinimumDifference(TreeNode root)
    {
        Inorder(root);
        return _minDiff;
    }

    private void Inorder(TreeNode node)
    {
        if (node == null) return;

        Inorder(node.left);

        if (_prev != -1)
        {
            int diff = node.val - _prev;
            if (diff < _minDiff) _minDiff = diff;
        }
        _prev = node.val;

        Inorder(node.right);
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
var getMinimumDifference = function(root) {
    let prev = null;
    let minDiff = Infinity;
    
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        if (prev !== null) {
            const diff = node.val - prev;
            if (diff < minDiff) minDiff = diff;
        }
        prev = node.val;
        inorder(node.right);
    };
    
    inorder(root);
    return minDiff;
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

function getMinimumDifference(root: TreeNode | null): number {
    if (!root) return 0;
    let prev: number | null = null;
    let minDiff = Number.MAX_SAFE_INTEGER;

    const inorder = (node: TreeNode | null): void => {
        if (!node) return;
        inorder(node.left);
        if (prev !== null) {
            const diff = node.val - prev;
            if (diff < minDiff) minDiff = diff;
        }
        prev = node.val;
        inorder(node.right);
    };

    inorder(root);
    return minDiff;
}
```

## Php

```php
<?php
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
    private $prev = null;
    private $minDiff;

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function getMinimumDifference($root) {
        $this->minDiff = PHP_INT_MAX;
        $this->inorder($root);
        return $this->minDiff;
    }

    private function inorder($node) {
        if ($node === null) {
            return;
        }
        $this->inorder($node->left);
        if ($this->prev !== null) {
            $diff = $node->val - $this->prev;
            if ($diff < $this->minDiff) {
                $this->minDiff = $diff;
            }
        }
        $this->prev = $node->val;
        $this->inorder($node->right);
    }
}
?>
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
    func getMinimumDifference(_ root: TreeNode?) -> Int {
        var stack = [TreeNode]()
        var node = root
        var prevVal: Int? = nil
        var minDiff = Int.max
        
        while node != nil || !stack.isEmpty {
            while let cur = node {
                stack.append(cur)
                node = cur.left
            }
            let current = stack.removeLast()
            if let p = prevVal {
                let diff = current.val - p
                if diff < minDiff { minDiff = diff }
            }
            prevVal = current.val
            node = current.right
        }
        return minDiff
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
    private var prev: Int? = null
    private var minDiff = Int.MAX_VALUE

    fun getMinimumDifference(root: TreeNode?): Int {
        inorder(root)
        return minDiff
    }

    private fun inorder(node: TreeNode?) {
        if (node == null) return
        inorder(node.left)
        prev?.let {
            val diff = node.`val` - it
            if (diff < minDiff) minDiff = diff
        }
        prev = node.`val`
        inorder(node.right)
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
  int getMinimumDifference(TreeNode? root) {
    int minDiff = 1 << 30; // sufficiently large
    int? prev;

    void inorder(TreeNode? node) {
      if (node == null) return;
      inorder(node.left);
      if (prev != null) {
        int diff = node.val - prev!;
        if (diff < minDiff) minDiff = diff;
      }
      prev = node.val;
      inorder(node.right);
    }

    inorder(root);
    return minDiff;
  }
}
```

## Golang

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getMinimumDifference(root *TreeNode) int {
    maxInt := int(^uint(0) >> 1)
    minDiff := maxInt
    var prevVal int
    hasPrev := false

    var inorder func(node *TreeNode)
    inorder = func(node *TreeNode) {
        if node == nil {
            return
        }
        inorder(node.Left)

        if hasPrev {
            diff := node.Val - prevVal
            if diff < minDiff {
                minDiff = diff
            }
        }
        prevVal = node.Val
        hasPrev = true

        inorder(node.Right)
    }

    inorder(root)
    return minDiff
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

def get_minimum_difference(root)
  prev = nil
  min_diff = Float::INFINITY
  stack = []
  node = root

  while node || !stack.empty?
    while node
      stack << node
      node = node.left
    end
    node = stack.pop
    if !prev.nil?
      diff = node.val - prev
      min_diff = diff if diff < min_diff
    end
    prev = node.val
    node = node.right
  end

  min_diff.to_i
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
    def getMinimumDifference(root: TreeNode): Int = {
        var prev: Integer = null
        var minDiff = Int.MaxValue

        def inorder(node: TreeNode): Unit = {
            if (node == null) return
            inorder(node.left)
            if (prev != null) {
                val diff = node.value - prev.intValue()
                if (diff < minDiff) minDiff = diff
            }
            prev = node.value
            inorder(node.right)
        }

        inorder(root)
        minDiff
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn get_minimum_difference(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn inorder(node: &Option<Rc<RefCell<TreeNode>>>, prev: &mut Option<i32>, min_diff: &mut i32) {
            if let Some(rc) = node {
                let left = rc.borrow().left.clone();
                inorder(&left, prev, min_diff);
                
                let val = rc.borrow().val;
                if let Some(p) = *prev {
                    let diff = (val - p).abs();
                    if diff < *min_diff {
                        *min_diff = diff;
                    }
                }
                *prev = Some(val);
                
                let right = rc.borrow().right.clone();
                inorder(&right, prev, min_diff);
            }
        }

        let mut prev: Option<i32> = None;
        let mut min_diff = i32::MAX;
        inorder(&root, &mut prev, &mut min_diff);
        min_diff
    }
}
```

## Racket

```racket
; Definition for a binary tree node.
#|
; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (get-minimum-difference root)
  (-> (or/c tree-node? #f) exact-integer?)
  (if (not root)
      0
      (let ()
        (define prev #f)
        (define mindiff most-positive-fixnum)
        (define (inorder node)
          (when node
            (inorder (tree-node-left node))
            (let ((val (tree-node-val node)))
              (when prev
                (set! mindiff (min mindiff (- val prev))))
              (set! prev val))
            (inorder (tree-node-right node))))
        (inorder root)
        mindiff)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec get_minimum_difference(Root :: #tree_node{} | null) -> integer().
get_minimum_difference(null) ->
    0;
get_minimum_difference(Root) ->
    {_, MinDiff} = inorder(Root, undefined, 1000000),
    MinDiff.

inorder(null, Prev, Min) ->
    {Prev, Min};
inorder(#tree_node{val = Val, left = L, right = R}, Prev, Min) ->
    {Prev1, Min1} = inorder(L, Prev, Min),
    NewMin = case Prev1 of
        undefined -> Min1;
        _ -> erlang:min(Min1, erlang:abs(Val - Prev1))
    end,
    inorder(R, Val, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_minimum_difference(root :: TreeNode.t() | nil) :: integer()
  def get_minimum_difference(root) do
    {_prev, min_diff} = inorder(root, nil, 1_000_000_000)
    min_diff
  end

  defp inorder(nil, prev, min), do: {prev, min}

  defp inorder(%TreeNode{val: v, left: l, right: r}, prev, min) do
    # Traverse left subtree
    {prev_left, min_left} = inorder(l, prev, min)

    # Update min difference using the current node and previous node in-order
    {new_min, new_prev} =
      case prev_left do
        nil -> {min_left, v}
        p ->
          diff = Kernel.abs(v - p)
          {if(diff < min_left, do: diff, else: min_left), v}
      end

    # Traverse right subtree with updated state
    inorder(r, new_prev, new_min)
  end
end
```
