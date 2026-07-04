# 0682. Baseball Game

## Cpp

```cpp
class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> st;
        for (const string& op : operations) {
            if (op == "C") {
                if (!st.empty()) st.pop_back();
            } else if (op == "D") {
                int val = 2 * st.back();
                st.push_back(val);
            } else if (op == "+") {
                int sz = st.size();
                int val = st[sz - 1] + st[sz - 2];
                st.push_back(val);
            } else {
                st.push_back(stoi(op));
            }
        }
        int sum = 0;
        for (int v : st) sum += v;
        return sum;
    }
};
```

## Java

```java
class Solution {
    public int calPoints(String[] operations) {
        int n = operations.length;
        int[] stack = new int[n];
        int top = -1;
        for (String op : operations) {
            if ("C".equals(op)) {
                top--;
            } else if ("D".equals(op)) {
                stack[++top] = 2 * stack[top - 1];
            } else if ("+".equals(op)) {
                stack[++top] = stack[top - 1] + stack[top - 2];
            } else {
                stack[++top] = Integer.parseInt(op);
            }
        }
        int sum = 0;
        for (int i = 0; i <= top; i++) {
            sum += stack[i];
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for op in operations:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)
```

## Python3

```python
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: List[int] = []
        total = 0
        for op in operations:
            if op == "C":
                val = stack.pop()
                total -= val
            elif op == "D":
                val = 2 * stack[-1]
                stack.append(val)
                total += val
            elif op == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
                total += val
            else:
                val = int(op)
                stack.append(val)
                total += val
        return total
```

## C

```c
#include <stdlib.h>
#include <string.h>

int calPoints(char** operations, int operationsSize) {
    int *stack = (int *)malloc(sizeof(int) * operationsSize);
    int top = 0;
    for (int i = 0; i < operationsSize; ++i) {
        char *op = operations[i];
        if (op[0] == 'C' && op[1] == '\0') {
            if (top > 0) top--;
        } else if (op[0] == 'D' && op[1] == '\0') {
            stack[top] = 2 * stack[top - 1];
            ++top;
        } else if (op[0] == '+' && op[1] == '\0') {
            stack[top] = stack[top - 1] + stack[top - 2];
            ++top;
        } else {
            stack[top] = atoi(op);
            ++top;
        }
    }
    int sum = 0;
    for (int i = 0; i < top; ++i) sum += stack[i];
    free(stack);
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public int CalPoints(string[] operations) {
        var stack = new System.Collections.Generic.List<int>();
        foreach (var op in operations) {
            if (op == "C") {
                if (stack.Count > 0) stack.RemoveAt(stack.Count - 1);
            } else if (op == "D") {
                int last = stack[stack.Count - 1];
                stack.Add(last * 2);
            } else if (op == "+") {
                int sum = stack[stack.Count - 1] + stack[stack.Count - 2];
                stack.Add(sum);
            } else {
                stack.Add(int.Parse(op));
            }
        }
        int total = 0;
        foreach (int score in stack) total += score;
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
    const stack = [];
    for (const op of operations) {
        if (op === "C") {
            stack.pop();
        } else if (op === "D") {
            stack.push(stack[stack.length - 1] * 2);
        } else if (op === "+") {
            const n = stack.length;
            stack.push(stack[n - 1] + stack[n - 2]);
        } else {
            stack.push(parseInt(op, 10));
        }
    }
    return stack.reduce((sum, val) => sum + val, 0);
};
```

## Typescript

```typescript
function calPoints(operations: string[]): number {
    const stack: number[] = [];
    for (const op of operations) {
        if (op === "C") {
            stack.pop();
        } else if (op === "D") {
            const last = stack[stack.length - 1];
            stack.push(last * 2);
        } else if (op === "+") {
            const n = stack.length;
            stack.push(stack[n - 1] + stack[n - 2]);
        } else {
            stack.push(parseInt(op, 10));
        }
    }
    let total = 0;
    for (const score of stack) {
        total += score;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $operations
     * @return Integer
     */
    function calPoints($operations) {
        $stack = [];
        foreach ($operations as $op) {
            if ($op === "C") {
                array_pop($stack);
            } elseif ($op === "D") {
                $last = end($stack);
                $stack[] = $last * 2;
            } elseif ($op === "+") {
                $n = count($stack);
                $sum = $stack[$n - 1] + $stack[$n - 2];
                $stack[] = $sum;
            } else {
                $stack[] = (int)$op;
            }
        }
        return array_sum($stack);
    }
}
```

## Swift

