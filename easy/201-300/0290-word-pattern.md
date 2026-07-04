# 0290. Word Pattern

## Cpp

```cpp
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        string word;
        for (size_t i = 0; i < s.size(); ++i) {
            if (s[i] == ' ') {
                words.push_back(word);
                word.clear();
            } else {
                word += s[i];
            }
        }
        if (!word.empty()) words.push_back(word);
        
        if (words.size() != pattern.size()) return false;
        
        unordered_map<char, string> c2w;
        unordered_map<string, char> w2c;
        for (size_t i = 0; i < pattern.size(); ++i) {
            char c = pattern[i];
            const string& w = words[i];
            auto itC = c2w.find(c);
            if (itC != c2w.end()) {
                if (itC->second != w) return false;
            } else {
                c2w[c] = w;
            }
            auto itW = w2c.find(w);
            if (itW != w2c.end()) {
                if (itW->second != c) return false;
            } else {
                w2c[w] = c;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (pattern.length() != words.length) return false;
        java.util.Map<Character, String> map = new java.util.HashMap<>();
        java.util.Map<String, Character> rev = new java.util.HashMap<>();
        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String w = words[i];
            if (!map.containsKey(c)) {
                if (rev.containsKey(w)) return false;
                map.put(c, w);
                rev.put(w, c);
            } else {
                if (!map.get(c).equals(w)) return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        used_words = set()

        for ch, w in zip(pattern, words):
            if ch in char_to_word:
                if char_to_word[ch] != w:
                    return False
            else:
                if w in used_words:
                    return False
                char_to_word[ch] = w
                used_words.add(w)
        return True
```

## Python3

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        used_words = set()
        for c, w in zip(pattern, words):
            if c not in char_to_word:
                if w in used_words:
                    return False
                char_to_word[c] = w
                used_words.add(w)
            elif char_to_word[c] != w:
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static char* str_dup(const char *src) {
    size_t len = strlen(src);
    char *dst = (char*)malloc(len + 1);
    if (dst) memcpy(dst, src, len + 1);
    return dst;
}

