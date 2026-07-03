# 0002. Add Two Numbers

## Cpp

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* cur = &dummy;
        int carry = 0;
        while (l1 || l2 || carry) {
            int sum = carry;
            if (l1) { sum += l1->val; l1 = l1->next; }
            if (l2) { sum += l2->val; l2 = l2->next; }
            carry = sum / 10;
            cur->next = new ListNode(sum % 10);
            cur = cur->next;
        }
        return dummy.next;
    }
};
```

## Java

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;
            int sum = x + y + carry;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        return dummy.next;
    }
}
```

## Python

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
```

## Python3

```python
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
```

## C

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy;
    struct ListNode *curr = &dummy;
    int carry = 0;
    
    while (l1 != NULL || l2 != NULL || carry != 0) {
        int x = (l1 != NULL) ? l1->val : 0;
        int y = (l2 != NULL) ? l2->val : 0;
        int sum = x + y + carry;
        carry = sum / 10;
        
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = sum % 10;
        node->next = NULL;
        curr->next = node;
        curr = node;
        
        if (l1 != NULL) l1 = l1->next;
        if (l2 != NULL) l2 = l2->next;
    }
    
    return dummy.next;
}
```

## Csharp

```csharp
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int x = l1?.val ?? 0;
            int y = l2?.val ?? 0;
            int sum = x + y + carry;
            carry = sum / 10;
            current.next = new ListNode(sum % 10);
            current = current.next;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        return dummyHead.next;
    }
}
```

## Javascript

```javascript
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode(0);
    let curr = dummy;
    let carry = 0;
    
    while (l1 !== null || l2 !== null || carry !== 0) {
        const x = l1 ? l1.val : 0;
        const y = l2 ? l2.val : 0;
        const sum = x + y + carry;
        carry = Math.floor(sum / 10);
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }
    
    return dummy.next;
};
```

## Typescript

```typescript
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummy = new ListNode(0);
    let current = dummy;
    let carry = 0;

    while (l1 !== null || l2 !== null || carry !== 0) {
        const x = l1?.val ?? 0;
        const y = l2?.val ?? 0;
        const sum = x + y + carry;
        carry = Math.floor(sum / 10);
        current.next = new ListNode(sum % 10);
        current = current.next;

        if (l1 !== null) l1 = l1.next;
        if (l2 !== null) l2 = l2.next;
    }

    return dummy.next;
}
```

## Php

```php
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        $dummy = new ListNode(0);
        $curr = $dummy;
        $carry = 0;

        while ($l1 !== null || $l2 !== null || $carry > 0) {
            $x = ($l1 !== null) ? $l1->val : 0;
            $y = ($l2 !== null) ? $l2->val : 0;

            $sum = $x + $y + $carry;
            $carry = intdiv($sum, 10);
            $curr->next = new ListNode($sum % 10);
            $curr = $curr->next;

            if ($l1 !== null) $l1 = $l1->next;
            if ($l2 !== null) $l2 = $l2->next;
        }

        return $dummy->next;
    }
}
```

## Swift

```swift
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var p = l1
        var q = l2
        let dummyHead = ListNode(0)
        var current: ListNode? = dummyHead
        var carry = 0
        
        while p != nil || q != nil || carry != 0 {
            let x = p?.val ?? 0
            let y = q?.val ?? 0
            let sum = x + y + carry
            carry = sum / 10
            current?.next = ListNode(sum % 10)
            current = current?.next
            
            if let nextP = p?.next {
                p = nextP
            } else {
                p = nil
            }
            
            if let nextQ = q?.next {
                q = nextQ
            } else {
                q = nil
            }
        }
        
        return dummyHead.next
    }
}
```

## Kotlin

```kotlin
/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var p = l1
        var q = l2
        val dummy = ListNode(0)
        var curr = dummy
        var carry = 0
        while (p != null || q != null || carry != 0) {
            val x = p?.`val` ?: 0
            val y = q?.`val` ?: 0
            val sum = x + y + carry
            carry = sum / 10
            curr.next = ListNode(sum % 10)
            curr = curr.next!!
            if (p != null) p = p.next
            if (q != null) q = q.next
        }
        return dummy.next
    }
}
```

## Dart

```dart
/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
class Solution {
  ListNode? addTwoNumbers(ListNode? l1, ListNode? l2) {
    final dummy = ListNode(0);
    var current = dummy;
    int carry = 0;

    while (l1 != null || l2 != null || carry != 0) {
      int x = l1?.val ?? 0;
      int y = l2?.val ?? 0;
      int sum = x + y + carry;
      carry = sum ~/ 10;
      current.next = ListNode(sum % 10);
      current = current.next!;

      if (l1 != null) l1 = l1!.next;
      if (l2 != null) l2 = l2!.next;
    }

    return dummy.next;
  }
}
```

