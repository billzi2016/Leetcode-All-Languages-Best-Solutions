# 0657. Robot Return to Origin

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        for (char c : moves) {
            switch (c) {
                case 'U': ++y; break;
                case 'D': --y; break;
                case 'L': --x; break;
                case 'R': ++x; break;
            }
        }
        return x == 0 && y == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean judgeCircle(String moves) {
        int x = 0, y = 0;
        for (int i = 0; i < moves.length(); i++) {
            char c = moves.charAt(i);
            switch (c) {
                case 'U': y++; break;
                case 'D': y--; break;
                case 'L': x--; break;
                case 'R': x++; break;
            }
        }
        return x == 0 && y == 0;
    }
}
```

## Python

```python
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for c in moves:
            if c == 'L':
                x -= 1
            elif c == 'R':
                x += 1
            elif c == 'U':
                y += 1
            else:  # 'D'
                y -= 1
        return x == 0 and y == 0
```

## Python3

```python
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for c in moves:
            if c == 'U':
                y += 1
            elif c == 'D':
                y -= 1
            elif c == 'R':
                x += 1
            else:  # 'L'
                x -= 1
        return x == 0 and y == 0
```

## C

```c
#include <stdbool.h>

bool judgeCircle(char* moves) {
    int x = 0, y = 0;
    for (int i = 0; moves[i] != '\0'; ++i) {
        switch (moves[i]) {
            case 'U': y++; break;
            case 'D': y--; break;
            case 'L': x--; break;
            case 'R': x++; break;
        }
    }
    return x == 0 && y == 0;
}
```

## Csharp

```csharp
public class Solution
{
    public bool JudgeCircle(string moves)
    {
        int x = 0, y = 0;
        foreach (char c in moves)
        {
            switch (c)
            {
                case 'U': y++; break;
                case 'D': y--; break;
                case 'L': x--; break;
                case 'R': x++; break;
            }
        }
        return x == 0 && y == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    let x = 0, y = 0;
    for (let i = 0; i < moves.length; i++) {
        const c = moves.charCodeAt(i);
        // 'U' = 85, 'D' = 68, 'L' = 76, 'R' = 82
        if (c === 85) y++;          // U
        else if (c === 68) y--;     // D
        else if (c === 76) x--;     // L
        else if (c === 82) x++;     // R
    }
    return x === 0 && y === 0;
};
```

## Typescript

```typescript
function judgeCircle(moves: string): boolean {
    let x = 0, y = 0;
    for (const ch of moves) {
        if (ch === 'U') y++;
        else if (ch === 'D') y--;
        else if (ch === 'R') x++;
        else if (ch === 'L') x--;
    }
    return x === 0 && y === 0;
}
```

## Php

```php
class Solution {
    /**
     * @param String $moves
     * @return Boolean
     */
    function judgeCircle($moves) {
        $x = 0;
        $y = 0;
        $len = strlen($moves);
        for ($i = 0; $i < $len; $i++) {
            switch ($moves[$i]) {
                case 'U':
                    $y++;
                    break;
                case 'D':
                    $y--;
                    break;
                case 'L':
                    $x--;
                    break;
                case 'R':
                    $x++;
                    break;
            }
        }
        return $x === 0 && $y === 0;
    }
}
```

## Swift

```swift
class Solution {
    func judgeCircle(_ moves: String) -> Bool {
        var x = 0
        var y = 0
        for move in moves {
            switch move {
            case "U":
                y += 1
            case "D":
                y -= 1
            case "L":
                x -= 1
            case "R":
                x += 1
            default:
                break
            }
        }
        return x == 0 && y == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun judgeCircle(moves: String): Boolean {
        var x = 0
        var y = 0
        for (c in moves) {
            when (c) {
                'U' -> y++
                'D' -> y--
                'L' -> x--
                'R' -> x++
            }
        }
        return x == 0 && y == 0
    }
}
```

## Dart

```dart
class Solution {
  bool judgeCircle(String moves) {
    int x = 0, y = 0;
    for (int i = 0; i < moves.length; i++) {
      switch (moves[i]) {
        case 'U':
          y++;
          break;
        case 'D':
          y--;
          break;
        case 'L':
          x--;
          break;
        case 'R':
          x++;
          break;
      }
    }
    return x == 0 && y == 0;
  }
}
```

## Golang

```go
func judgeCircle(moves string) bool {
	var x, y int
	for _, c := range moves {
		switch c {
		case 'U':
			y++
		case 'D':
			y--
		case 'L':
			x--
		case 'R':
			x++
		}
	}
	return x == 0 && y == 0
}
```

## Ruby

```ruby
def judge_circle(moves)
  x = y = 0
  moves.each_char do |c|
    case c
    when 'U' then y += 1
    when 'D' then y -= 1
    when 'L' then x -= 1
    when 'R' then x += 1
    end
  end
  x == 0 && y == 0
end
```

## Scala

```scala
object Solution {
    def judgeCircle(moves: String): Boolean = {
        var x = 0
        var y = 0
        for (c <- moves) {
            c match {
                case 'U' => y += 1
                case 'D' => y -= 1
                case 'L' => x -= 1
                case 'R' => x += 1
                case _   => // ignore invalid characters
            }
        }
        x == 0 && y == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn judge_circle(moves: String) -> bool {
        let mut x = 0i32;
        let mut y = 0i32;
        for c in moves.chars() {
            match c {
                'U' => y += 1,
                'D' => y -= 1,
                'L' => x -= 1,
                'R' => x += 1,
                _ => {}
            }
        }
        x == 0 && y == 0
    }
}
```

## Racket

```racket
(define/contract (judge-circle moves)
  (-> string? boolean?)
  (let loop ((i 0) (x 0) (y 0))
    (if (= i (string-length moves))
        (and (= x 0) (= y 0))
        (let ((c (string-ref moves i)))
          (cond
            [(char=? c #\U) (loop (+ i 1) x (+ y 1))]
            [(char=? c #\D) (loop (+ i 1) x (- y 1))]
            [(char=? c #\L) (loop (+ i 1) (- x 1) y)]
            [(char=? c #\R) (loop (+ i 1) (+ x 1) y)]
            [else           (loop (+ i 1) x y)])))))
```

## Erlang

```erlang
-spec judge_circle(Moves :: unicode:unicode_binary()) -> boolean().
judge_circle(Moves) ->
    judge_circle(Moves, 0, 0).

judge_circle(<<>>, X, Y) ->
    X =:= 0 andalso Y =:= 0;
judge_circle(<<$U, Rest/binary>>, X, Y) ->
    judge_circle(Rest, X, Y - 1);
judge_circle(<<$D, Rest/binary>>, X, Y) ->
    judge_circle(Rest, X, Y + 1);
judge_circle(<<$L, Rest/binary>>, X, Y) ->
    judge_circle(Rest, X - 1, Y);
judge_circle(<<$R, Rest/binary>>, X, Y) ->
    judge_circle(Rest, X + 1, Y).
```

## Elixir

```elixir
defmodule Solution do
  @spec judge_circle(moves :: String.t) :: boolean
  def judge_circle(moves) do
    {x, y} =
      moves
      |> String.graphemes()
      |> Enum.reduce({0, 0}, fn
        "U", {x, y} -> {x, y + 1}
        "D", {x, y} -> {x, y - 1}
        "L", {x, y} -> {x - 1, y}
        "R", {x, y} -> {x + 1, y}
      end)

    x == 0 and y == 0
  end
end
```
