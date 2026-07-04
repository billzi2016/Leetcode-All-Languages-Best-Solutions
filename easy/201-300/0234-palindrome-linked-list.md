# 0234. Palindrome Linked List

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
    bool isPalindrome(ListNode* head) {
        if (!head || !head->next) return true;
        
        // Find middle (end of first half)
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Reverse second half
        ListNode* secondHalfStart = reverseList(slow->next);
        ListNode* firstHalfIter = head;
        ListNode* secondHalfIter = secondHalfStart;
        bool palindrome = true;
        while (secondHalfIter) {
            if (firstHalfIter->val != secondHalfIter->val) {
                palindrome = false;
                break;
            }
            firstHalfIter = firstHalfIter->next;
            secondHalfIter = secondHalfIter->next;
        }
        
        // Restore the list (optional)
        slow->next = reverseList(secondHalfStart);
        return palindrome;
    }
    
private:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        while (head) {
            ListNode* nxt = head->next;
            head->next = prev;
            prev = head;
            head = nxt;
        }
        return prev;
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
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;
        
        // Find middle (end of first half)
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Reverse second half
        ListNode secondHalfStart = reverseList(slow.next);
        ListNode firstHalfIter = head;
        ListNode secondHalfIter = secondHalfStart;
        boolean result = true;
        while (result && secondHalfIter != null) {
            if (firstHalfIter.val != secondHalfIter.val) result = false;
            firstHalfIter = firstHalfIter.next;
            secondHalfIter = secondHalfIter.next;
        }
        
        // Restore the list (optional)
        slow.next = reverseList(secondHalfStart);
        return result;
    }
    
    private ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode nxt = head.next;
            head.next = prev;
            prev = head;
            head = nxt;
        }
        return prev;
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
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # Find end of first half
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second_half_start = self._reverseList(slow.next)

        # Compare both halves
        p1, p2 = head, second_half_start
        result = True
        while result and p2:
            if p1.val != p2.val:
                result = False
            p1 = p1.next
            p2 = p2.next

        # Restore the list (optional)
        slow.next = self._reverseList(second_half_start)

        return result

    def _reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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
    def isPalindrome(self, head: Optional['ListNode']) -> bool:
        if not head or not head.next:
            return True

        # Find middle (slow will point to start of second half)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Skip the middle node for odd length lists
        if fast:
            slow = slow.next

        # Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half_head = prev

        # Compare first and second halves
        p1, p2 = head, second_half_head
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
```

## C

```c
#include <stdbool.h>

bool isPalindrome(struct ListNode* head) {
    if (!head || !head->next) return true;

    struct ListNode *slow = head, *fast = head;
    struct ListNode *prev = NULL, *tmp = NULL;

    while (fast && fast->next) {
        fast = fast->next->next;

        tmp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = tmp;
    }

    if (fast) { // odd length, skip middle node
        slow = slow->next;
    }

    while (prev && slow) {
        if (prev->val != slow->val) return false;
        prev = prev->next;
        slow = slow->next;
    }
    return true;
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
    public bool IsPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        // Find middle of the list
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse second half
        ListNode prev = null;
        ListNode curr = slow;
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }

        // Compare first and reversed second half
        ListNode p1 = head, p2 = prev;
        while (p2 != null) {
            if (p1.val != p2.val) return false;
            p1 = p1.next;
            p2 = p2.next;
        }
        return true;
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
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    if (!head || !head.next) return true;
    
    // Find middle of the list
    let slow = head, fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // Reverse second half
    let prev = null;
    while (slow) {
        const nxt = slow.next;
        slow.next = prev;
        prev = slow;
        slow = nxt;
    }
    
    // Compare first half and reversed second half
    let p1 = head, p2 = prev;
    while (p2) {
        if (p1.val !== p2.val) return false;
        p1 = p1.next;
        p2 = p2.next;
    }
    return true;
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

