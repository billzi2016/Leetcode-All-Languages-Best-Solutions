# 支持语言

数据集中为多种 LeetCode 语言提供 starter code。生成器必须以 starter code 作为提交入口的来源。

## 语言特点

算法语言行使用 LeetCode 1 `Two Sum` 展示提交入口。数据库和数据分析行使用数据集中第一次出现的对应题型 LeetCode 175 `Combine Two Tables`。Shell 行使用 LeetCode 192 `Word Frequency`。生成结果必须保留 starter code 中的入口形态，不能把 LeetCode 需要的类、函数、模块、contract、spec、SQL 方言、DataFrame 函数或文件处理注释改掉。

## 提交入口规则

| 语言 | 语言特点 | 提交入口示例 |
| --- | --- | --- |
| C | 面向系统编程和底层性能场景，常见于操作系统、嵌入式、数据库内核和高性能基础库。LeetCode 中需要显式处理指针、数组长度、返回数组和内存分配，能清楚展示对底层数据表示和边界条件的控制。 | `int* twoSum(int* nums, int numsSize, int target, int* returnSize)` |
| C++ | 面向性能敏感的工程和竞赛算法场景，常见于游戏引擎、交易系统、图形计算和基础设施。LeetCode 中通常依赖 STL 容器、排序、堆、哈希表和 `class Solution`，适合表达复杂数据结构和高性能算法。 | `class Solution { public: vector<int> twoSum(vector<int>& nums, int target) }` |
| Java | 面向企业后端、服务端系统和 Android 生态的强类型面向对象语言。LeetCode 中提交入口稳定，集合库成熟，适合展示面向对象结构、泛型集合、优先队列、图搜索和动态规划等标准工程写法。 | `class Solution { public int[] twoSum(int[] nums, int target) }` |
| Python | 面向脚本、自动化、数据处理和快速原型开发的动态语言。LeetCode 中代码短、表达直接，适合快速描述算法思路，但需要注意旧版 Python 入口、整数除法、迭代器和性能边界。 | `class Solution(object): def twoSum(self, nums, target)` |
| Python3 | 当前主流 Python 版本，常用于后端脚本、机器学习、数据分析、自动化和算法原型。LeetCode 中通常带类型标注，标准库和语法更现代，适合清晰表达哈希、递归、堆、双指针和动态规划逻辑。 | `class Solution: def twoSum(self, nums: List[int], target: int) -> List[int]` |
| C# | 面向 .NET 平台、企业应用、桌面工具、游戏开发和云服务的强类型语言。LeetCode 中使用类方法提交，集合、LINQ 和泛型能力完整，适合展示 .NET 风格的数据结构和面向对象实现。 | `public class Solution { public int[] TwoSum(int[] nums, int target) }` |
| JavaScript | Web 前端、Node.js 后端、脚本自动化和全栈开发的核心语言。LeetCode 中多为函数式提交，数组和对象操作灵活，适合表达哈希表、字符串处理和模拟题，但要注意数字精度和动态类型行为。 | `var twoSum = function(nums, target)` |
| TypeScript | JavaScript 的类型增强版本，常用于大型前端工程、Node.js 服务和可维护的全栈项目。LeetCode 中在函数提交基础上加入类型约束，能让数组、对象、返回值和辅助结构的意图更明确。 | `function twoSum(nums: number[], target: number): number[]` |
| PHP | 常见于 Web 后端、CMS、电商系统和传统服务端页面开发。LeetCode 中使用类方法提交，数组同时承担列表和映射角色，适合展示字符串、哈希表和简单动态规划题的服务端脚本写法。 | `class Solution { function twoSum($nums, $target) }` |
| Swift | Apple 平台开发语言，主要用于 iOS、macOS、watchOS 和 tvOS 应用开发。LeetCode 中使用强类型数组和类方法提交，语法现代，适合展示安全的集合操作和清晰的移动端工程语言风格。 | `class Solution { func twoSum(_ nums: [Int], _ target: Int) -> [Int] }` |
| Kotlin | 面向 JVM、Android 和服务端开发的现代强类型语言，也常用于替代部分 Java 工程代码。LeetCode 中入口简洁，空安全、数据类和集合 API 友好，适合展示 Android/JVM 生态下的现代算法实现。 | `class Solution { fun twoSum(nums: IntArray, target: Int): IntArray }` |
| Dart | Flutter 的主要开发语言，常用于跨平台移动端、桌面端和 Web 应用。LeetCode 中以类方法提交，列表和映射 API 清晰，适合展示 Flutter 生态语言在算法题中的基础数据结构能力。 | `class Solution { List<int> twoSum(List<int> nums, int target) }` |
| Go | 面向云原生、后端服务、网络服务、命令行工具和并发系统的工程语言。LeetCode 中函数入口简洁，切片、map 和结构体常用，适合展示高可读性的哈希、图遍历、队列和并发友好工程风格。 | `func twoSum(nums []int, target int) []int` |
| Ruby | 面向脚本开发、Web 应用和快速业务迭代的动态语言，Rails 生态影响很大。LeetCode 中方法提交简洁，数组和哈希操作表达力强，适合展示字符串、枚举、哈希表和模拟逻辑。 | `def two_sum(nums, target)` |
| Scala | JVM 生态里的函数式和面向对象混合语言，常见于 Spark、Flink、Akka 等大数据和分布式系统场景。LeetCode 中既可以使用函数式集合操作，也可以写命令式算法，适合展示大数据生态语言的算法表达能力。 | `object Solution { def twoSum(nums: Array[Int], target: Int): Array[Int] }` |
| Rust | 面向系统编程、性能敏感服务、区块链、编译器、浏览器组件和安全基础设施的现代语言。LeetCode 中通过所有权、借用和 `impl Solution` 组织代码，适合展示内存安全、零成本抽象和严谨边界处理。 | `impl Solution { pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> }` |
| Racket | Lisp/Scheme 家族语言，常用于函数式编程、教学、语言实验和 DSL 构建。LeetCode 中保留 contract 很重要，适合展示递归、列表处理、高阶函数和函数式思维。 | `(define/contract (two-sum nums target) ...)` |
| Erlang | 面向高并发、高可用和分布式系统的函数式语言，常见于电信、消息系统和容错服务。LeetCode 中使用 spec 和函数定义，适合展示模式匹配、递归、不可变数据和函数式列表处理。 | `-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].` |
| Elixir | 构建在 Erlang VM 上的现代函数式语言，常用于 Phoenix Web 服务、实时系统、消息处理和高并发应用。LeetCode 中使用模块化函数提交，适合展示管道、模式匹配、递归和不可变集合处理。 | `defmodule Solution do ... def two_sum(nums, target) do ... end` |
| MySQL | 常见的关系型数据库方言，广泛用于 Web 应用、业务系统和运营数据库。LeetCode 数据库题中主要考察 join、group by、聚合、过滤、窗口函数和 MySQL 方言细节。 | LeetCode 175: `# Write your MySQL query statement below` |
| MS SQL Server | Microsoft SQL Server 使用的 T-SQL 方言，常见于企业报表、业务数据平台和后端数据系统。LeetCode 数据库题中需要保留 T-SQL starter comment，并注意 SQL Server 特有函数和语法。 | LeetCode 175: `/* Write your T-SQL query statement below */` |
| Oracle SQL | Oracle 数据库的 SQL / PL-SQL 环境，常见于金融、电信和大型企业数据系统。LeetCode 数据库题中需要保留 PL-SQL 风格 starter code，并处理 Oracle 方言差异。 | LeetCode 175: `/* Write your PL/SQL query statement below */` |
| PostgreSQL | 功能完整的开源关系型数据库，常用于后端系统、分析平台、地理数据和复杂查询场景。LeetCode 数据库题中常用 CTE、窗口函数、日期处理、聚合和 PostgreSQL 方言语法。 | LeetCode 175: `-- Write your PostgreSQL query statement below` |
| Pandas | Python 数据分析生态中的表格数据处理库，常用于 DataFrame 清洗、join、groupby、筛选、重塑和统计分析。LeetCode Pandas 题不是 `class Solution` 算法入口，而是带类型标注的 DataFrame 函数。 | LeetCode 175: `def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame` |
| Bash | Unix shell 脚本语言，常用于命令行自动化、文本处理、管道组合和运维脚本。LeetCode Shell 题通常读取文件或标准输入，并组合 `cat`、`awk`、`sort`、`uniq`、`sed` 等工具完成处理。 | LeetCode 192: `# Read from the file words.txt and output the word frequency list to stdout.` |

这些入口必须出现在最终代码里，这样生成代码才能直接粘贴到 LeetCode。
