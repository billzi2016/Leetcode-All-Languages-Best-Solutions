# 0589. N-ary Tree Preorder Traversal

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
    vector<int> preorder(Node* root) {
        if (!root) return {};
        vector<int> result;
        stack<Node*> st;
        st.push(root);
        while (!st.empty()) {
            Node* node = st.top();
            st.pop();
            result.push_back(node->val);
            for (int i = (int)node->children.size() - 1; i >= 0; --i) {
                if (node->children[i])
                    st.push(node->children[i]);
            }
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> preorder(Node root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Deque<Node> stack = new ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            result.add(node.val);
            List<Node> children = node.children;
            if (children != null && !children.isEmpty()) {
                for (int i = children.size() - 1; i >= 0; i--) {
                    stack.push(children.get(i));
                }
            }
        }
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
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        output = []
        while stack:
            node = stack.pop()
            output.append(node.val)
            # Ensure children are processed left to right
            if node.children:
                for child in reversed(node.children):
                    if child:  # safety check
                        stack.append(child)
        return output
```

## Python3

```python
from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.children:
                # add children in reverse order to process leftmost first
                for child in reversed(node.children):
                    stack.append(child)
        return result
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

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* preorder(struct Node* root, int* returnSize) {
    *returnSize = 0;
    if (root == NULL) {
        return NULL;
    }

    int resCap = 1024;
    int *result = (int *)malloc(resCap * sizeof(int));

    int stackCap = 1024;
    struct Node **stack = (struct Node **)malloc(stackCap * sizeof(struct Node *));
    int top = 0;

    // push root
    if (top == stackCap) {
        stackCap <<= 1;
        stack = (struct Node **)realloc(stack, stackCap * sizeof(struct Node *));
    }
    stack[top++] = root;

    while (top > 0) {
        struct Node *node = stack[--top];

        // store node value
        if (*returnSize >= resCap) {
            resCap <<= 1;
            result = (int *)realloc(result, resCap * sizeof(int));
        }
        result[(*returnSize)++] = node->val;

        // push children in reverse order for correct preorder
        for (int i = node->numChildren - 1; i >= 0; --i) {
            if (top == stackCap) {
                stackCap <<= 1;
                stack = (struct Node **)realloc(stack, stackCap * sizeof(struct Node *));
            }
            stack[top++] = node->children[i];
        }
    }

    // shrink result to exact size
    result = (int *)realloc(result, (*returnSize) * sizeof(int));
    free(stack);
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> Preorder(Node root) {
        var result = new List<int>();
        if (root == null) return result;
        
        var stack = new Stack<Node>();
        stack.Push(root);
        
        while (stack.Count > 0) {
            var node = stack.Pop();
            result.Add(node.val);
            if (node.children != null && node.children.Count > 0) {
                for (int i = node.children.Count - 1; i >= 0; i--) {
                    stack.Push(node.children[i]);
                }
            }
        }
        
        return result;
    }
}
```

## Javascript

```javascript
/**
 * // Definition for a _Node.
 * function _Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number[]}
 */
var preorder = function(root) {
    const result = [];
    if (!root) return result;
    const stack = [root];
    while (stack.length) {
        const node = stack.pop();
        result.push(node.val);
        if (node.children && node.children.length) {
            for (let i = node.children.length - 1; i >= 0; i--) {
                const child = node.children[i];
                if (child) stack.push(child);
            }
        }
    }
    return result;
};
```

## Typescript

```typescript
/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     children: _Node[]
 * 
 *     constructor(val?: number, children?: _Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.children = (children===undefined ? [] : children)
 *     }
 * }
 */

function preorder(root: _Node | null): number[] {
    if (!root) return [];
    const result: number[] = [];
    const stack: _Node[] = [root];
    while (stack.length) {
        const node = stack.pop()!;
        result.push(node.val);
        for (let i = node.children.length - 1; i >= 0; i--) {
            stack.push(node.children[i]);
        }
    }
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
    function preorder($root) {
        $result = [];
        if ($root === null) {
            return $result;
        }
        $stack = [$root];
        while (!empty($stack)) {
            /** @var Node $node */
            $node = array_pop($stack);
            $result[] = $node->val;
            if (isset($node->children) && is_array($node->children) && !empty($node->children)) {
                for ($i = count($node->children) - 1; $i >= 0; $i--) {
                    $stack[] = $node->children[$i];
                }
            }
        }
        return $result;
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
    func preorder(_ root: Node?) -> [Int] {
        guard let root = root else { return [] }
        var result: [Int] = []
        var stack: [Node] = [root]
        
        while let node = stack.popLast() {
            result.append(node.val)
            if !node.children.isEmpty {
                for child in node.children.reversed() {
                    stack.append(child)
                }
            }
        }
        return result
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
    fun preorder(root: Node?): List<Int> {
        if (root == null) return emptyList()
        val result = ArrayList<Int>()
        val stack = mutableListOf<Node>()
        stack.add(root)
        while (stack.isNotEmpty()) {
            val node = stack.removeAt(stack.size - 1)
            result.add(node.`val`)
            for (i in node.children.size - 1 downTo 0) {
                node.children[i]?.let { stack.add(it) }
            }
        }
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

func preorder(root *Node) []int {
	if root == nil {
		return []int{}
	}
	var result []int
	stack := []*Node{root}
	for len(stack) > 0 {
		// Pop the last element
		n := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		result = append(result, n.Val)

		// Push children in reverse order to process leftmost child first
		for i := len(n.Children) - 1; i >= 0; i-- {
			if n.Children[i] != nil {
				stack = append(stack, n.Children[i])
			}
		}
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

def preorder(root)
  return [] if root.nil?
  stack = [root]
  result = []
  until stack.empty?
    node = stack.pop
    result << node.val
    node.children.reverse_each { |child| stack << child }
  end
  result
end
```

## Scala

```scala
import scala.collection.mutable.{Stack, ListBuffer}

/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var children: List[Node] = List()
 * }
 */
object Solution {
  def preorder(root: Node): List[Int] = {
    if (root == null) return Nil
    val stack = Stack[Node]()
    val result = ListBuffer[Int]()
    stack.push(root)
    while (stack.nonEmpty) {
      val node = stack.pop()
      result += node.value
      // push children in reverse order to process leftmost first
      for (child <- node.children.reverse) {
        if (child != null) stack.push(child)
      }
    }
    result.toList
  }
}
```
