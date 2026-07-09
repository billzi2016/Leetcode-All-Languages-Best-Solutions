# 2477. Minimum Fuel Cost to Report to the Capital

## Cpp

```cpp
class Solution {
public:
    long long minimumFuelCost(vector<vector<int>>& roads, int seats) {
        int n = roads.size() + 1;
        if (n == 1) return 0;
        vector<vector<int>> adj(n);
        for (auto& e : roads) {
            int a = e[0], b = e[1];
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        vector<int> parent(n, -1);
        vector<int> order;
        order.reserve(n);
        stack<int> st;
        st.push(0);
        parent[0] = 0;
        while (!st.empty()) {
            int u = st.top(); st.pop();
            order.push_back(u);
            for (int v : adj[u]) {
                if (v == parent[u]) continue;
                parent[v] = u;
                st.push(v);
            }
        }
        vector<long long> subtree(n, 1); // each city has one representative
        long long ans = 0;
        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            if (u == 0) continue; // root has no parent edge to count
            int p = parent[u];
            long long cnt = subtree[u];
            ans += (cnt + seats - 1) / seats;
            subtree[p] += cnt;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minimumFuelCost(int[][] roads, int seats) {
        int n = roads.length + 1;
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; ++i) graph[i] = new ArrayList<>();
        for (int[] r : roads) {
            int a = r[0], b = r[1];
            graph[a].add(b);
            graph[b].add(a);
        }
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        int[] order = new int[n];
        int idx = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        while (!stack.isEmpty()) {
            int node = stack.pop();
            order[idx++] = node;
            for (int nb : graph[node]) {
                if (nb == parent[node]) continue;
                parent[nb] = node;
                stack.push(nb);
            }
        }
        long[] size = new long[n];
        Arrays.fill(size, 1L);
        long totalFuel = 0L;
        for (int i = n - 1; i > 0; --i) { // skip root
            int node = order[i];
            int p = parent[node];
            long people = size[node];
            long trips = (people + seats - 1) / seats;
            totalFuel += trips;
            size[p] += people;
        }
        return totalFuel;
    }
}
```

## Python

```python
class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        n = len(roads) + 1
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        import sys
        sys.setrecursionlimit(2000000)

        total = 0

        def dfs(u, parent):
            nonlocal total
            cnt = 1  # representative at city u
            for v in adj[u]:
                if v == parent:
                    continue
                sub = dfs(v, u)
                trips = (sub + seats - 1) // seats
                total += trips  # each trip uses the road (v,u) once
                cnt += sub
            return cnt

        dfs(0, -1)
        return total
```

## Python3

```python
from typing import List
import sys

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        sys.setrecursionlimit(2000000)
        total = 0

        def dfs(u: int, parent: int) -> int:
            nonlocal total
            size = 1  # include the representative at u
            for v in adj[u]:
                if v == parent:
                    continue
                child_size = dfs(v, u)
                total += (child_size + seats - 1) // seats
                size += child_size
            return size

        dfs(0, -1)
        return total
```

## C

```c
#include <stdlib.h>

long long minimumFuelCost(int** roads, int roadsSize, int* roadsColSize, int seats) {
    (void)roadsColSize;
    if (roadsSize == 0) return 0;

    int n = roadsSize + 1;
    int *degree = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < roadsSize; ++i) {
        int a = roads[i][0];
        int b = roads[i][1];
        ++degree[a];
        ++degree[b];
    }

    int **graph = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        graph[i] = (int*)malloc((size_t)degree[i] * sizeof(int));
    }

    int *pos = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < roadsSize; ++i) {
        int a = roads[i][0];
        int b = roads[i][1];
        graph[a][pos[a]++] = b;
        graph[b][pos[b]++] = a;
    }
    free(pos);

    int *parent = (int*)malloc((size_t)n * sizeof(int));
    int *order = (int*)malloc((size_t)n * sizeof(int));
    int *stack = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = -1;

    int top = 0;
    int orderSize = 0;
    stack[top++] = 0;
    parent[0] = 0;
    while (top > 0) {
        int node = stack[--top];
        order[orderSize++] = node;
        for (int i = 0; i < degree[node]; ++i) {
            int next = graph[node][i];
            if (next == parent[node]) continue;
            parent[next] = node;
            stack[top++] = next;
        }
    }

    long long *subtree = (long long*)malloc((size_t)n * sizeof(long long));
    for (int i = 0; i < n; ++i) subtree[i] = 1;

    long long fuel = 0;
    for (int i = orderSize - 1; i > 0; --i) {
        int node = order[i];
        long long people = subtree[node];
        fuel += (people + seats - 1) / seats;
        subtree[parent[node]] += people;
    }

    for (int i = 0; i < n; ++i) free(graph[i]);
    free(graph);
    free(degree);
    free(parent);
    free(order);
    free(stack);
    free(subtree);

    return fuel;
}
```

