# 2920. Maximum Points After Collecting Coins From All Nodes

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumPoints(vector<vector<int>>& edges, vector<int>& coins, int k) {
        int n = coins.size();
        const int MAX_T = 14; // 2^14 > 10000
        vector<vector<int>> g(n);
        for (auto &e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        vector<int> parent(n, -1), order;
        order.reserve(n);
        stack<int> st;
        st.push(0);
        parent[0] = 0;
        while (!st.empty()) {
            int u = st.top(); st.pop();
            order.push_back(u);
            for (int v : g[u]) if (parent[v] == -1) {
                parent[v] = u;
                st.push(v);
            }
        }

        vector<array<long long, MAX_T + 2>> dp(n);
        // initialize all to 0
        for (int idx = n - 1; idx >= 0; --idx) {
            int u = order[idx];
            for (int t = 0; t <= MAX_T; ++t) {
                long long val_t = (coins[u] >> t);
                long long opt1 = val_t - k;
                long long opt2 = (coins[u] >> (t + 1));
                for (int v : g[u]) if (parent[v] == u) {
                    opt1 += dp[v][t];
                    int nt = t + 1;
                    if (nt > MAX_T) nt = MAX_T;
                    opt2 += dp[v][nt];
                }
                dp[u][t] = max(opt1, opt2);
            }
            // for safety fill the extra slot MAX_T+1 as same as MAX_T
            dp[u][MAX_T + 1] = dp[u][MAX_T];
        }
        return (int)dp[0][0];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maximumPoints(int[][] edges, int[] coins, int k) {
        int n = coins.length;
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; ++i) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        // Determine maximum shift needed
        int maxCoin = 0;
        for (int c : coins) if (c > maxCoin) maxCoin = c;
        int maxShift = 0;
        while ((maxCoin >> maxShift) > 0) ++maxShift; // value becomes zero after this shift
        int MAX_T = maxShift + 2; // extra margin

        // Build parent array and traversal order (preorder)
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        int[] order = new int[n];
        int idx = 0;
        int[] stack = new int[n];
        int sp = 0;
        stack[sp++] = 0;
        parent[0] = -2; // root marker
        while (sp > 0) {
            int node = stack[--sp];
            order[idx++] = node;
            for (int nb : graph[node]) {
                if (parent[nb] == -1) {
                    parent[nb] = node;
                    stack[sp++] = nb;
                }
            }
        }

        long[][] dp = new long[n][MAX_T + 1];

        // Process nodes in post-order
        for (int i = n - 1; i >= 0; --i) {
            int x = order[i];
            for (int t = 0; t <= MAX_T; ++t) {
                long sumFirst = 0;
                long sumSecond = 0;
                for (int nb : graph[x]) {
                    if (parent[nb] == x) { // child
                        sumFirst += dp[nb][t];
                        int tp = t + 1;
                        if (tp <= MAX_T) sumSecond += dp[nb][tp];
                    }
                }
                long optA = ((long) (coins[x] >> t)) - k + sumFirst;
                long optB = ((long) (coins[x] >> (t + 1))) + sumSecond;
                dp[x][t] = Math.max(optA, optB);
            }
        }

        return (int) dp[0][0];
    }
}
```

## Python

```python
class Solution(object):
    def maximumPoints(self, edges, coins, k):
        """
        :type edges: List[List[int]]
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        n = len(coins)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        MAX_T = 14  # since coins[i] <= 10^4 < 2^14
        dp = [[0] * (MAX_T + 1) for _ in range(n)]

        stack = [(0, -1, 0)]  # node, parent, state (0=pre,1=post)
        while stack:
            node, parent, state = stack.pop()
            if state == 0:
                stack.append((node, parent, 1))
                for nb in g[node]:
                    if nb != parent:
                        stack.append((nb, node, 0))
            else:
                children = [c for c in g[node] if c != parent]
                # compute dp for this node
                for t in range(MAX_T - 1, -1, -1):
                    sum_same = 0
                    sum_next = 0
                    for ch in children:
                        child_dp = dp[ch]
                        sum_same += child_dp[t]
                        sum_next += child_dp[t + 1]  # t+1 <= MAX_T
                    opt1 = (coins[node] >> t) - k + sum_same
                    opt2 = (coins[node] >> (t + 1)) + sum_next
                    dp[node][t] = max(opt1, opt2)
                dp[node][MAX_T] = 0  # already zero but explicit

        return dp[0][0]
```

## Python3

```python
import sys
from typing import List

sys.setrecursionlimit(300000)

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        MAX_T = 15  # since 2^15 > 10^4

        def dfs(u: int, parent: int) -> List[int]:
            child_dps = []
            for v in adj[u]:
                if v == parent:
                    continue
                child_dps.append(dfs(v, u))

            dp = [0] * (MAX_T + 1)
            # compute from larger t to smaller (order not important but fine)
            for t in range(MAX_T, -1, -1):
                sum_first = 0
                sum_second = 0
                for cd in child_dps:
                    sum_first += cd[t]
                    if t + 1 <= MAX_T:
                        sum_second += cd[t + 1]
                opt1 = (coins[u] >> t) - k + sum_first
                opt2 = (coins[u] >> (t + 1)) + sum_second if t + 1 <= MAX_T else sum_second
                dp[t] = max(opt1, opt2)
            return dp

        return dfs(0, -1)[0]
```

## C

```c
#include <stdlib.h>

int maximumPoints(int** edges, int edgesSize, int* edgesColSize, int* coins, int coinsSize, int k) {
    (void)edgesColSize;

    const int MAX_SHIFT = 15;
    const int DP_COLS = MAX_SHIFT + 2;
    int n = coinsSize;

    int *degree = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        ++degree[a];
        ++degree[b];
    }

    int **graph = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        graph[i] = (int*)malloc((size_t)degree[i] * sizeof(int));
    }

    int *pos = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        graph[a][pos[a]++] = b;
        graph[b][pos[b]++] = a;
    }
    free(pos);

    int *parent = (int*)malloc((size_t)n * sizeof(int));
    int *order = (int*)malloc((size_t)n * sizeof(int));
    int *stack = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = -2;

    int top = 0;
    int orderSize = 0;
    stack[top++] = 0;
    parent[0] = -1;
    while (top > 0) {
        int node = stack[--top];
        order[orderSize++] = node;
        for (int i = 0; i < degree[node]; ++i) {
            int next = graph[node][i];
            if (parent[next] != -2) continue;
            parent[next] = node;
            stack[top++] = next;
        }
    }

    long long *dp = (long long*)calloc((size_t)n * DP_COLS, sizeof(long long));
    for (int idx = orderSize - 1; idx >= 0; --idx) {
        int node = order[idx];
        for (int shift = MAX_SHIFT; shift >= 0; --shift) {
            long long takeNow = ((long long)coins[node] >> shift) - k;
            long long halveFirst = (long long)coins[node] >> (shift + 1);

            for (int i = 0; i < degree[node]; ++i) {
                int child = graph[node][i];
                if (parent[child] != node) continue;
                takeNow += dp[(size_t)child * DP_COLS + shift];
                halveFirst += dp[(size_t)child * DP_COLS + shift + 1];
            }

            dp[(size_t)node * DP_COLS + shift] = takeNow > halveFirst ? takeNow : halveFirst;
        }
    }

    int answer = (int)dp[0];

    for (int i = 0; i < n; ++i) free(graph[i]);
    free(graph);
    free(degree);
    free(parent);
    free(order);
    free(stack);
    free(dp);

    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumPoints(int[][] edges, int[] coins, int k) {
        int n = coins.Length;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        int[] parent = new int[n];
        Array.Fill(parent, -1);
        var order = new List<int>(n);
        var stack = new Stack<int>();
        stack.Push(0);
        parent[0] = 0;
        while (stack.Count > 0) {
            int node = stack.Pop();
            order.Add(node);
            foreach (int nb in graph[node]) {
                if (parent[nb] == -1) {
                    parent[nb] = node;
                    stack.Push(nb);
                }
            }
        }

        const int MAX_T = 15; // enough because coins[i] <= 10^4 < 2^14
        long[,] dp = new long[n, MAX_T + 1];

        for (int idx = order.Count - 1; idx >= 0; idx--) {
            int node = order[idx];
            for (int t = 0; t <= MAX_T; t++) {
                long sumSame = 0;
                long sumInc = 0;
                foreach (int child in graph[node]) {
                    if (child == parent[node]) continue;
                    sumSame += dp[child, t];
                    int tp = t + 1 > MAX_T ? MAX_T : t + 1;
                    sumInc += dp[child, tp];
                }
                long opt1 = ((long)coins[node] >> t) - k + sumSame;
                long opt2 = ((long)coins[node] >> (t + 1)) + sumInc;
                dp[node, t] = Math.Max(opt1, opt2);
            }
        }

        return (int)dp[0, 0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[]} coins
 * @param {number} k
 * @return {number}
 */
var maximumPoints = function(edges, coins, k) {
    const n = coins.length;
    const adj = Array.from({length: n}, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    // Build parent array and order for post‑order traversal
    const parent = new Int32Array(n).fill(-1);
    const order = [];
    const stack = [0];
    parent[0] = -2; // mark root visited
    while (stack.length) {
        const u = stack.pop();
        order.push(u);
        for (const v of adj[u]) {
            if (parent[v] === -1) {
                parent[v] = u;
                stack.push(v);
            }
        }
    }

    const LIM = 15; // enough because coins[i] <= 10^4 < 2^14
    const dp = Array.from({length: n}, () => new Array(LIM + 2).fill(0));

    for (let idx = order.length - 1; idx >= 0; --idx) {
        const u = order[idx];
        // sum[t] = Σ child dp[child][t]
        const sum = new Array(LIM + 2).fill(0);
        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            const childDP = dp[v];
            for (let t = 0; t <= LIM; ++t) {
                sum[t] += childDP[t];
            }
        }

        const cur = dp[u];
        const coinU = coins[u];
        for (let t = 0; t <= LIM; ++t) {
            const opt1 = (coinU >> t) - k + sum[t];
            const opt2 = (coinU >> (t + 1)) + sum[t + 1];
            cur[t] = opt1 > opt2 ? opt1 : opt2;
        }
    }

    return dp[0][0];
};
```

## Typescript

```typescript
function maximumPoints(edges: number[][], coins: number[], k: number): number {
    const n = coins.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // Build parent array and traversal order (preorder)
    const parent = new Int32Array(n).fill(-1);
    const order: number[] = [];
    const stack: number[] = [0];
    parent[0] = 0;
    while (stack.length) {
        const node = stack.pop()!;
        order.push(node);
        for (const nb of adj[node]) {
            if (parent[nb] === -1) {
                parent[nb] = node;
                stack.push(nb);
            }
        }
    }

    const MAX_T = 14; // because 2^14 > 10000
    const dp: number[][] = new Array(n);

    for (let i = order.length - 1; i >= 0; --i) {
        const node = order[i];
        const sum = new Array(MAX_T + 2).fill(0);
        for (const nb of adj[node]) {
            if (parent[nb] === node) {
                const childDP = dp[nb];
                for (let t = 0; t <= MAX_T + 1; ++t) {
                    sum[t] += childDP[t];
                }
            }
        }

        const cur = new Array(MAX_T + 2).fill(0);
        const coin = coins[node];
        for (let t = 0; t <= MAX_T; ++t) {
            const takeFirst = (coin >> t) - k + sum[t];
            const takeSecond = (coin >> (t + 1)) + sum[t + 1];
            cur[t] = Math.max(takeFirst, takeSecond);
        }
        // cur[MAX_T+1] stays 0
        dp[node] = cur;
    }

    return dp[0][0];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $edges
     * @param Integer[] $coins
     * @param Integer $k
     * @return Integer
     */
    function maximumPoints($edges, $coins, $k) {
        $n = count($coins);
        // build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        // parent and order (DFS stack)
        $parent = array_fill(0, $n, -1);
        $order = [];
        $stack = [0];
        $parent[0] = -2; // root marker
        while (!empty($stack)) {
            $u = array_pop($stack);
            $order[] = $u;
            foreach ($adj[$u] as $v) {
                if ($v === $parent[$u]) continue;
                $parent[$v] = $u;
                $stack[] = $v;
            }
        }

        // limit for number of halvings (2^14 > 10000)
        $LIMIT = 14;
        $SIZE = $LIMIT + 2; // extra slot for t+1 access

        // dp storage per node
        $dpAll = array_fill(0, $n, null);

        // process nodes in post-order
        for ($idx = count($order) - 1; $idx >= 0; --$idx) {
            $u = $order[$idx];
            $sumSame = array_fill(0, $SIZE, 0);
            $sumNext = array_fill(0, $SIZE, 0);

            foreach ($adj[$u] as $v) {
                if ($parent[$v] !== $u) continue; // only children
                $childDP = $dpAll[$v];
                for ($t = 0; $t <= $LIMIT; ++$t) {
                    $sumSame[$t] += $childDP[$t];
                    $sumNext[$t] += $childDP[$t + 1];
                }
            }

            $dpNode = array_fill(0, $SIZE, 0);
            for ($t = 0; $t <= $LIMIT; ++$t) {
                $val1 = ($coins[$u] >> $t) - $k + $sumSame[$t];
                $val2 = ($coins[$u] >> ($t + 1)) + $sumNext[$t];
                $dpNode[$t] = ($val1 > $val2) ? $val1 : $val2;
            }
            // values for t > LIMIT remain 0 (already set)
            $dpAll[$u] = $dpNode;
        }

        return $dpAll[0][0];
    }
}
```

## Swift

```swift
class Solution {
    func maximumPoints(_ edges: [[Int]], _ coins: [Int], _ k: Int) -> Int {
        let n = coins.count
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let a = e[0], b = e[1]
            adj[a].append(b)
            adj[b].append(a)
        }
        
        var parent = [Int](repeating: -1, count: n)
        var children = [[Int]](repeating: [], count: n)
        var order = [Int]()
        var stack = [0]
        parent[0] = 0
        while let node = stack.popLast() {
            order.append(node)
            for nb in adj[node] {
                if parent[nb] == -1 {
                    parent[nb] = node
                    children[node].append(nb)
                    stack.append(nb)
                }
            }
        }
        
        let maxT = 15   // enough because coins[i] <= 10^4
        var dp = [[Int]](repeating: [Int](repeating: 0, count: maxT + 1), count: n)
        
        for node in order.reversed() {
            for t in 0...maxT {
                var sumSame = 0
                var sumNext = 0
                let nextIdx = min(t + 1, maxT)
                for child in children[node] {
                    sumSame += dp[child][t]
                    sumNext += dp[child][nextIdx]
                }
                let firstVal = (coins[node] >> t) - k + sumSame
                let secondVal = (coins[node] >> (t + 1)) + sumNext
                dp[node][t] = max(firstVal, secondVal)
            }
        }
        
        return dp[0][0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumPoints(edges: Array<IntArray>, coins: IntArray, k: Int): Int {
        val n = coins.size
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            adj[b].add(a)
        }
        val parent = IntArray(n) { -1 }
        val order = IntArray(n)
        var idx = 0
        val stack = java.util.ArrayDeque<Int>()
        stack.add(0)
        parent[0] = 0
        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            order[idx++] = node
            for (nei in adj[node]) {
                if (parent[nei] == -1) {
                    parent[nei] = node
                    stack.add(nei)
                }
            }
        }

        val LIM = 15 // enough because coins[i] <= 10^4
        val dp = Array(n) { IntArray(LIM + 2) } // extra slot for t+1 beyond LIM

        for (i in n - 1 downTo 0) {
            val x = order[i]
            val sumSame = IntArray(LIM + 2)
            val sumNext = IntArray(LIM + 2)

            for (child in adj[x]) {
                if (parent[child] == x) {
                    val childDp = dp[child]
                    for (t in 0..LIM) {
                        sumSame[t] += childDp[t]
                        sumNext[t] += childDp[t + 1]
                    }
                }
            }

            for (t in 0..LIM) {
                val opt1 = (coins[x] ushr t) - k + sumSame[t]
                val opt2 = (coins[x] ushr (t + 1)) + sumNext[t]
                dp[x][t] = if (opt1 > opt2) opt1 else opt2
            }
        }

        return dp[0][0]
    }
}
```

## Dart

```dart
class Solution {
  int maximumPoints(List<List<int>> edges, List<int> coins, int k) {
    int n = coins.length;
    const int maxT = 15; // enough because coins[i] <= 1e4
    List<List<int>> g = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0], b = e[1];
      g[a].add(b);
      g[b].add(a);
    }

    // Build parent array and traversal order using stack (iterative DFS)
    List<int> parent = List.filled(n, -1);
    List<int> order = [];
    List<int> stack = [0];
    parent[0] = 0;
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      order.add(node);
      for (int nb in g[node]) {
        if (nb == parent[node]) continue;
        parent[nb] = node;
        stack.add(nb);
      }
    }

    // dp[node][t] where t in [0, maxT]
    List<List<int>> dp = List.generate(n, (_) => List.filled(maxT + 1, 0));

    // Process nodes in post-order (reverse of order)
    for (int idx = order.length - 1; idx >= 0; --idx) {
      int node = order[idx];
      // sumChild[t] = sum over children dp[child][t]
      List<int> sumChild = List.filled(maxT + 1, 0);
      for (int nb in g[node]) {
        if (nb == parent[node]) continue;
        for (int t = 0; t <= maxT; ++t) {
          sumChild[t] += dp[nb][t];
        }
      }

      int coinVal = coins[node];
      for (int t = 0; t <= maxT; ++t) {
        int optA = (coinVal >> t) - k + sumChild[t];
        int nextT = t + 1;
        if (nextT > maxT) nextT = maxT;
        int optB = (coinVal >> nextT) + sumChild[nextT];
        dp[node][t] = optA > optB ? optA : optB;
      }
    }

    return dp[0][0];
  }
}
```

## Golang

```go
func maximumPoints(edges [][]int, coins []int, k int) int {
    n := len(coins)
    adj := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        adj[a] = append(adj[a], b)
        adj[b] = append(adj[b], a)
    }

    const maxT = 14 // enough because coins[i] <= 10^4
    var dfs func(int, int) []int64
    dfs = func(u, parent int) []int64 {
        sums := make([]int64, maxT+1)
        for _, v := range adj[u] {
            if v == parent {
                continue
            }
            childDP := dfs(v, u)
            for t := 0; t <= maxT; t++ {
                sums[t] += childDP[t]
            }
        }

        dp := make([]int64, maxT+1)
        coinVal := int64(coins[u])
        kVal := int64(k)

        for t := 0; t <= maxT; t++ {
            // First way: collect now, pay k
            val1 := (coinVal >> uint(t)) - kVal + sums[t]

            // Second way: apply division by 2, no cost, increase shift for children
            var shifted int64
            if t+1 <= maxT {
                shifted = coinVal >> uint(t+1)
            }
            var sumChild int64
            if t+1 <= maxT {
                sumChild = sums[t+1]
            }
            val2 := shifted + sumChild

            if val1 > val2 {
                dp[t] = val1
            } else {
                dp[t] = val2
            }
        }
        return dp
    }

    rootDP := dfs(0, -1)
    return int(rootDP[0])
}
```

## Ruby

```ruby
def maximum_points(edges, coins, k)
  n = coins.length
  adj = Array.new(n) { [] }
  edges.each do |a, b|
    adj[a] << b
    adj[b] << a
  end

  parent = Array.new(n, -1)
  order = []
  stack = [0]
  parent[0] = -2
  until stack.empty?
    node = stack.pop
    order << node
    adj[node].each do |nbr|
      next if nbr == parent[node]
      parent[nbr] = node
      stack << nbr
    end
  end

  lim = 15 # t = 0..14, shift >=14 yields zero for max coin 10^4
  dp = Array.new(n) { Array.new(lim, 0) }

  order.reverse_each do |node|
    children = adj[node].reject { |v| v == parent[node] }
    cur = Array.new(lim, 0)
    (lim - 1).downto(0) do |t|
      sum0 = 0
      sum1 = 0
      children.each do |ch|
        child_dp = dp[ch]
        sum0 += child_dp[t] if t < lim
        sum1 += child_dp[t + 1] if (t + 1) < lim
      end
      val1 = (coins[node] >> t) - k + sum0
      val2 = (coins[node] >> (t + 1)) + sum1
      cur[t] = val1 > val2 ? val1 : val2
    end
    dp[node] = cur
  end

  dp[0][0]
end
```

## Scala

```scala
object Solution {
  def maximumPoints(edges: Array[Array[Int]], coins: Array[Int], k: Int): Int = {
    val n = coins.length
    val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      adj(a).append(b)
      adj(b).append(a)
    }

    // Build parent array and traversal order using stack (iterative DFS)
    val parent = Array.fill(n)(-1)
    val order = scala.collection.mutable.ArrayBuffer.empty[Int]
    val stack = new java.util.ArrayDeque[Int]()
    stack.push(0)
    parent(0) = -2
    while (!stack.isEmpty) {
      val u = stack.pop()
      order.append(u)
      for (v <- adj(u)) {
        if (parent(v) == -1) {
          parent(v) = u
          stack.push(v)
        }
      }
    }

    // Maximum number of halvings needed (log2(10000) < 14)
    val MAX_T = 15
    val dp = Array.ofDim[Long](n, MAX_T + 2) // extra column for t+1 safety

    // Process nodes in post-order
    var idx = order.length - 1
    while (idx >= 0) {
      val u = order(idx)
      val sum = new Array[Long](MAX_T + 2)

      // accumulate children's dp values
      for (v <- adj(u)) {
        if (parent(v) == u) { // v is a child of u
          var t = 0
          while (t <= MAX_T) {
            sum(t) += dp(v)(t)
            t += 1
          }
        }
      }

      var t = 0
      while (t <= MAX_T) {
        val coinShiftT   = (coins(u) >> t).toLong
        val option1 = coinShiftT - k + sum(t)

        val coinShiftTp1 = (coins(u) >> (t + 1)).toLong
        val option2 = coinShiftTp1 + sum(t + 1)

        dp(u)(t) = if (option1 > option2) option1 else option2
        t += 1
      }

      idx -= 1
    }

    dp(0)(0).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_points(edges: Vec<Vec<i32>>, coins: Vec<i32>, k: i32) -> i32 {
        let n = coins.len();
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        // Build parent array and traversal order (preorder)
        let mut parent: Vec<usize> = vec![usize::MAX; n];
        let mut order: Vec<usize> = Vec::with_capacity(n);
        let mut stack: Vec<usize> = Vec::new();
        stack.push(0);
        parent[0] = 0;
        while let Some(u) = stack.pop() {
            order.push(u);
            for &v in adj[u].iter() {
                if v != parent[u] {
                    parent[v] = u;
                    stack.push(v);
                }
            }
        }

        // Maximum t needed (since coins[i] <= 10^4, 2^14 > 10^4)
        const MAX_T: usize = 15; // handle up to shift 16 safely
        let mut dp: Vec<Vec<i64>> = vec![vec![0i64; MAX_T + 2]; n];
        let k_i64 = k as i64;

        for &node in order.iter().rev() {
            // accumulate children's contributions for each t
            let mut sum_same = vec![0i64; MAX_T + 1];
            let mut sum_next = vec![0i64; MAX_T + 1];
            for &child in adj[node].iter() {
                if child == parent[node] {
                    continue;
                }
                for t in 0..=MAX_T {
                    sum_same[t] += dp[child][t];
                    sum_next[t] += dp[child][t + 1]; // safe because dp has size MAX_T+2
                }
            }

            let coin = coins[node] as i64;
            for t in (0..=MAX_T).rev() {
                let option_first = (coin >> t) - k_i64 + sum_same[t];
                let option_second = (coin >> (t + 1)) + sum_next[t];
                dp[node][t] = if option_first > option_second { option_first } else { option_second };
            }
        }

        dp[0][0] as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/vector)

(define (maximum-points edges coins k)
  (define n (vector-length (list->vector coins)))
  ;; build adjacency list
  (define adj (make-vector n '()))
  (for ([e edges])
    (define a (first e))
    (define b (second e))
    (vector-set! adj a (cons b (vector-ref adj a)))
    (vector-set! adj b (cons a (vector-ref adj b))))
  ;; parent array and order (preorder)
  (define parent (make-vector n -1))
  (vector-set! parent 0 0)
  (let loop ((stack (list 0)) (order '()))
    (if (null? stack)
        (reverse order) ; return postorder later
        (let* ([node (car stack)]
               [rest (cdr stack)])
          (define new-order (cons node order))
          (define children
            (for/list ([nbr (vector-ref adj node)]
                       #:when (= (vector-ref parent nbr) -1))
              (begin
                (vector-set! parent nbr node)
                nbr)))
          (loop (append children rest) new-order))))
  ;; compute dp vectors
  (define MAX-T 15) ; enough for coins <= 10^4
  (define dp-vec (make-vector n #f))
  (define coins-vec (list->vector coins))
  (define postorder
    (let loop ((stack (list 0)) (visited '()) (order '()))
      (if (null? stack)
          (reverse order)
          (let* ([node (car stack)]
                 [rest (cdr stack)])
            (if (member node visited)
                (loop rest visited (cons node order))
                (let ([new-visited (cons node visited)]
                      [children
                       (for/list ([nbr (vector-ref adj node)]
                                  #:when (= (vector-ref parent nbr) node))
                         nbr)])
                  (loop (append children (cons node rest)) new-visited order)))))))
  ;; process nodes in postorder
  (for ([node postorder])
    (define sums (make-vector (+ MAX-T 2) 0))
    ;; accumulate children's dp contributions
    (for ([nbr (vector-ref adj node)]
          #:when (= (vector-ref parent nbr) node))
      (define child-dp (vector-ref dp-vec nbr))
      (for ([t (in-range 0 (+ MAX-T 1))])
        (define cur (vector-ref sums t))
        (vector-set! sums t (+ cur (vector-ref child-dp t)))))
    ;; compute dp for this node
    (define node-dp (make-vector (+ MAX-T 1) 0))
    (define coin (vector-ref coins-vec node))
    (for ([t (in-range 0 (+ MAX-T 1))])
      (define shifted1 (arithmetic-shift coin (- t))) ; floor(coin / 2^t)
      (define shifted2
        (if (> (+ t 1) MAX-T)
            0
            (arithmetic-shift coin (- (+ t 1)))))
      (define sum-t (vector-ref sums t))
      (define sum-tp1 (vector-ref sums (+ t 1)))
      (define val1 (+ (- k) shifted1 sum-t))
      (define val2 (+ shifted2 sum-tp1))
      (vector-set! node-dp t (max val1 val2)))
    (vector-set! dp-vec node node-dp))
  ;; answer is dp[root][0]
  (define root-dp (vector-ref dp-vec 0))
  (vector-ref root-dp 0))
```

## Erlang

```erlang
-spec maximum_points(Edges :: [[integer()]], Coins :: [integer()], K :: integer()) -> integer().
maximum_points(Edges, Coins, K) ->
    MaxT = 15,
    Adj = build_adj(Edges),
    CoinTuple = list_to_tuple(Coins),
    {ParentMap, Order} = bfs_order(Adj),
    DpMap = compute_dp_all(Order, Adj, ParentMap, CoinTuple, K, MaxT),
    hd(maps:get(0, DpMap)).

%% Build adjacency map
build_adj(Edges) ->
    lists:foldl(fun([A,B], Acc) ->
        Acc1 = maps:update_with(A,
                fun(L) -> [B|L] end,
                [B],
                Acc),
        maps:update_with(B,
                fun(L) -> [A|L] end,
                [A],
                Acc1)
    end, #{}, Edges).

%% BFS to get parent map and preorder list
bfs_order(Adj) ->
    bfs([0], #{0 => -1}, [] , Adj).

bfs([], ParentMap, Order, _Adj) ->
    {ParentMap, lists:reverse(Order)};
bfs([Node|RestStack], ParentMap, Order, Adj) ->
    NewOrder = [Node|Order],
    Neigh = maps:get(Node, Adj, []),
    {NewParentMap, NewStack} =
        lists:foldl(fun(Child, {PMap, Stk}) ->
            case maps:is_key(Child, PMap) of
                true -> {PMap, Stk};
                false ->
                    {maps:put(Child, Node, PMap), [Child|Stk]}
            end
        end, {ParentMap, RestStack}, Neigh),
    bfs(NewStack, NewParentMap, NewOrder, Adj).

%% Compute DP for all nodes in postorder
compute_dp_all(PostOrder, Adj, ParentMap, CoinTuple, K, MaxT) ->
    lists:foldl(fun(Node, DpAcc) ->
        Children = [C || C <- maps:get(Node, Adj, []), maps:get(C, ParentMap) =:= Node],
        SumList = sum_children_dp(Children, DpAcc, MaxT),
        CoinVal = element(Node+1, CoinTuple),
        DPNode = build_node_dp(CoinVal, K, SumList, MaxT),
        maps:put(Node, DPNode, DpAcc)
    end, #{}, PostOrder).

%% Sum children's dp vectors (length MaxT+2)
sum_children_dp(Children, DpMap, MaxT) ->
    Zero = lists:duplicate(MaxT+2, 0),
    lists:foldl(fun(Child, Acc) ->
        ChildDP = maps:get(Child, DpMap),
        Padded = ChildDP ++ [0],
        add_lists(Acc, Padded)
    end, Zero, Children).

%% Element‑wise addition of two equal length lists
add_lists([], []) -> [];
add_lists([A|As], [B|Bs]) -> [A+B | add_lists(As, Bs)].

%% Build DP vector for a node
build_node_dp(Coin, K, SumList, MaxT) ->
    build_node_dp(Coin, K, SumList, 0, MaxT, []).

build_node_dp(_Coin, _K, [], _T, _MaxT, Acc) ->
    lists:reverse(Acc);
build_node_dp(Coin, K, [S_cur,S_next|Rest], T, MaxT, Acc) when T =< MaxT ->
    First = (Coin bsr T) - K + S_cur,
    Second = (Coin bsr (T+1)) + S_next,
    D = erlang:max(First, Second),
    build_node_dp(Coin, K, Rest, T+1, MaxT, [D|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_points(edges :: [[integer]], coins :: [integer], k :: integer) :: integer
  def maximum_points(edges, coins, k) do
    n = length(coins)
    adj = build_adj(n, edges)

    {parent, postorder} = dfs_order(adj)

    max_t = 15
    dp_container = :array.new(n, default: nil)
    coins_arr = :array.from_list(coins)

    dp_filled =
      Enum.reduce(postorder, dp_container, fn node, acc_dp ->
        children = Enum.filter(adj[node], fn nb -> nb != Map.get(parent, node) end)
        child_arrays = Enum.map(children, fn c -> :array.get(c, acc_dp) end)

        vals =
          for t <- 0..max_t do
            sum_t =
              Enum.reduce(child_arrays, 0, fn arr, s ->
                s + (:array.get(t, arr))
              end)

            sum_tp1 =
              if t < max_t do
                Enum.reduce(child_arrays, 0, fn arr, s ->
                  s + (:array.get(t + 1, arr))
                end)
              else
                0
              end

            coin = :array.get(node, coins_arr)
            val1 = (:erlang.bsr(coin, t)) - k + sum_t
            shift2 = if t < max_t, do: :erlang.bsr(coin, t + 1), else: 0
            val2 = shift2 + sum_tp1

            if val1 > val2, do: val1, else: val2
          end

        :array.set(node, :array.from_list(vals), acc_dp)
      end)

    root_array = :array.get(0, dp_filled)
    :array.get(0, root_array)
  end

  defp build_adj(n, edges) do
    Enum.reduce(edges, List.duplicate([], n), fn [a, b], acc ->
      acc = List.update_at(acc, a, &[b | &1])
      List.update_at(acc, b, &[a | &1])
    end)
  end

  defp dfs_order(adj) do
    traverse([{0, -1}], %{}, [], adj)
  end

  defp traverse([], parent, order, _adj), do: {parent, Enum.reverse(order)}

  defp traverse([{node, par} | rest], parent, order, adj) do
    parent = Map.put(parent, node, par)
    order = [node | order]
    children = Enum.filter(adj[node], fn nb -> nb != par end)

    new_stack =
      Enum.reduce(children, rest, fn child, acc ->
        [{child, node} | acc]
      end)

    traverse(new_stack, parent, order, adj)
  end
end
```
