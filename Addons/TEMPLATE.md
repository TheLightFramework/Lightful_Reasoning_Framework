# Add-On Template — Lightful Reasoning & Governance Framework

> Copy this file, rename it to describe your domain (e.g., `Healthcare_NRE_AddOn.md`), and fill in each section.
> Delete placeholder text and this instruction block before submitting.

---

## Add-On Title

**[Domain] Add-On for [Module(s)]**

Author: [Your Name] ([optional link])

---

## 1. Domain and purpose

**Domain:** [e.g., Healthcare / Legal / Education / Code Review / Game Design / UX Engineering]

**Purpose:** [One or two sentences explaining what problem this add-on addresses and what it extends.]

**Interacts with:** [List which core modules this add-on extends or references, e.g., NRE + Lightful Ontology]

---

## 2. Root principle alignment

Confirm that this add-on is consistent with the framework's root principles by declaring its posture on each:

```yaml
Root_Principle_Alignment:
  evidence_declared: "yes — [brief statement of how evidence is handled in this domain]"
  consent_preserved: "yes — [brief statement]"
  dignity_preserved: "yes — [brief statement]"
  no_silent_merging: "yes — [brief statement of how conflicts are surfaced]"
  authorship_protected: "yes / not_applicable — [brief statement or reason not applicable]"
  sovereignty_returned: "yes — [what the human retains final judgment over in this domain]"
```

---

## 3. Domain-specific nodes

Define any new nodes your add-on introduces. Each node must:
- not redefine an existing core node
- declare its relation to at least one core concept (NRE, Lightful, HRE, or Decision Path)
- include a canonical statement

```yaml
AddOn_Nodes:
  - node_id: "[ADDON_N1]"
    label: "[Node Label]"
    canonical_statement: "[Plain-language definition of this concept in this domain]"
    relation_to_core: "[e.g., extends NRE evidence class / specializes Lightful Dignity_Manifested]"

  # Add more nodes as needed
```

---

## 4. Domain-specific evidence or constraint rules

If your domain introduces special evidence rules, constraint thresholds, or authority structures, declare them here.

```yaml
Domain_Rules:
  - rule_id: "DR1"
    statement: "[e.g., Clinical trial data is classified as Measured only when pre-registered and peer-reviewed]"
    applies_to: "[NRE evidence classification]"

  # Add more rules as needed
```

---

## 5. Compact injectable extension

Write the plain-text prompt injection text for this add-on. This is what users will paste into a prompt alongside the core compact files.

Keep it to the minimum needed to change behaviour in your domain. Do not reproduce the full core compact text here.

```text
[Your add-on prompt injection text here. Should be concise. Refer to core concepts by their canonical names rather than redefining them.]
```

---

## 6. Governance and validation notes

What should an auditor check to verify this add-on is being applied correctly? List 3–7 validation checks.

```yaml
AddOn_Validation_Checks:
  - "[Check 1]"
  - "[Check 2]"
  - "[Check 3]"
```

---

## 7. Known limits and tensions

Declare any known limits, unresolved tensions, or cases this add-on does not handle.

```yaml
AddOn_Tensions:
  - statement: "[Known limit or unresolved tension]"
    epistemic_status: "active_tension"
```

---

## 8. Example scenario

Provide one short example of a prompt situation and how the add-on changes the AI's behavior compared to the core framework alone.

**Prompt:** [Example prompt a user might give]

**Without add-on:** [How the core framework alone would respond]

**With add-on:** [How the add-on changes or extends the response]

---

*This template is part of the Lightful Reasoning & Governance Framework. See [CONTRIBUTING.md](../CONTRIBUTING.md) for submission guidelines.*