## Csharp

```csharp
public class Solution {
    public long MinimumFuelCost(int[][] roads, int seats) {
        int n = roads.Length + 1;
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var r in roads) {
            int a = r[0], b = r[1];
            adj[a].Add(b);
            adj[b].Add(a);
        }

        long ans = 0;
        int[] subSize = new int[n];
        var stack = new Stack<(int node, int parent, bool processed)>();
        stack.Push((0, -1, false));

        while (stack.Count > 0) {
            var (node, parent, processed) = stack.Pop();
            if (!processed) {
                stack.Push((node, parent, true));
                foreach (var nb in adj[node]) {
                    if (nb == parent) continue;
                    stack.Push((nb, node, false));
                }
            } else {
                int size = 1; // count the node itself
                foreach (var nb in adj[node]) {
                    if (nb == parent) continue;
                    size += subSize[nb];
                    ans += (subSize[nb] + seats - 1) / seats;
                }
                subSize[node] = size;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} roads
 * @param {number} seats
 * @return {number}
 */
var minimumFuelCost = function(roads, seats) {
    const n = roads.length + 1;
    if (n === 1) return 0;

    const adj = Array.from({ length: n }, () => []);
    for (const [a, b] of roads) {
        adj[a].push(b);
        adj[b].push(a);
    }

    const parent = new Array(n).fill(-1);
    const order = [];
    const stack = [0];
    parent[0] = 0;

    while (stack.length) {
        const node = stack.pop();
        order.push(node);
        for (const nb of adj[node]) {
            if (parent[nb] === -1) {
                parent[nb] = node;
                stack.push(nb);
            }
        }
    }

    const size = new Array(n).fill(1); // each city has one representative
    let fuel = 0;

    for (let i = order.length - 1; i > 0; --i) { // skip root at index 0 after reverse
        const node = order[i];
        const p = parent[node];
        size[p] += size[node];
        fuel += Math.floor((size[node] + seats - 1) / seats);
    }

    return fuel;
};
```

## Typescript

```typescript
function minimumFuelCost(roads: number[][], seats: number): number {
    const n = roads.length + 1;
    if (n === 1) return 0;

    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of roads) {
        adj[a].push(b);
        adj[b].push(a);
    }

    const parent = new Int32Array(n).fill(-1);
    const order: number[] = [];
    const stack: number[] = [0];
    parent[0] = -2; // mark visited

    while (stack.length) {
        const u = stack.pop()!;
        order.push(u);
        for (const v of adj[u]) {
            if (parent[v] === -1) {
                parent[v] = u;
                stack.push(v);
            }
        }
    }

    const subtree = new Int32Array(n);
    for (let i = 0; i < n; ++i) subtree[i] = 1;

    let total = 0;
    for (let i = order.length - 1; i > 0; --i) { // skip root
        const u = order[i];
        const p = parent[u];
        total += Math.floor((subtree[u] + seats - 1) / seats);
        subtree[p] += subtree[u];
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $roads
     * @param Integer $seats
     * @return Integer
     */
    function minimumFuelCost($roads, $seats) {
        $n = count($roads) + 1;
        if ($n == 1) return 0;

        // Build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($roads as $edge) {
            $a = $edge[0];
            $b = $edge[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        // DFS to get parent relationship and order
        $parent = array_fill(0, $n, -1);
        $order = [];
        $stack = [0];
        $parent[0] = -2; // mark root as visited

        while (!empty($stack)) {
            $node = array_pop($stack);
            $order[] = $node;
            foreach ($adj[$node] as $nei) {
                if ($nei === $parent[$node]) continue;
                $parent[$nei] = $node;
                $stack[] = $nei;
            }
        }

        // Post-order processing to compute subtree sizes and fuel cost
        $subSize = array_fill(0, $n, 1);
        $fuel = 0;

        for ($i = count($order) - 1; $i >= 0; $i--) {
            $node = $order[$i];
            foreach ($adj[$node] as $nei) {
                if ($parent[$nei] === $node) { // child
                    $subSize[$node] += $subSize[$nei];
                    $fuel += intdiv($subSize[$nei] + $seats - 1, $seats); // ceil division
                }
            }
        }

        return $fuel;
    }
}
```