function isPalindrome(head: ListNode | null): boolean {
    if (!head || !head.next) return true;

    // Find middle (slow will point to start of second half)
    let slow: ListNode | null = head;
    let fast: ListNode | null = head;
    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;
    }

    // For odd length, skip the middle node
    if (fast) { // fast not null means odd number of nodes
        slow = slow!.next;
    }

    // Reverse second half
    const reverse = (node: ListNode | null): ListNode | null => {
        let prev: ListNode | null = null;
        let curr: ListNode | null = node;
        while (curr) {
            const nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }
        return prev;
    };
    const secondHalfHead = reverse(slow);

    // Compare first half and reversed second half
    let p1: ListNode | null = head;
    let p2: ListNode | null = secondHalfHead;
    while (p2) {
        if (p1!.val !== p2.val) return false;
        p1 = p1!.next;
        p2 = p2.next;
    }

    // Optional: restore list (not required for problem)
    // reverse(secondHalfHead);

    return true;
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
     * @param ListNode $head
     * @return bool
     */
    function isPalindrome($head) {
        if ($head === null || $head->next === null) {
            return true;
        }

        // Find middle using fast and slow pointers
        $slow = $head;
        $fast = $head;
        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }

        // For odd length, skip the middle node
        if ($fast !== null) { // odd number of nodes
            $slow = $slow->next;
        }

        // Reverse second half starting from $slow
        $prev = null;
        $curr = $slow;
        while ($curr !== null) {
            $next = $curr->next;
            $curr->next = $prev;
            $prev = $curr;
            $curr = $next;
        }
        // $prev is head of reversed second half
        $secondHalf = $prev;
        $firstHalf = $head;

        // Compare both halves
        while ($secondHalf !== null) {
            if ($firstHalf->val !== $secondHalf->val) {
                return false;
            }
            $firstHalf = $firstHalf->next;
            $secondHalf = $secondHalf->next;
        }

        return true;
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
    func isPalindrome(_ head: ListNode?) -> Bool {
        guard let _ = head else { return true }
        let firstHalfEnd = endOfFirstHalf(head)
        let secondHalfStart = reverse(firstHalfEnd?.next)

        var p1 = head
        var p2 = secondHalfStart
        var result = true

        while let node2 = p2 {
            if p1!.val != node2.val {
                result = false
                break
            }
            p1 = p1?.next
            p2 = node2.next
        }

        // Restore the list (optional)
        firstHalfEnd?.next = reverse(secondHalfStart)

        return result
    }

    private func endOfFirstHalf(_ head: ListNode?) -> ListNode? {
        var fast = head
        var slow = head
        while fast?.next != nil && fast?.next?.next != nil {
            fast = fast?.next?.next
            slow = slow?.next
        }
        return slow
    }

    private func reverse(_ head: ListNode?) -> ListNode? {
        var prev: ListNode? = nil
        var curr = head
        while let node = curr {
            let nextTemp = node.next
            node.next = prev
            prev = node
            curr = nextTemp
        }
        return prev
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun isPalindrome(head: ListNode?): Boolean {
        if (head == null || head.next == null) return true

        // Find middle of the list
        var slow: ListNode? = head
        var fast: ListNode? = head
        while (fast?.next != null && fast.next?.next != null) {
            slow = slow!!.next
            fast = fast.next!!.next
        }

        // Reverse second half
        var secondHalfStart = reverse(slow!!.next)

        // Compare first and second halves
        var p1: ListNode? = head
        var p2: ListNode? = secondHalfStart
        while (p2 != null) {
            if (p1!!.`val` != p2.`val`) return false
            p1 = p1.next
            p2 = p2.next
        }

        // Optional: restore the list (not required for correctness)
        // slow!!.next = reverse(secondHalfStart)

        return true
    }

    private fun reverse(head: ListNode?): ListNode? {
        var prev: ListNode? = null
        var curr = head
        while (curr != null) {
            val nextTmp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTmp
        }
        return prev
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
  bool isPalindrome(ListNode? head) {
    if (head == null || head.next == null) return true;

    // Find middle while reversing first half
    ListNode? slow = head;
    ListNode? fast = head;
    ListNode? prev = null; // reversed part

    while (fast != null && fast.next != null) {
      fast = fast!.next!.next;

      // reverse the node pointed by slow
      ListNode? nextSlow = slow!.next;
      slow!.next = prev;
      prev = slow;
      slow = nextSlow;
    }

    // For odd length, skip the middle node
    if (fast != null) {
      slow = slow!.next;
    }

    // Compare reversed first half (prev) with second half (slow)
    ListNode? left = prev;
    ListNode? right = slow;
    bool isPal = true;

    while (left != null && right != null) {
      if (left.val != right.val) {
        isPal = false;
        break;
      }
      left = left.next;
      right = right.next;
    }

    // Optional: restore the list (not required for correctness)
    // Reverse the first half back to original order
    ListNode? cur = prev;
    ListNode? revPrev = null;
    while (cur != null) {
      ListNode? nxt = cur.next;
      cur.next = revPrev;
      revPrev = cur;
      cur = nxt;
    }
    // Reconnect restored part if needed (head remains unchanged)

    return isPal;
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
func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}
	// Find middle using fast and slow pointers
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	// Reverse second half starting from slow
	var prev *ListNode
	curr := slow
	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	// Compare first half and reversed second half
	p1, p2 := head, prev
	for p2 != nil {
		if p1.Val != p2.Val {
			return false
		}
		p1 = p1.Next
		p2 = p2.Next
	}
	return true
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
# @param {ListNode} head
# @return {Boolean}
def is_palindrome(head)
  return true if head.nil? || head.next.nil?

  slow = head
  fast = head
  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
  end

  # Skip the middle node for odd length lists
  slow = slow.next if fast

  # Reverse the second half of the list
  prev = nil
  curr = slow
  while curr
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
  end

  # Compare the first half and the reversed second half
  p1 = head
  p2 = prev
  while p2
    return false if p1.val != p2.val
    p1 = p1.next
    p2 = p2.next
  end

  true
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
    def isPalindrome(head: ListNode): Boolean = {
        if (head == null || head.next == null) return true

        var slow: ListNode = head
        var fast: ListNode = head
        var prev: ListNode = null

        // Reverse first half while finding middle
        while (fast != null && fast.next != null) {
            fast = fast.next.next
            val nextSlow = slow.next
            slow.next = prev
            prev = slow
            slow = nextSlow
        }

        // If odd length, skip the middle node
        if (fast != null) {
            slow = slow.next
        }

        var left: ListNode = prev
        var right: ListNode = slow

        while (left != null && right != null) {
            if (left.x != right.x) return false
            left = left.next
            right = right.next
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut vals = Vec::new();
        let mut cur = &head;
        while let Some(node) = cur.as_ref() {
            vals.push(node.val);
            cur = &node.next;
        }
        let n = vals.len();
        for i in 0..n / 2 {
            if vals[i] != vals[n - 1 - i] {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
#|
; Definition for singly-linked list:
; val : integer?
; next : (or/c list-node? #f)
(struct list-node
  (val next) #:mutable #:transparent)

; constructor
(define (make-list-node [val 0])
  (list-node val #f))
|#

(define/contract (is-palindrome head)
  (-> (or/c list-node? #f) boolean?)
  (if (not head)
      #t
      (let loop ((slow head) (fast head) (prev #f))
        (if (and fast (list-node-next fast))
            (let* ((next-slow (list-node-next slow))
                   (next-fast (list-node-next (list-node-next fast))))
              (set-list-node-next! slow prev)
              (loop next-slow next-fast slow))
            (let ((second (if fast
                             (list-node-next slow) ; odd length, skip middle
                             slow))               ; even length
                  (first prev))
              (let compare ((p first) (q second))
                (cond [(and (not p) (not q)) #t]
                      [(or (not p) (not q)) #f]
                      [(= (list-node-val p) (list-node-val q))
                       (compare (list-node-next p) (list-node-next q))]
                      [else #f]))))))))
```

## Erlang

```erlang
-module(solution).
-export([is_palindrome/1]).

-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec is_palindrome(Head :: #list_node{} | null) -> boolean().
is_palindrome(Head) ->
    Values = collect_vals(Head, []),
    Values == lists:reverse(Values).

collect_vals(null, Acc) -> lists:reverse(Acc);
collect_vals(#list_node{val=V,next=N}, Acc) ->
    collect_vals(N, [V|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_palindrome(head :: ListNode.t | nil) :: boolean
  def is_palindrome(head) do
    vals = collect_vals(head, [])
    vals == Enum.reverse(vals)
  end

  defp collect_vals(nil, acc), do: :lists.reverse(acc)

  defp collect_vals(%ListNode{val: v, next: nxt}, acc) do
    collect_vals(nxt, [v | acc])
  end
end
```
