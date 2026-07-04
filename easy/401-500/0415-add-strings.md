# 0415. Add Strings

## Cpp

```cpp
class Solution {
public:
    string addStrings(string num1, string num2) {
        int i = (int)num1.size() - 1;
        int j = (int)num2.size() - 1;
        int carry = 0;
        string res;
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) sum += num1[i--] - '0';
            if (j >= 0) sum += num2[j--] - '0';
            res.push_back(char('0' + (sum % 10)));
            carry = sum / 10;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

## Java

```java
class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        int carry = 0;
        while (i >= 0 || j >= 0 || carry != 0) {
            int sum = carry;
            if (i >= 0) sum += num1.charAt(i--) - '0';
            if (j >= 0) sum += num2.charAt(j--) - '0';
            sb.append((char)('0' + (sum % 10)));
            carry = sum / 10;
        }
        return sb.reverse().toString();
    }
}
```

## Python

```python
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            n1 = ord(num1[i]) - 48 if i >= 0 else 0
            n2 = ord(num2[j]) - 48 if j >= 0 else 0
            total = n1 + n2 + carry
            res.append(chr((total % 10) + 48))
            carry = total // 10
            i -= 1
            j -= 1
        return ''.join(reversed(res))
```

## Python3

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            n1 = ord(num1[i]) - 48 if i >= 0 else 0
            n2 = ord(num2[j]) - 48 if j >= 0 else 0
            total = n1 + n2 + carry
            res.append(chr(total % 10 + 48))
            carry = total // 10
            i -= 1
            j -= 1
        return ''.join(reversed(res))
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* addStrings(char* num1, char* num2) {
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    int maxlen = len1 > len2 ? len1 : len2;
    
    // Allocate space for possible carry and null terminator
    char *res = (char *)malloc(maxlen + 2);
    if (!res) return NULL;
    res[maxlen + 1] = '\0';
    
    int i = len1 - 1, j = len2 - 1;
    int p = maxlen;          // position to fill in res
    int carry = 0;
    
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += num1[i--] - '0';
        if (j >= 0) sum += num2[j--] - '0';
        res[p--] = (char)((sum % 10) + '0');
        carry = sum / 10;
    }
    
    int start = p + 1; // first valid character
    memmove(res, res + start, maxlen + 2 - start);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string AddStrings(string num1, string num2) {
        int i = num1.Length - 1;
        int j = num2.Length - 1;
        int carry = 0;
        var sb = new System.Text.StringBuilder();
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry;
            if (i >= 0) sum += num1[i--] - '0';
            if (j >= 0) sum += num2[j--] - '0';
            sb.Append((char)('0' + (sum % 10)));
            carry = sum / 10;
        }
        char[] result = sb.ToString().ToCharArray();
        System.Array.Reverse(result);
        return new string(result);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    let i = num1.length - 1;
    let j = num2.length - 1;
    let carry = 0;
    const res = [];
    while (i >= 0 || j >= 0 || carry) {
        const x = i >= 0 ? num1.charCodeAt(i) - 48 : 0;
        const y = j >= 0 ? num2.charCodeAt(j) - 48 : 0;
        const sum = x + y + carry;
        res.push(String.fromCharCode((sum % 10) + 48));
        carry = Math.floor(sum / 10);
        i--;
        j--;
    }
    return res.reverse().join('');
};
```

## Typescript

```typescript
function addStrings(num1: string, num2: string): string {
    let i = num1.length - 1;
    let j = num2.length - 1;
    let carry = 0;
    const result: string[] = [];

    while (i >= 0 || j >= 0 || carry) {
        const x = i >= 0 ? num1.charCodeAt(i) - 48 : 0;
        const y = j >= 0 ? num2.charCodeAt(j) - 48 : 0;
        const sum = x + y + carry;
        result.push(String.fromCharCode((sum % 10) + 48));
        carry = Math.floor(sum / 10);
        i--;
        j--;
    }

    return result.reverse().join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $num1
     * @param String $num2
     * @return String
     */
    function addStrings($num1, $num2) {
        $i = strlen($num1) - 1;
        $j = strlen($num2) - 1;
        $carry = 0;
        $res = '';
        while ($i >= 0 || $j >= 0 || $carry) {
            $sum = $carry;
            if ($i >= 0) {
                $sum += ord($num1[$i]) - 48;
                $i--;
            }
            if ($j >= 0) {
                $sum += ord($num2[$j]) - 48;
                $j--;
            }
            $res .= chr(($sum % 10) + 48);
            $carry = intdiv($sum, 10);
        }
        return strrev($res);
    }
}
```

