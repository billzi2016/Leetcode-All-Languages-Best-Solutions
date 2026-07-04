# 0405. Convert a Number to Hexadecimal

## Cpp

```cpp
class Solution {
public:
    std::string toHex(int num) {
        if (num == 0) return "0";
        unsigned int n = static_cast<unsigned int>(num);
        std::string res;
        const char* hexChars = "0123456789abcdef";
        while (n) {
            res.push_back(hexChars[n & 0xF]);
            n >>= 4;
        }
        std::reverse(res.begin(), res.end());
        return res;
    }
};
```

## Java

```java
class Solution {
    public String toHex(int num) {
        if (num == 0) return "0";
        char[] hex = {'0','1','2','3','4','5','6','7','8','9',
                      'a','b','c','d','e','f'};
        StringBuilder sb = new StringBuilder();
        while (num != 0) {
            int digit = num & 0xf;
            sb.append(hex[digit]);
            num >>>= 4;
        }
        return sb.reverse().toString();
    }
}
```

## Python

```python
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        n = num & 0xffffffff
        res = []
        while n:
            res.append(hex_chars[n & 0xf])
            n >>= 4
        return "".join(reversed(res))
```

## Python3

```python
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        n = num & 0xffffffff
        res = []
        while n:
            res.append(hex_chars[n & 0xf])
            n >>= 4
        return ''.join(reversed(res))
```

## C

```c
#include <stdlib.h>

char* toHex(int num) {
    const char *digits = "0123456789abcdef";
    unsigned int n = (unsigned int)num;
    
    if (n == 0) {
        char *res = (char *)malloc(2);
        res[0] = '0';
        res[1] = '\0';
        return res;
    }
    
    char buf[8];
    int len = 0;
    while (n != 0) {
        buf[len++] = digits[n & 0xF];
        n >>= 4;
    }
    
    char *res = (char *)malloc(len + 1);
    for (int i = 0; i < len; ++i) {
        res[i] = buf[len - 1 - i];
    }
    res[len] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string ToHex(int num) {
        if (num == 0) return "0";
        uint n = (uint)num;
        const string map = "0123456789abcdef";
        var sb = new System.Text.StringBuilder();
        while (n != 0) {
            uint digit = n & 0xF;
            sb.Append(map[(int)digit]);
            n >>= 4;
        }
        char[] arr = sb.ToString().ToCharArray();
        System.Array.Reverse(arr);
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {string}
 */
var toHex = function(num) {
    if (num === 0) return "0";
    const hexChars = '0123456789abcdef';
    let n = num >>> 0; // treat as unsigned 32-bit integer
    let res = '';
    while (n !== 0) {
        const digit = n & 0xf;
        res = hexChars[digit] + res;
        n = n >>> 4;
    }
    return res;
};
```

## Typescript

```typescript
function toHex(num: number): string {
    if (num === 0) return "0";
    const hexChars = "0123456789abcdef";
    let n = num >>> 0; // treat as unsigned 32-bit
    let result = "";
    while (n !== 0) {
        const digit = n & 15;
        result = hexChars[digit] + result;
        n = n >>> 4;
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $num
     * @return String
     */
    function toHex($num) {
        if ($num == 0) return "0";
        $hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
        $num = $num & 0xffffffff;
        $res = '';
        while ($num != 0) {
            $digit = $num & 0xf;
            $res = $hex[$digit] . $res;
            $num = $num >> 4;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func toHex(_ num: Int) -> String {
        if num == 0 { return "0" }
        let hexChars = Array("0123456789abcdef")
        var n = UInt32(bitPattern: Int32(num))
        var chars: [Character] = []
        while n != 0 {
            let digit = Int(n & 0xF)
            chars.append(hexChars[digit])
            n >>= 4
        }
        return String(chars.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun toHex(num: Int): String {
        if (num == 0) return "0"
        var n = num
        val sb = StringBuilder()
        val hexChars = charArrayOf('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
        while (n != 0) {
            val digit = n and 0xF
            sb.append(hexChars[digit])
            n = n ushr 4
        }
        return sb.reverse().toString()
    }
}
```

## Dart

```dart
class Solution {
  String toHex(int num) {
    const String hexChars = '0123456789abcdef';
    int n = num & 0xffffffff;
    if (n == 0) return '0';
    String result = '';
    while (n != 0) {
      int digit = n & 15;
      result = hexChars[digit] + result;
      n >>= 4;
    }
    return result;
  }
}
```

## Golang

```go
func toHex(num int) string {
	if num == 0 {
		return "0"
	}
	hexChars := []byte("0123456789abcdef")
	var n uint32 = uint32(num)
	var res []byte
	for n != 0 {
		digit := n & 0xf
		res = append(res, hexChars[digit])
		n >>= 4
	}
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return string(res)
}
```

## Ruby

```ruby
def to_hex(num)
  return "0" if num == 0
  hex_chars = "0123456789abcdef"
  n = num & 0xffffffff
  res = ""
  while n != 0
    digit = n & 0xf
    res << hex_chars[digit]
    n >>= 4
  end
  res.reverse
end
```

## Scala

```scala
object Solution {
    def toHex(num: Int): String = {
        if (num == 0) return "0"
        val hexChars = "0123456789abcdef".toCharArray
        var n = num
        val sb = new java.lang.StringBuilder()
        while (n != 0) {
            val digit = n & 0xf
            sb.append(hexChars(digit))
            n = n >>> 4
        }
        sb.reverse.toString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn to_hex(num: i32) -> String {
        if num == 0 {
            return "0".to_string();
        }
        let mut n = num as u32;
        const HEX: &[u8; 16] = b"0123456789abcdef";
        let mut chars = Vec::new();
        while n != 0 {
            let digit = (n & 0xf) as usize;
            chars.push(HEX[digit] as char);
            n >>= 4;
        }
        chars.iter().rev().collect()
    }
}
```

## Racket

```racket
(define hex-digits "0123456789abcdef")

(define/contract (to-hex num)
  (-> exact-integer? string?)
  (if (= num 0)
      "0"
      (let loop ((n (bitwise-and num #xffffffff)) (chars '()))
        (if (= n 0)
            (list->string (reverse chars))
            (let* ([digit (bitwise-and n 15)]
                   [ch (string-ref hex-digits digit)])
              (loop (arithmetic-shift n -4) (cons ch chars)))))))
```

## Erlang

```erlang
-module(solution).
-export([to_hex/1]).

-spec to_hex(Num :: integer()) -> unicode:unicode_binary().
to_hex(Num) ->
    Mask = 16#FFFFFFFF,
    Unsigned = Num band Mask,
    case Unsigned of
        0 -> <<"0">>;
        _ -> build_hex(Unsigned, [])
    end.

build_hex(0, Acc) ->
    list_to_binary(Acc);
build_hex(N, Acc) ->
    Digit = N band 15,
    Char = if
        Digit < 10 -> $0 + Digit;
        true       -> $a + (Digit - 10)
    end,
    build_hex(N bsr 4, [Char | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec to_hex(num :: integer) :: String.t()
  def to_hex(num) do
    if num == 0 do
      "0"
    else
      unsigned = Bitwise.band(num, 0xFFFFFFFF)

      unsigned
      |> build_hex([])
      |> Enum.join()
    end
  end

  defp build_hex(0, acc), do: acc

  defp build_hex(n, acc) do
    digit = rem(n, 16)

    char =
      if digit < 10 do
        <<?0 + digit>>
      else
        <<?a + (digit - 10)>>
      end

    build_hex(div(n, 16), [char | acc])
  end
end
```
