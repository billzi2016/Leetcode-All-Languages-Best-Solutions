"""LLM-backed candidate generation for validate-pro."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class OllamaSettings:
    """Ollama generation settings for controlled case generation."""

    model: str = "gpt-oss:120b"
    temperature: float = 0.2
    num_predict: int = 2048
    think: str = "high"


def parse_strict_json(text: str) -> dict[str, Any]:
    """Parse strict JSON and reject extra non-JSON text."""

    parsed = json.loads(text)
    if not isinstance(parsed, dict):
        raise ValueError("candidate JSON must be an object")
    return parsed


class OllamaCaseGenerator:
    """Generate one candidate test case with Ollama."""

    def __init__(self, settings: OllamaSettings | None = None) -> None:
        """Create a generator with optional settings."""

        self.settings = settings or OllamaSettings()

    def generate(self, prompt: str) -> dict[str, Any]:
        """Generate and parse one strict JSON candidate."""

        import ollama

        response = ollama.generate(
            model=self.settings.model,
            prompt=prompt,
            options={
                "temperature": self.settings.temperature,
                "num_predict": self.settings.num_predict,
                "think": self.settings.think,
            },
        )
        text = str(response.get("response", "")).strip()
        return parse_strict_json(text)

