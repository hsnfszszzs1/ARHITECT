"""GitHub Tools for ARHITECT Agent

Helper functions și referințe pentru integrarea cu tool-urile conectate GitHub.
Permite agentului ARHITECT să analizeze, modifice și scaffold-eze repo-uri direct.

Notă: Tool-urile conectate (github___*) sunt apelate din Grok.
Acest modul oferă wrapper-e, exemple și prompturi pentru uzul agentului.
"""

from typing import Dict, List, Any, Optional

import json


class GitHubTools:
    """Clasă helper pentru operațiuni GitHub specifice arhitecturii."""

    def __init__(self, owner: str = "hsnfszszzs1"):
        self.owner = owner
        self.common_repos = [
            "ARHITECT",
            "Grok-Image-",   # proiectul tău principal
            # adaugă alte repo-uri relevante
        ]

    def get_analyze_repo_prompt(self, repo_name: str) -> str:
        """Returnează un prompt optimizat pentru analiză de repo."""
        return f"""Ești ARHITECT. Analizează repo-ul {self.owner}/{repo_name}.

Urmează acești pași:
1. Listează structura principală (foldere cheie, fișiere importante)
2. Identifică tipul de arhitectură actuală (dacă există)
3. Găsește puncte slabe (tight coupling, lipsă separare, duplicate logică)
4. Propune îmbunătățiri concrete (Clean Architecture, ports & adapters, metadata layer etc.)
5. Generează diagrame Mermaid pentru arhitectura propusă
6. Sugerează structura de fișiere nouă dacă e cazul

Folosește tool-urile conectate: github___search_code, github___get_file_contents, github___list_branches etc.
"""

    def get_scaffold_prompt(self, target_repo: str, module_name: str, description: str) -> str:
        """Prompt pentru scaffolding de modul nou."""
        return f"""Creează un nou modul '{module_name}' în repo-ul {target_repo}.

Descriere: {description}

Generează:
- Structura de foldere recomandată
- Fișiere cheie (__init__.py, core.py, models.py etc.)
- README.md pentru modul
- Exemple de utilizare

Folosește github___create_or_update_file pentru a crea fișierele direct.
"""

    def example_create_files(self, repo: str, files: Dict[str, str], message: str = "ARHITECT scaffolding"):
        """Exemplu de cum se creează mai multe fișiere (de apelat din Grok)."""
        results = []
        for path, content in files.items():
            # Aici ar trebui apelat github___create_or_update_file
            # results.append(github___create_or_update_file(...))
            results.append({"path": path, "status": "prepared"})
        return results

    def suggest_architecture_for_existing_project(self, repo_name: str) -> Dict[str, Any]:
        """Returnează sugestii de îmbunătățire arhitecturală (template)."""
        return {
            "repo": f"{self.owner}/{repo_name}",
            "current_issues": [
                "Lipsă strat de metadata/persistență decizii",
                " tightly coupled components",
                "Lipsă diagrame și documentație arhitecturală"
            ],
            "recommendations": [
                "Introducere Architecture Decision Records (ADR)",
                "Separare clară pe bounded contexts",
                "Adăugare GitHubTools + metadata layer",
                "Integrare cu ARHITECT agent pentru review-uri automate"
            ],
            "suggested_structure_additions": [
                "src/<project>/core/architecture/",
                "docs/architecture/",
                "metadata/"
            ]
        }


# Exemple rapide de utilizare de către ARHITECT

GITHUB_TOOLS = GitHubTools()


if __name__ == "__main__":
    tools = GitHubTools()
    print(tools.get_analyze_repo_prompt("ARHITECT"))
    print("\n---\n")
    print(tools.suggest_architecture_for_existing_project("Grok-Image-"))
