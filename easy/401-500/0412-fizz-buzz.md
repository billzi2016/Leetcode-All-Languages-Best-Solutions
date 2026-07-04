# 0412. Fizz Buzz

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> ans;
        ans.reserve(n);
        for (int i = 1; i <= n; ++i) {
            bool div3 = (i % 3 == 0);
            bool div5 = (i % 5 == 0);
            if (div3 && div5) ans.push_back("FizzBuzz");
            else if (div3) ans.push_back("Fizz");
            else if (div5) ans.push_back("Buzz");
            else ans.push_back(to_string(i));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> ans = new ArrayList<>(n);
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                ans.add("FizzBuzz");
            } else if (i % 3 == 0) {
                ans.add("Fizz");
            } else if (i % 5 == 0) {
                ans.add("Buzz");
            } else {
                ans.add(Integer.toString(i));
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
```

## Python3

```python
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) {
    char **res = (char **)malloc(n * sizeof(char *));
    *returnSize = n;
    for (int i = 1; i <= n; ++i) {
        if (i % 15 == 0) {
            res[i - 1] = strdup("FizzBuzz");
        } else if (i % 3 == 0) {
            res[i - 1] = strdup("Fizz");
        } else if (i % 5 == 0) {
            res[i - 1] = strdup("Buzz");
        } else {
            char buf[12];
            int len = snprintf(buf, sizeof(buf), "%d", i);
            res[i - 1] = (char *)malloc(len + 1);
            strcpy(res[i - 1], buf);
        }
    }
    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<string> FizzBuzz(int n) {
        var result = new List<string>(n);
        for (int i = 1; i <= n; i++) {
            string s = "";
            if (i % 3 == 0) s += "Fizz";
            if (i % 5 == 0) s += "Buzz";
            if (s.Length == 0) s = i.ToString();
            result.Add(s);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    const result = [];
    for (let i = 1; i <= n; i++) {
        if (i % 15 === 0) {
            result.push("FizzBuzz");
        } else if (i % 3 === 0) {
            result.push("Fizz");
        } else if (i % 5 === 0) {
            result.push("Buzz");
        } else {
            result.push(i.toString());
        }
    }
    return result;
};
```

## Typescript

```typescript
function fizzBuzz(n: number): string[] {
    const result: string[] = [];
    for (let i = 1; i <= n; i++) {
        if (i % 15 === 0) {
            result.push("FizzBuzz");
        } else if (i % 3 === 0) {
            result.push("Fizz");
        } else if (i % 5 === 0) {
            result.push("Buzz");
        } else {
            result.push(i.toString());
        }
    }
    return result;
};
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return String[]
     */
    function fizzBuzz($n) {
        $result = [];
        for ($i = 1; $i <= $n; $i++) {
            $s = '';
            if ($i % 3 == 0) {
                $s .= 'Fizz';
            }
            if ($i % 5 == 0) {
                $s .= 'Buzz';
            }
            if ($s === '') {
                $s = (string)$i;
            }
            $result[] = $s;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func fizzBuzz(_ n: Int) -> [String] {
        var result = [String]()
        for i in 1...n {
            if i % 15 == 0 {
                result.append("FizzBuzz")
            } else if i % 3 == 0 {
                result.append("Fizz")
            } else if i % 5 == 0 {
                result.append("Buzz")
            } else {
                result.append(String(i))
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun fizzBuzz(n: Int): List<String> {
        val result = ArrayList<String>(n)
        for (i in 1..n) {
            when {
                i % 15 == 0 -> result.add("FizzBuzz")
                i % 3 == 0 -> result.add("Fizz")
                i % 5 == 0 -> result.add("Buzz")
                else -> result.add(i.toString())
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> fizzBuzz(int n) {
    List<String> ans = [];
    for (int i = 1; i <= n; i++) {
      bool div3 = i % 3 == 0;
      bool div5 = i % 5 == 0;
      if (div3 && div5) {
        ans.add('FizzBuzz');
      } else if (div3) {
        ans.add('Fizz');
      } else if (div5) {
        ans.add('Buzz');
      } else {
        ans.add(i.toString());
      }
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "strconv"

func fizzBuzz(n int) []string {
	res := make([]string, n)
	for i := 1; i <= n; i++ {
		switch {
		case i%15 == 0:
			res[i-1] = "FizzBuzz"
		case i%3 == 0:
			res[i-1] = "Fizz"
		case i%5 == 0:
			res[i-1] = "Buzz"
		default:
			res[i-1] = strconv.Itoa(i)
		}
	}
	return res
}
```

## Ruby

```ruby
def fizz_buzz(n)
  result = []
  (1..n).each do |i|
    if i % 15 == 0
      result << "FizzBuzz"
    elsif i % 3 == 0
      result << "Fizzz"
    elsif i % 5 == 0
      result << "Buzz"
    else
      result << i.to_s
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def fizzBuzz(n: Int): List[String] = {
        (1 to n).map { i =>
            if (i % 15 == 0) "FizzBuzz"
            else if (i % 3 == 0) "Fizz"
            else if (i % 5 == 0) "Buzz"
            else i.toString
        }.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut result = Vec::with_capacity(n as usize);
        for i in 1..=n {
            let s = match (i % 3 == 0, i % 5 == 0) {
                (true, true) => "FizzBuzz".to_string(),
                (true, false) => "Fizz".to_string(),
                (false, true) => "Buzz".to_string(),
                _ => i.to_string(),
            };
            result.push(s);
        }
        result
    }
}
```

## Racket

```racket
#lang racket
(define/contract (fizz-buzz n)
  (-> exact-integer? (listof string?))
  (for/list ([i (in-range 1 (+ n 1))])
    (cond [(zero? (modulo i 15)) "FizzBuzz"]
          [(zero? (modulo i 3)) "Fizz"]
          [(zero? (modulo i 5)) "Buzz"]
          [else (number->string i)])))
```

## Erlang

```erlang
-module(solution).
-export([fizz_buzz/1]).

-spec fizz_buzz(N :: integer()) -> [unicode:unicode_binary()].
fizz_buzz(N) when is_integer(N), N >= 0 ->
    [ fizz_item(I) || I <- lists:seq(1, N) ].

fizz_item(I) ->
    case {I rem 3, I rem 5} of
        {0,0} -> <<"FizzBuzz">>;
        {0,_} -> <<"Fizz">>;
        {_,0} -> <<"Buzz">>;
        _     -> integer_to_binary(I)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec fizz_buzz(n :: integer) :: [String.t()]
  def fizz_buzz(n) when is_integer(n) and n >= 1 do
    1..n
    |> Enum.map(fn i ->
      cond do
        rem(i, 15) == 0 -> "FizzBuzz"
        rem(i, 3) == 0 -> "Fizz"
        rem(i, 5) == 0 -> "Buzz"
        true -> Integer.to_string(i)
      end
    end)
  end
end
```
