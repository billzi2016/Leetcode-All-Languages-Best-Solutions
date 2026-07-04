# 0653. Two Sum IV - Input is a BST

## Cpp

```cpp
/ **
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
    bool findTarget(TreeNode* root, int k) {
        std::unordered_set<int> seen;
        return dfs(root, k, seen);
    }
private:
    bool dfs(TreeNode* node, int k, std::unordered_set<int>& seen) {
        if (!node) return false;
        if (seen.count(k - node->val)) return true;
        seen.insert(node->val);
        return dfs(node->left, k, seen) || dfs(node->right, k, seen);
    }
};
```

## Java

```java
import java.util.HashSet;
import java.util.Set;

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
    public boolean findTarget(TreeNode root, int k) {
        Set<Integer> seen = new HashSet<>();
        return dfs(root, k, seen);
    }

    private boolean dfs(TreeNode node, int k, Set<Integer> seen) {
        if (node == null) {
            return false;
        }
        if (seen.contains(k - node.val)) {
            return true;
        }
        seen.add(node.val);
        return dfs(node.left, k, seen) || dfs(node.right, k, seen);
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
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            complement = k - node.val
            if complement in seen:
                return True
            seen.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            complement = k - node.val
            if complement in seen:
                return True
            seen.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
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
static bool dfs(struct TreeNode* root, int k, char *seen) {
    if (!root) return false;
    int complement = k - root->val;
    if (complement >= -10000 && complement <= 10000 && seen[complement + 10000])
        return true;
    seen[root->val + 10000] = 1;
    if (dfs(root->left, k, seen)) return true;
    if (dfs(root->right, k, seen)) return true;
    return false;
}

bool findTarget(struct TreeNode* root, int k) {
    char seen[20001] = {0}; // index offset by +10000
    return dfs(root, k, seen);
}
```

## Csharp

