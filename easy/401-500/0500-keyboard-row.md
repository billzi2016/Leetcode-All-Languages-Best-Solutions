# 0500. Keyboard Row

## Cpp

```cpp
class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        // Map each letter to its keyboard row index
        int row[26];
        string rows[3] = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        for (int i = 0; i < 3; ++i) {
            for (char c : rows[i]) {
                row[c - 'a'] = i;
            }
        }

        vector<string> ans;
        for (const string& w : words) {
            if (w.empty()) continue;
            int firstRow = row[tolower(w[0]) - 'a'];
            bool ok = true;
            for (size_t j = 1; j < w.size(); ++j) {
                if (row[tolower(w[j]) - 'a'] != firstRow) {
                    ok = false;
                    break;
                }
            }
            if (ok) ans.push_back(w);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String[] findWords(String[] words) {
        int[] rows = new int[26];
        // Row 1
        for (char c : "qwertyuiop".toCharArray()) rows[c - 'a'] = 1;
        // Row 2
        for (char c : "asdfghjkl".toCharArray()) rows[c - 'a'] = 2;
        // Row 3
        for (char c : "zxcvbnm".toCharArray()) rows[c - 'a'] = 3;

        java.util.List<String> result = new java.util.ArrayList<>();
        outer:
        for (String word : words) {
            if (word.isEmpty()) continue;
            int firstRow = rows[Character.toLowerCase(word.charAt(0)) - 'a'];
            for (int i = 1; i < word.length(); i++) {
                char ch = Character.toLowerCase(word.charAt(i));
                if (rows[ch - 'a'] != firstRow) {
                    continue outer;
                }
            }
            result.add(word);
        }
        return result.toArray(new String[0]);
    }
}
```

## Python

```python
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        rows = [row1, row2, row3]

        result = []
        for word in words:
            lower = word.lower()
            # Determine which row the first character belongs to
            for r in rows:
                if lower[0] in r:
                    target_row = r
                    break
            else:
                continue  # shouldn't happen as all letters are alphabetic

            if all(ch in target_row for ch in lower):
                result.append(word)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        rows = [row1, row2, row3]
        result = []
        for word in words:
            lower = word.lower()
            # Determine which row the first character belongs to
            for r in rows:
                if lower[0] in r:
                    target_row = r
                    break
            else:
                continue  # shouldn't happen as all letters are alphabetic
            if all(ch in target_row for ch in lower):
                result.append(word)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findWords(char** words, int wordsSize, int* returnSize) {
    int row[26];
    memset(row, -1, sizeof(row));
    
    const char *r0 = "qwertyuiop";
    const char *r1 = "asdfghjkl";
    const char *r2 = "zxcvbnm";
    
    for (int i = 0; r0[i]; ++i) row[r0[i] - 'a'] = 0;
    for (int i = 0; r1[i]; ++i) row[r1[i] - 'a'] = 1;
    for (int i = 0; r2[i]; ++i) row[r2[i] - 'a'] = 2;
    
    char **result = (char **)malloc(wordsSize * sizeof(char *));
    int count = 0;
    
    for (int i = 0; i < wordsSize; ++i) {
        char *w = words[i];
        if (!w || !*w) continue;
        
        bool ok = true;
        int firstRow = -1;
        for (int j = 0; w[j]; ++j) {
            char c = tolower((unsigned char)w[j]);
            int r = row[c - 'a'];
            if (firstRow == -1) {
                firstRow = r;
            } else if (r != firstRow) {
                ok = false;
                break;
            }
        }
        if (ok) {
            result[count++] = w;
        }
    }
    
    *returnSize = count;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string[] FindWords(string[] words)
    {
        var rowMap = new Dictionary<char, int>();
        string row1 = "qwertyuiop";
        string row2 = "asdfghjkl";
        string row3 = "zxcvbnm";

        foreach (char c in row1) rowMap[Char.ToLower(c)] = 0;
        foreach (char c in row2) rowMap[Char.ToLower(c)] = 1;
        foreach (char c in row3) rowMap[Char.ToLower(c)] = 2;

        var result = new List<string>();

        foreach (var word in words)
        {
            if (string.IsNullOrEmpty(word)) continue;
            int firstRow = rowMap[Char.ToLower(word[0])];
            bool sameRow = true;
            for (int i = 1; i < word.Length; i++)
            {
                if (rowMap[Char.ToLower(word[i])] != firstRow)
                {
                    sameRow = false;
                    break;
                }
            }
            if (sameRow) result.Add(word);
        }

        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(words) {
    const rows = [
        new Set(['q','w','e','r','t','y','u','i','o','p']),
        new Set(['a','s','d','f','g','h','j','k','l']),
        new Set(['z','x','c','v','b','n','m'])
    ];
    
    const result = [];
    
    for (const word of words) {
        if (!word) continue;
        const lower = word.toLowerCase();
        let rowIndex = -1;
        // Determine which row the first character belongs to
        for (let i = 0; i < rows.length; i++) {
            if (rows[i].has(lower[0])) {
                rowIndex = i;
                break;
            }
        }
        if (rowIndex === -1) continue; // shouldn't happen
        
        let ok = true;
        const rowSet = rows[rowIndex];
        for (let j = 1; j < lower.length; j++) {
            if (!rowSet.has(lower[j])) {
                ok = false;
                break;
            }
        }
        if (ok) result.push(word);
    }
    
    return result;
};
```

