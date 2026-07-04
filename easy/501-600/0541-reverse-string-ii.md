# 0541. Reverse String II

## Cpp

```cpp
class Solution {
public:
    string reverseStr(string s, int k) {
        int n = s.size();
        for (int start = 0; start < n; start += 2 * k) {
            int left = start;
            int right = min(start + k - 1, n - 1);
            while (left < right) {
                swap(s[left], s[right]);
                ++left;
                --right;
            }
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String reverseStr(String s, int k) {
        char[] a = s.toCharArray();
        int n = a.length;
        for (int start = 0; start < n; start += 2 * k) {
            int i = start;
            int j = Math.min(start + k - 1, n - 1);
            while (i < j) {
                char tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;
                i++;
                j--;
            }
        }
        return new String(a);
    }
}
```

## Python

```python
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a = list(s)
        n = len(a)
        step = 2 * k
        for start in range(0, n, step):
            left = start
            right = min(start + k - 1, n - 1)
            while left < right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        return ''.join(a)
```

## Python3

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        n = len(a)
        for i in range(0, n, 2 * k):
            left, right = i, min(i + k - 1, n - 1)
            while left < right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        return ''.join(a)
```

## C

```c
#include <string.h>

char* reverseStr(char* s, int k) {
    int n = strlen(s);
    for (int start = 0; start < n; start += 2 * k) {
        int i = start;
        int j = start + k - 1;
        if (j >= n) j = n - 1;
        while (i < j) {
            char tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
            ++i;
            --j;
        }
    }
    return s;
}
```

## Csharp

```csharp
public class Solution
{
    public string ReverseStr(string s, int k)
    {
        char[] a = s.ToCharArray();
        int n = a.Length;
        for (int start = 0; start < n; start += 2 * k)
        {
            int i = start;
            int j = Math.Min(start + k - 1, n - 1);
            while (i < j)
            {
                char tmp = a[i];
                a[i++] = a[j];
                a[j--] = tmp;
            }
        }
        return new string(a);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function(s, k) {
    const arr = s.split('');
    const n = arr.length;
    for (let start = 0; start < n; start += 2 * k) {
        let left = start;
        let right = Math.min(start + k - 1, n - 1);
        while (left < right) {
            const tmp = arr[left];
            arr[left] = arr[right];
            arr[right] = tmp;
            left++;
            right--;
        }
    }
    return arr.join('');
};
```

## Typescript

```typescript
function reverseStr(s: string, k: number): string {
    const arr = s.split('');
    const n = arr.length;
    for (let start = 0; start < n; start += 2 * k) {
        let i = start;
        let j = Math.min(start + k - 1, n - 1);
        while (i < j) {
            const temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
    return arr.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function reverseStr($s, $k) {
        $n = strlen($s);
        $arr = str_split($s);
        for ($start = 0; $start < $n; $start += 2 * $k) {
            $left = $start;
            $right = min($start + $k - 1, $n - 1);
            while ($left < $right) {
                $tmp = $arr[$left];
                $arr[$left] = $arr[$right];
                $arr[$right] = $tmp;
                $left++;
                $right--;
            }
        }
        return implode('', $arr);
    }
}
```

## Swift

```swift
class Solution {
    func reverseStr(_ s: String, _ k: Int) -> String {
        var chars = Array(s)
        let n = chars.count
        var i = 0
        while i < n {
            var left = i
            var right = min(i + k - 1, n - 1)
            while left < right {
                chars.swapAt(left, right)
                left += 1
                right -= 1
            }
            i += 2 * k
        }
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reverseStr(s: String, k: Int): String {
        val chars = s.toCharArray()
        var start = 0
        val n = chars.size
        while (start < n) {
            var left = start
            var right = minOf(start + k - 1, n - 1)
            while (left < right) {
                val tmp = chars[left]
                chars[left] = chars[right]
                chars[right] = tmp
                left++
                right--
            }
            start += 2 * k
        }
        return String(chars)
    }
}
```

## Dart

```dart
class Solution {
  String reverseStr(String s, int k) {
    List<String> chars = s.split('');
    int n = chars.length;
    for (int start = 0; start < n; start += 2 * k) {
      int left = start;
      int right = (start + k - 1).clamp(0, n - 1);
      while (left < right) {
        String temp = chars[left];
        chars[left] = chars[right];
        chars[right] = temp;
        left++;
        right--;
      }
    }
    return chars.join();
  }
}
```

## Golang

```go
func reverseStr(s string, k int) string {
	n := len(s)
	if n == 0 || k <= 0 {
		return s
	}
	b := []byte(s)
	for start := 0; start < n; start += 2 * k {
		end := start + k - 1
		if end >= n {
			end = n - 1
		}
		i, j := start, end
		for i < j {
			b[i], b[j] = b[j], b[i]
			i++
			j--
		}
	}
	return string(b)
}
```

## Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def reverse_str(s, k)
  chars = s.chars
  n = chars.length
  i = 0
  while i < n
    left = i
    right = [i + k - 1, n - 1].min
    while left < right
      chars[left], chars[right] = chars[right], chars[left]
      left += 1
      right -= 1
    end
    i += 2 * k
  end
  chars.join
end
```

## Scala

```scala
object Solution {
    def reverseStr(s: String, k: Int): String = {
        val arr = s.toCharArray
        var i = 0
        while (i < arr.length) {
            var left = i
            var right = Math.min(i + k - 1, arr.length - 1)
            while (left < right) {
                val tmp = arr(left)
                arr(left) = arr(right)
                arr(right) = tmp
                left += 1
                right -= 1
            }
            i += 2 * k
        }
        new String(arr)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_str(s: String, k: i32) -> String {
        let mut chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let k = k as usize;
        if k == 0 || n == 0 {
            return s;
        }
        let step = 2 * k;
        let mut start = 0usize;
        while start < n {
            let end = std::cmp::min(start + k, n);
            chars[start..end].reverse();
            start += step;
        }
        chars.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (reverse-str s k)
  (-> string? exact-integer? string?)
  (let* ([n (string-length s)]
         [chunks
          (let loop ((i 0) (acc '()))
            (cond
              [(>= i n) (reverse acc)]
              [(< (- n i) k)
               (let* ([part (substring s i n)]
                      [rev-part (list->string (reverse (string->list part)))])
                 (loop n (cons rev-part acc)))]
              [else
               (let* ([first-end (+ i k)]
                      [first-part (substring s i first-end)]
                      [rev-first (list->string (reverse (string->list first-part)))]

                      [second-end (min (+ i (* 2 k)) n)]
                      [second-part (substring s first-end second-end)])
                 (loop second-end (cons second-part (cons rev-first acc))))]))])
    (apply string-append chunks)))
```

## Erlang

```erlang
-spec reverse_str(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
reverse_str(S, K) ->
    List = binary_to_list(S),
    Processed = process_chunks(List, K),
    list_to_binary(Processed).

process_chunks([], _K) -> [];
process_chunks(L, K) ->
    {Chunk, Rest} = lists:split(2 * K, L),
    ProcessedChunk = process_chunk(Chunk, K),
    ProcessedChunk ++ process_chunks(Rest, K).

process_chunk(Chunk, K) ->
    case length(Chunk) >= K of
        true ->
            {FirstK, Rest} = lists:split(K, Chunk),
            lists:reverse(FirstK) ++ Rest;
        false ->
            lists:reverse(Chunk)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_str(s :: String.t(), k :: integer) :: String.t()
  def reverse_str(s, k) do
    chars = String.to_charlist(s)
    process(chars, k, [])
  end

  defp process([], _k, chunks) do
    chunks
    |> Enum.reverse()
    |> Enum.concat()
    |> List.to_string()
  end

  defp process(list, k, chunks) do
    {chunk, rest} = Enum.split(list, 2 * k)
    {first_k, second_part} = Enum.split(chunk, k)
    new_chunk = :lists.reverse(first_k) ++ second_part
    process(rest, k, [new_chunk | chunks])
  end
end
```