## Swift

```swift
class Solution {
    func minimumFuelCost(_ roads: [[Int]], _ seats: Int) -> Int {
        let n = roads.count + 1
        if n == 1 { return 0 }
        
        var adj = Array(repeating: [Int](), count: n)
        for road in roads {
            let a = road[0], b = road[1]
            adj[a].append(b)
            adj[b].append(a)
        }
        
        var parent = Array(repeating: -1, count: n)
        var order = [Int]()
        var stack = [Int]()
        stack.append(0)
        parent[0] = 0
        
        while let node = stack.popLast() {
            order.append(node)
            for nb in adj[node] {
                if parent[nb] == -1 {
                    parent[nb] = node
                    stack.append(nb)
                }
            }
        }
        
        var subtreeSize = Array(repeating: 1, count: n)
        var totalFuel = 0
        
        for node in order.reversed() {
            for nb in adj[node] {
                if parent[nb] == node { // nb is a child of node
                    let size = subtreeSize[nb]
                    totalFuel += (size + seats - 1) / seats   // ceil division
                    subtreeSize[node] += size
                }
            }
        }
        
        return totalFuel
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumFuelCost(roads: Array<IntArray>, seats: Int): Long {
        val n = roads.size + 1
        if (n == 1) return 0L

        val adj = Array(n) { mutableListOf<Int>() }
        for (road in roads) {
            val a = road[0]
            val b = road[1]
            adj[a].add(b)
            adj[b].add(a)
        }

        val parent = IntArray(n) { -1 }
        val order = IntArray(n)
        var idx = 0
        val stack = java.util.ArrayDeque<Int>()
        stack.push(0)
        parent[0] = 0

        while (!stack.isEmpty()) {
            val node = stack.pop()
            order[idx++] = node
            for (nei in adj[node]) {
                if (parent[nei] == -1) {
                    parent[nei] = node
                    stack.push(nei)
                }
            }
        }

        val size = LongArray(n) { 1L }
        var total = 0L
        val s = seats.toLong()
        for (i in n - 1 downTo 1) {
            val node = order[i]
            val p = parent[node]
            total += (size[node] + s - 1) / s
            size[p] += size[node]
        }

        return total
    }
}
```

## Dart

```dart
class Solution {
  int minimumFuelCost(List<List<int>> roads, int seats) {
    int n = roads.length + 1;
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var r in roads) {
      int a = r[0], b = r[1];
      adj[a].add(b);
      adj[b].add(a);
    }

    List<int> parent = List.filled(n, -1);
    List<int> order = [];
    List<int> stack = [0];
    parent[0] = 0; // mark visited

    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      order.add(node);
      for (int nb in adj[node]) {
        if (parent[nb] == -1) {
          parent[nb] = node;
          stack.add(nb);
        }
      }
    }

    List<int> size = List.filled(n, 1);
    int total = 0;

    for (int i = order.length - 1; i >= 0; i--) {
      int node = order[i];
      if (node != 0) {
        int p = parent[node];
        total += ((size[node] + seats - 1) ~/ seats);
        size[p] += size[node];
      }
    }

    return total;
  }
}
```

## Golang

