# 0455. Assign Cookies

## Cpp

```cpp
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int child = 0, cookie = 0;
        while (child < (int)g.size() && cookie < (int)s.size()) {
            if (s[cookie] >= g[child]) ++child;
            ++cookie;
        }
        return child;
    }
};
```

## Java

```java
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        java.util.Arrays.sort(g);
        java.util.Arrays.sort(s);
        int child = 0, cookie = 0;
        while (child < g.length && cookie < s.length) {
            if (s[cookie] >= g[child]) {
                child++;
            }
            cookie++;
        }
        return child;
    }
}
```

## Python

```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i
```

## Python3

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        for size in s:
            if child < len(g) and size >= g[child]:
                child += 1
        return child
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

int findContentChildren(int* g, int gSize, int* s, int sSize) {
    if (gSize == 0 || sSize == 0) return 0;
    qsort(g, (size_t)gSize, sizeof(int), cmp_int);
    qsort(s, (size_t)sSize, sizeof(int), cmp_int);
    
    int i = 0, j = 0, count = 0;
    while (i < gSize && j < sSize) {
        if (s[j] >= g[i]) {
            ++count;
            ++i;
        }
        ++j;
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindContentChildren(int[] g, int[] s)
    {
        if (g == null || s == null) return 0;
        System.Array.Sort(g);
        System.Array.Sort(s);
        int child = 0, cookie = 0;
        while (child < g.Length && cookie < s.Length)
        {
            if (s[cookie] >= g[child])
            {
                child++;
            }
            cookie++;
        }
        return child;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);
    let i = 0, j = 0, content = 0;
    while (i < g.length && j < s.length) {
        if (s[j] >= g[i]) {
            content++;
            i++;
        }
        j++;
    }
    return content;
};
```

## Typescript

```typescript
function findContentChildren(g: number[], s: number[]): number {
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);
    let i = 0, j = 0, content = 0;
    while (i < g.length && j < s.length) {
        if (s[j] >= g[i]) {
            content++;
            i++;
        }
        j++;
    }
    return content;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $g
     * @param Integer[] $s
     * @return Integer
     */
    function findContentChildren($g, $s) {
        sort($g);
        sort($s);
        $i = 0;
        $j = 0;
        $content = 0;
        $n = count($g);
        $m = count($s);
        while ($i < $n && $j < $m) {
            if ($s[$j] >= $g[$i]) {
                $content++;
                $i++;
                $j++;
            } else {
                $j++;
            }
        }
        return $content;
    }
}
```

## Swift

```swift
class Solution {
    func findContentChildren(_ g: [Int], _ s: [Int]) -> Int {
        let children = g.sorted()
        let cookies = s.sorted()
        var childIndex = 0
        var cookieIndex = 0
        
        while childIndex < children.count && cookieIndex < cookies.count {
            if cookies[cookieIndex] >= children[childIndex] {
                childIndex += 1
            }
            cookieIndex += 1
        }
        
        return childIndex
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findContentChildren(g: IntArray, s: IntArray): Int {
        g.sort()
        s.sort()
        var child = 0
        var cookie = 0
        while (child < g.size && cookie < s.size) {
            if (s[cookie] >= g[child]) {
                child++
            }
            cookie++
        }
        return child
    }
}
```

## Dart

```dart
class Solution {
  int findContentChildren(List<int> g, List<int> s) {
    g.sort();
    s.sort();
    int i = 0, j = 0, content = 0;
    while (i < g.length && j < s.length) {
      if (s[j] >= g[i]) {
        content++;
        i++;
      }
      j++;
    }
    return content;
  }
}
```

## Golang

```go
func findContentChildren(g []int, s []int) int {
    if len(g) == 0 || len(s) == 0 {
        return 0
    }
    sort.Ints(g)
    sort.Ints(s)

    childIdx, cookieIdx := 0, 0
    for childIdx < len(g) && cookieIdx < len(s) {
        if s[cookieIdx] >= g[childIdx] {
            childIdx++
        }
        cookieIdx++
    }
    return childIdx
}
```

## Ruby

```ruby
def find_content_children(g, s)
  g.sort!
  s.sort!
  child = 0
  cookie = 0
  while child < g.length && cookie < s.length
    if s[cookie] >= g[child]
      child += 1
    end
    cookie += 1
  end
  child
end
```

## Scala

```scala
object Solution {
    def findContentChildren(g: Array[Int], s: Array[Int]): Int = {
        java.util.Arrays.sort(g)
        java.util.Arrays.sort(s)
        var child = 0
        var cookie = 0
        while (child < g.length && cookie < s.length) {
            if (s(cookie) >= g(child)) {
                child += 1
            }
            cookie += 1
        }
        child
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_content_children(mut g: Vec<i32>, mut s: Vec<i32>) -> i32 {
        g.sort_unstable();
        s.sort_unstable();
        let (mut child, mut cookie) = (0usize, 0usize);
        let mut satisfied = 0;
        while child < g.len() && cookie < s.len() {
            if s[cookie] >= g[child] {
                satisfied += 1;
                child += 1;
            }
            cookie += 1;
        }
        satisfied as i32
    }
}
```

## Racket

```racket
(define/contract (find-content-children g s)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((g-sorted (sort g <))
         (s-sorted (sort s <)))
    (let loop ((i 0) (j 0) (cnt 0))
      (cond
        [(or (= i (length g-sorted)) (= j (length s-sorted))) cnt]
        [(>= (list-ref s-sorted j) (list-ref g-sorted i))
         (loop (+ i 1) (+ j 1) (+ cnt 1))]
        [else
         (loop i (+ j 1) cnt)]))))
```

## Erlang

```erlang
-module(solution).
-export([find_content_children/2]).

-spec find_content_children(G :: [integer()], S :: [integer()]) -> integer().
find_content_children(G, S) ->
    GSorted = lists:sort(G),
    SSorted = lists:sort(S),
    assign(GSorted, SSorted).

assign([], _) -> 0;
assign(_, []) -> 0;
assign([Gh|Gt], [Sh|St]) when Sh >= Gh ->
    1 + assign(Gt, St);
assign(G, [_Sh|St]) ->
    assign(G, St).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_content_children(g :: [integer], s :: [integer]) :: integer
  def find_content_children(g, s) do
    g = Enum.sort(g)
    s = Enum.sort(s)
    assign(g, s, 0)
  end

  defp assign([], _cookies, count), do: count
  defp assign(_children, [], count), do: count

  defp assign([child_greed | rest_children] = children, [cookie_size | rest_cookies], count) do
    if cookie_size >= child_greed do
      assign(rest_children, rest_cookies, count + 1)
    else
      assign(children, rest_cookies, count)
    end
  end
end
```
