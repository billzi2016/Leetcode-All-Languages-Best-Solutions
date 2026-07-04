# 0551. Student Attendance Record I

## Cpp

```cpp
class Solution {
public:
    bool checkRecord(string s) {
        int absent = 0;
        int lateStreak = 0;
        for (char c : s) {
            if (c == 'A') {
                ++absent;
                if (absent > 1) return false;
                lateStreak = 0;
            } else if (c == 'L') {
                ++lateStreak;
                if (lateStreak >= 3) return false;
            } else { // 'P'
                lateStreak = 0;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkRecord(String s) {
        int absentCount = 0;
        int lateStreak = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'A') {
                absentCount++;
                if (absentCount > 1) return false;
                lateStreak = 0;
            } else if (c == 'L') {
                lateStreak++;
                if (lateStreak >= 3) return false;
            } else { // 'P'
                lateStreak = 0;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = 0
        late_streak = 0
        for ch in s:
            if ch == 'A':
                absent += 1
                if absent > 1:
                    return False
                late_streak = 0
            elif ch == 'L':
                late_streak += 1
                if late_streak >= 3:
                    return False
            else:  # 'P'
                late_streak = 0
        return True
```

## Python3

```python
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late_streak = 0
        for ch in s:
            if ch == 'A':
                absent += 1
                if absent > 1:
                    return False
                late_streak = 0
            elif ch == 'L':
                late_streak += 1
                if late_streak >= 3:
                    return False
            else:  # 'P'
                late_streak = 0
        return True
```

## C

```c
#include <stdbool.h>

bool checkRecord(char* s) {
    int aCount = 0;
    int consecutiveL = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        char c = s[i];
        if (c == 'A') {
            if (++aCount > 1) return false;
            consecutiveL = 0;
        } else if (c == 'L') {
            if (++consecutiveL >= 3) return false;
        } else { // 'P'
            consecutiveL = 0;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckRecord(string s) {
        int absentCount = 0;
        int lateStreak = 0;
        foreach (char c in s) {
            if (c == 'A') {
                absentCount++;
                if (absentCount > 1) return false;
                lateStreak = 0;
            } else if (c == 'L') {
                lateStreak++;
                if (lateStreak >= 3) return false;
            } else { // 'P'
                lateStreak = 0;
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkRecord = function(s) {
    let absentCount = 0;
    let lateStreak = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c === 'A') {
            absentCount++;
            if (absentCount > 1) return false;
            lateStreak = 0;
        } else if (c === 'L') {
            lateStreak++;
            if (lateStreak >= 3) return false;
        } else { // 'P'
            lateStreak = 0;
        }
    }
    return true;
};
```

## Typescript

```typescript
function checkRecord(s: string): boolean {
    let absentCount = 0;
    let lateStreak = 0;
    for (let i = 0; i < s.length; i++) {
        const ch = s.charAt(i);
        if (ch === 'A') {
            absentCount++;
            if (absentCount > 1) return false;
            lateStreak = 0;
        } else if (ch === 'L') {
            lateStreak++;
            if (lateStreak >= 3) return false;
        } else { // 'P'
            lateStreak = 0;
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function checkRecord($s) {
        $absences = 0;
        $lateStreak = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c === 'A') {
                $absences++;
                if ($absences > 1) {
                    return false;
                }
                $lateStreak = 0;
            } elseif ($c === 'L') {
                $lateStreak++;
                if ($lateStreak >= 3) {
                    return false;
                }
            } else { // 'P'
                $lateStreak = 0;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkRecord(_ s: String) -> Bool {
        var absentCount = 0
        var consecutiveLates = 0
        
        for ch in s {
            if ch == "A" {
                absentCount += 1
                if absentCount > 1 { return false }
                consecutiveLates = 0
            } else if ch == "L" {
                consecutiveLates += 1
                if consecutiveLates >= 3 { return false }
            } else { // 'P'
                consecutiveLates = 0
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkRecord(s: String): Boolean {
        var absent = 0
        var consecutiveL = 0
        for (ch in s) {
            when (ch) {
                'A' -> {
                    absent++
                    if (absent > 1) return false
                    consecutiveL = 0
                }
                'L' -> {
                    consecutiveL++
                    if (consecutiveL >= 3) return false
                }
                else -> { // 'P'
                    consecutiveL = 0
                }
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkRecord(String s) {
    int absent = 0;
    int lateStreak = 0;
    for (int i = 0; i < s.length; i++) {
      String c = s[i];
      if (c == 'A') {
        absent++;
        if (absent > 1) return false;
        lateStreak = 0;
      } else if (c == 'L') {
        lateStreak++;
        if (lateStreak >= 3) return false;
      } else { // 'P'
        lateStreak = 0;
      }
    }
    return true;
  }
}
```

