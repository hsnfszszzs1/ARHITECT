"""Simple CLI for ARHITECT agent."""

import typer
from rich.console import Console

from .core.agent import ArhitectAgent
from .core.config import ArhitectConfig

app = typer.Typer(help="ARHITECT - Agent specializat în arhitectură software")
console = Console()


@app.command()
def run(
    task: str = typer.Argument(..., help="Descrierea sarcinii de arhitectură"),
    mode: str = typer.Option("full", help="Mod: requirements | high_level | diagram | review | full"),
    lang: str = typer.Option("ro", help="Limbă: ro sau en"),
):
    """Rulează agentul ARHITECT pe o sarcină dată."""
    config = ArhitectConfig(language=lang, mode=mode)
    agent = ArhitectAgent(config)
    agent.run(task, mode=mode)
    console.print("[green]✓ Workflow ARHITECT finalizat![/green]")


if __name__ == "__main__":
    app()
