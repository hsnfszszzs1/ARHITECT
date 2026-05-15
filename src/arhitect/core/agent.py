"""ARHITECT Core Agent - Orchestrator cu integrare GitHubTools automată."""

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

from ..tools.github_tools import GitHubTools


@dataclass
class ArchitectureDecision:
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    mode: str = ""
    summary: str = ""
    details: str = ""
    diagram: Optional[str] = None
    github_repo: Optional[str] = None


class ArhitectAgent:
    """Agentul ARHITECT cu integrare automată GitHubTools.

    Acum poate:
    - Analiza repo-uri GitHub
    - Propune și pregăti scaffolding în repo-uri existente
    - Folosi GitHubTools pentru prompturi și sugestii specializate
    """

    def __init__(self, config: Optional[ArhitectConfig] = None, github_owner: str = "hsnfszszzs1"):
        self.config = config or DEFAULT_CONFIG
        self.decisions: List[ArchitectureDecision] = []
        self.console = Console() if RICH_AVAILABLE else None
        self.github = GitHubTools(owner=github_owner)   # <-- Integrare automată

    def _print(self, content: str, title: str = "ARHITECT"):
        if self.console:
            self.console.print(Panel(Markdown(content), title=title, border_style="blue"))
        else:
            print(f"\n=== {title} ===\n{content}")

    def get_system_prompt(self) -> str:
        return get_system_prompt(self.config.language)

    # ==================== METODE NOI CU GITHUB ====================

    def analyze_github_repo(self, repo_name: str) -> ArchitectureDecision:
        """Analizează un repo GitHub folosind GitHubTools."""
        prompt = self.github.get_analyze_repo_prompt(repo_name)

        decision = ArchitectureDecision(
            mode="github_analysis",
            summary=f"Analiză repo: {repo_name}",
            details=prompt,
            github_repo=repo_name
        )
        self.decisions.append(decision)

        self._print(
            f"**Repo analizat:** {repo_name}\n\n"
            f"Prompt generat pentru analiză detaliată. "
            f"Poți copia promptul sau folosi tool-urile conectate GitHub.",
            "GitHub Analysis"
        )
        return decision

    def scaffold_module_in_repo(self, repo_name: str, module_name: str, description: str) -> ArchitectureDecision:
        """Pregătește scaffolding pentru un modul nou în repo-ul dat."""
        prompt = self.github.get_scaffold_prompt(repo_name, module_name, description)

        decision = ArchitectureDecision(
            mode="github_scaffold",
            summary=f"Scaffolding modul '{module_name}' în {repo_name}",
            details=prompt,
            github_repo=repo_name
        )
        self.decisions.append(decision)

        self._print(
            f"**Modul propus:** {module_name} \u2192 {repo_name}\n\n"
            f"Prompt de scaffolding generat. Folosește-l cu github___create_or_update_file.",
            "GitHub Scaffolding"
        )
        return decision

    def get_github_suggestions(self, repo_name: str) -> Dict[str, Any]:
        """Returnează sugestii de îmbunătățire arhitecturală pentru un repo."""
        return self.github.suggest_architecture_for_existing_project(repo_name)

    # ==================== METODE EXISTENTE ====================

    def analyze_requirements(self, user_input: str) -> ArchitectureDecision:
        decision = ArchitectureDecision(
            mode="requirements",
            summary="Analiză cerințe",
            details=f"Input: {user_input}\n\nRecomandări: Clarifică scope, actori, bounded contexts, riscuri."
        )
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
            "config": self.config.__dict__,
            "decisions": [d.__dict__ for d in self.decisions],
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return filepath

    def run(self, task: str, mode: Optional[str] = None, github_repo: Optional[str] = None):
        """Punct de intrare principal. Suportă acum github_repo pentru analiză automată."""
        if mode:
            self.config.mode = mode

        self._print(f"**Task:** {task}\n**Mod:** {self.config.mode}", "ARHITECT")

        # === Integrare GitHub automată ===
        if github_repo:
            self.analyze_github_repo(github_repo)

        if self.config.mode in ["requirements", "full"]:
            self.analyze_requirements(task)

        if self.config.mode in ["design", "high_level", "full"]:
            self.generate_high_level_design(task)

        if self.config.mode in ["github", "full"] and github_repo:
            self.scaffold_module_in_repo(github_repo, "new_module", task)

        if self.config.use_metadata:
            path = self.save_metadata()
            self._print(f"Metadata salvată: {path}", "Persistență")

        self._print("Workflow finalizat. GitHubTools este integrat automat.", "ARHITECT")


if __name__ == "__main__":
    agent = ArhitectAgent()
    # Exemplu cu GitHub integrat
    agent.run(
        "Adaugă un modul nou de analiză arhitecturală",
        mode="full",
        github_repo="ARHITECT"
    )