## Typescript

```typescript
function findWords(words: string[]): string[] {
    const rows = [
        new Set(['q','w','e','r','t','y','u','i','o','p']),
        new Set(['a','s','d','f','g','h','j','k','l']),
        new Set(['z','x','c','v','b','n','m'])
    ];
    const result: string[] = [];
    for (const word of words) {
        const lower = word.toLowerCase();
        let rowIdx = -1;
        for (let i = 0; i < 3; i++) {
            if (rows[i].has(lower[0])) {
                rowIdx = i;
                break;
            }
        }
        if (rowIdx === -1) continue;
        let ok = true;
        for (let j = 1; j < lower.length; j++) {
            if (!rows[rowIdx].has(lower[j])) {
                ok = false;
                break;
            }
        }
        if (ok) result.push(word);
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @return String[]
     */
    function findWords($words) {
        $rowMap = [];
        foreach (str_split('qwertyuiop') as $c) { $rowMap[$c] = 1; }
        foreach (str_split('asdfghjkl') as $c) { $rowMap[$c] = 2; }
        foreach (str_split('zxcvbnm') as $c) { $rowMap[$c] = 3; }

        $result = [];
        foreach ($words as $word) {
            $len = strlen($word);
            if ($len == 0) continue;
            $firstRow = $rowMap[strtolower($word[0])] ?? null;
            $ok = true;
            for ($i = 1; $i < $len; $i++) {
                $c = strtolower($word[$i]);
                if (($rowMap[$c] ?? -1) !== $firstRow) {
                    $ok = false;
                    break;
                }
            }
            if ($ok) {
                $result[] = $word;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findWords(_ words: [String]) -> [String] {
        let rows: [Set<Character>] = [
            Set("qwertyuiop"),
            Set("asdfghjkl"),
            Set("zxcvbnm")
        ]
        var result = [String]()
        for word in words {
            let lower = word.lowercased()
            guard let firstChar = lower.first else { continue }
            var rowIdx: Int? = nil
            for (i, set) in rows.enumerated() {
                if set.contains(firstChar) {
                    rowIdx = i
                    break
                }
            }
            guard let idx = rowIdx else { continue }
            var ok = true
            for ch in lower {
                if !rows[idx].contains(ch) {
                    ok = false
                    break
                }
            }
            if ok {
                result.append(word)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findWords(words: Array<String>): Array<String> {
        val rowMap = IntArray(26)
        for (c in "qwertyuiop") rowMap[c - 'a'] = 0
        for (c in "asdfghjkl") rowMap[c - 'a'] = 1
        for (c in "zxcvbnm") rowMap[c - 'a'] = 2

        val result = mutableListOf<String>()
        for (word in words) {
            if (word.isEmpty()) continue
            val firstRow = rowMap[word[0].lowercaseChar() - 'a']
            var ok = true
            for (ch in word) {
                if (rowMap[ch.lowercaseChar() - 'a'] != firstRow) {
                    ok = false
                    break
                }
            }
            if (ok) result.add(word)
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<String> findWords(List<String> words) {
    const row1 = 'qwertyuiop';
    const row2 = 'asdfghjkl';
    const row3 = 'zxcvbnm';
    List<String> result = [];
    for (var word in words) {
      String lower = word.toLowerCase();
      int? currentRow;
      bool valid = true;
      for (int i = 0; i < lower.length; i++) {
        String ch = lower[i];
        int row;
        if (row1.contains(ch)) {
          row = 1;
        } else if (row2.contains(ch)) {
          row = 2;
        } else {
          row = 3;
        }
        if (currentRow == null) {
          currentRow = row;
        } else if (row != currentRow) {
          valid = false;
          break;
        }
      }
      if (valid) result.add(word);
    }
    return result;
  }
}
```

## Golang

```go
func findWords(words []string) []string {
    rows := []string{
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
    }
    charRow := make(map[byte]int, 26)
    for i, row := range rows {
        for j := 0; j < len(row); j++ {
            charRow[row[j]] = i
        }
    }

    var result []string
    for _, w := range words {
        if len(w) == 0 {
            continue
        }
        first := w[0]
        if first >= 'A' && first <= 'Z' {
            first = first - 'A' + 'a'
        }
        rowIdx, ok := charRow[first]
        if !ok {
            continue
        }
        valid := true
        for i := 1; i < len(w); i++ {
            c := w[i]
            if c >= 'A' && c <= 'Z' {
                c = c - 'A' + 'a'
            }
            if charRow[c] != rowIdx {
                valid = false
                break
            }
        }
        if valid {
            result = append(result, w)
        }
    }
    return result
}
```