## Golang

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummy := &ListNode{}
    curr := dummy
    carry := 0

    for l1 != nil || l2 != nil || carry != 0 {
        sum := carry
        if l1 != nil {
            sum += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            sum += l2.Val
            l2 = l2.Next
        }
        carry = sum / 10
        curr.Next = &ListNode{Val: sum % 10}
        curr = curr.Next
    }

    return dummy.Next
}
```

## Ruby

```ruby
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end

def add_two_numbers(l1, l2)
  dummy = ListNode.new(0)
  current = dummy
  carry = 0

  while l1 || l2 || carry != 0
    x = l1 ? l1.val : 0
    y = l2 ? l2.val : 0
    sum = x + y + carry
    carry = sum / 10
    current.next = ListNode.new(sum % 10)
    current = current.next
    l1 = l1&.next
    l2 = l2&.next
  end

  dummy.next
end
```

## Scala

```scala
/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
        var p = l1
        var q = l2
        val dummy = new ListNode(0)
        var curr = dummy
        var carry = 0

        while (p != null || q != null || carry != 0) {
            val x = if (p != null) p.x else 0
            val y = if (q != null) q.x else 0
            val sum = x + y + carry
            carry = sum / 10
            curr.next = new ListNode(sum % 10)
            curr = curr.next
            if (p != null) p = p.next
            if (q != null) q = q.next
        }

        dummy.next
    }
}
```

## Rust

```rust
impl Solution {
    pub fn add_two_numbers(
        mut l1: Option<Box<ListNode>>,
        mut l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy = ListNode::new(0);
        let mut cur = &mut dummy;
        let mut carry = 0;

        while l1.is_some() || l2.is_some() || carry != 0 {
            let mut sum = carry;
            if let Some(node) = l1 {
                sum += node.val;
                l1 = node.next;
            }
            if let Some(node) = l2 {
                sum += node.val;
                l2 = node.next;
            }

            carry = sum / 10;
            cur.next = Some(Box::new(ListNode::new((sum % 10) as i32)));
            cur = cur.next.as_mut().unwrap();
        }

        dummy.next
    }
}
```

## Racket

```racket
(define/contract (add-two-numbers l1 l2)
  (-> (or/c list-node? #f) (or/c list-node? #f) (or/c list-node? #f))
  (let ((dummy (make-list-node 0)))
    (let loop ((p1 l1) (p2 l2) (carry 0) (curr dummy))
      (if (and (not p1) (not p2) (= carry 0))
          (list-node-next dummy)
          (let* ((x (if p1 (list-node-val p1) 0))
                 (y (if p2 (list-node-val p2) 0))
                 (sum (+ x y carry))
                 (digit (remainder sum 10))
                 (new-carry (quotient sum 10))
                 (node (make-list-node digit)))
            (set-list-node-next! curr node)
            (loop (if p1 (list-node-next p1) #f)
                  (if p2 (list-node-next p2) #f)
                  new-carry
                  node))))))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec add_two_numbers(L1 :: #list_node{} | null,
                      L2 :: #list_node{} | null) -> #list_node{} | null.
add_two_numbers(L1, L2) ->
    add_two_numbers(L1, L2, 0).

%% Helper with carry
add_two_numbers(null, null, 0) ->
    null;
add_two_numbers(null, null, Carry) when Carry > 0 ->
    #list_node{val = Carry, next = null};
add_two_numbers(N1, N2, Carry) ->
    X = case N1 of
            null -> 0;
            #list_node{val = V} -> V
        end,
    Y = case N2 of
            null -> 0;
            #list_node{val = V} -> V
        end,
    Sum = X + Y + Carry,
    NewVal = Sum rem 10,
    NewCarry = Sum div 10,
    Next1 = case N1 of
                null -> null;
                #list_node{next = N} -> N
            end,
    Next2 = case N2 of
                null -> null;
                #list_node{next = N} -> N
            end,
    #list_node{
        val = NewVal,
        next = add_two_numbers(Next1, Next2, NewCarry)
    }.
```

## Elixir

```elixir
defmodule Solution do
  @spec add_two_numbers(l1 :: ListNode.t | nil, l2 :: ListNode.t | nil) :: ListNode.t | nil
  def add_two_numbers(l1, l2) do
    add(l1, l2, 0)
  end

  defp add(nil, nil, 0), do: nil

  defp add(l1, l2, carry) do
    x = if l1 != nil, do: l1.val, else: 0
    y = if l2 != nil, do: l2.val, else: 0
    sum = x + y + carry

    next_l1 = if l1 != nil, do: l1.next, else: nil
    next_l2 = if l2 != nil, do: l2.next, else: nil

    %ListNode{
      val: rem(sum, 10),
      next: add(next_l1, next_l2, div(sum, 10))
    }
  end
end
```
