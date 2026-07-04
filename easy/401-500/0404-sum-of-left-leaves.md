# 0404. Sum of Left Leaves

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
    int sumOfLeftLeaves(TreeNode* root) {
        return dfs(root, false);
    }
private:
    int dfs(TreeNode* node, bool isLeft) {
        if (!node) return 0;
        if (!node->left && !node->right) {
            return isLeft ? node->val : 0;
        }
        return dfs(node->left, true) + dfs(node->right, false);
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
    public int sumOfLeftLeaves(TreeNode root) {
        return dfs(root, false);
    }

    private int dfs(TreeNode node, boolean isLeft) {
        if (node == null) {
            return 0;
        }
        if (node.left == null && node.right == null) {
            return isLeft ? node.val : 0;
        }
        return dfs(node.left, true) + dfs(node.right, false);
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: Optional[TreeNode], is_left: bool) -> int:
            if not node:
                return 0
            if not node.left and not node.right:  # leaf
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)
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
static int dfs(struct TreeNode* node, int isLeft) {
    if (!node) return 0;
    if (!node->left && !node->right) {
        return isLeft ? node->val : 0;
    }
    return dfs(node->left, 1) + dfs(node->right, 0);
}

int sumOfLeftLeaves(struct TreeNode* root) {
    return dfs(root, 0);
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
    public int SumOfLeftLeaves(TreeNode root) {
        if (root == null) return 0;
        int sum = 0;
        if (root.left != null) {
            if (root.left.left == null && root.left.right == null) {
                sum += root.left.val;
            } else {
                sum += SumOfLeftLeaves(root.left);
            }
        }
        sum += SumOfLeftLeaves(root.right);
        return sum;
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
var sumOfLeftLeaves = function(root) {
    const dfs = (node, isLeft) => {
        if (!node) return 0;
        if (!node.left && !node.right) {
            return isLeft ? node.val : 0;
        }
        return dfs(node.left, true) + dfs(node.right, false);
    };
    return dfs(root, false);
};
```

## Typescript

```typescript
function sumOfLeftLeaves(root: TreeNode | null): number {
    if (!root) return 0;
    let sum = 0;
    const dfs = (node: TreeNode | null, isLeft: boolean): void => {
        if (!node) return;
        if (!node.left && !node.right && isLeft) {
            sum += node.val;
            return;
        }
        dfs(node.left, true);
        dfs(node.right, false);
    };
    dfs(root, false);
    return sum;
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

    /**
     * @param TreeNode $root
     * @return int
     */
    function sumOfLeftLeaves($root) {
        $dfs = function($node, $isLeft) use (&$dfs) {
            if ($node === null) {
                return 0;
            }
            if ($node->left === null && $node->right === null) {
                return $isLeft ? $node->val : 0;
            }
            return $dfs($node->left, true) + $dfs($node->right, false);
        };
        return $dfs($root, false);
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
    func sumOfLeftLeaves(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        var total = 0
        
        func dfs(_ node: TreeNode?) {
            guard let node = node else { return }
            if let left = node.left {
                if left.left == nil && left.right == nil {
                    total += left.val
                } else {
                    dfs(left)
                }
            }
            dfs(node.right)
        }
        
        dfs(root)
        return total
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun sumOfLeftLeaves(root: TreeNode?): Int {
        return dfs(root, false)
    }

    private fun dfs(node: TreeNode?, isLeft: Boolean): Int {
        if (node == null) return 0
        if (node.left == null && node.right == null) {
            return if (isLeft) node.`val` else 0
        }
        val leftSum = dfs(node.left, true)
        val rightSum = dfs(node.right, false)
        return leftSum + rightSum
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
  int sumOfLeftLeaves(TreeNode? root) {
    int dfs(TreeNode? node, bool isLeft) {
      if (node == null) return 0;
      if (node.left == null && node.right == null) {
        return isLeft ? node.val : 0;
      }
      return dfs(node.left, true) + dfs(node.right, false);
    }

    return dfs(root, false);
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
func sumOfLeftLeaves(root *TreeNode) int {
	if root == nil {
		return 0
	}
	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		sum := 0
		if node.Left != nil && node.Left.Left == nil && node.Left.Right == nil {
			sum += node.Left.Val
		} else {
			sum += dfs(node.Left)
		}
		sum += dfs(node.Right)
		return sum
	}
	return dfs(root)
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

def sum_of_left_leaves(root)
  return 0 unless root
  sum = 0
  stack = [[root, false]]
  until stack.empty?
    node, is_left = stack.pop
    next if node.nil?
    if is_left && node.left.nil? && node.right.nil?
      sum += node.val
    else
      stack << [node.right, false] if node.right
      stack << [node.left, true] if node.left
    end
  end
  sum
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
    def sumOfLeftLeaves(root: TreeNode): Int = {
        def dfs(node: TreeNode, isLeft: Boolean): Int = {
            if (node == null) 0
            else if (node.left == null && node.right == null) {
                if (isLeft) node.value else 0
            } else {
                dfs(node.left, true) + dfs(node.right, false)
            }
        }
        dfs(root, false)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn sum_of_left_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, is_left: bool) -> i32 {
            if let Some(rc) = node {
                let n = rc.borrow();
                if n.left.is_none() && n.right.is_none() {
                    return if is_left { n.val } else { 0 };
                }
                let left_sum = dfs(n.left.clone(), true);
                let right_sum = dfs(n.right.clone(), false);
                left_sum + right_sum
            } else {
                0
            }
        }
        dfs(root, false)
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

(define/contract (sum-of-left-leaves root)
  (-> (or/c tree-node? #f) exact-integer?)
  (letrec ((helper
            (lambda (node is-left)
              (if (not node)
                  0
                  (let ((l (tree-node-left node))
                        (r (tree-node-right node)))
                    (if (and (not l) (not r) is-left)
                        (tree-node-val node)
                        (+ (helper l #t) (helper r #f))))))))
    (helper root #f)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec sum_of_left_leaves(Root :: #tree_node{} | null) -> integer().
sum_of_left_leaves(null) ->
    0;
sum_of_left_leaves(Root) ->
    sum(Root).

-spec sum(#tree_node{} | null) -> integer().
sum(null) ->
    0;
sum(#tree_node{left = Left, right = Right}) ->
    LeftSum =
        case Left of
            #tree_node{left = null, right = null, val = V} -> V;
            #tree_node{} -> sum(Left);
            _ -> 0
        end,
    RightSum = sum(Right),
    LeftSum + RightSum.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_left_leaves(root :: TreeNode.t() | nil) :: integer
  def sum_of_left_leaves(nil), do: 0

  def sum_of_left_leaves(%TreeNode{left: left, right: right}) do
    left_sum =
      case left do
        %TreeNode{left: nil, right: nil, val: v} -> v
        _ -> sum_of_left_leaves(left)
      end

    right_sum = sum_of_left_leaves(right)
    left_sum + right_sum
  end
end
```
