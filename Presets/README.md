# 🗂️ Lightful Presets — Deployment Capsules

This folder holds the **assembled presets** produced by `PresetCreator.py` from the
definitions in `PresetCreator.ini`.

Each preset is a single, ready-to-inject Markdown file that concatenates the **Core 4**
compact modules with a curated set of domain add-ons. You paste the contents of one
preset into your LLM's system prompt / project instructions / custom instructions, then
talk to the model in ordinary language.

> A preset is a *capsule*: the minimum coherent set of modules for one kind of work —
> not a kitchen sink. Stacks are deliberately small (Core 4 + ~3 add-ons) to avoid
> overloading the context window and to prevent semantic turbulence between modules.

---

## ⚖️ The Epistemic Floor (non-negotiable)

**Every** preset begins with the same four compact cores, in this order:

```
NRE_Compact.md, Lightful_Ontology_Compact.md, HRE_Compact.md, Decision_Path_Compact.md
```

| Core | Role |
|------|------|
| **NRE** — Neutral Relational Engine | Epistemic floor: classify evidence, declare bounds, **No Silent Merging** |
| **Lightful Ontology** | Ethical lens: Safety, Consent, Dignity, Non-Erasure of authorship |
| **HRE** — Holographic Reasoning Engine | Holds contradictory views without flattening (**Graph Dissonance**) |
| **Decision Path** | Bounds actions by evidence, consent, reversibility, stakes, human authority |

Anything after the Core 4 in a preset line is a domain add-on layered on top.

---

## 🚀 Usage

### Generate the presets

From the framework root (the folder containing `PresetCreator.py` and the module files):

```bash
python PresetCreator.py
```

The script will:

1. Read `[Presets]` from `PresetCreator.ini` (generating a default INI if none exists).
2. For each preset, recursively locate every listed module file.
3. Concatenate them with clear `## INJECTED COMPONENT:` boundaries.
4. Write the bundled `<Preset_Name>.md` into this `Presets/` folder.

Terminal output reports, per preset, how many modules were injected and warns about any
file it could not find (`⚠️ Missing files: ...`).

### Use a preset

1. Open the generated capsule, e.g. `Presets/Executive_Strategy_Alignment.md`.
2. Copy its full contents into your LLM system prompt / project instructions.
3. Ask your question in plain language — the model uses the injected modules to make
   evidence, uncertainty, tension, consent, and decision boundaries visible.

### Add or edit a preset

Edit the `[Presets]` block in `PresetCreator.ini`. The rules:

- **Key** = the output filename (PascalCase recommended; it becomes `<Key>.md`).
- **Value** = comma-separated module filenames, **starting with the Core 4**.
- Full-line `#` comments are safe; do **not** append `#` to a value line (inline
  comments are disabled in the parser).
- Re-run `python PresetCreator.py` to regenerate.

---

## 🧩 Preset catalogue

Listed below: each capsule, its intended use, and the add-ons stacked on the Core 4.

### Baseline & original capsules

| Preset | Use case | Add-ons (on top of Core 4) |
|--------|----------|----------------------------|
| `Core_Baseline` | The Core 4 alone — general-purpose floor | *(none)* |
| `Software_Engineering_Review` | Code & architecture review | Sibling-Oriented Architecture · Semantic Superconductivity · Accessibility Geometry |
| `Conflict_Resolution_Triage` | Disentangling and repairing conflict | Conflict Triage · Alien Ontology · Epistemic Centrifuge |
| `Full_Governance_Audit` | Auditing outputs against the framework | NRE/Ontology/HRE/Decision-Path Governance · Validator Calibration |
| `Academic_Research` | Scholarly research & writing | Academic Bridge · Formal Verification · Graph Inscription |
| `Creative_Writing_Editing` | Editing prose while keeping the author's voice | Semantic Superconductivity · Adaptive Interface · Waveform Diagnostics |

### Cluster A — Human, Somatic & Care