## Golang

```go
func checkRecord(s string) bool {
    aCount := 0
    lStreak := 0
    for i := 0; i < len(s); i++ {
        c := s[i]
        if c == 'A' {
            aCount++
            if aCount > 1 {
                return false
            }
        }
        if c == 'L' {
            lStreak++
            if lStreak >= 3 {
                return false
            }
        } else {
            lStreak = 0
        }
    }
    return true
}
```

## Ruby

```ruby
def check_record(s)
  a_count = 0
  l_consec = 0
  s.each_char do |c|
    if c == 'A'
      a_count += 1
      return false if a_count > 1
      l_consec = 0
    elsif c == 'L'
      l_consec += 1
      return false if l_consec >= 3
    else
      l_consec = 0
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def checkRecord(s: String): Boolean = {
        var aCount = 0
        var lStreak = 0
        for (c <- s) {
            c match {
                case 'A' =>
                    aCount += 1
                    if (aCount > 1) return false
                    lStreak = 0
                case 'L' =>
                    lStreak += 1
                    if (lStreak >= 3) return false
                case _ => // 'P'
                    lStreak = 0
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_record(s: String) -> bool {
        let mut a_cnt = 0;
        let mut l_consec = 0;
        for ch in s.bytes() {
            match ch {
                b'A' => {
                    a_cnt += 1;
                    if a_cnt > 1 {
                        return false;
                    }
                    l_consec = 0;
                }
                b'L' => {
                    l_consec += 1;
                    if l_consec >= 3 {
                        return false;
                    }
                }
                _ => {
                    l_consec = 0;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (check-record s)
  (-> string? boolean?)
  (let loop ((i 0) (absences 0) (late-streak 0))
    (cond
      [(>= i (string-length s)) #t]
      [else
       (define ch (string-ref s i))
       (cond
         [(char=? ch #\A)
          (if (= (+ absences 1) 2)
              #f
              (loop (+ i 1) (+ absences 1) 0))]
         [(char=? ch #\L)
          (let ((new-streak (+ late-streak 1)))
            (if (= new-streak 3)
                #f
                (loop (+ i 1) absences new-streak)))]
         [else ; #\P
          (loop (+ i 1) absences 0)])])))
```

## Erlang

```erlang
-module(solution).
-export([check_record/1]).

-spec check_record(S :: unicode:unicode_binary()) -> boolean().
check_record(S) ->
    check_record(S, 0, 0).

check_record(<<>>, Abs, _ConsL) ->
    Abs =< 1;
check_record(<<$A, Rest/binary>>, Abs, _ConsL) ->
    NewAbs = Abs + 1,
    if NewAbs > 1 -> false; true -> check_record(Rest, NewAbs, 0) end;
check_record(<<$L, Rest/binary>>, Abs, ConsL) ->
    NewCons = ConsL + 1,
    if NewCons >= 3 -> false; true -> check_record(Rest, Abs, NewCons) end;
check_record(<<$P, Rest/binary>>, Abs, _ConsL) ->
    check_record(Rest, Abs, 0);
check_record(_, _, _) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_record(s :: String.t) :: boolean
  def check_record(s) do
    {a_cnt, _, max_l} =
      String.graphemes(s)
      |> Enum.reduce({0, 0, 0}, fn ch, {a, cur, max} ->
        case ch do
          "A" -> {a + 1, 0, max}
          "L" ->
            new_cur = cur + 1
            {a, new_cur, if new_cur > max, do: new_cur, else: max}
          _ -> {a, 0, max}
        end
      end)

    a_cnt <= 1 and max_l < 3
  end
end
```
