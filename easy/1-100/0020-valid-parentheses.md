# 0020. Valid Parentheses

## Cpp

```cpp
class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        stack.reserve(s.size());
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push_back(c);
            } else {
                if (stack.empty()) return false;
                char top = stack.back();
                stack.pop_back();
                if ((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')) {
                    return false;
                }
            }
        }
        return stack.empty();
    }
};
```

## Java

```java
class Solution {
    public boolean isValid(String s) {
        java.util.Deque<Character> stack = new java.util.ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            switch (c) {
                case '(':
                case '[':
                case '{':
                    stack.push(c);
                    break;
                case ')':
                    if (stack.isEmpty() || stack.pop() != '(') return false;
                    break;
                case ']':
                    if (stack.isEmpty() || stack.pop() != '[') return false;
                    break;
                case '}':
                    if (stack.isEmpty() || stack.pop() != '{') return false;
                    break;
                default:
                    // invalid character, though per constraints this won't happen
                    return false;
            }
        }
        return stack.isEmpty();
    }
}
```

## Python

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in pair.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != pair.get(ch):
                    return False
                stack.pop()
        return not stack
```

## Python3

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isValid(char* s) {
    int n = strlen(s);
    char *stack = (char*)malloc(n);
    int top = -1;
    for (int i = 0; i < n; ++i) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') {
            stack[++top] = c;
        } else {
            if (top < 0) { free(stack); return false; }
            char open = stack[top--];
            if ((c == ')' && open != '(') ||
                (c == ']' && open != '[') ||
                (c == '}' && open != '{')) {
                free(stack);
                return false;
            }
        }
    }
    bool ok = (top == -1);
    free(stack);
    return ok;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsValid(string s) {
        var stack = new System.Collections.Generic.Stack<char>();
        foreach (char c in s) {
            if (c == '(' || c == '[' || c == '{') {
                stack.Push(c);
            } else {
                if (stack.Count == 0) return false;
                char top = stack.Pop();
                if ((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')) {
                    return false;
                }
            }
        }
        return stack.Count == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    const pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    for (const ch of s) {
        if (pairs[ch]) {
            if (stack.length === 0 || stack.pop() !== pairs[ch]) {
                return false;
            }
        } else {
            stack.push(ch);
        }
    }
    return stack.length === 0;
};
```

## Typescript

```typescript
function isValid(s: string): boolean {
    const stack: string[] = [];
    const pairs: { [key: string]: string } = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    for (const ch of s) {
        if (ch === '(' || ch === '{' || ch === '[') {
            stack.push(ch);
        } else {
            const top = stack.pop();
            if (top !== pairs[ch]) return false;
        }
    }
    return stack.length === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $stack = [];
        $pairs = [')' => '(', ']' => '[', '}' => '{'];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (isset($pairs[$ch])) { // closing bracket
                if (empty($stack) || array_pop($stack) !== $pairs[$ch]) {
                    return false;
                }
            } else { // opening bracket
                $stack[] = $ch;
            }
        }
        return empty($stack);
    }
}
```

## Swift

```swift
class Solution {
    func isValid(_ s: String) -> Bool {
        var stack = [Character]()
        for ch in s {
            switch ch {
            case "(", "[", "{":
                stack.append(ch)
            case ")":
                if stack.isEmpty || stack.removeLast() != "(" { return false }
            case "]":
                if stack.isEmpty || stack.removeLast() != "[" { return false }
            case "}":
                if stack.isEmpty || stack.removeLast() != "{" { return false }
            default:
                break
            }
        }
        return stack.isEmpty
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isValid(s: String): Boolean {
        val stack = ArrayDeque<Char>()
        for (ch in s) {
            when (ch) {
                '(', '[', '{' -> stack.addLast(ch)
                ')' -> if (stack.isEmpty() || stack.removeLast() != '(') return false
                ']' -> if (stack.isEmpty() || stack.removeLast() != '[') return false
                '}' -> if (stack.isEmpty() || stack.removeLast() != '{') return false
            }
        }
        return stack.isEmpty()
    }
}
```

## Dart

```dart
class Solution {
  bool isValid(String s) {
    List<String> stack = [];
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      if (ch == '(' || ch == '[' || ch == '{') {
        stack.add(ch);
      } else {
        if (stack.isEmpty) return false;
        String top = stack.removeLast();
        if ((ch == ')' && top != '(') ||
            (ch == ']' && top != '[') ||
            (ch == '}' && top != '{')) {
          return false;
        }
      }
    }
    return stack.isEmpty;
  }
}
```