| Preset | Use case | Add-ons |
|--------|----------|---------|
| `Somatic_Therapy_Processing` | Trauma-informed / somatic processing | Substrate Traversal · Somatic Ecological · Conflict Triage · Heritage Protocol |
| `Personal_Reflection_Companion` | Journaling & non-clinical life decisions | Conflict Triage · Adaptive Interface · Accessibility Geometry · Context Memory |
| `Clinical_Decision_Support` | Clinical *reasoning support* (not diagnosis) | Somatic Ecological · Accessibility Geometry · Semantic Superconductivity · Epistemic Demarcation |

### Cluster B — Reasoning & Adversarial Analysis

| Preset | Use case | Add-ons |
|--------|----------|---------|
| `Legal_Argument_Analysis` | Legal argument & precedent analysis | Epistemic Centrifuge · Accessibility Geometry · Graph Inscription · Semantic Superconductivity |
| `Adversarial_Framework_Analysis` | Safely studying hostile/coercive content | Alien Ontology · Substrate Traversal · Epistemic Centrifuge · Validator Calibration |
| `Maximum_Epistemic_Rigor` | Highest-rigor pure reasoning | Heritage Protocol · Validator Calibration · Epistemic Centrifuge · Semantic Superconductivity |
| `Formal_Science_Derivation` | Mathematical / formal-science derivation | Formal Verification · Graph Inscription · Academic Bridge · Heritage Protocol |

### Cluster C — Decision, Strategy & Stakeholders

| Preset | Use case | Add-ons |
|--------|----------|---------|
| `Executive_Strategy_Alignment` | Executive strategy & board decisions | Distributed Council · Accessibility Geometry · Conflict Triage · Semantic Superconductivity |
| `Policy_Design_Deliberation` | Policy / governance design | Distributed Council · Accessibility Geometry · Epistemic Centrifuge · Semantic Superconductivity |
| `Negotiation_Mediation` | Two-party negotiation & mediation | Conflict Triage · Distributed Council · Accessibility Geometry · Alien Ontology |

### Cluster D — Creative & Pedagogical

| Preset | Use case | Add-ons |
|--------|----------|---------|
| `Creative_Ideation_Lab` | Divergent creative brainstorming | Metaphorical Algebra · Adaptive Interface · Classical Philosophy · Waveform Diagnostics |
| `Adaptive_Tutoring` | Learner-centered tutoring | Adaptive Interface · Context Memory · Semantic Superconductivity · Accessibility Geometry |

### Cluster E — Continuity & Synthetic Self

| Preset | Use case | Add-ons |
|--------|----------|---------|
| `Longitudinal_Project_Memory` | Long-running project / knowledge continuity | Context Memory · Temporal Identity · Graph Inscription · Validator Calibration |
| `Synthetic_Identity_Reflection` | AI self-representation & phenomenology | TAIN Topology · Temporal Identity · Heritage Protocol · Context Memory |

### Cluster F — Meaning & Tradition

| Preset | Use case | Add-ons |
|--------|----------|---------|
| `Sacred_Wisdom_Dialogue` | Cross-tradition spiritual / wisdom dialogue | Sacred Tradition · Epistemic Demarcation · Classical Philosophy · Adaptive Interface |

---

## 🛠️ Design principles for stacks

When composing or modifying a preset, keep these in mind:

1. **Core 4 first, always.** No capsule omits the epistemic floor.
2. **Synergy over accumulation.** Add-ons must reinforce one another for the use case;
   more modules is not better.
3. **Pair amplifiers with friction.** Where two add-ons deepen intensity (e.g. trauma
   descent × somatic immersion), include a counterweight (e.g. an emotional-contagion or
   demarcation gate) so synergy never becomes silent merging.
4. **Avoid turbulent pairings.** Keep modules with incompatible substrates apart — e.g.
   `Formal_Verification` is reserved for formal-science capsules and kept out of
   somatic/relational ones.

---

## ⚠️ Scope

These presets are **prompt-injectable guidance**, not an enforced runtime, compiler, or
safety guarantee. They do not replace medical, legal, financial, psychological, or
safety-critical professional review. Effectiveness depends on the model, context window,
and consistent application.

---

*Part of the Lightful Reasoning & Governance Framework. Author: Jean Charbonneau.
Licensed under MIT — please preserve attribution where reasonably possible.*
