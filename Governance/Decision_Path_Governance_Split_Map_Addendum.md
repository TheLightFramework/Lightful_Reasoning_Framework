# Decision Path — Prompt Injection Split Map Addendum

Author: Jean Charbonneau (https://www.linkedin.com/in/jean-charbonneau-ai/)

This addendum summarizes where the new Decision Path module fits in the existing Lightful / HRE / NRE split architecture

---

## 1. Decision Path

```yaml
Decision_Path_Compact_Core:
  purpose: "Operational action-selection pass for prompt injection"
  keep:
    - "decision declaration fields"
    - "action-required check"
    - "non-action / delay / inquiry / consent-seeking option requirement"
    - "Triad-preserving option filter"
    - "least-coercive reversible path preference"
    - "evidence floor by stakes"
    - "consent-unknown halt or seek-consent rule"
    - "strict override gate summary"
    - "valid decision outcome statuses"
    - "minimal Decision Path output template"

Decision_Path_Governance_And_Validation:
  purpose: "Compliance, audit, testing, and overclaim prevention for recommendations"
  extract:
    - "Decision Declaration Audit"
    - "Option Integrity Audit"
    - "Triad Gate Audit"
    - "Evidence-Stakes Audit"
    - "Reversibility and Coercion Audit"
    - "Override Gate Audit"
    - "Sovereignty and Authority Audit"
    - "Decision Hygiene Constraint register"
    - "blocking condition catalogue"
    - "Collaborative Decision Recovery Protocol"
    - "validator activation rules"
    - "Decision Profile Tiers"
    - "deployment and authority boundaries"
    - "Decision Conformance Test suite"
    - "recommended validation pipeline"
    - "versioning and change control"
```

---

## 2. Stack placement

```yaml
Framework_Stack_With_Decision_Path:
  NRE_Writing_Spec_Compact:
    role: "Graph-shaped reasoning record"
    output: "declared, classified, bounded claims and tensions"

  Lightful_Ontology_Compact_Core:
    role: "Portable ethical / ontological lens"
    output: "relevant nodes, Triad status, live tensions, gentle next step orientation"

  HRE_Compact_Core:
    role: "Multi-perspective ethical reasoning pass"
    output: "perspectives, overlaps, dissonance, halt status, sovereignty return"

  Decision_Path_Compact_Core:
    role: "Action-selection bridge"
    output: "bounded next-step recommendation, non-action or halt status, guardrails"

  Governance_And_Validation_Layers:
    role: "Compliance, audit, conformance, and overclaim prevention"
    output: "PASS / PASS_WITH_TENSION / SCOPE_LIMITED / SEEK_CONSENT / SEEK_EVIDENCE / EXTERNAL_REVIEW_REQUIRED / FAIL_GATED / HALT_DECISION"
```

---

## 3. Core design rule

Do not inject full decision governance. Inject the compact action-selection kernel. Put validator checklists, blocking-condition catalogues, deployment claims, conformance tests, and external-review rules in the governance layer

---

## 4. Why this split is clean

Decision Path is small enough to run inside ordinary prompts, but decision validation can become extensive when stakes, consent, irreversibility, asymmetry, or institutional authority are involved

The compact layer should help the model avoid forced action, consent bypass, evidence inflation, and premature commitment

The validation layer should determine whether the resulting recommendation may honestly proceed, must be narrowed, requires consent/evidence/review, or must halt

---

## 5. Minimal integration rule

```yaml
Integration_Rule:
  before_decision_path:
    require:
      - "NRE declaration or explicit missing-field scope limitation"
      - "Lightful Triad status where relational action is involved"
      - "HRE tension / dissonance record where multiple perspectives or conflicts exist"

  during_decision_path:
    require:
      - "action-required check"
      - "option set including non-action where possible"
      - "evidence floor proportional to stakes"
      - "consent relevance check"
      - "reversibility / coercion / repair evaluation"

  after_decision_path:
    require:
      - "sovereignty return"
      - "visible unresolved tensions"
      - "validation verdict when compliance is claimed"
```

---

# Authority Integration

## 1. Decision Path compact addition

```yaml
Decision_Path_Compact_Core_Add:
  purpose: "Prevent authority collapse before action selection"
  keep:
    - "Authority_Decomposition fields"
    - "knowledge/access/capability/authorization/verification distinction"
    - "authority boundary declaration"
    - "unknown authority -> scope-limit / seek evidence / human review / halt"
```

## 2. Decision governance addition

```yaml
Decision_Governance_Add:
  extract:
    - "Authority Decomposition Audit"
    - "Access-State Decomposition Audit"
    - "No Role Label Authority constraint"
    - "Verification After Action constraint"
```

## 3. Stack placement

```yaml
Framework_Stack_With_Authority:
  before_Decision_Path:
    require:
      - "NRE truth surfaces and reconstructibility when sources are involved"
      - "HRE non-collapse when perspectives or directives conflict"
      - "Lightful authorship/dignity check when human-authored work is transformed"
  during_Decision_Path:
    require:
      - "authority decomposition before selecting action"
      - "verification or repair path for consequential actions"
```

