"""Reference solvers and normalization for supported problem shapes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


class CandidateError(ValueError):
    """Raised when a candidate case cannot be retained."""


@dataclass(frozen=True)
class Adapter:
    """Reference adapter for one supported problem shape."""

    kind: str
    solve: Callable[[dict[str, Any]], Any]
    validate_input: Callable[[dict[str, Any]], None]
    normalize: Callable[[Any], Any]
    max_cases: int = 50

    def equivalent(self, expected: Any, actual: Any) -> bool:
        """Compare expected and actual values after adapter normalization."""

        return self.normalize(expected) == self.normalize(actual)


def require_keys(case_input: dict[str, Any], keys: set[str]) -> None:
    """Require input keys exactly include the expected keys."""

    missing = keys - set(case_input)
    if missing:
        raise CandidateError(f"missing input keys: {sorted(missing)}")


def require_int_list(value: Any, name: str, max_len: int = 200) -> list[int]:
    """Validate and return a list of ints."""

    if not isinstance(value, list) or len(value) > max_len or not all(isinstance(item, int) for item in value):
        raise CandidateError(f"{name} must be a list[int] with length <= {max_len}")
    return value


def validate_two_sum(case_input: dict[str, Any]) -> None:
    """Validate a Two Sum style input."""

    require_keys(case_input, {"nums", "target"})
    nums = require_int_list(case_input["nums"], "nums", max_len=200)
    if len(nums) < 2:
        raise CandidateError("nums must contain at least two elements")
    if not isinstance(case_input["target"], int):
        raise CandidateError("target must be int")


def solve_two_sum(case_input: dict[str, Any]) -> list[int]:
    """Brute-force Two Sum reference solver."""

    nums = case_input["nums"]
    target = case_input["target"]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    raise CandidateError("no valid pair exists")


def normalize_index_pair(value: Any) -> list[int]:
    """Normalize an index pair for order-insensitive comparison."""

    if not isinstance(value, list) or len(value) != 2 or not all(isinstance(item, int) for item in value):
        raise CandidateError("expected value must be a two-index list")
    return sorted(value)


def validate_string_bool(case_input: dict[str, Any]) -> None:
    """Validate a string-to-bool input."""

    require_keys(case_input, {"s"})
    if not isinstance(case_input["s"], str) or len(case_input["s"]) > 1000:
        raise CandidateError("s must be a string with length <= 1000")


def solve_valid_parentheses(case_input: dict[str, Any]) -> bool:
    """Reference solver for Valid Parentheses."""

    stack: list[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in case_input["s"]:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            return False
    return not stack


def validate_stock(case_input: dict[str, Any]) -> None:
    """Validate a stock-prices array input."""

    require_keys(case_input, {"prices"})
    require_int_list(case_input["prices"], "prices", max_len=500)


def solve_max_profit(case_input: dict[str, Any]) -> int:
    """Reference solver for Best Time to Buy and Sell Stock."""

    prices = case_input["prices"]
    best = 0
    min_price = prices[0] if prices else 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best


def validate_linked_add(case_input: dict[str, Any]) -> None:
    """Validate Add Two Numbers list inputs."""

    require_keys(case_input, {"l1", "l2"})
    require_int_list(case_input["l1"], "l1", max_len=200)
    require_int_list(case_input["l2"], "l2", max_len=200)
    if not case_input["l1"] or not case_input["l2"]:
        raise CandidateError("l1 and l2 must be non-empty")
    if any(item < 0 or item > 9 for item in case_input["l1"] + case_input["l2"]):
        raise CandidateError("digits must be in [0, 9]")


def solve_add_two_numbers(case_input: dict[str, Any]) -> list[int]:
    """Reference solver for Add Two Numbers using digit arrays."""

    l1 = case_input["l1"]
    l2 = case_input["l2"]
    output: list[int] = []
    carry = 0
    for index in range(max(len(l1), len(l2))):
        total = carry
        if index < len(l1):
            total += l1[index]
        if index < len(l2):
            total += l2[index]
        output.append(total % 10)
        carry = total // 10
    if carry:
        output.append(carry)
    return output


def validate_merge_lists(case_input: dict[str, Any]) -> None:
    """Validate Merge Two Sorted Lists inputs."""

    require_keys(case_input, {"list1", "list2"})
    list1 = require_int_list(case_input["list1"], "list1", max_len=500)
    list2 = require_int_list(case_input["list2"], "list2", max_len=500)
    if list1 != sorted(list1) or list2 != sorted(list2):
        raise CandidateError("list inputs must be sorted")


def solve_merge_two_lists(case_input: dict[str, Any]) -> list[int]:
    """Reference solver for merging two sorted lists."""

    return sorted(case_input["list1"] + case_input["list2"])


def normalize_identity(value: Any) -> Any:
    """Return value unchanged."""

    return value


ADAPTERS = {
    "array_int_target_indices": Adapter("array_int_target_indices", solve_two_sum, validate_two_sum, normalize_index_pair),
    "string_bool": Adapter("string_bool", solve_valid_parentheses, validate_string_bool, normalize_identity),
    "array_int_result": Adapter("array_int_result", solve_max_profit, validate_stock, normalize_identity),
    "linked_list_addition": Adapter("linked_list_addition", solve_add_two_numbers, validate_linked_add, normalize_identity),
    "merge_two_sorted_lists": Adapter("merge_two_sorted_lists", solve_merge_two_lists, validate_merge_lists, normalize_identity),
}


def get_adapter(kind: str) -> Adapter | None:
    """Return the adapter for a problem kind, if supported."""

    return ADAPTERS.get(kind)

