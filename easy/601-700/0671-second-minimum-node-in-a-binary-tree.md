# 0671. Second Minimum Node In a Binary Tree

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
    int findSecondMinimumValue(TreeNode* root) {
        if (!root) return -1;
        long long ans = LLONG_MAX;
        int minVal = root->val;
        function<void(TreeNode*)> dfs = [&](TreeNode* node){
            if (!node) return;
            if (node->val > minVal && node->val < ans) {
                ans = node->val;
            } else if (node->val == minVal) {
                dfs(node->left);
                dfs(node->right);
            }
        };
        dfs(root);
        return ans == LLONG_MAX ? -1 : static_cast<int>(ans);
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
    private int minVal;
    
    public int findSecondMinimumValue(TreeNode root) {
        minVal = root.val;
        return dfs(root);
    }
    
    private int dfs(TreeNode node) {
        if (node == null) return -1;
        if (node.val > minVal) return node.val;
        int left = dfs(node.left);
        int right = dfs(node.right);
        if (left == -1) return right;
        if (right == -1) return left;
        return Math.min(left, right);
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
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return -1
        self.min_val = root.val

        def dfs(node):
            if not node:
                return float('inf')
            # If we find a value greater than min_val, it could be candidate
            if node.val > self.min_val:
                return node.val
            left_candidate = dfs(node.left)
            right_candidate = dfs(node.right)
            return min(left_candidate, right_candidate)

        ans = dfs(root)
        return -1 if ans == float('inf') else ans
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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        min_val = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            # If node value is greater than the minimum, it's a candidate.
            if node.val > min_val:
                return node.val
            # Otherwise, continue searching in both subtrees.
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1:
                return right
            if right == -1:
                return left
            return min(left, right)

        return dfs(root)
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
static int dfs(struct TreeNode* node, int minVal) {
    if (!node) return -1;
    if (node->val > minVal) return node->val;
    int left = dfs(node->left, minVal);
    int right = dfs(node->right, minVal);
    if (left != -1 && right != -1) return left < right ? left : right;
    if (left != -1) return left;
    return right;  // may be -1
}

int findSecondMinimumValue(struct TreeNode* root) {
    if (!root) return -1;
    return dfs(root, root->val);
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
    public int FindSecondMinimumValue(TreeNode root) {
        if (root == null) return -1;
        int minVal = root.val;
        int secondMin = int.MaxValue;

        void Dfs(TreeNode node) {
            if (node == null) return;
            if (node.val > minVal && node.val < secondMin) {
                secondMin = node.val;
            } else if (node.val == minVal) {
                Dfs(node.left);
                Dfs(node.right);
            }
        }

        Dfs(root);
        return secondMin == int.MaxValue ? -1 : secondMin;
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
var findSecondMinimumValue = function(root) {
    const minVal = root.val;
    let second = Infinity;
    
    const dfs = (node) => {
        if (!node) return;
        if (node.val > minVal && node.val < second) {
            second = node.val;
        } else if (node.val === minVal) {
            dfs(node.left);
            dfs(node.right);
        }
    };
    
    dfs(root);
    return second === Infinity ? -1 : second;
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

function findSecondMinimumValue(root: TreeNode | null): number {
    if (!root) return -1;
    const minVal = root.val;
    let secondMin = Infinity;

    function dfs(node: TreeNode | null): void {
        if (!node || node.val >= secondMin) return;
        if (node.val > minVal && node.val < secondMin) {
            secondMin = node.val;
            // No need to explore further from this node because its children are >= node.val
            return;
        }
        // node.val === minVal
        dfs(node.left);
        dfs(node.right);
    }

    dfs(root);
    return secondMin === Infinity ? -1 : secondMin;
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
     * @return integer
     */
    function findSecondMinimumValue($root) {
        if ($root === null) return -1;
        $second = $this->dfs($root, $root->val);
        return $second === PHP_INT_MAX ? -1 : $second;
    }

    private function dfs($node, $minVal) {
        if ($node === null) {
            return PHP_INT_MAX;
        }
        // If node value is greater than the minimum, it could be a candidate.
        if ($node->val > $minVal) {
            return $node->val;
        }
        // Otherwise continue searching in both subtrees.
        $left = $this->dfs($node->left, $minVal);
        $right = $this->dfs($node->right, $minVal);
        return min($left, $right);
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
    func findSecondMinimumValue(_ root: TreeNode?) -> Int {
        guard let root = root else { return -1 }
        let minVal = root.val
        var secondMin = Int.max
        
        func dfs(_ node: TreeNode?) {
            guard let node = node else { return }
            if node.val > minVal && node.val < secondMin {
                secondMin = node.val
            } else if node.val == minVal {
                dfs(node.left)
                dfs(node.right)
            }
        }
        
        dfs(root)
        return secondMin == Int.max ? -1 : secondMin
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
    fun findSecondMinimumValue(root: TreeNode?): Int {
        if (root == null) return -1
        val minVal = root.`val`
        var ans = Int.MAX_VALUE

        fun dfs(node: TreeNode?) {
            if (node == null) return
            when {
                node.`val` > minVal && node.`val` < ans -> ans = node.`val`
                node.`val` == minVal -> {
                    dfs(node.left)
                    dfs(node.right)
                }
            }
        }

        dfs(root)
        return if (ans == Int.MAX_VALUE) -1 else ans
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
  int findSecondMinimumValue(TreeNode? root) {
    if (root == null) return -1;
    final int minVal = root.val;
    int ans = -1;

    void dfs(TreeNode? node) {
      if (node == null) return;
      if (node.val > minVal) {
        if (ans == -1 || node.val < ans) ans = node.val;
      } else {
        // node.val == minVal
        dfs(node.left);
        dfs(node.right);
      }
    }

    dfs(root);
    return ans;
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
func findSecondMinimumValue(root *TreeNode) int {
	if root == nil {
		return -1
	}
	minVal := root.Val

	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return -1
		}
		if node.Val > minVal {
			return node.Val
		}
		left := dfs(node.Left)
		right := dfs(node.Right)

		if left == -1 {
			return right
		}
		if right == -1 {
			return left
		}
		if left < right {
			return left
		}
		return right
	}

	return dfs(root)
}
```

## Ruby

```ruby
def find_second_minimum_value(root)
  return -1 unless root
  min_val = root.val
  second = Float::INFINITY
  stack = [root]
  until stack.empty?
    node = stack.pop
    next if node.nil?
    if node.val > min_val && node.val < second
      second = node.val
    elsif node.val == min_val
      stack << node.left
      stack << node.right
    end
  end
  second == Float::INFINITY ? -1 : second.to_i
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
  def findSecondMinimumValue(root: TreeNode): Int = {
    val minVal = root.value
    var secondMin = Int.MaxValue

    def dfs(node: TreeNode): Unit = {
      if (node == null) return
      if (node.value > minVal && node.value < secondMin) {
        secondMin = node.value
        // children cannot improve the answer, prune
        return
      }
      if (node.value == minVal) {
        dfs(node.left)
        dfs(node.right)
      }
    }

    dfs(root)
    if (secondMin == Int.MaxValue) -1 else secondMin
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn find_second_minimum_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return -1;
        }
        let min_val = root.as_ref().unwrap().borrow().val;
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, min_val: i32) -> i32 {
            match node {
                Some(rc) => {
                    let val = rc.borrow().val;
                    if val > min_val {
                        return val;
                    }
                    let left = dfs(rc.borrow().left.clone(), min_val);
                    let right = dfs(rc.borrow().right.clone(), min_val);
                    if left == -1 { return right; }
                    if right == -1 { return left; }
                    std::cmp::min(left, right)
                },
                None => -1,
            }
        }
        dfs(root, min_val)
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

(define/contract (find-second-minimum-value root)
  (-> (or/c tree-node? #f) exact-integer?)
  (if (not (tree-node? root))
      -1
      (let* ([min-val (tree-node-val root)]
             [second
              (let recur ((node root))
                (cond [(not (tree-node? node)) #f]
                      [else
                       (let ([v (tree-node-val node)])
                         (if (> v min-val)
                             v
                             (let* ([l (recur (tree-node-left node))]
                                    [r (recur (tree-node-right node))])
                               (cond [(and l r) (min l r)]
                                     [l l]
                                     [r r]
                                     [else #f]))))))])])
        (if second second -1))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec find_second_minimum_value(Root :: #tree_node{} | null) -> integer().
find_second_minimum_value(Root) ->
    case Root of
        null -> -1;
        _ ->
            Min = Root#tree_node.val,
            case find(Root, Min) of
                undefined -> -1;
                V -> V
            end
    end.

%% helper functions
find(null, _Min) -> undefined;
find(Node, Min) ->
    Val = Node#tree_node.val,
    if Val > Min ->
            Val;
       true ->
            LeftRes = find(Node#tree_node.left, Min),
            RightRes = find(Node#tree_node.right, Min),
            combine(LeftRes, RightRes)
    end.

combine(undefined, undefined) -> undefined;
combine(V, undefined) when is_integer(V) -> V;
combine(undefined, V) when is_integer(V) -> V;
combine(A, B) ->
    if A < B -> A; true -> B end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_second_minimum_value(root :: TreeNode.t | nil) :: integer
  def find_second_minimum_value(nil), do: -1

  def find_second_minimum_value(%TreeNode{val: min_val} = root) do
    case second_min(root, min_val) do
      nil -> -1
      v -> v
    end
  end

  defp second_min(nil, _min), do: nil

  defp second_min(%TreeNode{val: val, left: l, right: r}, min) do
    cond do
      val > min ->
        val

      true ->
        left_res = second_min(l, min)
        right_res = second_min(r, min)

        case {left_res, right_res} do
          {nil, nil} -> nil
          {x, nil} -> x
          {nil, y} -> y
          {x, y} -> if x < y, do: x, else: y
        end
    end
  end
end
```
