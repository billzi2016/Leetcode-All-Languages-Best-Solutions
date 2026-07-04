# 0257. Binary Tree Paths

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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        if (!root) return ans;
        dfs(root, "", ans);
        return ans;
    }
private:
    void dfs(TreeNode* node, const string& path, vector<string>& ans) {
        string cur = path.empty() ? to_string(node->val) : path + "->" + to_string(node->val);
        if (!node->left && !node->right) {
            ans.push_back(cur);
            return;
        }
        if (node->left) dfs(node->left, cur, ans);
        if (node->right) dfs(node->right, cur, ans);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        if (root == null) return result;
        dfs(root, "", result);
        return result;
    }
    
    private void dfs(TreeNode node, String path, List<String> result) {
        if (node == null) return;
        String currentPath = path.isEmpty() ? Integer.toString(node.val) : path + "->" + node.val;
        if (node.left == null && node.right == null) {
            result.add(currentPath);
            return;
        }
        if (node.left != null) dfs(node.left, currentPath, result);
        if (node.right != null) dfs(node.right, currentPath, result);
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
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        def dfs(node, path):
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            new_path = path + str(node.val) + "->"
            if node.left:
                dfs(node.left, new_path)
            if node.right:
                dfs(node.right, new_path)
        dfs(root, "")
        return res
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result: List[str] = []

        def dfs(node: TreeNode, path: str) -> None:
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return
            new_path = path + str(node.val) + "->"
            if node.left:
                dfs(node.left, new_path)
            if node.right:
                dfs(node.right, new_path)

        dfs(root, "")
        return result
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/* Helper DFS function */
static void dfs(struct TreeNode* node, char *path, int len,
                char **res, int *cnt) {
    if (!node) return;

    /* Append current node's value */
    int n = sprintf(path + len, "%d", node->val);
    len += n;

    if (!node->left && !node->right) {
        /* Leaf: store the path string */
        char *p = (char *)malloc(len + 1);
        memcpy(p, path, len + 1);
        res[(*cnt)++] = p;
        return;
    }

    /* Not a leaf: add arrow and continue */
    path[len] = '-';
    path[len + 1] = '>';
    int newlen = len + 2;

    if (node->left)
        dfs(node->left, path, newlen, res, cnt);
    if (node->right)
        dfs(node->right, path, newlen, res, cnt);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** binaryTreePaths(struct TreeNode* root, int* returnSize) {
    /* Maximum possible number of leaf paths is 100 (number of nodes) */
    char **result = (char **)malloc(sizeof(char *) * 100);
    int count = 0;

    if (!root) {
        *returnSize = 0;
        return result;
    }

    char buffer[600]; /* Sufficient for max path length */
    dfs(root, buffer, 0, result, &count);

    *returnSize = count;
    return result;
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
    public IList<string> BinaryTreePaths(TreeNode root) {
        var result = new List<string>();
        if (root == null) return result;
        Dfs(root, "", result);
        return result;
    }

    private void Dfs(TreeNode node, string path, List<string> result) {
        if (node == null) return;

        // Build current path
        var curPath = string.IsNullOrEmpty(path) ? node.val.ToString() : $"{path}->{node.val}";

        // If leaf, add to result
        if (node.left == null && node.right == null) {
            result.Add(curPath);
            return;
        }

        // Recurse on children
        if (node.left != null) Dfs(node.left, curPath, result);
        if (node.right != null) Dfs(node.right, curPath, result);
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
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    const result = [];
    if (!root) return result;
    
    const dfs = (node, path) => {
        if (!node) return;
        const newPath = path + node.val;
        if (!node.left && !node.right) {
            result.push(newPath);
        } else {
            const extended = newPath + '->';
            if (node.left) dfs(node.left, extended);
            if (node.right) dfs(node.right, extended);
        }
    };
    
    dfs(root, '');
    return result;
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

function binaryTreePaths(root: TreeNode | null): string[] {
    const paths: string[] = [];
    if (!root) return paths;

    const dfs = (node: TreeNode, path: string) => {
        const curPath = path ? `${path}->${node.val}` : `${node.val}`;
        if (!node.left && !node.right) {
            paths.push(curPath);
            return;
        }
        if (node.left) dfs(node.left, curPath);
        if (node.right) dfs(node.right, curPath);
    };

    dfs(root, '');
    return paths;
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
     * @return String[]
     */
    function binaryTreePaths($root) {
        $result = [];
        if ($root === null) {
            return $result;
        }
        $this->dfs($root, '', $result);
        return $result;
    }

    private function dfs($node, $path, &$res) {
        if ($node === null) {
            return;
        }
        $newPath = $path . $node->val;
        if ($node->left === null && $node->right === null) {
            $res[] = $newPath;
        } else {
            $newPath .= '->';
            if ($node->left !== null) {
                $this->dfs($node->left, $newPath, $res);
            }
            if ($node->right !== null) {
                $this->dfs($node->right, $newPath, $res);
            }
        }
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
    func binaryTreePaths(_ root: TreeNode?) -> [String] {
        var result = [String]()
        guard let start = root else { return result }
        
        func dfs(_ node: TreeNode, _ path: String) {
            let currentPath = path.isEmpty ? "\(node.val)" : "\(path)->\(node.val)"
            if node.left == nil && node.right == nil {
                result.append(currentPath)
                return
            }
            if let left = node.left { dfs(left, currentPath) }
            if let right = node.right { dfs(right, currentPath) }
        }
        
        dfs(start, "")
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
    fun binaryTreePaths(root: TreeNode?): List<String> {
        val result = mutableListOf<String>()
        if (root == null) return result

        fun dfs(node: TreeNode?, path: String) {
            if (node == null) return
            val newPath = if (path.isEmpty()) "${node.`val`}" else "$path->${node.`val`}"
            if (node.left == null && node.right == null) {
                result.add(newPath)
            } else {
                dfs(node.left, newPath)
                dfs(node.right, newPath)
            }
        }

        dfs(root, "")
        return result
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
  List<String> binaryTreePaths(TreeNode? root) {
    final List<String> result = [];

    void dfs(TreeNode? node, String path) {
      if (node == null) return;
      final String curPath = path.isEmpty ? '${node.val}' : '$path->${node.val}';
      if (node.left == null && node.right == null) {
        result.add(curPath);
        return;
      }
      dfs(node.left, curPath);
      dfs(node.right, curPath);
    }

    dfs(root, '');
    return result;
  }
}
```

## Golang

```go
package main

import "strconv"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func binaryTreePaths(root *TreeNode) []string {
	var res []string
	if root == nil {
		return res
	}
	var dfs func(node *TreeNode, path string)
	dfs = func(node *TreeNode, path string) {
		if node == nil {
			return
		}
		if path == "" {
			path = strconv.Itoa(node.Val)
		} else {
			path = path + "->" + strconv.Itoa(node.Val)
		}
		if node.Left == nil && node.Right == nil {
			res = append(res, path)
			return
		}
		if node.Left != nil {
			dfs(node.Left, path)
		}
		if node.Right != nil {
			dfs(node.Right, path)
		}
	}
	dfs(root, "")
	return res
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

def binary_tree_paths(root)
  return [] unless root
  result = []
  dfs = nil
  dfs = lambda do |node, path|
    if node.left.nil? && node.right.nil?
      result << (path + node.val.to_s)
    else
      new_path = path + node.val.to_s + '->'
      dfs.call(node.left, new_path) if node.left
      dfs.call(node.right, new_path) if node.right
    end
  end
  dfs.call(root, '')
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
    def binaryTreePaths(root: TreeNode): List[String] = {
        val result = scala.collection.mutable.ListBuffer[String]()
        def dfs(node: TreeNode, path: String): Unit = {
            if (node == null) return
            val cur = if (path.isEmpty) node.value.toString else s"$path->${node.value}"
            if (node.left == null && node.right == null) {
                result += cur
            } else {
                dfs(node.left, cur)
                dfs(node.right, cur)
            }
        }
        dfs(root, "")
        result.toList
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn binary_tree_paths(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, path: String, res: &mut Vec<String>) {
            if let Some(rc) = node {
                let n = rc.borrow();
                let cur = if path.is_empty() {
                    n.val.to_string()
                } else {
                    format!("{}->{}", path, n.val)
                };
                if n.left.is_none() && n.right.is_none() {
                    res.push(cur);
                } else {
                    dfs(n.left.clone(), cur.clone(), res);
                    dfs(n.right.clone(), cur, res);
                }
            }
        }

        let mut result = Vec::new();
        dfs(root, String::new(), &mut result);
        result
    }
}
```

## Racket

```racket
(define/contract (binary-tree-paths root)
  (-> (or/c tree-node? #f) (listof string?))
  (define (dfs node path)
    (if (not node)
        '()
        (let* ((new-path (if (string=? path "")
                             (number->string (tree-node-val node))
                             (string-append path "->" (number->string (tree-node-val node))))))
          (if (and (not (tree-node-left node)) (not (tree-node-right node)))
              (list new-path)
              (append (dfs (tree-node-left node) new-path)
                      (dfs (tree-node-right node) new-path))))))
  (dfs root ""))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec binary_tree_paths(Root :: #tree_node{} | null) -> [unicode:unicode_binary()].
binary_tree_paths(Root) ->
    case Root of
        null -> [];
        _ -> binary_tree_paths(Root, <<>>)
    end.

binary_tree_paths(Node, PathBin) when is_record(Node, tree_node) ->
    ValStr = integer_to_binary(Node#tree_node.val),
    NewPath = case PathBin of
                  <<>> -> ValStr;
                  _ -> <<PathBin/binary, "->", ValStr/binary>>
              end,
    Left = Node#tree_node.left,
    Right = Node#tree_node.right,
    case {Left, Right} of
        {null, null} ->
            [NewPath];
        _ ->
            lists:flatten([
                (if Left =/= null -> binary_tree_paths(Left, NewPath); true -> [] end),
                (if Right =/= null -> binary_tree_paths(Right, NewPath); true -> [] end)
            ])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec binary_tree_paths(root :: TreeNode.t() | nil) :: [String.t()]
  def binary_tree_paths(root) do
    traverse(root, "")
  end

  defp traverse(nil, _path), do: []

  defp traverse(%TreeNode{val: val, left: left, right: right}, path) do
    new_path =
      if path == "" do
        Integer.to_string(val)
      else
        path <> "->" <> Integer.to_string(val)
      end

    if left == nil and right == nil do
      [new_path]
    else
      traverse(left, new_path) ++ traverse(right, new_path)
    end
  end
end
```
