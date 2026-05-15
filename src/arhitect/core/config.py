"""Configuration for ARHITECT agent."""

from dataclasses import dataclass
from typing import Literal


@dataclass
class ArhitectConfig:
    """Configurație de bază pentru agentul ARHITECT."""
    language: Literal["ro", "en"] = "ro"
    mode: str = "full"  # requirements | design | diagram | review | github | full
    use_metadata: bool = True
    output_format: Literal["text", "markdown", "json"] = "markdown"
    max_tokens: int = 4000

    # Preset styles
    style: str = "professional"  # professional | creative | strict | balanced


DEFAULT_CONFIG = ArhitectConfig()