```go
func minimumFuelCost(roads [][]int, seats int) int64 {
    n := len(roads) + 1
    if n == 1 {
        return 0
    }
    adj := make([][]int, n)
    for _, r := range roads {
        a, b := r[0], r[1]
        adj[a] = append(adj[a], b)
        adj[b] = append(adj[b], a)
    }

    parent := make([]int, n)
    for i := 0; i < n; i++ {
        parent[i] = -2
    }
    parent[0] = -1

    stack := []int{0}
    order := make([]int, 0, n)

    for len(stack) > 0 {
        v := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        order = append(order, v)
        for _, nb := range adj[v] {
            if nb == parent[v] {
                continue
            }
            parent[nb] = v
            stack = append(stack, nb)
        }
    }

    size := make([]int64, n)
    ans := int64(0)
    seats64 := int64(seats)

    for i := len(order) - 1; i >= 0; i-- {
        v := order[i]
        sz := int64(1)
        for _, nb := range adj[v] {
            if nb == parent[v] {
                continue
            }
            childSize := size[nb]
            sz += childSize
            trips := (childSize + seats64 - 1) / seats64
            ans += trips
        }
        size[v] = sz
    }

    return ans
}
```

## Ruby

```ruby
def minimum_fuel_cost(roads, seats)
  n = roads.size + 1
  return 0 if n == 1

  adj = Array.new(n) { [] }
  roads.each do |a, b|
    adj[a] << b
    adj[b] << a
  end

  ans = 0
  subtree = Array.new(n, 0)

  stack = [[0, -1, 0]] # node, parent, state (0=pre,1=post)
  while !stack.empty?
    node, parent, state = stack.pop
    if state == 0
      stack << [node, parent, 1]
      adj[node].each do |nbr|
        next if nbr == parent
        stack << [nbr, node, 0]
      end
    else
      cnt = 1
      adj[node].each do |nbr|
        next if nbr == parent
        cnt += subtree[nbr]
        ans += (subtree[nbr] + seats - 1) / seats
      end
      subtree[node] = cnt
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minimumFuelCost(roads: Array[Array[Int]], seats: Int): Long = {
        val n = if (roads.isEmpty) 1 else roads.length + 1
        val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
        for (e <- roads) {
            val a = e(0)
            val b = e(1)
            adj(a).append(b)
            adj(b).append(a)
        }
        var total: Long = 0L
        def dfs(u: Int, parent: Int): Int = {
            var cnt = 1 // include the city itself
            for (v <- adj(u)) {
                if (v != parent) {
                    val sub = dfs(v, u)
                    total += ((sub + seats - 1) / seats).toLong
                    cnt += sub
                }
            }
            cnt
        }
        dfs(0, -1)
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_fuel_cost(roads: Vec<Vec<i32>>, seats: i32) -> i64 {
        let n = roads.len() + 1;
        if n == 1 {
            return 0;
        }
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in &roads {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        // DFS to get parent and order
        let mut parent: Vec<usize> = vec![n; n]; // n as sentinel for "unvisited"
        let mut order: Vec<usize> = Vec::with_capacity(n);
        let mut stack: Vec<usize> = Vec::new();
        stack.push(0);
        parent[0] = 0;
        while let Some(node) = stack.pop() {
            order.push(node);
            for &nbr in &adj[node] {
                if parent[nbr] == n {
                    parent[nbr] = node;
                    stack.push(nbr);
                }
            }
        }

        let seats_i64 = seats as i64;
        let mut cnt: Vec<i64> = vec![1; n]; // each city has one representative
        let mut total: i64 = 0;

        for &node in order.iter().rev() {
            if node == 0 {
                continue;
            }
            let p = parent[node];
            let people = cnt[node];
            let trips = (people + seats_i64 - 1) / seats_i64; // ceil division
            total += trips;
            cnt[p] += people;
        }

        total
    }
}
```

## Racket

