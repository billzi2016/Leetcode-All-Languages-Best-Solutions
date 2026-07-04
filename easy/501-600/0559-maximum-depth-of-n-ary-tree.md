# 0559. Maximum Depth of N-ary Tree

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
    int maxDepth(Node* root) {
        if (!root) return 0;
        int depth = 0;
        for (Node* child : root->children) {
            depth = max(depth, maxDepth(child));
        }
        return depth + 1;
    }
};
```

## Java

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public int maxDepth(Node root) {
        if (root == null) return 0;
        int maxChildDepth = 0;
        if (root.children != null) {
            for (Node child : root.children) {
                int childDepth = maxDepth(child);
                if (childDepth > maxChildDepth) {
                    maxChildDepth = childDepth;
                }
            }
        }
        return maxChildDepth + 1;
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
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.children:
                for child in node.children:
                    if child:
                        stack.append((child, depth + 1))
        return max_depth
```

## Python3

```python
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        max_child_depth = 0
        for child in root.children:
            child_depth = self.maxDepth(child)
            if child_depth > max_child_depth:
                max_child_depth = child_depth
        return max_child_depth + 1
```

## C

```c
/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

int maxDepth(struct Node* root) {
    if (root == NULL) return 0;
    int max_child_depth = 0;
    for (int i = 0; i < root->numChildren; ++i) {
        int child_depth = maxDepth(root->children[i]);
        if (child_depth > max_child_depth) {
            max_child_depth = child_depth;
        }
    }
    return max_child_depth + 1;
}
```

## Csharp

```csharp
/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, IList<Node> _children) {
        val = _val;
        children = _children;
    }
}
*/

public class Solution {
    public int MaxDepth(Node root) {
        if (root == null) return 0;
        int maxChildDepth = 0;
        if (root.children != null) {
            foreach (var child in root.children) {
                int depth = MaxDepth(child);
                if (depth > maxChildDepth) maxChildDepth = depth;
            }
        }
        return maxChildDepth + 1;
    }
}
```

## Javascript

```javascript
/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val === undefined ? null : val;
 *    this.children = children === undefined ? null : children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number}
 */
var maxDepth = function(root) {
    if (!root) return 0;
    let depth = 0;
    const childs = root.children || [];
    for (let child of childs) {
        const d = maxDepth(child);
        if (d > depth) depth = d;
    }
    return depth + 1;
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

function maxDepth(root: _Node | null): number {
    if (!root) return 0;
    let deepest = 0;
    for (const child of root.children) {
        const d = maxDepth(child);
        if (d > deepest) deepest = d;
    }
    return deepest + 1;
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
     * @return integer
     */
    function maxDepth($root) {
        if ($root === null) {
            return 0;
        }
        $max = 0;
        foreach ($root->children as $child) {
            $depth = $this->maxDepth($child);
            if ($depth > $max) {
                $max = $depth;
            }
        }
        return $max + 1;
    }
}
```

## Swift

```swift
/ **
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
    func maxDepth(_ root: Node?) -> Int {
        guard let node = root else { return 0 }
        var deepest = 0
        for child in node.children {
            let depth = maxDepth(child)
            if depth > deepest {
                deepest = depth
            }
        }
        return deepest + 1
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
    fun maxDepth(root: Node?): Int {
        if (root == null) return 0
        var maxChild = 0
        for (child in root.children) {
            val depth = maxDepth(child)
            if (depth > maxChild) maxChild = depth
        }
        return maxChild + 1
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

func maxDepth(root *Node) int {
    if root == nil {
        return 0
    }
    max := 0
    for _, child := range root.Children {
        d := maxDepth(child)
        if d > max {
            max = d
        }
    }
    return max + 1
}
```

## Ruby

```ruby
def maxDepth(root)
  return 0 if root.nil?
  max_child_depth = 0
  root.children.each do |child|
    child_depth = maxDepth(child)
    max_child_depth = child_depth if child_depth > max_child_depth
  end
  1 + max_child_depth
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
  def maxDepth(root: Node): Int = {
    if (root == null) return 0
    var maxChildDepth = 0
    for (child <- root.children) {
      val d = maxDepth(child)
      if (d > maxChildDepth) maxChildDepth = d
    }
    maxChildDepth + 1
  }
}
```
