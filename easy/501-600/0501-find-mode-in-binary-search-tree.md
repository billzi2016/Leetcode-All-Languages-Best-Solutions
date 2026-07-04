# 0501. Find Mode in Binary Search Tree

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
    vector<int> findMode(TreeNode* root) {
        curCount = 0;
        maxCount = 0;
        modes.clear();
        inorder(root);
        return modes;
    }
private:
    int curVal{};
    int curCount{};
    int maxCount{};
    vector<int> modes;

    void handleValue(int val) {
        if (curCount == 0 || val != curVal) {
            curVal = val;
            curCount = 1;
        } else {
            ++curCount;
        }
        if (curCount > maxCount) {
            maxCount = curCount;
            modes.clear();
            modes.push_back(val);
        } else if (curCount == maxCount) {
            modes.push_back(val);
        }
    }

    void inorder(TreeNode* node) {
        if (!node) return;
        inorder(node->left);
        handleValue(node->val);
        inorder(node->right);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private List<Integer> modes = new ArrayList<>();
    private int curVal;
    private int curCount = 0;
    private int maxCount = 0;

    public int[] findMode(TreeNode root) {
        inorder(root);
        int[] res = new int[modes.size()];
        for (int i = 0; i < modes.size(); i++) {
            res[i] = modes.get(i);
        }
        return res;
    }

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        handle(node.val);
        inorder(node.right);
    }

    private void handle(int val) {
        if (curCount == 0 || val != curVal) {
            curVal = val;
            curCount = 1;
        } else {
            curCount++;
        }
        if (curCount > maxCount) {
            maxCount = curCount;
            modes.clear();
            modes.add(val);
        } else if (curCount == maxCount) {
            modes.add(val);
        }
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
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.prev = None          # previous value in inorder traversal
        self.currCount = 0        # count of current value
        self.maxCount = 0         # maximum frequency seen so far
        self.modes = []           # list of mode values
        
        def handle(val):
            if self.prev is None or val != self.prev:
                self.currCount = 1
            else:
                self.currCount += 1
            
            if self.currCount > self.maxCount:
                self.maxCount = self.currCount
                self.modes = [val]
            elif self.currCount == self.maxCount:
                self.modes.append(val)
            
            self.prev = val
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            handle(node.val)
            inorder(node.right)
        
        inorder(root)
        return self.modes
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None          # previous value in inorder traversal
        self.currCount = 0        # count of the current value
        self.maxCount = 0         # maximum frequency seen so far
        self.modes = []           # list of mode values
        
        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            
            # process current node's value
            if self.prev is None or node.val != self.prev:
                self.currCount = 1
            else:
                self.currCount += 1
            
            if self.currCount > self.maxCount:
                self.maxCount = self.currCount
                self.modes = [node.val]
            elif self.currCount == self.maxCount:
                self.modes.append(node.val)
            
            self.prev = node.val
            inorder(node.right)
        
        inorder(root)
        return self.modes
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/* Global traversal state */
static int  prevVal;
static bool hasPrev;
static int  currCount;
static int  maxCount;

static int *modes = NULL;
static int   modesSize = 0;
static int   modesCap  = 0;

/* Ensure capacity for the result array */
static void ensure_capacity(void) {
    if (modesSize >= modesCap) {
        modesCap = modesCap ? modesCap * 2 : 4;
        modes = realloc(modes, modesCap * sizeof(int));
    }
}

/* Process a node value during inorder traversal */
static void handle(int val) {
    if (!hasPrev || val != prevVal) {
        currCount = 1;
        prevVal   = val;
        hasPrev   = true;
    } else {
        ++currCount;
    }

    if (currCount > maxCount) {
        maxCount   = currCount;
        modesSize  = 0;               /* reset result list */
        ensure_capacity();
        modes[modesSize++] = val;
    } else if (currCount == maxCount) {
        ensure_capacity();
        modes[modesSize++] = val;
    }
}

/* Recursive inorder traversal */
static void inorder(struct TreeNode *node) {
    if (!node) return;
    inorder(node->left);
    handle(node->val);
    inorder(node->right);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMode(struct TreeNode* root, int* returnSize) {
    /* Initialize traversal state */
    hasPrev   = false;
    currCount = 0;
    maxCount  = 0;
    modesSize = 0;
    modesCap  = 0;
    free(modes);
    modes = NULL;

    inorder(root);

    *returnSize = modesSize;
    /* Shrink to exact size if desired */
    if (modesSize != modesCap) {
        int *tmp = realloc(modes, modesSize * sizeof(int));
        if (tmp) modes = tmp;
    }
    return modes;
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
    private List<int> modes = new List<int>();
    private int? prevVal = null;
    private int curCount = 0;
    private int maxCount = 0;

    public int[] FindMode(TreeNode root) {
        Inorder(root);
        return modes.ToArray();
    }

    private void Inorder(TreeNode node) {
        if (node == null) return;
        Inorder(node.left);

        // Update count for current value
        if (prevVal.HasValue && node.val == prevVal.Value) {
            curCount++;
        } else {
            curCount = 1;
        }
        prevVal = node.val;

        // Update modes list based on counts
        if (curCount > maxCount) {
            maxCount = curCount;
            modes.Clear();
            modes.Add(node.val);
        } else if (curCount == maxCount) {
            modes.Add(node.val);
        }

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
 * @return {number[]}
 */
var findMode = function(root) {
    if (!root) return [];
    
    let maxCount = 0;
    let curCount = 0;
    let prevVal = null;
    const modes = [];
    
    const handle = (val) => {
        if (prevVal === null || val !== prevVal) {
            curCount = 1;
        } else {
            curCount++;
        }
        
        if (curCount > maxCount) {
            maxCount = curCount;
            modes.length = 0;
            modes.push(val);
        } else if (curCount === maxCount) {
            modes.push(val);
        }
        prevVal = val;
    };
    
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        handle(node.val);
        inorder(node.right);
    };
    
    inorder(root);
    return modes;
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

function findMode(root: TreeNode | null): number[] {
    let result: number[] = [];
    let maxCount = 0;
    let currCount = 0;
    let prevVal: number | null = null;

    const inorder = (node: TreeNode | null): void => {
        if (!node) return;
        inorder(node.left);

        if (prevVal !== null && node.val === prevVal) {
            currCount++;
        } else {
            currCount = 1;
        }

        if (currCount > maxCount) {
            maxCount = currCount;
            result = [node.val];
        } else if (currCount === maxCount) {
            result.push(node.val);
        }

        prevVal = node.val;

        inorder(node.right);
    };

    inorder(root);
    return result;
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
    private $prevVal = null;
    private $currCount = 0;
    private $maxCount = 0;
    private $modes = [];

    /**
     * @param TreeNode $root
     * @return Integer[]
     */
    function findMode($root) {
        $this->inorder($root);
        return $this->modes;
    }

    private function inorder($node) {
        if ($node === null) {
            return;
        }
        $this->inorder($node->left);

        $val = $node->val;
        if ($this->prevVal !== null && $val === $this->prevVal) {
            $this->currCount++;
        } else {
            $this->currCount = 1;
        }

        if ($this->currCount > $this->maxCount) {
            $this->maxCount = $this->currCount;
            $this->modes = [$val];
        } elseif ($this->currCount == $this->maxCount) {
            $this->modes[] = $val;
        }

        $this->prevVal = $val;

        $this->inorder($node->right);
    }
}
```

## Swift

```swift
class Solution {
    private var previous: Int?
    private var currentCount = 0
    private var maxCount = 0
    private var modes = [Int]()
    
    func findMode(_ root: TreeNode?) -> [Int] {
        inorder(root)
        return modes
    }
    
    private func handleValue(_ val: Int) {
        if let prev = previous, prev == val {
            currentCount += 1
        } else {
            currentCount = 1
        }
        previous = val
        
        if currentCount > maxCount {
            maxCount = currentCount
            modes = [val]
        } else if currentCount == maxCount {
            modes.append(val)
        }
    }
    
    private func inorder(_ node: TreeNode?) {
        guard let n = node else { return }
        inorder(n.left)
        handleValue(n.val)
        inorder(n.right)
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
    private var prev: Int? = null
    private var curCount = 0
    private var maxCount = 0
    private val modes = mutableListOf<Int>()

    fun findMode(root: TreeNode?): IntArray {
        inorder(root)
        return modes.toIntArray()
    }

    private fun handle(value: Int) {
        if (prev == null || prev != value) {
            curCount = 1
        } else {
            curCount++
        }
        prev = value

        when {
            curCount > maxCount -> {
                maxCount = curCount
                modes.clear()
                modes.add(value)
            }
            curCount == maxCount -> {
                modes.add(value)
            }
        }
    }

    private fun inorder(node: TreeNode?) {
        if (node == null) return
        inorder(node.left)
        handle(node.`val`)
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
  List<int> findMode(TreeNode? root) {
    int? prev;
    int curCount = 0;
    int maxCount = 0;
    List<int> modes = [];

    void handle(int val) {
      if (prev != null && val == prev) {
        curCount++;
      } else {
        curCount = 1;
        prev = val;
      }
      if (curCount > maxCount) {
        maxCount = curCount;
        modes = [val];
      } else if (curCount == maxCount) {
        modes.add(val);
      }
    }

    void inorder(TreeNode? node) {
      if (node == null) return;
      inorder(node.left);
      handle(node.val);
      inorder(node.right);
    }

    inorder(root);
    return modes;
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
func findMode(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var (
		prev      *TreeNode
		curCount  int
		maxCount  int
		modes     []int
	)
	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)

		if prev != nil && node.Val == prev.Val {
			curCount++
		} else {
			curCount = 1
		}
		if curCount > maxCount {
			maxCount = curCount
			modes = []int{node.Val}
		} else if curCount == maxCount {
			modes = append(modes, node.Val)
		}
		prev = node

		inorder(node.Right)
	}
	inorder(root)
	return modes
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

def find_mode(root)
  return [] if root.nil?

  prev = nil
  curr_count = 0
  max_count = 0
  result = []

  dfs = lambda do |node|
    return if node.nil?
    dfs.call(node.left)

    if prev == node.val
      curr_count += 1
    else
      curr_count = 1
      prev = node.val
    end

    if curr_count > max_count
      max_count = curr_count
      result = [node.val]
    elsif curr_count == max_count
      result << node.val
    end

    dfs.call(node.right)
  end

  dfs.call(root)
  result
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
  import scala.collection.mutable.ArrayBuffer

  private var prevVal: Option[Int] = None
  private var curCount: Int = 0
  private var maxCount: Int = 0
  private val modes = ArrayBuffer[Int]()

  def findMode(root: TreeNode): Array[Int] = {
    if (root == null) return Array.emptyIntArray
    inorder(root)
    modes.toArray
  }

  private def inorder(node: TreeNode): Unit = {
    if (node == null) return
    inorder(node.left)
    handle(node.value)
    inorder(node.right)
  }

  private def handle(v: Int): Unit = {
    prevVal match {
      case Some(p) if p == v => curCount += 1
      case _                 => curCount = 1
    }
    if (curCount > maxCount) {
      maxCount = curCount
      modes.clear()
      modes += v
    } else if (curCount == maxCount) {
      modes += v
    }
    prevVal = Some(v)
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

impl Solution {
    pub fn find_mode(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut freq: HashMap<i32, i32> = HashMap::new();

        fn inorder(node: &Option<Rc<RefCell<TreeNode>>>, map: &mut HashMap<i32, i32>) {
            if let Some(rc) = node {
                let n = rc.borrow();
                inorder(&n.left, map);
                *map.entry(n.val).or_insert(0) += 1;
                inorder(&n.right, map);
            }
        }

        inorder(&root, &mut freq);

        let mut max_cnt = 0;
        for &cnt in freq.values() {
            if cnt > max_cnt {
                max_cnt = cnt;
            }
        }

        let mut result = Vec::new();
        for (&val, &cnt) in freq.iter() {
            if cnt == max_cnt {
                result.push(val);
            }
        }
        result
    }
}
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
(struct tree-node (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))

(define/contract (find-mode root)
  (-> (or/c tree-node? #f) (listof exact-integer?))
  (if (not root)
      '()
      (let ((freq (make-hash)))
        (define (dfs node)
          (when node
            (dfs (tree-node-left node))
            (hash-set! freq (tree-node-val node)
                       (+ 1 (hash-ref freq (tree-node-val node) 0)))
            (dfs (tree-node-right node))))
        (dfs root)
        (let* ((max-freq (apply max (hash-values freq)))
               (modes (for/list ([(k v) (in-hash freq)]
                                 #:when (= v max-freq))
                        k)))
          modes))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec find_mode(Root :: #tree_node{} | null) -> [integer()].
find_mode(Root) ->
    case Root of
        null -> [];
        _ ->
            FreqMap = dfs(Root, #{ }),
            MaxFreq = max_freq(FreqMap),
            [K || {K,V} <- maps:to_list(FreqMap), V =:= MaxFreq]
    end.

dfs(null, Acc) -> Acc;
dfs(#tree_node{val=V,left=L,right=R}, Acc) ->
    NewAcc = maps:update_with(V,
                              fun(C) -> C + 1 end,
                              1,
                              Acc),
    Acc1 = dfs(L, NewAcc),
    dfs(R, Acc1).

max_freq(Map) ->
    lists:max(maps:values(Map)).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_mode(root :: TreeNode.t() | nil) :: [integer]
  def find_mode(nil), do: []

  def find_mode(root) do
    freq = dfs(root, %{})
    max_freq = freq |> Map.values() |> Enum.max(fn -> 0 end)

    freq
    |> Enum.filter(fn {_k, v} -> v == max_freq end)
    |> Enum.map(fn {k, _v} -> k end)
  end

  defp dfs(nil, acc), do: acc

  defp dfs(%TreeNode{val: val, left: l, right: r}, acc) do
    acc = Map.update(acc, val, 1, &(&1 + 1))
    acc = dfs(l, acc)
    dfs(r, acc)
  end
end
```
