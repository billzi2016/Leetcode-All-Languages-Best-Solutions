# 0383. Ransom Note

## Cpp

```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int cnt[26] = {0};
        for (char c : magazine) ++cnt[c - 'a'];
        for (char c : ransomNote) {
            if (--cnt[c - 'a'] < 0) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] count = new int[26];
        for (int i = 0; i < magazine.length(); i++) {
            count[magazine.charAt(i) - 'a']++;
        }
        for (int i = 0; i < ransomNote.length(); i++) {
            int idx = ransomNote.charAt(i) - 'a';
            if (--count[idx] < 0) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        counts = [0] * 26
        for ch in magazine:
            counts[ord(ch) - 97] += 1
        for ch in ransomNote:
            idx = ord(ch) - 97
            counts[idx] -= 1
            if counts[idx] < 0:
                return False
        return True
```

## Python3

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        cnt = [0] * 26
        for ch in magazine:
            cnt[ord(ch) - 97] += 1
        for ch in ransomNote:
            idx = ord(ch) - 97
            cnt[idx] -= 1
            if cnt[idx] < 0:
                return False
        return True
```

## C

```c
#include <stdbool.h>

bool canConstruct(char* ransomNote, char* magazine) {
    int cnt[26] = {0};
    for (char *p = magazine; *p; ++p) {
        cnt[*p - 'a']++;
    }
    for (char *p = ransomNote; *p; ++p) {
        if (--cnt[*p - 'a'] < 0) {
            return false;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        int[] count = new int[26];
        foreach (char c in magazine) {
            count[c - 'a']++;
        }
        foreach (char c in ransomNote) {
            if (--count[c - 'a'] < 0) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < magazine.length; ++i) {
        cnt[magazine.charCodeAt(i) - 97]++;
    }
    for (let i = 0; i < ransomNote.length; ++i) {
        const idx = ransomNote.charCodeAt(i) - 97;
        if (cnt[idx] === 0) return false;
        cnt[idx]--;
    }
    return true;
};
```

## Typescript

```typescript
function canConstruct(ransomNote: string, magazine: string): boolean {
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < magazine.length; i++) {
        cnt[magazine.charCodeAt(i) - 97]++;
    }
    for (let i = 0; i < ransomNote.length; i++) {
        const idx = ransomNote.charCodeAt(i) - 97;
        if (cnt[idx] === 0) return false;
        cnt[idx]--;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $ransomNote
     * @param String $magazine
     * @return Boolean
     */
    function canConstruct($ransomNote, $magazine) {
        $counts = array_fill(0, 26, 0);
        $lenM = strlen($magazine);
        for ($i = 0; $i < $lenM; $i++) {
            $idx = ord($magazine[$i]) - 97;
            $counts[$idx]++;
        }

        $lenR = strlen($ransomNote);
        for ($i = 0; $i < $lenR; $i++) {
            $idx = ord($ransomNote[$i]) - 97;
            if ($counts[$idx] === 0) {
                return false;
            }
            $counts[$idx]--;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canConstruct(_ ransomNote: String, _ magazine: String) -> Bool {
        var count = [Int](repeating: 0, count: 26)
        for byte in magazine.utf8 {
            count[Int(byte - 97)] += 1
        }
        for byte in ransomNote.utf8 {
            let idx = Int(byte - 97)
            count[idx] -= 1
            if count[idx] < 0 { return false }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canConstruct(ransomNote: String, magazine: String): Boolean {
        if (ransomNote.length > magazine.length) return false
        val counts = IntArray(26)
        for (c in magazine) {
            counts[c - 'a']++
        }
        for (c in ransomNote) {
            val idx = c - 'a'
            counts[idx]--
            if (counts[idx] < 0) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canConstruct(String ransomNote, String magazine) {
    List<int> count = List.filled(26, 0);
    for (int i = 0; i < magazine.length; i++) {
      count[magazine.codeUnitAt(i) - 97]++;
    }
    for (int i = 0; i < ransomNote.length; i++) {
      int idx = ransomNote.codeUnitAt(i) - 97;
      if (count[idx] == 0) return false;
      count[idx]--;
    }
    return true;
  }
}
```

## Golang

```go
func canConstruct(ransomNote string, magazine string) bool {
    var cnt [26]int
    for i := 0; i < len(magazine); i++ {
        cnt[magazine[i]-'a']++
    }
    for i := 0; i < len(ransomNote); i++ {
        idx := ransomNote[i] - 'a'
        cnt[idx]--
        if cnt[idx] < 0 {
            return false
        }
    }
    return true
}
```

## Ruby

```ruby
def can_construct(ransom_note, magazine)
  counts = Array.new(26, 0)
  magazine.each_byte { |b| counts[b - 97] += 1 }
  ransom_note.each_byte do |b|
    idx = b - 97
    counts[idx] -= 1
    return false if counts[idx] < 0
  end
  true
end
```

## Scala

```scala
object Solution {
    def canConstruct(ransomNote: String, magazine: String): Boolean = {
        val counts = new Array[Int](26)
        for (c <- magazine) {
            counts(c - 'a') += 1
        }
        for (c <- ransomNote) {
            val idx = c - 'a'
            counts(idx) -= 1
            if (counts(idx) < 0) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut count = [0i32; 26];
        for b in magazine.bytes() {
            count[(b - b'a') as usize] += 1;
        }
        for b in ransom_note.bytes() {
            let idx = (b - b'a') as usize;
            count[idx] -= 1;
            if count[idx] < 0 {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (can-construct ransomNote magazine)
  (-> string? string? boolean?)
  (let* ([freq (make-vector 26 0)]
         [maglen (string-length magazine)])
    ;; Count characters in magazine
    (for ([i (in-range maglen)])
      (let* ([ch (char->integer (string-ref magazine i))]
             [idx (- ch (char->integer #\a))])
        (vector-set! freq idx (+ 1 (vector-ref freq idx)))))
    ;; Verify ransomNote can be built
    (let loop ((i 0) (rlen (string-length ransomNote)))
      (if (= i rlen)
          #t
          (let* ([ch (char->integer (string-ref ransomNote i))]
                 [idx (- ch (char->integer #\a))])
            (define cur (vector-ref freq idx))
            (if (zero? cur)
                #f
                (begin
                  (vector-set! freq idx (- cur 1))
                  (loop (+ i 1) rlen))))))))
```

## Erlang

```erlang
-spec can_construct(RansomNote :: unicode:unicode_binary(), Magazine :: unicode:unicode_binary()) -> boolean().
can_construct(RansomNote, Magazine) ->
    Counts = count_chars(Magazine, erlang:make_tuple(26, 0)),
    check(RansomNote, Counts).

count_chars(<<>>, Counts) -> Counts;
count_chars(<<Char, Rest/binary>>, Counts) ->
    Index = Char - $a + 1,
    Old = element(Index, Counts),
    NewCounts = setelement(Index, Counts, Old + 1),
    count_chars(Rest, NewCounts).

check(<<>>, _Counts) -> true;
check(<<Char, Rest/binary>>, Counts) ->
    Index = Char - $a + 1,
    Old = element(Index, Counts),
    if
        Old =:= 0 -> false;
        true ->
            NewCounts = setelement(Index, Counts, Old - 1),
            check(Rest, NewCounts)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_construct(ransom_note :: String.t(), magazine :: String.t()) :: boolean()
  def can_construct(ransom_note, magazine) do
    counts =
      :binary.bin_to_list(magazine)
      |> Enum.reduce(:array.new(26, default: 0), fn char, arr ->
        idx = char - ?a
        val = :array.get(idx, arr)
        :array.set(idx, val + 1, arr)
      end)

    result =
      :binary.bin_to_list(ransom_note)
      |> Enum.reduce_while(counts, fn char, arr ->
        idx = char - ?a
        val = :array.get(idx, arr)

        if val > 0 do
          {:cont, :array.set(idx, val - 1, arr)}
        else
          {:halt, false}
        end
      end)

    result != false
  end
end
```