bool wordPattern(char* pattern, char* s) {
    int pat_len = strlen(pattern);
    
    // Duplicate s because strtok modifies the string
    char *s_copy = str_dup(s);
    if (!s_copy) return false;
    
    // Split s into words
    char *words[300];
    int word_cnt = 0;
    char *token = strtok(s_copy, " ");
    while (token) {
        words[word_cnt++] = token;
        token = strtok(NULL, " ");
    }
    
    if (pat_len != word_cnt) {
        free(s_copy);
        return false;
    }
    
    char *map[26] = {0};
    
    for (int i = 0; i < pat_len; ++i) {
        int idx = pattern[i] - 'a';
        char *w = words[i];
        
        if (!map[idx]) {
            // Ensure the word is not already mapped to another character
            for (int j = 0; j < 26; ++j) {
                if (j != idx && map[j] && strcmp(map[j], w) == 0) {
                    free(s_copy);
                    return false;
                }
            }
            map[idx] = str_dup(w);
            if (!map[idx]) {
                // cleanup before returning
                for (int k = 0; k < 26; ++k)
                    if (map[k]) free(map[k]);
                free(s_copy);
                return false;
            }
        } else {
            if (strcmp(map[idx], w) != 0) {
                for (int k = 0; k < 26; ++k)
                    if (map[k]) free(map[k]);
                free(s_copy);
                return false;
            }
        }
    }
    
    // Cleanup
    for (int i = 0; i < 26; ++i)
        if (map[i]) free(map[i]);
    free(s_copy);
    
    return true;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public bool WordPattern(string pattern, string s) {
        var words = s.Split(' ');
        if (pattern.Length != words.Length) return false;
        
        var charToWord = new Dictionary<char, string>();
        var wordToChar = new Dictionary<string, char>();
        
        for (int i = 0; i < pattern.Length; i++) {
            char c = pattern[i];
            string w = words[i];
            
            if (charToWord.TryGetValue(c, out var mappedWord)) {
                if (mappedWord != w) return false;
            } else {
                charToWord[c] = w;
            }
            
            if (wordToChar.TryGetValue(w, out var mappedChar)) {
                if (mappedChar != c) return false;
            } else {
                wordToChar[w] = c;
            }
        }
        
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const words = s.split(' ');
    if (pattern.length !== words.length) return false;
    const charToWord = new Map();
    const usedWords = new Set();
    for (let i = 0; i < pattern.length; i++) {
        const ch = pattern[i];
        const word = words[i];
        if (charToWord.has(ch)) {
            if (charToWord.get(ch) !== word) return false;
        } else {
            if (usedWords.has(word)) return false;
            charToWord.set(ch, word);
            usedWords.add(word);
        }
    }
    return true;
};
```

## Typescript

```typescript
function wordPattern(pattern: string, s: string): boolean {
    const words = s.split(' ');
    if (pattern.length !== words.length) return false;

    const charToWord = new Map<string, string>();
    const wordToChar = new Map<string, string>();

    for (let i = 0; i < pattern.length; i++) {
        const c = pattern[i];
        const w = words[i];

        const mappedWord = charToWord.get(c);
        if (mappedWord !== undefined) {
            if (mappedWord !== w) return false;
        } else {
            charToWord.set(c, w);
        }

        const mappedChar = wordToChar.get(w);
        if (mappedChar !== undefined) {
            if (mappedChar !== c) return false;
        } else {
            wordToChar.set(w, c);
        }
    }

    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $pattern
     * @param String $s
     * @return Boolean
     */
    function wordPattern($pattern, $s) {
        $words = explode(' ', $s);
        if (strlen($pattern) !== count($words)) {
            return false;
        }

        $charToWord = [];
        $wordToChar = [];

        for ($i = 0; $i < strlen($pattern); $i++) {
            $c = $pattern[$i];
            $w = $words[$i];

            if (isset($charToWord[$c])) {
                if ($charToWord[$c] !== $w) {
                    return false;
                }
            } else {
                $charToWord[$c] = $w;
            }

            if (isset($wordToChar[$w])) {
                if ($wordToChar[$w] !== $c) {
                    return false;
                }
            } else {
                $wordToChar[$w] = $c;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func wordPattern(_ pattern: String, _ s: String) -> Bool {
        let words = s.split(separator: " ").map { String($0) }
        let chars = Array(pattern)
        if chars.count != words.count { return false }
        
        var charToWord = [Character: String]()
        var wordToChar = [String: Character]()
        
        for i in 0..<chars.count {
            let c = chars[i]
            let w = words[i]
            
            if let mappedWord = charToWord[c] {
                if mappedWord != w { return false }
            } else {
                if wordToChar[w] != nil { return false }
                charToWord[c] = w
                wordToChar[w] = c
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun wordPattern(pattern: String, s: String): Boolean {
        val words = s.split(' ')
        if (pattern.length != words.size) return false

        val charToWord = HashMap<Char, String>()
        val wordToChar = HashMap<String, Char>()

        for (i in pattern.indices) {
            val c = pattern[i]
            val w = words[i]

            val mappedWord = charToWord[c]
            if (mappedWord != null) {
                if (mappedWord != w) return false
            } else {
                if (wordToChar.containsKey(w)) return false
                charToWord[c] = w
                wordToChar[w] = c
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool wordPattern(String pattern, String s) {
    List<String> words = s.split(' ');
    if (words.length != pattern.length) return false;

    Map<String, String> charToWord = {};
    Map<String, String> wordToChar = {};

    for (int i = 0; i < pattern.length; i++) {
      String c = pattern[i];
      String w = words[i];

      if (charToWord.containsKey(c)) {
        if (charToWord[c] != w) return false;
      } else {
        if (wordToChar.containsKey(w)) return false;
        charToWord[c] = w;
        wordToChar[w] = c;
      }
    }

    return true;
  }
}
```

## Golang

```go
package main

import "strings"

func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")
	if len(words) != len(pattern) {
		return false
	}
	charToWord := make(map[byte]string)
	wordToChar := make(map[string]byte)

	for i := 0; i < len(pattern); i++ {
		c := pattern[i]
		w := words[i]

		if mapped, ok := charToWord[c]; ok {
			if mapped != w {
				return false
			}
		} else {
			if rev, ok2 := wordToChar[w]; ok2 && rev != c {
				return false
			}
			charToWord[c] = w
			wordToChar[w] = c
		}
	}
	return true
}
```

## Ruby

```ruby
def word_pattern(pattern, s)
  words = s.split(' ')
  return false unless pattern.length == words.length

  char_to_word = {}
  word_to_char = {}

  pattern.chars.each_with_index do |ch, i|
    w = words[i]

    if char_to_word.key?(ch)
      return false unless char_to_word[ch] == w
    else
      char_to_word[ch] = w
    end

    if word_to_char.key?(w)
      return false unless word_to_char[w] == ch
    else
      word_to_char[w] = ch
    end
  end

  true
end
```

## Scala

```scala
object Solution {
  def wordPattern(pattern: String, s: String): Boolean = {
    val words = s.split(" ")
    if (pattern.length != words.length) return false

    val charToWord = scala.collection.mutable.Map[Char, String]()
    val wordToChar = scala.collection.mutable.Map[String, Char]()

    for ((c, w) <- pattern.zip(words)) {
      charToWord.get(c) match {
        case Some(mapped) =>
          if (mapped != w) return false
        case None =>
          wordToChar.get(w) match {
            case Some(matchedC) =>
              if (matchedC != c) return false
            case None =>
              charToWord(c) = w
              wordToChar(w) = c
          }
      }
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        let words: Vec<&str> = s.split_whitespace().collect();
        if pattern.len() != words.len() {
            return false;
        }
        use std::collections::HashMap;
        let mut char_to_word: HashMap<char, &str> = HashMap::new();
        let mut word_to_char: HashMap<&str, char> = HashMap::new();

        for (ch, w) in pattern.chars().zip(words.iter()) {
            let word = *w;
            if let Some(&mapped_word) = char_to_word.get(&ch) {
                if mapped_word != word {
                    return false;
                }
            } else {
                if let Some(&mapped_ch) = word_to_char.get(word) {
                    if mapped_ch != ch {
                        return false;
                    }
                }
                char_to_word.insert(ch, word);
                word_to_char.insert(word, ch);
            }
        }
        true
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (word-pattern pattern s)
  (-> string? string? boolean?)
  (let* ([words (string-split s)]
         [chars (string->list pattern)])
    (if (not (= (length words) (length chars)))
        #f
        (let ([c2w (make-hash)] [w2c (make-hash)])
          (for/and ([ch chars] [wd words])
            (define existing-w (hash-ref c2w ch #f))
            (define existing-c (hash-ref w2c wd #f))
            (cond
              [(and existing-w (not (equal? existing-w wd))) #f]
              [(and existing-c (not (equal? existing-c ch))) #f]
              [else
               (unless existing-w (hash-set! c2w ch wd))
               (unless existing-c (hash-set! w2c wd ch))
               #t]))))))
```

## Erlang

```erlang
-module(solution).
-export([word_pattern/2]).

-spec word_pattern(Pattern :: unicode:unicode_binary(), S :: unicode:unicode_binary()) -> boolean().
word_pattern(Pattern, S) ->
    PatternChars = unicode:characters_to_list(Pattern),
    Words = binary:split(S, <<" ">>, [global]),
    case length(PatternChars) == length(Words) of
        false -> false;
        true -> check(PatternChars, Words, #{}, #{})
    end.

check([], [], _CharMap, _WordMap) ->
    true;
check([C|Cs], [W|Ws], CharMap, WordMap) ->
    case {maps:get(C, CharMap, undefined), maps:get(W, WordMap, undefined)} of
        {undefined, undefined} ->
            NewCharMap = maps:put(C, W, CharMap),
            NewWordMap = maps:put(W, C, WordMap),
            check(Cs, Ws, NewCharMap, NewWordMap);
        {W2, C2} when W2 == W, C2 == C ->
            check(Cs, Ws, CharMap, WordMap);
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec word_pattern(pattern :: String.t(), s :: String.t()) :: boolean()
  def word_pattern(pattern, s) do
    words = String.split(s, " ", trim: true)
    chars = String.graphemes(pattern)

    if length(chars) != length(words) do
      false
    else
      case Enum.reduce_while(Enum.zip(chars, words), {%{}, %{}}, fn {c, w}, {map_c2w, map_w2c} ->
        cond do
          Map.has_key?(map_c2w, c) and Map.get(map_c2w, c) != w ->
            {:halt, :error}
          not Map.has_key?(map_c2w, c) and Map.has_key?(map_w2c, w) ->
            {:halt, :error}
          true ->
            {:cont, {Map.put(map_c2w, c, w), Map.put(map_w2c, w, c)}}
        end
      end) do
        :error -> false
        _ -> true
      end
    end
  end
end
```
