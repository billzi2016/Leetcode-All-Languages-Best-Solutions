# 0637. Average of Levels in Binary Tree

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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> ans;
        if (!root) return ans;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            long long sum = 0;
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                sum += node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            ans.push_back(static_cast<double>(sum) / sz);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> averages = new ArrayList<>();
        if (root == null) return averages;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            long sum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                sum += node.val;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            averages.add(sum / (double) size);
        }
        return averages;
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
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        from collections import deque
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level_sum = 0
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_sum / float(size))
        return res
```

## Python3

```python
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            level_sum = 0
            level_count = len(q)
            for _ in range(level_count):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_sum / level_count)
        return result
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

double* averageOfLevels(struct TreeNode* root, int* returnSize) {
    if (!root) {
        *returnSize = 0;
        return NULL;
    }
    
    // Maximum possible nodes as per constraints
    int maxNodes = 10005;
    struct TreeNode** queue = (struct TreeNode**)malloc(sizeof(struct TreeNode*) * maxNodes);
    int head = 0, tail = 0;
    queue[tail++] = root;
    
    int cap = 128;
    double* averages = (double*)malloc(sizeof(double) * cap);
    int levels = 0;
    
    while (head < tail) {
        int levelCount = tail - head;          // nodes at current level
        long long sum = 0;                     // use 64-bit to avoid overflow
        for (int i = 0; i < levelCount; ++i) {
            struct TreeNode* node = queue[head++];
            sum += node->val;
            if (node->left)  queue[tail++] = node->left;
            if (node->right) queue[tail++] = node->right;
        }
        double avg = (double)sum / levelCount;
        if (levels == cap) {
            cap <<= 1;
            averages = (double*)realloc(averages, sizeof(double) * cap);
        }
        averages[levels++] = avg;
    }
    
    free(queue);
    *returnSize = levels;
    return averages;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<double> AverageOfLevels(TreeNode root) {
        var averages = new List<double>();
        if (root == null) return averages;
        
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        
        while (queue.Count > 0) {
            int levelSize = queue.Count;
            long sum = 0;
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.Dequeue();
                sum += node.val;
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            averages.Add((double)sum / levelSize);
        }
        
        return averages;
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
var averageOfLevels = function(root) {
    const averages = [];
    if (!root) return averages;
    
    const queue = [root];
    let head = 0;
    
    while (head < queue.length) {
        const levelSize = queue.length - head;
        let sum = 0;
        for (let i = 0; i < levelSize; i++) {
            const node = queue[head++];
            sum += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        averages.push(sum / levelSize);
    }
    
    return averages;
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

function averageOfLevels(root: TreeNode | null): number[] {
    if (!root) return [];
    const averages: number[] = [];
    let queue: TreeNode[] = [root];
    while (queue.length > 0) {
        let sum = 0;
        const nextQueue: TreeNode[] = [];
        for (const node of queue) {
            sum += node.val;
            if (node.left) nextQueue.push(node.left);
            if (node.right) nextQueue.push(node.right);
        }
        averages.push(sum / queue.length);
        queue = nextQueue;
    }
    return averages;
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
     * @return Float[]
     */
    function averageOfLevels($root) {
        if ($root === null) {
            return [];
        }
        $queue = new SplQueue();
        $queue->enqueue($root);
        $result = [];

        while (!$queue->isEmpty()) {
            $levelSize = $queue->count();
            $sum = 0;
            for ($i = 0; $i < $levelSize; $i++) {
                /** @var TreeNode $node */
                $node = $queue->dequeue();
                $sum += $node->val;
                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }
            $result[] = $sum / $levelSize;
        }

        return $result;
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
    func averageOfLevels(_ root: TreeNode?) -> [Double] {
        guard let root = root else { return [] }
        var result = [Double]()
        var queue: [TreeNode] = [root]
        var index = 0
        
        while index < queue.count {
            let levelSize = queue.count - index
            var sum = 0.0
            for _ in 0..<levelSize {
                let node = queue[index]
                index += 1
                sum += Double(node.val)
                if let left = node.left { queue.append(left) }
                if let right = node.right { queue.append(right) }
            }
            result.append(sum / Double(levelSize))
        }
        
        return result
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
    fun averageOfLevels(root: TreeNode?): DoubleArray {
        if (root == null) return doubleArrayOf()
        val averages = mutableListOf<Double>()
        val queue: ArrayDeque<TreeNode> = ArrayDeque()
        queue.add(root)
        while (queue.isNotEmpty()) {
            val levelSize = queue.size
            var sum = 0L
            repeat(levelSize) {
                val node = queue.removeFirst()
                sum += node.`val`.toLong()
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            averages.add(sum.toDouble() / levelSize)
        }
        return DoubleArray(averages.size) { averages[it] }
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
  List<double> averageOfLevels(TreeNode? root) {
    if (root == null) return [];
    List<TreeNode> queue = [root];
    List<double> result = [];

    while (queue.isNotEmpty) {
      int levelSize = queue.length;
      double sum = 0.0;

      for (int i = 0; i < levelSize; i++) {
        TreeNode node = queue.removeAt(0);
        sum += node.val.toDouble();
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }

      result.add(sum / levelSize);
    }

    return result;
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
func averageOfLevels(root *TreeNode) []float64 {
	if root == nil {
		return []float64{}
	}
	queue := []*TreeNode{root}
	var result []float64

	for len(queue) > 0 {
		levelSize := len(queue)
		var sum int64
		for i := 0; i < levelSize; i++ {
			node := queue[0]
			queue = queue[1:]
			sum += int64(node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		avg := float64(sum) / float64(levelSize)
		result = append(result, avg)
	}

	return result
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

def average_of_levels(root)
  return [] if root.nil?
  result = []
  queue = [root]
  until queue.empty?
    level_size = queue.size
    sum = 0
    level_size.times do
      node = queue.shift
      sum += node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    result << sum.to_f / level_size
  end
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
    def averageOfLevels(root: TreeNode): Array[Double] = {
        if (root == null) return Array.empty[Double]
        import scala.collection.mutable.{Queue, ArrayBuffer}
        val queue = Queue[TreeNode]()
        val averages = ArrayBuffer[Double]()
        queue.enqueue(root)
        while (queue.nonEmpty) {
            val levelSize = queue.size
            var sum: Long = 0L
            for (_ <- 0 until levelSize) {
                val node = queue.dequeue()
                sum += node.value.toLong
                if (node.left != null) queue.enqueue(node.left)
                if (node.right != null) queue.enqueue(node.right)
            }
            averages.append(sum.toDouble / levelSize)
        }
        averages.toArray
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

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
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        let mut result = Vec::new();
        if root.is_none() {
            return result;
        }
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());

        while !queue.is_empty() {
            let level_size = queue.len();
            let mut sum: i64 = 0;
            for _ in 0..level_size {
                if let Some(node_rc) = queue.pop_front() {
                    let node_ref = node_rc.borrow();
                    sum += node_ref.val as i64;
                    if let Some(left) = &node_ref.left {
                        queue.push_back(Rc::clone(left));
                    }
                    if let Some(right) = &node_ref.right {
                        queue.push_back(Rc::clone(right));
                    }
                }
            }
            result.push(sum as f64 / level_size as f64);
        }

        result
    }
}
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
(struct tree-node
  (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))

(: average-of-levels ((or/c tree-node? #f) -> (listof flonum?)))
(define (average-of-levels root)
  (if (not root)
      '()
      (let loop ((queue (list root)) (acc '()))
        (if (null? queue)
            (reverse acc)
            (let* ((level-size (length queue))
                   (sum-and-children
                    (let recur ((nodes queue) (s 0.0) (c '()))
                      (if (null? nodes)
                          (values s c)
                          (let* ((node (car nodes))
                                 (val (tree-node-val node))
                                 (left (tree-node-left node))
                                 (right (tree-node-right node))
                                 (new-s (+ s (exact->inexact val)))
                                 (new-c (if left (cons left c) c))
                                 (new-c2 (if right (cons right new-c) new-c)))
                            (recur (cdr nodes) new-s new-c2))))))
              (let-values ([(sum children) sum-and-children])
                (loop (reverse children)
                      (cons (/ sum level-size) acc)))))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-module(solution).
-export([average_of_levels/1]).

-spec average_of_levels(Root :: #tree_node{} | null) -> [float()].
average_of_levels(null) ->
    [];
average_of_levels(Root) ->
    bfs([Root], []).

bfs([], Acc) ->
    lists:reverse(Acc);
bfs(CurrentLevel, Acc) ->
    {Sum, Count, NextLevel} = process_level(CurrentLevel, 0, 0, []),
    Avg = Sum / Count,
    bfs(NextLevel, [Avg | Acc]).

process_level([], Sum, Count, Next) ->
    {Sum, Count, lists:reverse(Next)};
process_level([Node | Rest], Sum, Count, Next) ->
    NewSum   = Sum + Node#tree_node.val,
    NewCount = Count + 1,
    Next1 = case Node#tree_node.left of
                null -> Next;
                L    -> [L | Next]
            end,
    Next2 = case Node#tree_node.right of
                null -> Next1;
                R    -> [R | Next1]
            end,
    process_level(Rest, NewSum, NewCount, Next2).
```

## Elixir

```elixir
defmodule Solution do
  @spec average_of_levels(root :: TreeNode.t | nil) :: [float]
  def average_of_levels(nil), do: []

  def average_of_levels(root) do
    bfs([root], [])
  end

  defp bfs([], acc), do: Enum.reverse(acc)

  defp bfs(nodes, acc) do
    {sum, cnt, next_rev} =
      Enum.reduce(nodes, {0, 0, []}, fn node, {s, c, nxt} ->
        s1 = s + node.val
        c1 = c + 1

        nxt1 =
          case node.left do
            nil -> nxt
            l -> [l | nxt]
          end

        nxt2 =
          case node.right do
            nil -> nxt1
            r -> [r | nxt1]
          end

        {s1, c1, nxt2}
      end)

    avg = sum / cnt
    bfs(Enum.reverse(next_rev), [avg | acc])
  end
end
```