## Ruby

```ruby
def find_words(words)
  rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
  char_to_row = {}
  rows.each_with_index do |row, idx|
    row.each_char do |ch|
      char_to_row[ch] = idx
      char_to_row[ch.upcase] = idx
    end
  end

  result = []
  words.each do |word|
    next if word.empty?
    target_row = char_to_row[word[0]]
    valid = true
    word.each_char do |ch|
      if char_to_row[ch] != target_row
        valid = false
        break
      end
    end
    result << word if valid
  end
  result
end
```

## Scala

```scala
object Solution {
    def findWords(words: Array[String]): Array[String] = {
        val row1 = Set('q','w','e','r','t','y','u','i','o','p')
        val row2 = Set('a','s','d','f','g','h','j','k','l')
        val row3 = Set('z','x','c','v','b','n','m')
        words.filter { w =>
            if (w.isEmpty) false
            else {
                val lower = w.toLowerCase
                val firstSet =
                    if (row1.contains(lower.charAt(0))) row1
                    else if (row2.contains(lower.charAt(0))) row2
                    else row3
                lower.forall(ch => firstSet.contains(ch))
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_words(words: Vec<String>) -> Vec<String> {
        let mut rows = [0u8; 26];
        for &c in b"qwertyuiop".iter() {
            rows[(c - b'a') as usize] = 0;
        }
        for &c in b"asdfghjkl".iter() {
            rows[(c - b'a') as usize] = 1;
        }
        for &c in b"zxcvbnm".iter() {
            rows[(c - b'a') as usize] = 2;
        }

        let mut result = Vec::new();
        'word_loop: for w in words.iter() {
            if w.is_empty() {
                continue;
            }
            let first_row = rows[(w.as_bytes()[0].to_ascii_lowercase() - b'a') as usize];
            for &b in w.as_bytes().iter() {
                let row = rows[(b.to_ascii_lowercase() - b'a') as usize];
                if row != first_row {
                    continue 'word_loop;
                }
            }
            result.push(w.clone());
        }
        result
    }
}
```

## Racket

```racket
(define/contract (find-words words)
  (-> (listof string?) (listof string?))
  (let* ([row1 "qwertyuiop"]
         [row2 "asdfghjkl"]
         [row3 "zxcvbnm"]
         [h (make-hash)])
    (for ([i (in-range (string-length row1))])
      (hash-set! h (string-ref row1 i) 1))
    (for ([i (in-range (string-length row2))])
      (hash-set! h (string-ref row2 i) 2))
    (for ([i (in-range (string-length row3))])
      (hash-set! h (string-ref row3 i) 3))
    (define (word-ok? w)
      (let* ([lw (string-downcase w)]
             [len (string-length lw)])
        (if (= len 0)
            #t
            (let ([first-row (hash-ref h (string-ref lw 0))])
              (let loop ([i 1])
                (or (= i len)
                    (and (= (hash-ref h (string-ref lw i)) first-row)
                         (loop (+ i 1)))))))))
    (filter word-ok? words)))
```

## Erlang

```erlang
-module(solution).
-export([find_words/1]).

-spec find_words(Words :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
find_words(Words) ->
    lists:filter(fun word_one_row/1, Words).

word_one_row(Word) ->
    Lower = string:lowercase(Word),
    Chars = unicode:characters_to_list(Lower),
    case Chars of
        [] -> false;
        [First|Rest] ->
            Row = row_of(First),
            Row =/= 0 andalso lists:all(fun(C) -> row_of(C) =:= Row end, Rest)
    end.

row_of(C) when is_integer(C) ->
    case C of
        $q;$w;$e;$r;$t;$y;$u;$i;$o;$p -> 1;
        $a;$s;$d;$f;$g;$h;$j;$k;$l -> 2;
        $z;$x;$c;$v;$b;$n;$m -> 3;
        _ -> 0
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_words(words :: [String.t]) :: [String.t]
  def find_words(words) do
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

    char_to_row =
      Enum.reduce(Enum.with_index(rows), %{}, fn {row, idx}, acc ->
        String.graphemes(row)
        |> Enum.reduce(acc, fn ch, a -> Map.put(a, ch, idx) end)
      end)

    Enum.filter(words, fn word ->
      lower = String.downcase(word)
      chars = String.graphemes(lower)

      case chars do
        [] -> false
        [first | rest] ->
          row = Map.get(char_to_row, first)
          Enum.all?(rest, fn ch -> Map.get(char_to_row, ch) == row end)
      end
    end)
  end
end
```
