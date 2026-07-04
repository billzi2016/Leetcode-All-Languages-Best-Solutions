# 0590. N-ary Tree Postorder Traversal

## Cpp

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> postorder(Node* root) {
        if (!root) return {};
        vector<int> result;
        stack<Node*> st;
        st.push(root);
        while (!st.empty()) {
            Node* node = st.top();
            st.pop();
            result.push_back(node->val);
            for (Node* child : node->children) {
                if (child) st.push(child);
            }
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> postorder(Node root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Deque<Node> stack = new ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            result.add(node.val);
            if (node.children != null) {
                for (Node child : node.children) {
                    if (child != null) {
                        stack.push(child);
                    }
                }
            }
        }
        Collections.reverse(result);
        return result;
    }
}
```

## Python

```python
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        order = []
        while stack:
            node = stack.pop()
            order.append(node.val)
            # push children to stack; they will be processed before the parent after reversal
            if node.children:
                stack.extend(node.children)
        return order[::-1]
```

## Python3

```python
# Definition for a Node.
class Node:
    def __init__(self, val: int = None, children=None):
        self.val = val
        self.children = children if children is not None else []

from typing import List

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        order = []
        while stack:
            node = stack.pop()
            order.append(node.val)
            if node.children:
                stack.extend(node.children)  # left to right
        return order[::-1]
```

## C

```c
#include <stdlib.h>

/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

static void dfs(struct Node* node, int **arr, int *size, int *cap) {
    if (!node) return;
    for (int i = 0; i < node->numChildren; ++i) {
        dfs(node->children[i], arr, size, cap);
    }
    if (*size >= *cap) {
        *cap *= 2;
        *arr = (int *)realloc(*arr, (*cap) * sizeof(int));
    }
    (*arr)[(*size)++] = node->val;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* postorder(struct Node* root, int* returnSize) {
    *returnSize = 0;
    if (!root) return NULL;

    int cap = 128;
    int *res = (int *)malloc(cap * sizeof(int));
    dfs(root, &res, returnSize, &cap);

    /* shrink to actual size */
    res = (int *)realloc(res, (*returnSize) * sizeof(int));
    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> Postorder(Node root) {
        var result = new List<int>();
        if (root == null) return result;
        
        var stack = new Stack<Node>();
        stack.Push(root);
        while (stack.Count > 0) {
            var node = stack.Pop();
            result.Add(node.val);
            if (node.children != null) {
                foreach (var child in node.children) {
                    if (child != null) stack.Push(child);
                }
            }
        }
        result.Reverse();
        return result;
    }
}
```

## Javascript

```javascript
/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number[]}
 */
var postorder = function(root) {
    if (!root) return [];
    const stack = [root];
    const result = [];
    while (stack.length) {
        const node = stack.pop();
        result.push(node.val);
        if (node.children && node.children.length) {
            for (const child of node.children) {
                if (child) stack.push(child);
            }
        }
    }
    return result.reverse();
};
```

## Typescript

```typescript
/**
 * Definition for node.
 * class _Node {
 *     val: number
 *     children: _Node[]
 *     constructor(val?: number) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.children = []
 *     }
 * }
 */

function postorder(root: _Node | null): number[] {
    if (!root) return [];
    const stack: _Node[] = [root];
    const result: number[] = [];

    while (stack.length) {
        const node = stack.pop()!;
        result.push(node.val);
        // push children left to right so they are processed right to left
        for (const child of node.children) {
            if (child) stack.push(child);
        }
    }

    result.reverse();
    return result;
}
```

## Php

```php
/**
 * Definition for a Node.
 * class Node {
 *     public $val = null;
 *     public $children = null;
 *     function __construct($val = 0) {
 *         $this->val = $val;
 *         $this->children = array();
 *     }
 * }
 */
class Solution {
    /**
     * @param Node $root
     * @return integer[]
     */
    function postorder($root) {
        if ($root === null) {
            return [];
        }
        $stack = [$root];
        $result = [];
        while (!empty($stack)) {
            $node = array_pop($stack);
            $result[] = $node->val;
            foreach ($node->children as $child) {
                if ($child !== null) {
                    $stack[] = $child;
                }
            }
        }
        return array_reverse($result);
    }
}
```

## Swift

```swift
/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var children: [Node]
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.children = []
 *     }
 * }
 */

class Solution {
    func postorder(_ root: Node?) -> [Int] {
        guard let root = root else { return [] }
        var stack: [Node] = [root]
        var result: [Int] = []
        
        while !stack.isEmpty {
            let node = stack.removeLast()
            result.append(node.val)
            // push children left to right so they are processed right to left
            for child in node.children {
                stack.append(child)
            }
        }
        return Array(result.reversed())
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var children: List<Node?> = listOf()
 * }
 */
class Solution {
    fun postorder(root: Node?): List<Int> {
        if (root == null) return emptyList()
        val stack = java.util.ArrayDeque<Node>()
        val result = mutableListOf<Int>()
        stack.push(root)
        while (!stack.isEmpty()) {
            val node = stack.pop()
            result.add(node.`val`)
            for (child in node.children) {
                if (child != null) {
                    stack.push(child)
                }
            }
        }
        result.reverse()
        return result
    }
}
```

## Golang

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func postorder(root *Node) []int {
	if root == nil {
		return []int{}
	}
	var result []int
	stack := []*Node{root}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, node.Val)
		for _, child := range node.Children {
			if child != nil {
				stack = append(stack, child)
			}
		}
	}
	// reverse to get postorder
	for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
		result[i], result[j] = result[j], result[i]
	}
	return result
}
```

## Ruby

```ruby
# Definition for a Node.
# class Node
#     attr_accessor :val, :children
#     def initialize(val)
#         @val = val
#         @children = []
#     end
# end

def postorder(root)
  return [] if root.nil?
  stack = [root]
  result = []

  until stack.empty?
    node = stack.pop
    result << node.val
    node.children.each { |child| stack << child }
  end

  result.reverse
end
```

## Scala

```scala
/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var children: List[Node] = List()
 * }
 */
object Solution {
  def postorder(root: Node): List[Int] = {
    if (root == null) return Nil

    val stack = scala.collection.mutable.Stack[Node]()
    val order = scala.collection.mutable.ArrayBuffer[Int]()

    stack.push(root)
    while (stack.nonEmpty) {
      val node = stack.pop()
      order += node.value
      // push children in original left-to-right order;
      // they will be processed right-to-left due to the stack.
      for (child <- node.children) {
        if (child != null) stack.push(child)
      }
    }

    order.reverse.toList
  }
}
```
