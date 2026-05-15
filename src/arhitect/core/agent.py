"""ARHITECT Core Agent"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime
import json

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


from ..prompts.system_prompts import get_system_prompt

from .config import DEFAULT_CONFIG, ArhitectConfig


@dataclass
class ArchitectureDecision:
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    mode: str = ""
    summary: str = ""
    details: str = ""
    diagram: Optional[str] = None


class ArhitectAgent:
    """Agentul ARHITECT - Orchestrator principal."""

    def __init__(self, config: Optional[ArhitectConfig] = None):
        self.config = config or DEFAULT_CONFIG
        self.decisions: List[ArchitectureDecision] = []
        self.console = Console() if RICH_AVAILABLE else None

    def _print(self, content: str, title: str = "ARHITECT"):
        if self.console:
            self.console.print(Panel(Markdown(content), title=title, border_style="blue"))
        else:
            print(f"\n=== {title} ===\n{content}")

    def get_system_prompt(self) -> str:
        return get_system_prompt(self.config.language)

    def analyze_requirements(self, user_input: str) -> ArchitectureDecision:
        decision = ArchitectureDecision(mode="requirements", summary="Analiză cerințe", details=f"Input: {user_input}\n\nRecomandări: Clarifică scope, actori, bounded contexts, riscuri.")
        self.decisions.append(decision)
        return decision

    def generate_high_level_design(self, context: str) -> ArchitectureDecision:
        decision = ArchitectureDecision(
            mode="high_level",
            summary="High-Level Design",
            details="""Propunere: Layered Architecture + C4 Context.

```mermaid
graph TD
    User --> App
    App --> Backend
    Backend --> DB
    Backend --> LLM
```""")
        self.decisions.append(decision)
        return decision

    def save_metadata(self, filepath: str = "architecture_decisions.json"):
        data = {
            "project": "ARHITECT",
            "timestamp": datetime.now().isoformat(),
            "decisions": [d.__dict__ for d in self.decisions],
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return filepath

    def run(self, task: str, mode: Optional[str] = None):
        if mode:
            self.config.mode = mode
        self._print(f"Task: {task} | Mod: {self.config.mode}")
        self.analyze_requirements(task)
        self.generate_high_level_design(task)
        if self.config.use_metadata:
            self.save_metadata()
        self._print("Workflow ARHITECT finalizat. Extinde cu LLM integration.")


if __name__ == "__main__":
    ArhitectAgent().run("Arhitectură pentru Advanced Body Editor v7 cu metadata și GitHub tools.")
