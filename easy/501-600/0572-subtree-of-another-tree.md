# 0572. Subtree of Another Tree

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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!subRoot) return true;
        if (!root) return false;
        if (isSame(root, subRoot)) return true;
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
private:
    bool isSame(TreeNode* s, TreeNode* t) {
        if (!s && !t) return true;
        if (!s || !t) return false;
        if (s->val != t->val) return false;
        return isSame(s->left, t->left) && isSame(s->right, t->right);
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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) {
            return subRoot == null;
        }
        if (isSame(root, subRoot)) {
            return true;
        }
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean isSame(TreeNode s, TreeNode t) {
        if (s == null && t == null) {
            return true;
        }
        if (s == null || t == null) {
            return false;
        }
        if (s.val != t.val) {
            return false;
        }
        return isSame(s.left, t.left) && isSame(s.right, t.right);
    }
}
```

## Python

```python
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not subRoot:
            return True
        if not root:
            return False

        def same(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return same(s.left, t.left) and same(s.right, t.right)

        if same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def same(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and same(s.left, t.left) and same(s.right, t.right)

        if same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```

## C

```c
#include <stdbool.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

static bool isSame(struct TreeNode* s, struct TreeNode* t) {
    if (!s && !t) return true;
    if (!s || !t) return false;
    if (s->val != t->val) return false;
    return isSame(s->left, t->left) && isSame(s->right, t->right);
}

bool isSubtree(struct TreeNode* root, struct TreeNode* subRoot) {
    if (!subRoot) return true;
    if (!root) return false;
    if (isSame(root, subRoot)) return true;
    return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
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
    public bool IsSubtree(TreeNode root, TreeNode subRoot) {
        if (subRoot == null) return true;
        if (root == null) return false;
        if (IsSame(root, subRoot)) return true;
        return IsSubtree(root.left, subRoot) || IsSubtree(root.right, subRoot);
    }
    
    private bool IsSame(TreeNode s, TreeNode t) {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;
        if (s.val != t.val) return false;
        return IsSame(s.left, t.left) && IsSame(s.right, t.right);
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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
    const isSame = (s, t) => {
        if (!s && !t) return true;
        if (!s || !t) return false;
        if (s.val !== t.val) return false;
        return isSame(s.left, t.left) && isSame(s.right, t.right);
    };
    
    if (!root) return false;
    if (isSame(root, subRoot)) return true;
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
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

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    const isSame = (s: TreeNode | null, t: TreeNode | null): boolean => {
        if (!s && !t) return true;
        if (!s || !t) return false;
        if (s.val !== t.val) return false;
        return isSame(s.left, t.left) && isSame(s.right, t.right);
    };

    if (!subRoot) return true;
    if (!root) return false;

    if (isSame(root, subRoot)) return true;
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
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
     * @param TreeNode $subRoot
     * @return bool
     */
    function isSubtree($root, $subRoot) {
        if ($subRoot === null) {
            return true;
        }
        if ($root === null) {
            return false;
        }
        if ($this->isSame($root, $subRoot)) {
            return true;
        }
        return $this->isSubtree($root->left, $subRoot) || $this->isSubtree($root->right, $subRoot);
    }

    /**
     * @param TreeNode $s
     * @param TreeNode $t
     * @return bool
     */
    private function isSame($s, $t) {
        if ($s === null && $t === null) {
            return true;
        }
        if ($s === null || $t === null) {
            return false;
        }
        if ($s->val !== $t->val) {
            return false;
        }
        return $this->isSame($s->left, $t->left) && $this->isSame($s->right, $t->right);
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
    func isSubtree(_ root: TreeNode?, _ subRoot: TreeNode?) -> Bool {
        guard let sub = subRoot else { return true }
        guard let r = root else { return false }
        if isSame(r, sub) { return true }
        return isSubtree(r.left, sub) || isSubtree(r.right, sub)
    }
    
    private func isSame(_ s: TreeNode?, _ t: TreeNode?) -> Bool {
        if s == nil && t == nil { return true }
        if s == nil || t == nil { return false }
        if s!.val != t!.val { return false }
        return isSame(s!.left, t!.left) && isSame(s!.right, t!.right)
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
    fun isSubtree(root: TreeNode?, subRoot: TreeNode?): Boolean {
        if (subRoot == null) return true
        if (root == null) return false
        if (isSame(root, subRoot)) return true
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
    }

    private fun isSame(s: TreeNode?, t: TreeNode?): Boolean {
        if (s == null && t == null) return true
        if (s == null || t == null) return false
        if (s.`val` != t.`val`) return false
        return isSame(s.left, t.left) && isSame(s.right, t.right)
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
  bool isSubtree(TreeNode? root, TreeNode? subRoot) {
    if (subRoot == null) return true;
    if (root == null) return false;
    if (_isSame(root, subRoot)) return true;
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
  }

  bool _isSame(TreeNode? s, TreeNode? t) {
    if (s == null && t == null) return true;
    if (s == null || t == null) return false;
    if (s.val != t.val) return false;
    return _isSame(s.left, t.left) && _isSame(s.right, t.right);
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
func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if subRoot == nil {
		return true
	}
	if root == nil {
		return false
	}
	if sameTree(root, subRoot) {
		return true
	}
	return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}

func sameTree(s *TreeNode, t *TreeNode) bool {
	if s == nil && t == nil {
		return true
	}
	if s == nil || t == nil {
		return false
	}
	if s.Val != t.Val {
		return false
	}
	return sameTree(s.Left, t.Left) && sameTree(s.Right, t.Right)
}
```

## Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#   attr_accessor :val, :left, :right
#   def initialize(val = 0, left = nil, right = nil)
#     @val = val
#     @left = left
#     @right = right
#   end
# end

def is_subtree(root, sub_root)
  return true if sub_root.nil?
  return false if root.nil?

  if same_tree?(root, sub_root)
    true
  else
    is_subtree(root.left, sub_root) || is_subtree(root.right, sub_root)
  end
end

def same_tree?(s, t)
  return true if s.nil? && t.nil?
  return false if s.nil? || t.nil?
  s.val == t.val && same_tree?(s.left, t.left) && same_tree?(s.right, t.right)
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
  def isSubtree(root: TreeNode, subRoot: TreeNode): Boolean = {
    @annotation.tailrec
    def sameTree(s: TreeNode, t: TreeNode): Boolean = {
      if (s == null && t == null) true
      else if (s == null || t == null) false
      else s.value == t.value && sameTree(s.left, t.left) && sameTree(s.right, t.right)
    }

    def dfs(r: TreeNode): Boolean = {
      if (r == null) false
      else if (sameTree(r, subRoot)) true
      else dfs(r.left) || dfs(r.right)
    }

    if (subRoot == null) true
    else dfs(root)
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn is_subtree(root: Option<Rc<RefCell<TreeNode>>>, sub_root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        // An empty tree is always a subtree
        if sub_root.is_none() {
            return true;
        }
        match root {
            None => false,
            Some(node) => {
                if Self::same_tree(Some(node.clone()), sub_root.clone()) {
                    return true;
                }
                let left = node.borrow().left.clone();
                let right = node.borrow().right.clone();
                Self::is_subtree(left, sub_root.clone()) || Self::is_subtree(right, sub_root)
            }
        }
    }

    fn same_tree(s: Option<Rc<RefCell<TreeNode>>>, t: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match (s, t) {
            (None, None) => true,
            (Some(a), Some(b)) => {
                let a_ref = a.borrow();
                let b_ref = b.borrow();
                if a_ref.val != b_ref.val {
                    return false;
                }
                Self::same_tree(a_ref.left.clone(), b_ref.left.clone())
                    && Self::same_tree(a_ref.right.clone(), b_ref.right.clone())
            }
            _ => false,
        }
    }
}
```

## Racket

```racket
(define/contract (identical? s t)
  (-> (or/c tree-node? #f) (or/c tree-node? #f) boolean?)
  (cond [(and (not s) (not t)) #t]
        [(or (not s) (not t)) #f]
        [else (and (= (tree-node-val s) (tree-node-val t))
                   (identical? (tree-node-left s) (tree-node-left t))
                   (identical? (tree-node-right s) (tree-node-right t)))]))

(define/contract (is-subtree root subRoot)
  (-> (or/c tree-node? #f) (or/c tree-node? #f) boolean?)
  (cond [(not subRoot) #t]
        [(not root) #f]
        [else (or (identical? root subRoot)
                  (is-subtree (tree-node-left root) subRoot)
                  (is-subtree (tree-node-right root) subRoot))]))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec is_subtree(Root :: #tree_node{} | null, SubRoot :: #tree_node{} | null) -> boolean().
is_subtree(_Root, null) ->
    true;
is_subtree(null, _SubRoot) ->
    false;
is_subtree(Root, SubRoot) ->
    is_subtree_(Root, SubRoot).

-spec is_subtree_(#tree_node{} | null, #tree_node{}) -> boolean().
is_subtree_(null, _SubRoot) ->
    false;
is_subtree_(Node, SubRoot) ->
    case identical(Node, SubRoot) of
        true -> true;
        false ->
            is_subtree_(Node#tree_node.left, SubRoot) orelse
            is_subtree_(Node#tree_node.right, SubRoot)
    end.

-spec identical(#tree_node{} | null, #tree_node{} | null) -> boolean().
identical(null, null) ->
    true;
identical(_, null) ->
    false;
identical(null, _) ->
    false;
identical(N1, N2) ->
    N1#tree_node.val =:= N2#tree_node.val andalso
    identical(N1#tree_node.left, N2#tree_node.left) andalso
    identical(N1#tree_node.right, N2#tree_node.right).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_subtree(root :: TreeNode.t | nil, sub_root :: TreeNode.t | nil) :: boolean
  def is_subtree(_, nil), do: true
  def is_subtree(nil, _), do: false

  def is_subtree(root, sub_root) do
    same?(root, sub_root) or
      is_subtree(root.left, sub_root) or
      is_subtree(root.right, sub_root)
  end

  defp same?(nil, nil), do: true
  defp same?(nil, _), do: false
  defp same?(_, nil), do: false

  defp same?(%TreeNode{val: v1, left: l1, right: r1}, %TreeNode{val: v2, left: l2, right: r2}) do
    v1 == v2 and same?(l1, l2) and same?(r1, r2)
  end
end
```