## Swift

```swift
class Solution {
    func addStrings(_ num1: String, _ num2: String) -> String {
        let a = Array(num1)
        let b = Array(num2)
        var i = a.count - 1
        var j = b.count - 1
        var carry = 0
        var res = [Character]()
        
        while i >= 0 || j >= 0 || carry > 0 {
            var sum = carry
            if i >= 0 {
                let val = Int(a[i].unicodeScalars.first!.value - 48)
                sum += val
                i -= 1
            }
            if j >= 0 {
                let val = Int(b[j].unicodeScalars.first!.value - 48)
                sum += val
                j -= 1
            }
            let digitChar = Character(UnicodeScalar(sum % 10 + 48)!)
            res.append(digitChar)
            carry = sum / 10
        }
        return String(res.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun addStrings(num1: String, num2: String): String {
        var i = num1.length - 1
        var j = num2.length - 1
        var carry = 0
        val sb = StringBuilder()
        while (i >= 0 || j >= 0 || carry != 0) {
            val n1 = if (i >= 0) num1[i] - '0' else 0
            val n2 = if (j >= 0) num2[j] - '0' else 0
            val sum = n1 + n2 + carry
            sb.append((sum % 10))
            carry = sum / 10
            i--
            j--
        }
        return sb.reverse().toString()
    }
}
```

## Dart

```dart
class Solution {
  String addStrings(String num1, String num2) {
    int i = num1.length - 1;
    int j = num2.length - 1;
    int carry = 0;
    List<String> res = [];

    while (i >= 0 || j >= 0 || carry != 0) {
      int x = i >= 0 ? num1.codeUnitAt(i) - 48 : 0;
      int y = j >= 0 ? num2.codeUnitAt(j) - 48 : 0;
      int sum = x + y + carry;
      res.add(String.fromCharCode((sum % 10) + 48));
      carry = sum ~/ 10;
      i--;
      j--;
    }

    return res.reversed.join();
  }
}
```

## Golang

```go
func addStrings(num1 string, num2 string) string {
	i := len(num1) - 1
	j := len(num2) - 1
	carry := 0
	var res []byte
	for i >= 0 || j >= 0 || carry > 0 {
		sum := carry
		if i >= 0 {
			sum += int(num1[i] - '0')
			i--
		}
		if j >= 0 {
			sum += int(num2[j] - '0')
			j--
		}
		res = append(res, byte(sum%10)+'0')
		carry = sum / 10
	}
	for l, r := 0, len(res)-1; l < r; l, r = l+1, r-1 {
		res[l], res[r] = res[r], res[l]
	}
	return string(res)
}
```

## Ruby

```ruby
def add_strings(num1, num2)
  i = num1.length - 1
  j = num2.length - 1
  carry = 0
  digits = []

  while i >= 0 || j >= 0 || carry > 0
    d1 = i >= 0 ? num1.getbyte(i) - 48 : 0
    d2 = j >= 0 ? num2.getbyte(j) - 48 : 0
    sum = d1 + d2 + carry
    digits << (sum % 10)
    carry = sum / 10
    i -= 1
    j -= 1
  end

  digits.reverse.map { |d| (d + 48).chr }.join
end
```

## Scala