```swift
class Solution {
    func calPoints(_ operations: [String]) -> Int {
        var stack = [Int]()
        for op in operations {
            if op == "C" {
                _ = stack.popLast()
            } else if op == "D" {
                if let last = stack.last {
                    stack.append(last * 2)
                }
            } else if op == "+" {
                let n = stack.count
                if n >= 2 {
                    stack.append(stack[n - 1] + stack[n - 2])
                }
            } else if let val = Int(op) {
                stack.append(val)
            }
        }
        return stack.reduce(0, +)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun calPoints(operations: Array<String>): Int {
        val n = operations.size
        val stack = IntArray(n)
        var top = 0
        var total = 0
        for (op in operations) {
            when (op) {
                "C" -> {
                    top--
                    total -= stack[top]
                }
                "D" -> {
                    val v = 2 * stack[top - 1]
                    stack[top++] = v
                    total += v
                }
                "+" -> {
                    val v = stack[top - 1] + stack[top - 2]
                    stack[top++] = v
                    total += v
                }
                else -> {
                    val v = op.toInt()
                    stack[top++] = v
                    total += v
                }
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int calPoints(List<String> operations) {
    List<int> stack = [];
    for (var op in operations) {
      if (op == 'C') {
        if (stack.isNotEmpty) stack.removeLast();
      } else if (op == 'D') {
        stack.add(stack.last * 2);
      } else if (op == '+') {
        int sum = stack[stack.length - 1] + stack[stack.length - 2];
        stack.add(sum);
      } else {
        stack.add(int.parse(op));
      }
    }
    int total = 0;
    for (var score in stack) {
      total += score;
    }
    return total;
  }
}
```

## Golang

```go
package main

import "strconv"

func calPoints(operations []string) int {
	stack := make([]int, 0, len(operations))
	for _, op := range operations {
		switch op {
		case "C":
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
		case "D":
			last := stack[len(stack)-1]
			stack = append(stack, last*2)
		case "+":
			n := len(stack)
			sum := stack[n-1] + stack[n-2]
			stack = append(stack, sum)
		default:
			val, _ := strconv.Atoi(op)
			stack = append(stack, val)
		}
	}
	total := 0
	for _, v := range stack {
		total += v
	}
	return total
}
```

## Ruby

```ruby
def cal_points(operations)
  stack = []
  operations.each do |op|
    case op
    when "C"
      stack.pop
    when "D"
      stack << (stack[-1] * 2)
    when "+"
      stack << (stack[-1] + stack[-2])
    else
      stack << op.to_i
    end
  end
  stack.sum
end
```

## Scala

```scala
object Solution {
    def calPoints(operations: Array[String]): Int = {
        import scala.collection.mutable.ArrayBuffer
        val stack = new ArrayBuffer[Int]()
        var total = 0
        for (op <- operations) {
            op match {
                case "C" =>
                    val removed = stack.remove(stack.length - 1)
                    total -= removed
                case "D" =>
                    val v = 2 * stack.last
                    stack.append(v)
                    total += v
                case "+" =>
                    val sz = stack.size
                    val v = stack(sz - 1) + stack(sz - 2)
                    stack.append(v)
                    total += v
                case numStr =>
                    val v = numStr.toInt
                    stack.append(v)
                    total += v
            }
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        for op in operations.iter() {
            match op.as_str() {
                "C" => { stack.pop(); },
                "D" => {
                    if let Some(&last) = stack.last() {
                        stack.push(last * 2);
                    }
                },
                "+" => {
                    let len = stack.len();
                    if len >= 2 {
                        let sum = stack[len - 1] + stack[len - 2];
                        stack.push(sum);
                    }
                },
                _ => {
                    let val: i32 = op.parse().unwrap();
                    stack.push(val);
                }
            }
        }
        stack.iter().sum()
    }
}
```

## Racket

```racket
(define/contract (cal-points operations)
  (-> (listof string?) exact-integer?)
  (let loop ((ops operations) (stack '()))
    (if (null? ops)
        (foldl + 0 stack)
        (let* ((op (car ops))
               (new-stack
                (cond
                  [(string=? op "C")
                   (cdr stack)]
                  [(string=? op "D")
                   (cons (* 2 (car stack)) stack)]
                  [(string=? op "+")
                   (let ((first (car stack))
                         (second (cadr stack)))
                     (cons (+ first second) stack))]
                  [else
                   (cons (string->number op) stack)])))
          (loop (cdr ops) new-stack)))))
```

## Erlang

```erlang
-spec cal_points(Operations :: [unicode:unicode_binary()]) -> integer().
cal_points(Operations) ->
    Stack = lists:foldl(
        fun(Op, Acc) ->
            case Op of
                <<"C">> ->
                    [_|Rest] = Acc,
                    Rest;
                <<"D">> ->
                    [Top|_] = Acc,
                    [(Top * 2) | Acc];
                <<"+">> ->
                    [Top1, Top2 | _] = Acc,
                    [(Top1 + Top2) | Acc];
                _ ->
                    Val = erlang:binary_to_integer(Op),
                    [Val | Acc]
            end
        end,
        [],
        Operations
    ),
    lists:sum(Stack).
```

## Elixir

```elixir
defmodule Solution do
  @spec cal_points(operations :: [String.t]) :: integer
  def cal_points(operations) do
    stack =
      Enum.reduce(operations, [], fn op, acc ->
        case op do
          "C" ->
            [_ | rest] = acc
            rest

          "D" ->
            [top | _] = acc
            [(top * 2) | acc]

          "+" ->
            [first, second | _] = acc
            [(first + second) | acc]

          _ ->
            {num, ""} = Integer.parse(op)
            [num | acc]
        end
      end)

    Enum.sum(stack)
  end
end
```
