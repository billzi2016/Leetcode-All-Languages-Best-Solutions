# 0700. Search in a Binary Search Tree

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
    TreeNode* searchBST(TreeNode* root, int val) {
        while (root && root->val != val) {
            if (val < root->val)
                root = root->left;
            else
                root = root->right;
        }
        return root;
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
    public TreeNode searchBST(TreeNode root, int val) {
        while (root != null) {
            if (val == root.val) {
                return root;
            } else if (val < root.val) {
                root = root.left;
            } else {
                root = root.right;
            }
        }
        return null;
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
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root
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
    def searchBST(self, root: Optional['TreeNode'], val: int) -> Optional['TreeNode']:
        while root:
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None
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
struct TreeNode* searchBST(struct TreeNode* root, int val) {
    while (root != NULL) {
        if (val == root->val) {
            return root;
        } else if (val < root->val) {
            root = root->left;
        } else {
            root = root->right;
        }
    }
    return NULL;
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
    public TreeNode SearchBST(TreeNode root, int val) {
        while (root != null) {
            if (val == root.val) return root;
            root = val < root.val ? root.left : root.right;
        }
        return null;
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
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function(root, val) {
    while (root !== null && root.val !== val) {
        if (val < root.val) {
            root = root.left;
        } else {
            root = root.right;
        }
    }
    return root;
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

function searchBST(root: TreeNode | null, val: number): TreeNode | null {
    while (root !== null && root.val !== val) {
        if (val < root.val) {
            root = root.left;
        } else {
            root = root.right;
        }
    }
    return root;
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
     * @param Integer $val
     * @return TreeNode|null
     */
    function searchBST($root, $val) {
        while ($root !== null && $root->val != $val) {
            if ($val < $root->val) {
                $root = $root->left;
            } else {
                $root = $root->right;
            }
        }
        return $root;
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
    func searchBST(_ root: TreeNode?, _ val: Int) -> TreeNode? {
        var node = root
        while let current = node {
            if val == current.val {
                return current
            } else if val < current.val {
                node = current.left
            } else {
                node = current.right
            }
        }
        return nil
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
    fun searchBST(root: TreeNode?, `val`: Int): TreeNode? {
        var node = root
        while (node != null) {
            when {
                node.`val` == `val` -> return node
                `val` < node.`val` -> node = node.left
                else -> node = node.right
            }
        }
        return null
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
  TreeNode? searchBST(TreeNode? root, int val) {
    while (root != null && root.val != val) {
      if (val < root.val) {
        root = root.left;
      } else {
        root = root.right;
      }
    }
    return root;
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
func searchBST(root *TreeNode, val int) *TreeNode {
    for root != nil && root.Val != val {
        if val < root.Val {
            root = root.Left
        } else {
            root = root.Right
        }
    }
    return root
}
```

## Ruby

```ruby
def search_bst(root, val)
  while root
    if val == root.val
      return root
    elsif val < root.val
      root = root.left
    else
      root = root.right
    end
  end
  nil
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
    def searchBST(root: TreeNode, `val`: Int): TreeNode = {
        var node = root
        while (node != null && node.value != `val`) {
            if (`val` < node.value) node = node.left
            else node = node.right
        }
        node
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
    pub fn search_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        let mut current = root;
        while let Some(node_rc) = current.clone() {
            let node_ref = node_rc.borrow();
            if node_ref.val == val {
                return Some(node_rc);
            } else if val < node_ref.val {
                current = node_ref.left.clone();
            } else {
                current = node_ref.right.clone();
            }
        }
        None
    }
}
```

## Racket

```racket
(define/contract (search-bst root val)
  (-> (or/c tree-node? #f) exact-integer? (or/c tree-node? #f))
  (let loop ((node root))
    (cond
      [(not node) #f]
      [(= (tree-node-val node) val) node]
      [(< val (tree-node-val node)) (loop (tree-node-left node))]
      [else (loop (tree-node-right node))])))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec search_bst(Root :: #tree_node{} | null, Val :: integer()) -> #tree_node{} | null.
search_bst(null, _Val) ->
    null;
search_bst(#tree_node{val = V}=Node, Val) when V =:= Val ->
    Node;
search_bst(#tree_node{val = V, left = L}, Val) when Val < V ->
    search_bst(L, Val);
search_bst(#tree_node{right = R}, _Val) ->
    search_bst(R, _Val).
```

## Elixir

```elixir
defmodule Solution do
  @spec search_bst(root :: TreeNode.t() | nil, val :: integer) :: TreeNode.t() | nil
  def search_bst(nil, _val), do: nil

  def search_bst(%TreeNode{val: v} = node, val) when v == val,
    do: node

  def search_bst(%TreeNode{val: v, left: left}, val) when val < v,
    do: search_bst(left, val)

  def search_bst(%TreeNode{right: right}, _val),
    do: search_bst(right, _val)
end
```
