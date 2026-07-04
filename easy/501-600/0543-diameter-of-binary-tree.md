# 0543. Diameter of Binary Tree

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
    int diameterOfBinaryTree(TreeNode* root) {
        int ans = 0;
        std::function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {
            if (!node) return 0;
            int leftDepth = dfs(node->left);
            int rightDepth = dfs(node->right);
            ans = std::max(ans, leftDepth + rightDepth);
            return std::max(leftDepth, rightDepth) + 1;
        };
        dfs(root);
        return ans;
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
    private int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);
        return maxDiameter;
    }

    private int depth(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = depth(node.left);
        int right = depth(node.right);
        maxDiameter = Math.max(maxDiameter, left + right);
        return Math.max(left, right) + 1;
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
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # path through this node = left edges + right edges
            self.max_diameter = max(self.max_diameter, left + right)
            # height of node = max edges to leaf
            return max(left, right) + 1

        depth(root)
        return self.max_diameter
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
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            # Update the maximum diameter found so far.
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            # Return height of this subtree.
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.max_diameter
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
static int depth(struct TreeNode* node, int *maxDia) {
    if (!node) return 0;
    int left = depth(node->left, maxDia);
    int right = depth(node->right, maxDia);
    if (left + right > *maxDia) *maxDia = left + right;
    return (left > right ? left : right) + 1;
}

int diameterOfBinaryTree(struct TreeNode* root) {
    int maxDia = 0;
    depth(root, &maxDia);
    return maxDia;
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
    private int maxDiameter = 0;

    public int DiameterOfBinaryTree(TreeNode root) {
        Height(root);
        return maxDiameter;
    }

    private int Height(TreeNode node) {
        if (node == null) return 0;
        int left = Height(node.left);
        int right = Height(node.right);
        // path through this node is left edges + right edges
        maxDiameter = Math.Max(maxDiameter, left + right);
        // height in edges from this node down to leaf
        return Math.Max(left, right) + 1;
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
var diameterOfBinaryTree = function(root) {
    let maxDiameter = 0;
    const depth = (node) => {
        if (!node) return 0;
        const left = depth(node.left);
        const right = depth(node.right);
        maxDiameter = Math.max(maxDiameter, left + right);
        return Math.max(left, right) + 1;
    };
    depth(root);
    return maxDiameter;
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

function diameterOfBinaryTree(root: TreeNode | null): number {
    let maxDiameter = 0;
    
    function depth(node: TreeNode | null): number {
        if (!node) return 0;
        const left = depth(node.left);
        const right = depth(node.right);
        // path through this node
        maxDiameter = Math.max(maxDiameter, left + right);
        // height of the node
        return Math.max(left, right) + 1;
    }
    
    depth(root);
    return maxDiameter;
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

    private $maxDiameter = 0;

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function diameterOfBinaryTree($root) {
        $this->dfs($root);
        return $this->maxDiameter;
    }

    private function dfs($node) {
        if ($node === null) {
            return 0;
        }
        $leftDepth = $this->dfs($node->left);
        $rightDepth = $this->dfs($node->right);

        // Update the maximum diameter found so far.
        $this->maxDiameter = max($this->maxDiameter, $leftDepth + $rightDepth);

        // Return height of current node.
        return max($leftDepth, $rightDepth) + 1;
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
    private var maxDiameter = 0
    
    func diameterOfBinaryTree(_ root: TreeNode?) -> Int {
        _ = depth(root)
        return maxDiameter
    }
    
    private func depth(_ node: TreeNode?) -> Int {
        guard let n = node else { return 0 }
        let leftDepth = depth(n.left)
        let rightDepth = depth(n.right)
        maxDiameter = max(maxDiameter, leftDepth + rightDepth)
        return max(leftDepth, rightDepth) + 1
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
    private var maxDiameter = 0

    fun diameterOfBinaryTree(root: TreeNode?): Int {
        depth(root)
        return maxDiameter
    }

    private fun depth(node: TreeNode?): Int {
        if (node == null) return 0
        val left = depth(node.left)
        val right = depth(node.right)
        maxDiameter = kotlin.math.max(maxDiameter, left + right)
        return kotlin.math.max(left, right) + 1
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
  int _maxDiameter = 0;

  int diameterOfBinaryTree(TreeNode? root) {
    _depth(root);
    return _maxDiameter;
  }

  int _depth(TreeNode? node) {
    if (node == null) return 0;
    int left = _depth(node.left);
    int right = _depth(node.right);
    if (left + right > _maxDiameter) {
      _maxDiameter = left + right;
    }
    return (left > right ? left : right) + 1;
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
func diameterOfBinaryTree(root *TreeNode) int {
    var maxDiameter int
    var dfs func(*TreeNode) int
    dfs = func(node *TreeNode) int {
        if node == nil {
            return 0
        }
        left := dfs(node.Left)
        right := dfs(node.Right)
        if left+right > maxDiameter {
            maxDiameter = left + right
        }
        if left > right {
            return left + 1
        }
        return right + 1
    }
    dfs(root)
    return maxDiameter
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

def diameter_of_binary_tree(root)
  @max_diameter = 0
  depth = ->(node) {
    return 0 unless node
    left = depth.call(node.left)
    right = depth.call(node.right)
    @max_diameter = [@max_diameter, left + right].max
    1 + (left > right ? left : right)
  }
  depth.call(root)
  @max_diameter
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
    def diameterOfBinaryTree(root: TreeNode): Int = {
        var maxDiameter = 0

        def depth(node: TreeNode): Int = {
            if (node == null) return 0
            val left = depth(node.left)
            val right = depth(node.right)
            maxDiameter = math.max(maxDiameter, left + right)
            math.max(left, right) + 1
        }

        depth(root)
        maxDiameter
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<&Rc<RefCell<TreeNode>>>, ans: &mut i32) -> i32 {
            if let Some(rc_node) = node {
                let left = dfs(rc_node.borrow().left.as_ref(), ans);
                let right = dfs(rc_node.borrow().right.as_ref(), ans);
                *ans = (*ans).max(left + right);
                1 + left.max(right)
            } else {
                0
            }
        }

        let mut max_diameter = 0;
        dfs(root.as_ref(), &mut max_diameter);
        max_diameter
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

(define/contract (diameter-of-binary-tree root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ((max-dia (box 0)))
    (define (height node)
      (if (not node)
          -1
          (let* ((lh (height (tree-node-left node)))
                 (rh (height (tree-node-right node))))
            (let ((dia (+ lh rh 2)))
              (when (> dia (unbox max-dia))
                (set-box! max-dia dia)))
            (max lh rh))))
    (height root)
    (unbox max-dia)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec diameter_of_binary_tree(Root :: #tree_node{} | null) -> integer().
diameter_of_binary_tree(Root) ->
    {_, Diameter} = dfs(Root),
    Diameter.

dfs(null) ->
    {-1, 0};
dfs(Node) ->
    {LHeight, LDia} = dfs(Node#tree_node.left),
    {RHeight, RDia} = dfs(Node#tree_node.right),
    Height = max(LHeight, RHeight) + 1,
    DiaThrough = LHeight + RHeight + 2,
    MaxDia = max(DiaThrough, max(LDia, RDia)),
    {Height, MaxDia}.
```

## Elixir

```elixir
# Definition for a binary tree node.
#
defmodule TreeNode do
  @type t :: %__MODULE__{
          val: integer,
          left: TreeNode.t() | nil,
          right: TreeNode.t() | nil
        }
  defstruct val: 0, left: nil, right: nil
end

defmodule Solution do
  @spec diameter_of_binary_tree(root :: TreeNode.t() | nil) :: integer
  def diameter_of_binary_tree(root) do
    {_height, diameter} = dfs(root)
    diameter
  end

  defp dfs(nil), do: {0, 0}

  defp dfs(%TreeNode{left: left, right: right}) do
    {lh, ld} = dfs(left)
    {rh, rd} = dfs(right)

    height = 1 + max(lh, rh)
    through_node = lh + rh
    diameter = max(through_node, max(ld, rd))

    {height, diameter}
  end
end
```