```scala
object Solution {
    def addStrings(num1: String, num2: String): String = {
        val sb = new java.lang.StringBuilder()
        var i = num1.length - 1
        var j = num2.length - 1
        var carry = 0
        while (i >= 0 || j >= 0 || carry != 0) {
            val n1 = if (i >= 0) num1.charAt(i) - '0' else 0
            val n2 = if (j >= 0) num2.charAt(j) - '0' else 0
            val sum = n1 + n2 + carry
            sb.append((sum % 10).toString)
            carry = sum / 10
            i -= 1
            j -= 1
        }
        sb.reverse.toString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn add_strings(num1: String, num2: String) -> String {
        let b1 = num1.as_bytes();
        let b2 = num2.as_bytes();
        let mut i: i32 = b1.len() as i32 - 1;
        let mut j: i32 = b2.len() as i32 - 1;
        let mut carry = 0;
        let mut res: Vec<u8> = Vec::new();

        while i >= 0 || j >= 0 || carry > 0 {
            let mut sum = carry;
            if i >= 0 {
                sum += (b1[i as usize] - b'0') as i32;
                i -= 1;
            }
            if j >= 0 {
                sum += (b2[j as usize] - b'0') as i32;
                j -= 1;
            }
            res.push((sum % 10) as u8 + b'0');
            carry = sum / 10;
        }

        res.reverse();
        unsafe { String::from_utf8_unchecked(res) }
    }
}
```

## Racket

```racket
(define/contract (add-strings num1 num2)
  (-> string? string? string?)
  (let* ((len1 (string-length num1))
         (len2 (string-length num2)))
    (let loop ((i (sub1 len1)) (j (sub1 len2)) (carry 0) (acc '()))
      (if (and (< i 0) (< j 0) (= carry 0))
          (list->string (reverse acc))
          (let* ((d1 (if (>= i 0)
                         (- (char->integer (string-ref num1 i)) 48)
                         0))
                 (d2 (if (>= j 0)
                         (- (char->integer (string-ref num2 j)) 48)
                         0))
                 (sum (+ d1 d2 carry))
                 (digit (modulo sum 10))
                 (newcarry (quotient sum 10)))
            (loop (sub1 i) (sub1 j) newcarry
                  (cons (integer->char (+ digit 48)) acc)))))))
```

## Erlang

```erlang
-export([add_strings/2]).
-spec add_strings(Num1 :: unicode:unicode_binary(), Num2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
add_strings(Num1, Num2) ->
    Rev1 = lists:reverse(binary_to_list(Num1)),
    Rev2 = lists:reverse(binary_to_list(Num2)),
    SumRev = add_lists(Rev1, Rev2, 0, []),
    list_to_binary(lists:reverse(SumRev)).

add_lists([], [], 0, Acc) ->
    Acc;
add_lists([], [], Carry, Acc) when Carry > 0 ->
    [Carry + $0 | Acc];
add_lists([H|T], [], Carry, Acc) ->
    Sum = (H - $0) + Carry,
    Digit = (Sum rem 10) + $0,
    NewCarry = Sum div 10,
    add_lists(T, [], NewCarry, [Digit | Acc]);
add_lists([], [H|T], Carry, Acc) ->
    Sum = (H - $0) + Carry,
    Digit = (Sum rem 10) + $0,
    NewCarry = Sum div 10,
    add_lists([], T, NewCarry, [Digit | Acc]);
add_lists([H1|T1], [H2|T2], Carry, Acc) ->
    Sum = (H1 - $0) + (H2 - $0) + Carry,
    Digit = (Sum rem 10) + $0,
    NewCarry = Sum div 10,
    add_lists(T1, T2, NewCarry, [Digit | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec add_strings(num1 :: String.t(), num2 :: String.t()) :: String.t()
  def add_strings(num1, num2) do
    i = byte_size(num1) - 1
    j = byte_size(num2) - 1

    add(num1, i, num2, j, 0, [])
    |> Enum.join()
  end

  defp add(_num1, i, _num2, j, carry, acc) when i < 0 and j < 0 and carry == 0 do
    Enum.reverse(acc)
  end

  defp add(num1, i, num2, j, carry, acc) do
    d1 = if i >= 0, do: :binary.at(num1, i) - ?0, else: 0
    d2 = if j >= 0, do: :binary.at(num2, j) - ?0, else: 0

    sum = d1 + d2 + carry
    digit = rem(sum, 10)
    new_carry = div(sum, 10)

    char = <<digit + ?0>>
    add(num1, i - 1, num2, j - 1, new_carry, [char | acc])
  end
end
```