```csharp
using System.Collections.Generic;

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
    public bool FindTarget(TreeNode root, int k) {
        var seen = new HashSet<int>();
        return Dfs(root, k, seen);
    }

    private bool Dfs(TreeNode node, int k, HashSet<int> seen) {
        if (node == null) return false;
        if (seen.Contains(k - node.val)) return true;
        seen.Add(node.val);
        return Dfs(node.left, k, seen) || Dfs(node.right, k, seen);
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
 * @param {number} k
 * @return {boolean}
 */
var findTarget = function(root, k) {
    const seen = new Set();
    let found = false;
    
    const dfs = (node) => {
        if (!node || found) return;
        if (seen.has(k - node.val)) {
            found = true;
            return;
        }
        seen.add(node.val);
        dfs(node.left);
        dfs(node.right);
    };
    
    dfs(root);
    return found;
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

function findTarget(root: TreeNode | null, k: number): boolean {
    const seen = new Set<number>();
    let found = false;

    function dfs(node: TreeNode | null): void {
        if (!node || found) return;
        dfs(node.left);
        if (seen.has(k - node.val)) {
            found = true;
            return;
        }
        seen.add(node.val);
        dfs(node.right);
    }

    dfs(root);
    return found;
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
     * @param Integer $k
     * @return Boolean
     */
    function findTarget($root, $k) {
        $stack = [];
        $seen = [];

        $node = $root;
        while ($stack || $node) {
            while ($node) {
                $stack[] = $node;
                $node = $node->left;
            }
            $node = array_pop($stack);
            $complement = $k - $node->val;
            if (isset($seen[$complement])) {
                return true;
            }
            $seen[$node->val] = true;
            $node = $node->right;
        }

        return false;
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
    func findTarget(_ root: TreeNode?, _ k: Int) -> Bool {
        var seen = Set<Int>()
        return dfs(root, k, &seen)
    }
    
    private func dfs(_ node: TreeNode?, _ k: Int, _ seen: inout Set<Int>) -> Bool {
        guard let n = node else { return false }
        if seen.contains(k - n.val) {
            return true
        }
        seen.insert(n.val)
        return dfs(n.left, k, &seen) || dfs(n.right, k, &seen)
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
    fun findTarget(root: TreeNode?, k: Int): Boolean {
        val seen = HashSet<Int>()
        return dfs(root, k, seen)
    }

    private fun dfs(node: TreeNode?, k: Int, set: MutableSet<Int>): Boolean {
        if (node == null) return false
        if (set.contains(k - node.`val`)) return true
        set.add(node.`val`)
        return dfs(node.left, k, set) || dfs(node.right, k, set)
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
  bool findTarget(TreeNode? root, int k) {
    if (root == null) return false;
    final Set<int> seen = {};
    final List<TreeNode> stack = [root];
    while (stack.isNotEmpty) {
      final node = stack.removeLast();
      final complement = k - node.val;
      if (seen.contains(complement)) return true;
      seen.add(node.val);
      if (node.right != null) stack.add(node.right!);
      if (node.left != null) stack.add(node.left!);
    }
    return false;
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
func findTarget(root *TreeNode, k int) bool {
    seen := make(map[int]struct{})
    var dfs func(*TreeNode) bool
    dfs = func(node *TreeNode) bool {
        if node == nil {
            return false
        }
        if _, ok := seen[k-node.Val]; ok {
            return true
        }
        seen[node.Val] = struct{}{}
        return dfs(node.Left) || dfs(node.Right)
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

def find_target(root, k)
  return false if root.nil?
  seen = {}
  stack = [root]
  until stack.empty?
    node = stack.pop
    complement = k - node.val
    return true if seen[complement]
    seen[node.val] = true
    stack << node.left if node.left
    stack << node.right if node.right
  end
  false
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
    def findTarget(root: TreeNode, k: Int): Boolean = {
        import scala.collection.mutable.HashSet
        val seen = new HashSet[Int]()
        def dfs(node: TreeNode): Boolean = {
            if (node == null) false
            else if (seen.contains(k - node.value)) true
            else {
                seen.add(node.value)
                dfs(node.left) || dfs(node.right)
            }
        }
        dfs(root)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashSet;

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

impl Solution {
    pub fn find_target(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> bool {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, k: i32, set: &mut HashSet<i32>) -> bool {
            if let Some(rc) = node {
                let n = rc.borrow();
                let complement = k - n.val;
                if set.contains(&complement) {
                    return true;
                }
                set.insert(n.val);
                if dfs(&n.left, k, set) {
                    return true;
                }
                if dfs(&n.right, k, set) {
                    return true;
                }
            }
            false
        }

        let mut seen = HashSet::new();
        dfs(&root, k, &mut seen)
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

(define/contract (find-target root k)
  (-> (or/c tree-node? #f) exact-integer? boolean?)
  (let loop ((stack '()) (node root) (seen (make-hash)))
    (cond
      [(and (null? stack) (not node)) #f] ; traversal finished, not found
      [node
       ;; descend left
       (loop (cons node stack) (tree-node-left node) seen)]
      [else
       (define curr (car stack))
       (define rest (cdr stack))
       (define val (tree-node-val curr))
       (define complement (- k val))
       (if (hash-has-key? seen complement)
           #t
           (begin
             (hash-set! seen val #t)
             ;; now traverse right subtree
             (loop rest (tree-node-right curr) seen)))])))
```

## Erlang

```erlang
-module(solution).
-export([find_target/2]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec find_target(Root :: #tree_node{} | null, K :: integer()) -> boolean().
find_target(Root, K) ->
    go(Root, K, #{}).

go(null, _K, _Seen) ->
    false;
go(#tree_node{val = Val, left = Left, right = Right}, K, Seen) ->
    Complement = K - Val,
    case maps:is_key(Complement, Seen) of
        true -> true;
        false ->
            NewSeen = maps:put(Val, true, Seen),
            go(Left, K, NewSeen) orelse go(Right, K, NewSeen)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_target(root :: TreeNode.t | nil, k :: integer) :: boolean
  def find_target(root, k) do
    dfs(root, k, MapSet.new())
  end

  defp dfs(nil, _k, _set), do: false

  defp dfs(%TreeNode{val: v, left: l, right: r}, k, set) do
    complement = k - v

    if MapSet.member?(set, complement) do
      true
    else
      new_set = MapSet.put(set, v)

      case dfs(l, k, new_set) do
        true -> true
        false -> dfs(r, k, new_set)
      end
    end
  end
end
```
