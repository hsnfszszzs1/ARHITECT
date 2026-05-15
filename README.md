# 🏛o ARHITECT

**Workspace specializat pentru agentul AI ARHITECT** — Software & System Architect profesionist.

> **Scop**: Un mediu complet, modular și extensibil pentru a dezvolta, rula și specializa un agent AI expert în arhitectură software, design de sisteme, diagrame, review-uri de arhitectură și scaffolding de proiecte.

Inspirat din cele mai bune practici din repo-uri precum awslabs/agent-plugins, edict (multi-agent orchestration), NirDiamant/GenAI_Agents și proiectele tale existente (Advanced Body Editor, Chess Trainer).

---

## 🎯 Caracteristici Principale

- **Agent specializat ARHITECT**: Prompturi de sistem puternice + moduri de lucru (Requirements, High-Level Design, Detailed Design, Technology Stack, Diagram Expert, Reviewer, GitHub Analyzer).
- **Arhitectură modulară**: Sub-agenti / module separate pentru fiecare etapă a procesului de arhitectură.
- **Generare diagrame**: Expert Mermaid, PlantUML, C4 model, sequence diagrams, deployment diagrams.
- **Scaffolder de proiecte**: Generează structuri complete de foldere + fișiere pentru arhitecturi comune (Clean Architecture, Hexagonal, FastAPI + modular, etc.).
- **Integrare GitHub nativă**: Tool-uri pentru analiză repo-uri existente, sugestii de refactorizare arhitecturală și crearea de structuri noi.
- **Metadata & persistență**: Salvare JSON cu decizii de arhitectură, preferințe și istoricul proiectului (similar cu proiectele tale de body editing).
- **CLI prietenos**: Interfață simplă pentru interacțiune rapidă.
- **Bilingual ready**: Suport Romanian + English (prompturi și documentație).
- **Extensibil**: Ușor de integrat cu Grok, alte LLM-uri, sau framework-uri multi-agent (LangGraph, CrewAI, etc.).

---

## 📁 Structura Workspace-ului

```
ARHITECT/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── pyproject.toml          # (opțional, pentru viitor)
├── src/
│   ├── arhitect/
│       ├── __init__.py
│       ├── core/
│       │   ├── agent.py              # Orchestratorul principal ARHITECT
│       │   ├── orchestrator.py
│       │   └── config.py
│       ├── agents/                 # Sub-agenti specializați
│       │   ├── requirements.py
│       │   ├── designer.py
│       │   ├── diagram_expert.py
│       │   ├── reviewer.py
│       │   └── github_analyzer.py
│       ├── prompts/
│       │   ├── system_prompts.py
│       │   └── templates/
│       ├── tools/
│       │   ├── github_tools.py
│       │   ├── diagram_tools.py
│       │   └── project_scaffolder.py
│       └── utils/
│           └── metadata.py
├── docs/
│   ├── architecture.md
│   ├── usage.md
│   └── examples/
├── examples/
│   ├── body_editor_architecture/
│   └── chess_trainer_design/
├── tests/
└── scripts/
```

---

## 🚀 Cum să folosești ARHITECT

1. **Clonează repo-ul**:
   ```bash
   git clone https://github.com/hsnfszszzs1/ARHITECT.git
   cd ARHITECT
   ```

2. **Instalează dependențele** (minimale):
   ```bash
   pip install -r requirements.txt
   ```

3. **Rulează agentul** (exemplu CLI):
   ```bash
   python -m src.arhitect.cli " Creează o arhitectură Clean Architecture pentru o aplicație de body remodeling cu FastAPI + AI image processing"
   ```

4. **Folosește în conversații cu Grok**: Copiază prompturile din `src/arhitect/prompts/` și activează modul ARHITECT.

---

## 📊 Exemple de utilizare

- Analiză cerințe și clarificare pentru un nou proiect (ex: Advanced Body Editor v7)
- Generare C4 diagrams + Mermaid pentru layered architecture
- Review arhitectural al unui repo existent (via GitHub tools)
- Scaffolding rapid pentru un nou modul "Arhitect" în proiectele tale
- Sugestii de tech stack și trade-off analysis (ex: Pillow vs OpenCV, metadata JSON vs DB)

---

## 🔧 Integrare cu GitHub & Tool-uri Conectate

Workspace-ul este pregătit să folosească tool-urile conectate GitHub (create/update files, search repos, etc.). Poți extinde `tools/github_tools.py` pentru a automatiza crearea de structuri sau review-uri directe pe repo-urile tale (Grok-Image-, EDITOR etc.).

---

## 🛠️ Roadmap & Extensii viitoare

- [ ] Implementare completă multi-agent orchestration (inspirat din edict)
- [ ] Integrare cu VisionAnalyzer / diagram image generation
- [ ] Suport PlantUML + export PDF/SVG
- [ ] Skill Grok personalizat (folosind skill-creator)
- [ ] Persistență metadata avansată + versioning decizii
- [ ] Template-uri ready-to-use pentru proiecte AI Image Editing & Body Remodeling

---

## 🤝 Contribuții

Acest workspace este creat special pentru tine (hsnfszszzs1). Poți modifica, extinde sau folosi tool-urile conectate pentru a adăuga fișiere noi direct din Grok.

**Creat cu Grok în data de 15 mai 2026** | Romania

---

*"Un bun arhitect nu desenează doar clădiri — construiește fundații solide pentru sisteme care rezistă timpului."*