## Golang

```go
func isValid(s string) bool {
	stack := []byte{}
	pairs := map[byte]byte{')': '(', '}': '{', ']': '['}
	for i := 0; i < len(s); i++ {
		c := s[i]
		if open, ok := pairs[c]; ok {
			if len(stack) == 0 || stack[len(stack)-1] != open {
				return false
			}
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, c)
		}
	}
	return len(stack) == 0
}
```

## Ruby

```ruby
def is_valid(s)
  stack = []
  s.each_char do |ch|
    case ch
    when '(', '[', '{'
      stack << ch
    when ')'
      return false if stack.pop != '('
    when ']'
      return false if stack.pop != '['
    when '}'
      return false if stack.pop != '{'
    end
  end
  stack.empty?
end
```

## Scala

```scala
object Solution {
  def isValid(s: String): Boolean = {
    val stack = new java.util.ArrayDeque[Char]()
    for (c <- s) {
      c match {
        case '(' | '[' | '{' => stack.push(c)
        case ')' =>
          if (stack.isEmpty || stack.pop() != '(') return false
        case ']' =>
          if (stack.isEmpty || stack.pop() != '[') return false
        case '}' =>
          if (stack.isEmpty || stack.pop() != '{') return false
        case _ => // ignore other characters
      }
    }
    stack.isEmpty
  }
}
```

## Rust

```rust
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        for ch in s.chars() {
            match ch {
                '(' | '[' | '{' => stack.push(ch),
                ')' => {
                    if stack.pop() != Some('(') {
                        return false;
                    }
                }
                ']' => {
                    if stack.pop() != Some('[') {
                        return false;
                    }
                }
                '}' => {
                    if stack.pop() != Some('{') {
                        return false;
                    }
                }
                _ => {}
            }
        }
        stack.is_empty()
    }
}
```

## Racket

```racket
(define/contract (is-valid s)
  (-> string? boolean?)
  (let loop ((chars (string->list s)) (stack '()))
    (cond
      [(null? chars) (null? stack)]
      [else
       (define c (car chars))
       (cond
         [(or (char=? c #\() (char=? c #\[) (char=? c #\{))
          (loop (cdr chars) (cons c stack))]
         [(or (char=? c #\)) (char=? c #\]) (char=? c #\}))
          (if (null? stack)
              #false
              (let ((top (car stack)))
                (cond
                  [(and (char=? c #\)) (char=? top #\())) (loop (cdr chars) (cdr stack))]
                  [(and (char=? c #\]) (char=? top #\[)) (loop (cdr chars) (cdr stack))]
                  [(and (char=? c #\}) (char=? top #\{)) (loop (cdr chars) (cdr stack))]
                  [else #false])))]
         [else (loop (cdr chars) stack)])))))
```

## Erlang

```erlang
-spec is_valid(unicode:unicode_binary()) -> boolean().
is_valid(S) ->
    Str = unicode:characters_to_list(S),
    is_valid(Str, []).

is_valid([], []) -> true;
is_valid([], _) -> false;
is_valid([C|Rest], Stack) ->
    case C of
        $( -> is_valid(Rest, [$( | Stack]);
        $[ -> is_valid(Rest, [$[ | Stack]);
        ${ -> is_valid(Rest, [${ | Stack]);
        $) -> pop($(, Rest, Stack);
        $] -> pop($[, Rest, Stack);
        $} -> pop(${, Rest, Stack)
    end.

pop(Open, Rest, [Open|Tail]) ->
    is_valid(Rest, Tail);
pop(_, _, _) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_valid(s :: String.t()) :: boolean()
  def is_valid(s) do
    case Enum.reduce_while(String.graphemes(s), [], fn ch, stack ->
           case ch do
             "(" -> {:cont, [ch | stack]}
             "[" -> {:cont, [ch | stack]}
             "{" -> {:cont, [ch | stack]}

             ")" ->
               case stack do
                 ["(" | rest] -> {:cont, rest}
                 _ -> {:halt, :invalid}
               end

             "]" ->
               case stack do
                 ["[" | rest] -> {:cont, rest}
                 _ -> {:halt, :invalid}
               end

             "}" ->
               case stack do
                 ["{" | rest] -> {:cont, rest}
                 _ -> {:halt, :invalid}
               end
           end
         end) do
      :invalid -> false
      remaining_stack -> remaining_stack == []
    end
  end
end
```