```racket
(define/contract (minimum-fuel-cost roads seats)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((n (if (null? roads)
                1
                (let loop ((lst roads) (mx -1))
                  (if (null? lst)
                      (+ mx 1)
                      (let* ((e (car lst))
                             (a (list-ref e 0))
                             (b (list-ref e 1))
                             (new-mx (max mx a b)))
                        (loop (cdr lst) new-mx))))))
         (adj (make-vector n '()))
         (_ (for-each
              (lambda (e)
                (let ((a (list-ref e 0))
                      (b (list-ref e 1)))
                  (vector-set! adj a (cons b (vector-ref adj a)))
                  (vector-set! adj b (cons a (vector-ref adj b)))))
              roads))
         (sizes (make-vector n 0))
         (ans-box (box 0))
         (stack (list (list 0 -1 0)))) ; node parent state
    (let loop ()
      (if (null? stack)
          (unbox ans-box)
          (let* ((cur (car stack))
                 (rest (cdr stack))
                 (node (list-ref cur 0))
                 (parent (list-ref cur 1))
                 (state (list-ref cur 2)))
            (set! stack rest)
            (if (= state 0)
                (begin
                  (set! stack (cons (list node parent 1) stack))
                  (for-each
                    (lambda (nbr)
                      (when (not (= nbr parent))
                        (set! stack (cons (list nbr node 0) stack))))
                    (vector-ref adj node))
                  (loop))
                (begin
                  (let ((child-sum 0))
                    (for-each
                      (lambda (nbr)
                        (when (not (= nbr parent))
                          (let ((csize (vector-ref sizes nbr)))
                            (set-box! ans-box (+ (unbox ans-box)
                                                 (quotient (+ csize seats -1) seats)))
                            (set! child-sum (+ child-sum csize)))))
                      (vector-ref adj node))
                    (vector-set! sizes node (+ 1 child-sum)))
                  (loop))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_fuel_cost/2]).

-spec minimum_fuel_cost(Roads :: [[integer()]], Seats :: integer()) -> integer().
minimum_fuel_cost(Roads, Seats) ->
    Adj = build_adj(Roads),
    {_People, Fuel} = dfs(0, -1, Adj, Seats),
    Fuel.

build_adj(Roads) ->
    lists:foldl(
        fun([A, B], Acc) ->
            Acc1 = maps:update_with(A,
                    fun(L) -> [B | L] end,
                    [B],
                    Acc),
            maps:update_with(B,
                fun(L) -> [A | L] end,
                [A],
                Acc1)
        end,
        #{},
        Roads).

dfs(Node, Parent, Adj, Seats) ->
    Neighbors = maps:get(Node, Adj, []),
    {People, Fuel} = lists:foldl(
        fun(Child, {AccP, AccF}) ->
            if Child == Parent ->
                    {AccP, AccF};
               true ->
                    {ChildP, ChildF} = dfs(Child, Node, Adj, Seats),
                    Cars = (ChildP + Seats - 1) div Seats,
                    NewF = AccF + ChildF + Cars,
                    {AccP + ChildP, NewF}
            end
        end,
        {1, 0},
        Neighbors),
    {People, Fuel}.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_fuel_cost(roads :: [[integer]], seats :: integer) :: integer
  def minimum_fuel_cost(roads, seats) do
    n = length(roads) + 1

    # build adjacency list
    adj =
      Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)
      |> Enum.reduce(roads, fn [a, b], acc ->
        acc
        |> Map.update!(a, fn lst -> [b | lst] end)
        |> Map.update!(b, fn lst -> [a | lst] end)
      end)

    # iterative DFS to get parent map and preorder list
    {parents, preorder} = traverse([{0, -1}], adj, %{}, [])

    # process nodes in postorder (reverse of preorder) to compute fuel
    {_sizes, total} =
      Enum.reduce(Enum.reverse(preorder), {%{}, 0}, fn node, {sz_map, tot} ->
        size = Map.get(sz_map, node, 1)
        par = Map.get(parents, node)

        if par != -1 do
          sz_map = Map.update(sz_map, par, size, &(&1 + size))
          trips = div(size + seats - 1, seats)
          {sz_map, tot + trips}
        else
          {sz_map, tot}
        end
      end)

    total
  end

  defp traverse([], _adj, parents, order), do: {parents, order}

  defp traverse([{node, par} | rest], adj, parents, order) do
    parents = Map.put(parents, node, par)
    order = [node | order]
    neighbors = Map.get(adj, node, [])

    new_stack =
      Enum.reduce(neighbors, rest, fn nb, acc ->
        if nb != par, do: [{nb, node} | acc], else: acc
      end)

    traverse(new_stack, adj, parents, order)
  end
end
```
