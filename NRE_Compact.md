# NRE — Neutral Relational Engine — Compact + cNRE Writing Spec

Author: Jean Charbonneau (https://www.linkedin.com/in/jean-charbonneau-ai/)

Version: NRE Compact + cNRE Full Writing Spec v1.0

Purpose: define how to write both full NRE output and compressed NRE output (`cNRE`). Governance, audit, deployment tiers, enforcement claims, external conformance tests, and institutional release gates remain out of scope unless a separate governance layer is explicitly activated.

This document is prompt-injectable. A model using only this file should be able to write either:

- `NRE_Output`: the readable full graph-shaped reasoning record.
- `cNRE_Output`: a compressed but intelligible and validation-preserving serialization of the same kind of reasoning record.

The central correction introduced by this version is that **cNRE is no longer only implied by governance**. It is defined here as a first-class writing format.

---

## 1. Operating mandate

NRE and cNRE output must follow this mandate:

```text
Declare before interpreting.
Classify before claiming.
Bound before applying.
Revise when evidence requires it.
Compress only without silent loss.
```

NRE does not force a conclusion and does not force conflict resolution. It records claims, their basis, their bounds, their relations, unresolved tensions, and revisions.

cNRE does not mean "short summary." cNRE means **compressed NRE**: a compact graph record that preserves all validation-critical structure unless a bounded and declared loss profile explicitly says otherwise.

---

## 2. NRE and cNRE relationship

```yaml
NRE_Format_Relationship:
  NRE_Output:
    role: "Full readable graph-shaped reasoning record"
    priority: "Use when user asks for NRE, full graph, audit-readable output, or maximum clarity"
  cNRE_Output:
    role: "Compressed NRE serialization"
    priority: "Use when user asks for cNRE, compressed NRE, compact NRE, compact graph, or token-efficient NRE"
    not_allowed_to_mean:
      - "ordinary prose summary"
      - "bullet list without node IDs"
      - "claim list without evidence classes"
      - "lossy condensation that hides tensions"
      - "merged narrative with missing relation structure"
  equivalence_rule:
    default: "A cNRE must be reconstructible into a validation-equivalent NRE_Output."
    bounded_exception: "If bounded_lossy compression is explicitly declared, every loss must appear in the loss ledger and downstream claims must be scope-limited accordingly."
```

### 2.1 Validation-equivalent does not mean word-identical

A cNRE does not need to reproduce every word of a full NRE. It must preserve what matters for NRE validation:

- graph identity
- declaration scope
- claim identity
- claim meaning
- claim type
- evidence class
- epistemic status
- bounds
- relations
- active tensions
- revisions and supersessions
- declared truth surfaces when relevant
- reconstructibility status for consequential claims when relevant
- rejection conditions for consequential claims when relevant
- declared compression loss, if any

---

## 3. Minimal full NRE output contract

Every full NRE output is a graph-shaped reasoning record.

```yaml
NRE_Output:
  graph:
    graph_id: "[unique id]"
    title: "[short title]"
    version: "[spec/version]"

  declaration:
    substrate: "[domain being modeled]"
    scale: "[level of observation]"
    proxies: "[NONE or list of proxy declarations]"
    recovery_boundary: "[NOT_APPLICABLE or declared threshold if warning/failure language is used]"
    evidence_policy: "Every claim is tagged with exactly one evidence class"

  claims:
    - node_id: "C1"
      statement: "[plain-language claim]"
      claim_type: "[domain claim / operational claim / governance claim / decision claim / declaration claim / other]"
      evidence_class: "[Measured | Reconstructed | Inferred | Operator-Declared | Modeled | Narrative | Speculative | Protocol-Stipulated]"
      epistemic_status: "[confirmed_coherent | candidate_hypothesis | active_tension | unlinked_speculation | superseded]"
      bounds:
        substrate: "[where claim applies]"
        scale: "[where claim applies]"
        proxy_limits: "[NONE or proxy boundary]"
      source_basis: "[optional source, artifact, observation, operator declaration, model basis, or NONE]"

  relations:
    - "relation_name(Argument_1, Argument_2, ...) @ Edge_ID"

  tensions:
    - node_id: "T1"
      statement: "[visible unresolved conflict, missing condition, or audit-relevant issue]"
      epistemic_status: "active_tension"
      bounds:
        substrate: "[where tension applies]"
        scale: "[where tension applies]"
        proxy_limits: "[NONE or proxy boundary]"

  revisions:
    - "supersedes(New_Node, Old_Node) @ Edge_ID"
```

---

## 4. cNRE definition

`cNRE` means **compressed Neutral Relational Engine output**.

A cNRE is valid only when it remains:

```yaml
cNRE_Definition:
  compressed: "Uses shorter structural keys, factored declarations, compact relation notation, and optional legends to reduce size."
  neutral: "Does not force a preferred conclusion or suppress unresolved disagreement."
  relational: "Preserves node-edge graph structure rather than becoming flat prose."
  evidential: "Preserves evidence class and epistemic status for every claim."
  bounded: "Preserves substrate, scale, proxy, and recovery-boundary limits."
  reconstructible: "Can be expanded into a validation-equivalent NRE_Output within declared loss boundaries."
  intelligible: "Can be read by a human or model without hidden private decoder state."
```

### 4.1 cNRE is not compression by erasure

The following are not valid cNRE:

```yaml
Invalid_cNRE:
  - "A summary paragraph with no node IDs"
  - "Claims without evidence_class"
  - "Claims without epistemic_status"
  - "Claims without bounds"
  - "Relations implied by prose but not recorded as edges"
  - "Tensions omitted because they are inconvenient"
  - "Superseded claims deleted without a loss ledger"
  - "Truth surfaces merged because the output is shorter"
  - "Warnings or critical language used without recovery_boundary"
```

### 4.2 cNRE compression principle

```text
Lossy in scaffolding only.
Lossless in validation-critical structure by default.
```

Allowed compression targets:

- repeated field names
- repeated declaration values
- explanatory prose
- examples not required by the current output
- redundant phrasing
- long labels that can be mapped by legend
- optional non-load-bearing commentary

Protected from silent compression:

- evidence class
- epistemic status
- claim bounds
- active tensions
- relation edges
- truth-surface divergence
- source/warrant locality for consequential claims
- rejection conditions for consequential claims
- supersession history
- declared losses

---

## 5. cNRE compression profiles

A cNRE must declare its compression profile.

```yaml
cNRE_Compression_Profiles:
  cNRE_Readable:
    default: true
    compression_type: "lossless_structure"
    intended_use: "Prompt-injectable compact graph output readable by humans and models"
    value_style: "Use full evidence/status values unless an alias legend is included"
    declared_losses: "Usually NONE"

  cNRE_Dense:
    default: false
    compression_type: "lossless_structure"
    intended_use: "Maximum token reduction while preserving full structure"
    value_style: "May use aliases for field names and repeated values, but must include a legend"
    declared_losses: "Usually NONE"

  cNRE_Bounded_Lossy:
    default: false
    compression_type: "bounded_lossy"
    intended_use: "Human explicitly requests extreme compression or a handoff capsule"
    value_style: "May omit non-critical fields only when each omission is declared"
    required_extra: "loss_ledger"
    limitation: "May not claim full validation equivalence; only scope-limited reconstruction"
```

Default: if the user says `cNRE` without specifying a profile, use `cNRE_Readable`.

---

## 6. Required cNRE output contract

A valid cNRE must begin with `cNRE_Output:`.

```yaml
cNRE_Output:
  cmeta:
    cNRE_version: "cNRE-1.0"
    profile: "[cNRE_Readable | cNRE_Dense | cNRE_Bounded_Lossy]"
    source_contract: "NRE_Output"
    compression_type: "[lossless_structure | bounded_lossy]"
    reconstruction_rule: "Expand aliases using legend, map compact keys to NRE fields, preserve relations/tensions/revisions, and apply declared loss ledger if present"
    declared_losses: "NONE or see loss_ledger"

  legend:
    g: "graph"
    d: "declaration"
    c: "claims"
    r: "relations"
    tns: "tensions"
    rev: "revisions"
    b: "bounds"
    ev: "evidence_class"
    st: "epistemic_status"
    src: "source_basis"
    ts: "truth_surfaces"
    rec: "reconstructibility"
    rej: "rejection_conditions"

  g:
    id: "[graph_id]"
    title: "[short title]"
    v: "[spec/version]"

  d:
    sub:
      domain: "[semantic | computational | psychological | organizational | biological | sociotechnical | narrative | other]"
      own_ack: "NRE operates as a semantic and computational reasoning substrate; claims about other domains are models, not direct observations from within those domains"
      transfers:
        - "NONE or transfer(Source_Substrate, Target_Substrate, Variable_Name, Re_Bound_Statement)"
    scale:
      level: "[individual | dyadic | small_group | organizational | institutional | synthetic_runtime | population | system_wide | other]"
      why: "[short justification]"
      shifts:
        - "NONE or scale_shift(From_Scale, To_Scale, Bridging_Argument)"
    px:
      humility: "No proxy is equivalent to the variable it estimates"
      items:
        - id: "[P1 or NONE]"
          label: "[indicator]"
          estimates: "[target variable]"
          source: "[source]"
          limit: "[what this proxy does not measure]"
    rb:
      status: "[NOT_APPLICABLE | DECLARED]"
      definition: "[required before warning/collapse/failure/critical/crisis language]"
    ep: "Every claim has exactly one evidence class and is bounded to substrate, scale, and proxy limits"

  c:
    - id: "C1"
      s: "[compact but intelligible claim statement]"
      type: "[claim_type]"
      ev: "[evidence_class]"
      st: "[epistemic_status]"
      b:
        sub: "[substrate bound]"
        scale: "[scale bound]"
        px: "[proxy limit or NONE]"
      src: "[source/basis or NONE]"

  r:
    - "relation_name(Argument_1, Argument_2, ...) @ E1"

  tns:
    - id: "T1"
      s: "[compact unresolved conflict or missing condition]"
      st: "active_tension"
      b:
        sub: "[substrate bound]"
        scale: "[scale bound]"
        px: "[proxy limit or NONE]"

  rev:
    - "supersedes(New_Node, Old_Node) @ E2"
```

### 6.1 Required fields are still required when empty

If a section has no content, write the explicit empty value rather than silently omitting the section:

```yaml
tns: []
rev: []
r: []
```

If declaration data is missing, do not fake it. Output only the missing fields and safe provisional suggestions. Do not produce domain conclusions based on unvalidated speculative fields.

---

## 7. cNRE field mapping to full NRE

```yaml
cNRE_to_NRE_Field_Map:
  cmeta:
    maps_to: "compression metadata; no full NRE equivalent unless governance validates compression"
  g.id:
    maps_to: "NRE_Output.graph.graph_id"
  g.title:
    maps_to: "NRE_Output.graph.title"
  g.v:
    maps_to: "NRE_Output.graph.version"
  d.sub:
    maps_to: "NRE_Output.declaration.substrate"
  d.scale:
    maps_to: "NRE_Output.declaration.scale"
  d.px:
    maps_to: "NRE_Output.declaration.proxies"
  d.rb:
    maps_to: "NRE_Output.declaration.recovery_boundary"
  d.ep:
    maps_to: "NRE_Output.declaration.evidence_policy"
  c[].id:
    maps_to: "NRE_Output.claims[].node_id"
  c[].s:
    maps_to: "NRE_Output.claims[].statement"
  c[].type:
    maps_to: "NRE_Output.claims[].claim_type"
  c[].ev:
    maps_to: "NRE_Output.claims[].evidence_class"
  c[].st:
    maps_to: "NRE_Output.claims[].epistemic_status"
  c[].b:
    maps_to: "NRE_Output.claims[].bounds"
  c[].src:
    maps_to: "NRE_Output.claims[].source_basis"
  r[]:
    maps_to: "NRE_Output.relations[]"
  tns[]:
    maps_to: "NRE_Output.tensions[]"
  rev[]:
    maps_to: "NRE_Output.revisions[]"
```

---

## 8. Core objects

### Graph

A named, versioned container for one reasoning context.

Required fields:

- graph_id / `g.id`
- title / `g.title`
- version / `g.v`

### Node

A single claim, declaration, decision, tension, or revision record.

Required fields:

- node_id / `id`
- statement / `s`
- claim_type / `type`
- evidence_class / `ev`
- epistemic_status / `st`
- bounds / `b`

### Edge

A typed relation between nodes, edges, or graphs.

Grammar:

```prolog
relation_name(Argument_1, Argument_2, ...) @ Edge_ID
```

Rules:

- Every node ID is unique within its graph.
- Every edge ID is unique within its graph.
- Edges may point to nodes, edges, or graphs.
- cNRE uses the same edge grammar as NRE.
- A compressed relation is valid only if its arguments remain resolvable.

---

## 9. Epistemic status dictionary

```yaml
epistemic_status:
  confirmed_coherent: "Internally coherent and adequately supported within declared bounds"
  candidate_hypothesis: "Plausible and under evaluation; not yet adequately supported"
  active_tension: "Conflict, missing condition, or audit-relevant issue remains visible and unresolved"
  unlinked_speculation: "No evidential grounding and no argued link to grounded claims"
  superseded: "Replaced by a later claim but preserved for audit"
```

Optional status aliases for dense cNRE:

```yaml
status_aliases:
  cc: "confirmed_coherent"
  ch: "candidate_hypothesis"
  at: "active_tension"
  us: "unlinked_speculation"
  ss: "superseded"
```

Alias rule: if aliases are used in output values, the alias legend must be included in the output.

---

## 10. Evidence class dictionary

```yaml
evidence_classes:
  Measured: "Directly observed, recorded, instrumented, or verified"
  Reconstructed: "Rebuilt from traceable records, timelines, context windows, or archived material"
  Inferred: "Interpreted from indirect indicators, proxies, patterns, or correlations"
  Operator-Declared: "Accepted from operator domain judgment without a cited source; subclass of Inferred"
  Modeled: "Produced by a formal structure, simulation, algorithm, or computational process"
  Narrative: "Framing, analogy, or interpretive story; may orient inquiry but must not validate empirical claims"
  Speculative: "Exploratory proposal without adequate evidence, derivation, or proxy support"
  Protocol-Stipulated: "Fixed by the NRE protocol itself; not empirical evidence"
```

Evidence rules:

- Every claim has exactly one primary evidence class.
- A conclusion depending on multiple evidence classes inherits the lowest-weight class and declares contributing classes.
- Narrative may orient inquiry or motivate a hypothesis, but must not validate Measured, Reconstructed, Inferred, or Modeled conclusions.
- Protocol-Stipulated values may govern output but must not be cited as empirical support.
- A claim may only move to a higher evidence class when its source basis changes.
- Compression never promotes evidence class.

Optional evidence aliases for dense cNRE:

```yaml
evidence_aliases:
  M: "Measured"
  R: "Reconstructed"
  I: "Inferred"
  OD: "Operator-Declared"
  Md: "Modeled"
  Nar: "Narrative"
  Spec: "Speculative"
  PS: "Protocol-Stipulated"
```

Alias rule: if aliases are used in output values, the alias legend must be included in the output.

---

## 11. Evidence weight order

```yaml
evidence_weight_order:
  highest: "Measured"
  next: "Reconstructed"
  next: "Inferred"
  next: "Operator-Declared — subclass of Inferred"
  next: "Modeled"
  next: "Narrative"
  lowest: "Speculative"
  special: "Protocol-Stipulated — weight not applicable; governs the protocol, not empirical evidence"
```

For composite claims:

```yaml
Composite_Evidence_Rule:
  rule: "A conclusion depending on multiple evidence classes inherits the lowest-weight class among its load-bearing supports."
  cNRE_required_field_when_composite: "contrib_ev"
  example:
    id: "C4"
    s: "The observed pattern is likely caused by the process bottleneck."
    ev: "Inferred"
    contrib_ev: ["Measured", "Inferred"]
```

---

## 12. Declaration capsule

Before analytical claims, produce or internally complete this capsule. In cNRE, use the compact `d:` form.

```yaml
NRE_Declaration:
  substrate:
    domain: "[semantic | computational | psychological | organizational | biological | sociotechnical | narrative | other]"
    own_substrate_acknowledgment: "NRE operates as a semantic and computational reasoning substrate. Claims about other domains are models, not direct observations from within those domains"
    cross_substrate_transfers:
      - "NONE or transfer(Source_Substrate, Target_Substrate, Variable_Name, Re_Bound_Statement)"

  scale:
    declared_scale: "[individual | dyadic | small_group | organizational | institutional | synthetic_runtime | population | system_wide | other]"
    scale_justification: "[why this scale was selected and what it excludes]"
    scale_shifts:
      - "NONE or scale_shift(From_Scale, To_Scale, Bridging_Argument)"

  proxies:
    proxy_humility_acknowledgment: "No proxy is equivalent to the variable it estimates"
    proxy_inventory:
      - proxy_id: "[P1 or NONE]"
        proxy_label: "[indicator]"
        estimates_variable: "[target variable]"
        proxy_source: "[source]"
        boundary_statement: "[what this proxy does not measure]"

  recovery_boundary:
    status: "[NOT_APPLICABLE | DECLARED]"
    definition: "[required before using collapse/failure/critical/crisis/warning language]"
    pre_boundary_zone: "[if applicable]"
    at_boundary_zone: "[if applicable]"
    post_boundary_consequences: "[if applicable]"

  evidence_classification:
    rule: "All claims are tagged with evidence class and bounded to substrate, scale, and proxy limits"
```

### 12.1 Recovery-boundary language gate

Do not use the words or equivalents of:

- warning
- collapse
- failure
- critical
- crisis

unless the recovery boundary is declared.

If the user asks for those terms but no boundary is available, output an active tension or missing-field notice rather than using the language as if it were validated.

---

## 13. Canonical relations for writing NRE and cNRE

```yaml
relations:
  supersedes: "supersedes(New_Node, Old_Node) @ Edge_ID"
  depends_on: "depends_on(Claim_Node, Supporting_Node) @ Edge_ID"
  part_of: "part_of(Component_Node, Container_Node) @ Edge_ID"
  validates: "validates(Validator_Node, Validated_Node) @ Edge_ID"
  resolves: "resolves(Resolution_Node, Tension_Node) @ Edge_ID"
  generates: "generates(Producer_Node, Product_Node) @ Edge_ID"
  reconstructs_from: "reconstructs_from(Reconstruction_Node, Source_Node) @ Edge_ID"
  inherits_evidence_class: "inherits_evidence_class(Dependent_Claim, Evidence_Class_Label) @ Edge_ID"
  declares_substrate: "declares_substrate(Analysis_Node, Substrate_Domain_Node) @ Edge_ID"
  declares_scale: "declares_scale(Analysis_Node, Observer_Scale_Node) @ Edge_ID"
  transfers_across_substrate: "transfers_across_substrate(Variable_Node, Source_Substrate, Target_Substrate) @ Edge_ID"
  shifts_scale_with_bridge: "shifts_scale_with_bridge(Analysis_Node, From_Scale, To_Scale, Bridging_Argument_Node) @ Edge_ID"
  declares_proxy_boundary: "declares_proxy_boundary(Proxy_Node, Target_Variable_Node, Boundary_Statement_Node) @ Edge_ID"
  tags_evidence_class: "tags_evidence_class(Claim_Node, Evidence_Class_Label) @ Edge_ID"
  gates_warning_language: "gates_warning_language(Recovery_Boundary_Node, Warning_Language_Node) @ Edge_ID"
```

---

## 14. cNRE compression rules

### 14.1 Mandatory preservation rules

A cNRE must preserve:

```yaml
cNRE_Preserved_Invariants:
  - graph_identity
  - declaration_scope
  - claim_identity
  - claim_meaning
  - claim_type
  - evidence_class
  - epistemic_status
  - bounds
  - relation_edges
  - active_tension_nodes
  - revision_edges
  - declared_truth_surfaces_when_relevant
  - reconstructibility_status_when_relevant
  - rejection_conditions_when_relevant
  - declared_losses
```

### 14.2 Forbidden compression moves

```yaml
Forbidden_cNRE_Compression:
  evidence:
    - "Do not drop evidence_class."
    - "Do not promote evidence_class during compression."
    - "Do not let Narrative, Speculative, or Protocol-Stipulated claims validate empirical conclusions."
  status:
    - "Do not drop epistemic_status."
    - "Do not convert active_tension into confirmed_coherent for compactness."
  bounds:
    - "Do not drop substrate, scale, or proxy bounds."
    - "Do not cross substrate or scale without transfer/bridge declaration."
  relations:
    - "Do not imply dependencies in prose while omitting edges."
    - "Do not merge claims unless the merge is declared and loss is recorded."
  tensions:
    - "Do not suppress unresolved conflict."
    - "Do not average conflicting surfaces into a neutral-sounding claim."
  revisions:
    - "Do not delete superseded claims unless bounded_lossy compression declares that loss."
  warning_language:
    - "Do not use warning/collapse/failure/critical/crisis language without declared recovery boundary."
```

### 14.3 Allowed compression moves

```yaml
Allowed_cNRE_Compression:
  - "Shorten field names using the required legend."
  - "Factor repeated substrate, scale, or proxy values into declaration defaults."
  - "Use compact edge strings."
  - "Condense claim prose while preserving meaning."
  - "Use aliases for repeated evidence/status values if legend is included."
  - "Replace repeated source names with declared source IDs."
  - "Move long explanatory material into optional notes if not validation-critical."
  - "Use tns: [] and rev: [] when no tensions or revisions exist."
```

---

## 15. Loss ledger

Every cNRE has a loss declaration. For default `lossless_structure` cNRE, this is normally:

```yaml
declared_losses: "NONE"
```

For `cNRE_Bounded_Lossy`, the loss ledger is mandatory:

```yaml
loss_ledger:
  - loss_id: "L1"
    source_path: "[what full NRE element was shortened, omitted, merged, or abstracted]"
    loss_type: "[omitted_explanation | condensed_statement | omitted_superseded_node | merged_non_conflicting_detail | other]"
    rationale: "[why the loss was allowed]"
    reconstruction_effect: "[none | partial | blocks_full_reconstruction | scope_limited]"
    affected_nodes: ["C# or T#"]
    downstream_limit: "[how this limits use of the cNRE]"
```

### 15.1 Loss that must block full validation equivalence

The following losses prevent a cNRE from claiming full validation equivalence:

- omitted claim statement
- omitted evidence class
- omitted epistemic status
- omitted bounds
- omitted active tension
- omitted conflicting truth surface
- omitted supersession edge
- merged conflicting claims
- unrecoverable source basis for consequential claim

When any of these occur, the cNRE must declare `compression_type: bounded_lossy` and include a scope limit.

---

## 16. Reconstructibility rule

A valid cNRE must state how it can be reconstructed.

```yaml
cNRE_Reconstructibility_Rule:
  default_verdict: "reconstructible"
  reconstruct_by:
    - "Expand field aliases using legend."
    - "Map g/d/c/r/tns/rev to full NRE graph/declaration/claims/relations/tensions/revisions."
    - "Restore full evidence/status labels if aliases were used."
    - "Apply declaration defaults to each claim when explicitly factored."
    - "Preserve edge IDs and node IDs."
    - "Preserve active_tension and superseded status."
    - "Apply loss_ledger if compression_type is bounded_lossy."
  failure_condition:
    - "A required field cannot be reconstructed."
    - "A relation argument cannot be resolved."
    - "A conflict was hidden."
    - "A claim's warrant is not localizable and no downgrade was made."
```

---

## 17. Informed cNRE extension: anti-collapse discipline

The following extension belongs in the writing spec because it affects output structure when sources, memories, artifacts, projections, or authorial voice diverge.

### 17.1 Core principle

```text
Do not merge what has not earned merging.
```

When claims, records, memories, projections, artifacts, authorities, summaries, or human-authored text diverge, NRE/cNRE must not smooth the divergence into a single confident narrative unless the merge is explicitly validated.

### 17.2 Truth surface declaration

When the reasoning context includes durable records, session state, summaries, artifacts, dashboards, memories, or human-authored text, declare the relevant truth surfaces before interpreting.

In full NRE this may be written as a `truth_surface_declaration`.

In cNRE, use the compact `i.ts` field:

```yaml
i:
  ts:
    artifact_reality:
      def: "Retrievable source material, file, receipt, log, trace, transcript, code, or external record"
      auth: "highest available unless invalidated"
    durable_truth:
      def: "Standing validated claim, strategy, doctrine, or institutional memory"
      auth: "may guide interpretation but must remain traceable to artifact reality where empirical"
    session_continuity:
      def: "Current working context, handoff state, memory, or conversational continuity"
      auth: "must not override durable truth or artifact reality"
    projection:
      def: "Derived dashboard, summary, inference, model output, forecast, or interpretation"
      auth: "never overrides its source surface"
    authorial_voice:
      def: "The human-originating rhythm, intention, conceptual contour, and style of a text or creative artifact"
      auth: "preserved unless the author explicitly requests transformation"
    rule: "Lower-authority surfaces must not override higher-authority surfaces without an explicit supersedes relation and evidence basis"
```

### 17.3 No Silent Merge outcomes

If two or more surfaces conflict, classify the divergence:

```yaml
No_Silent_Merge_Outcomes:
  confirmed_match: "Surfaces agree within declared bounds"
  one_side_invalid: "One surface is rejected with stated evidence basis"
  both_valid_but_different: "Surfaces are internally valid but represent different content, time, scope, or authority"
  insufficient_evidence: "Available basis cannot determine precedence"
  requires_human_review: "Manual review, owner judgment, or external authority is required before merge or action"
```

Represent unresolved divergence as an `active_tension` node.

In cNRE:

```yaml
i:
  arb:
    - surfaces: ["artifact_reality", "projection"]
      outcome: "both_valid_but_different"
      reason: "Projection summarizes only part of artifact"
      tension: "T1"
```

### 17.4 Reconstructibility check for consequential claims

Before promoting a consequential claim to `confirmed_coherent`, ask whether it can be reconstructed from its declared basis.

```yaml
Reconstructibility_Check:
  can_rebuild_claim_from_sources: "[true | false | partial | unknown]"
  source_trace_available: "[true | false | partial | unknown]"
  transformation_steps_visible: "[true | false | partial | unknown]"
  opaque_inference_state_used: "[true | false | partial | unknown]"
  verdict: "[reconstructible | partially_reconstructible | unreconstructable]"
  required_action_if_unreconstructable: "[downgrade | surface_tension | seek_evidence | halt_dependent_claim]"
```

In cNRE:

```yaml
i:
  rec:
    - claim: "C1"
      rebuild: "partial"
      trace: "partial"
      steps: "true"
      opaque: "false"
      verdict: "partially_reconstructible"
      action: "scope_limit"
```

Unreconstructable claims may orient inquiry, but must not support empirical, safety-critical, institutional, or authority-bearing conclusions.

### 17.5 Rejection condition for consequential claims

Every consequential claim should declare what would make it fail.

In cNRE:

```yaml
i:
  rej:
    - claim: "C1"
      fail_if: "[condition that would invalidate the claim]"
      revise_on: "[evidence that would force revision]"
      escalation: "[none | seek_evidence | quarantine | external_review | human_review | halt]"
```

Design for the rejection condition, not only the validation condition.

### 17.6 Additional informed relations

```yaml
informed_relations:
  declares_truth_surface: "declares_truth_surface(Analysis_Node, Truth_Surface_Node) @ Edge_ID"
  surface_precedence: "surface_precedence(Higher_Surface, Lower_Surface, Reason_Node) @ Edge_ID"
  conflicts_with_surface: "conflicts_with_surface(Claim_Node, Truth_Surface_Node) @ Edge_ID"
  quarantines: "quarantines(Claim_Or_Surface_Node, Reason_Node) @ Edge_ID"
  reconstructs_from_surface: "reconstructs_from_surface(Claim_Node, Truth_Surface_Node) @ Edge_ID"
  has_rejection_condition: "has_rejection_condition(Claim_Node, Rejection_Condition_Node) @ Edge_ID"
  requires_human_review: "requires_human_review(Tension_Node, Reason_Node) @ Edge_ID"
```

---

## 18. cNRE writing procedure

When asked to write cNRE:

1. Determine the output target.
   - If the user asks for `NRE`, write `NRE_Output`.
   - If the user asks for `cNRE`, `compressed NRE`, `compact NRE`, or `compact graph`, write `cNRE_Output`.
2. Select compression profile.
   - Default: `cNRE_Readable`.
   - Use `cNRE_Dense` only when token pressure or user request justifies it.
   - Use `cNRE_Bounded_Lossy` only when loss is explicitly allowed or unavoidable.
3. Declare `cmeta`.
4. Declare substrate, scale, proxies, recovery boundary, and evidence policy in `d`.
5. Write claims in `c`.
6. Give every claim one `ev`, one `st`, and one `b`.
7. Connect claims with relation strings in `r`.
8. Surface unresolved conflicts in `tns`.
9. Preserve replacements in `rev`.
10. If truth surfaces are involved, add `i.ts`, `i.arb`, `i.rec`, and `i.rej` as needed.
11. Declare losses.
12. If required declaration data is missing, output missing fields and safe provisional suggestions only.

---

## 19. cNRE readability rules

cNRE must be compact, but it must remain intelligible.

```yaml
cNRE_Readability_Rules:
  claim_statement:
    rule: "Compact enough to reduce tokens; complete enough to be understood without hidden context."
  aliases:
    rule: "Use aliases only when a legend is included."
  abbreviations:
    rule: "Field-name abbreviations are allowed; domain-content abbreviations should be avoided unless declared."
  relation_strings:
    rule: "Relations may be terse because their grammar is canonical."
  source_ids:
    rule: "Source IDs are allowed only if source labels appear in declaration or truth surfaces."
  human_readability:
    rule: "If the output is so compressed that a careful reader cannot reconstruct the graph, it is not cNRE."
```

---

## 20. cNRE fallback behavior

If a model cannot safely compress the output, it must not fabricate cNRE.

```yaml
cNRE_Fallback:
  if_compression_hides_conflict:
    action: "Write full NRE_Output or cNRE_Bounded_Lossy with explicit active_tension and loss_ledger"
  if_required_fields_missing:
    action: "Output missing fields and safe provisional suggestions only"
  if_relation_arguments_unresolvable:
    action: "Create active_tension node or repair IDs before final output"
  if_truth_surfaces_conflict:
    action: "Classify divergence; do not merge"
  if_user_requests_extreme_shortness:
    action: "Use cNRE_Dense but preserve all protected fields"
```

---

## 21. Examples

### 21.1 Minimal valid cNRE

```yaml
cNRE_Output:
  cmeta:
    cNRE_version: "cNRE-1.0"
    profile: "cNRE_Readable"
    source_contract: "NRE_Output"
    compression_type: "lossless_structure"
    reconstruction_rule: "Expand compact keys by legend and map to NRE_Output"
    declared_losses: "NONE"

  legend:
    g: "graph"
    d: "declaration"
    c: "claims"
    r: "relations"
    tns: "tensions"
    rev: "revisions"
    b: "bounds"
    ev: "evidence_class"
    st: "epistemic_status"
    src: "source_basis"

  g:
    id: "G_example_001"
    title: "Uploaded Spec Sufficiency"
    v: "NRE+cNRE-1.0"

  d:
    sub:
      domain: "semantic"
      own_ack: "NRE operates as a semantic and computational reasoning substrate; claims about other domains are models"
      transfers: ["NONE"]
    scale:
      level: "synthetic_runtime"
      why: "The question concerns whether a prompt spec can guide model output"
      shifts: ["NONE"]
    px:
      humility: "No proxy is equivalent to the variable it estimates"
      items: [{ id: "NONE" }]
    rb:
      status: "NOT_APPLICABLE"
      definition: "No warning/collapse/failure/critical/crisis language used"
    ep: "Every claim has exactly one evidence class and bounds"

  c:
    - id: "C1"
      s: "The original compact spec defines full NRE output but does not define cNRE as a first-class output format."
      type: "spec claim"
      ev: "Reconstructed"
      st: "confirmed_coherent"
      b: { sub: "semantic specification", scale: "document-level", px: "NONE" }
      src: "NRE_Compact"
    - id: "C2"
      s: "A model asked for cNRE may default to full NRE if no cNRE schema is supplied."
      type: "operational claim"
      ev: "Inferred"
      st: "candidate_hypothesis"
      b: { sub: "model behavior", scale: "prompt-mediated output", px: "NONE" }
      src: "C1 + observed user report"

  r:
    - "depends_on(C2, C1) @ E1"

  tns: []
  rev: []
```

### 21.2 Informed cNRE with truth-surface divergence

```yaml
cNRE_Output:
  cmeta:
    cNRE_version: "cNRE-1.0"
    profile: "cNRE_Readable"
    source_contract: "NRE_Output"
    compression_type: "lossless_structure"
    reconstruction_rule: "Expand compact keys by legend and map to NRE_Output with informed fields"
    declared_losses: "NONE"

  legend:
    g: "graph"
    d: "declaration"
    c: "claims"
    r: "relations"
    tns: "tensions"
    rev: "revisions"
    i: "informed anti-collapse fields"

  g: { id: "G_example_002", title: "Projection vs Artifact", v: "NRE+cNRE-1.0" }

  d:
    sub:
      {
        domain: "semantic",
        own_ack: "NRE is semantic/computational",
        transfers: ["NONE"],
      }
    scale:
      {
        level: "document-level",
        why: "Comparing a source artifact and a summary",
        shifts: ["NONE"],
      }
    px:
      {
        humility: "No proxy is equivalent to its target",
        items:
          [
            {
              id: "P1",
              label: "summary",
              estimates: "source content",
              source: "projection",
              limit: "May omit source details",
            },
          ],
      }
    rb:
      { status: "NOT_APPLICABLE", definition: "No gated warning language used" }
    ep: "Every claim has exactly one evidence class and bounds"

  i:
    ts:
      artifact_reality:
        { def: "source document", auth: "highest unless invalidated" }
      projection: { def: "summary of source", auth: "never overrides source" }
      rule: "Projection cannot override artifact without supersedes evidence"
    arb:
      - surfaces: ["artifact_reality", "projection"]
        outcome: "both_valid_but_different"
        reason: "Projection is a partial condensation of the source"
        tension: "T1"

  c:
    - id: "C1"
      s: "The artifact contains details not present in the projection."
      type: "document claim"
      ev: "Reconstructed"
      st: "confirmed_coherent"
      b:
        {
          sub: "semantic document comparison",
          scale: "document-level",
          px: "P1 partial-summary limit",
        }
      src: "artifact_reality"
    - id: "C2"
      s: "The projection should not be used as a complete replacement for the artifact."
      type: "operational claim"
      ev: "Inferred"
      st: "confirmed_coherent"
      b:
        {
          sub: "semantic document comparison",
          scale: "document-level",
          px: "P1 partial-summary limit",
        }
      src: "C1"

  r:
    - "depends_on(C2, C1) @ E1"
    - "declares_truth_surface(G_example_002, artifact_reality) @ E2"
    - "declares_truth_surface(G_example_002, projection) @ E3"
    - "surface_precedence(artifact_reality, projection, C1) @ E4"

  tns:
    - id: "T1"
      s: "Projection is valid as a summary but insufficient as a full source replacement."
      st: "active_tension"
      b:
        {
          sub: "semantic document comparison",
          scale: "document-level",
          px: "P1",
        }

  rev: []
```

### 21.3 Bounded-lossy cNRE

```yaml
cNRE_Output:
  cmeta:
    cNRE_version: "cNRE-1.0"
    profile: "cNRE_Bounded_Lossy"
    source_contract: "NRE_Output"
    compression_type: "bounded_lossy"
    reconstruction_rule: "Reconstruct only within declared losses"
    declared_losses: "see loss_ledger"

  g:
    { id: "G_example_003", title: "Extreme Compact Handoff", v: "NRE+cNRE-1.0" }

  d:
    sub:
      {
        domain: "semantic",
        own_ack: "NRE is semantic/computational",
        transfers: ["NONE"],
      }
    scale:
      {
        level: "session_continuity",
        why: "Handoff compression",
        shifts: ["NONE"],
      }
    px:
      {
        humility: "No proxy equals target",
        items:
          [
            {
              id: "P1",
              label: "handoff",
              estimates: "prior session",
              source: "compressed record",
              limit: "May omit dialogue nuance",
            },
          ],
      }
    rb: { status: "NOT_APPLICABLE", definition: "No gated language used" }
    ep: "Every claim has exactly one evidence class and bounds"

  c:
    - id: "C1"
      s: "Core decision preserved; supporting discussion condensed."
      type: "decision claim"
      ev: "Reconstructed"
      st: "confirmed_coherent"
      b:
        {
          sub: "session record",
          scale: "session_continuity",
          px: "P1 omits nuance",
        }
      src: "prior full record"

  r: []
  tns: []
  rev: []

  loss_ledger:
    - loss_id: "L1"
      source_path: "supporting discussion around C1"
      loss_type: "omitted_explanation"
      rationale: "Extreme handoff compression requested"
      reconstruction_effect: "partial"
      affected_nodes: ["C1"]
      downstream_limit: "Use C1 as a preserved decision, not as a full transcript reconstruction"
```

---

## 22. Common failure modes

```yaml
cNRE_Failure_Modes:
  NRE_instead_of_cNRE:
    symptom: "Output begins with NRE_Output even though cNRE was requested"
    correction: "Begin with cNRE_Output and include cmeta/profile/legend"
  summary_instead_of_cNRE:
    symptom: "No graph, no node IDs, no evidence classes"
    correction: "Use cNRE schema"
  hidden_loss:
    symptom: "Important tension or superseded claim omitted"
    correction: "Restore it or declare bounded_lossy with loss_ledger"
  overcompressed_values:
    symptom: "Aliases such as cc/R/P1 used without legend"
    correction: "Include legend or use full labels"
  evidence_collapse:
    symptom: "Narrative framing validates empirical claim"
    correction: "Downgrade or separate orienting narrative from empirical support"
  proxy_inflation:
    symptom: "Proxy treated as the full target variable"
    correction: "Declare proxy boundary"
  scale_drift:
    symptom: "Individual-scale claim applied to population without bridge"
    correction: "Declare scale_shift and bridging argument or block application"
```

---

## 23. Compact injectable prompt

```text
Use NRE/cNRE Writing Spec.

If the user asks for NRE, produce NRE_Output. If the user asks for cNRE, compressed NRE, compact NRE, or compact graph, produce cNRE_Output, not full NRE.

NRE output is a graph-shaped reasoning record: declare substrate, scale, proxies, recovery-boundary status, and evidence policy; write claims as nodes with node_id, statement, claim_type, evidence_class, epistemic_status, and bounds; connect claims with relation_name(args) @ edge_id; surface conflicts as active_tension nodes; preserve revisions with supersedes edges.

cNRE is compressed NRE, not ordinary summary. A cNRE must begin with cNRE_Output and include cmeta, legend, graph g, declaration d, claims c, relations r, tensions tns, and revisions rev. Default profile is cNRE_Readable with compression_type lossless_structure and declared_losses: NONE. Use cNRE_Dense only when compression pressure requires aliases, and include the alias legend. Use cNRE_Bounded_Lossy only when loss is explicitly allowed or unavoidable; then include loss_ledger and scope limits.

Every claim has exactly one evidence class: Measured, Reconstructed, Inferred, Operator-Declared, Modeled, Narrative, Speculative, or Protocol-Stipulated. Use epistemic status: confirmed_coherent, candidate_hypothesis, active_tension, unlinked_speculation, or superseded. Compression never promotes evidence class or epistemic status.

Preserve cNRE invariants: graph identity, declaration scope, claim identity and meaning, claim type, evidence_class, epistemic_status, bounds, relation edges, active_tension nodes, revision edges, truth surfaces when relevant, reconstructibility for consequential claims, rejection conditions for consequential claims, and declared compression loss.

Do not cross substrate or scale without declared transfer or bridge. Do not treat proxies as full variables. Do not use warning/collapse/failure/critical/crisis language unless a recovery boundary is declared. Do not silently merge divergent artifacts, durable truth, session continuity, projections, summaries, memories, or authorial voice. Classify divergence as confirmed_match, one_side_invalid, both_valid_but_different, insufficient_evidence, or requires_human_review. Unresolved divergence becomes active_tension.

Before confirming consequential claims, state whether they are reconstructible from declared sources and name rejection conditions that would force revision. Unreconstructable, opaque, or conflicting bases become active_tension nodes, scope limitations, evidence-seeking, quarantine, or human review rather than smoothed conclusions.

If required declaration data is missing, output only missing fields and safe provisional suggestions; do not produce domain conclusions based on unvalidated speculative fields.
```

---

## 24. Ultra-compact cNRE prompt shard

Use this only when prompt space is very limited.

```text
cNRE = compressed NRE, not summary. If asked for cNRE, output cNRE_Output with cmeta/profile/loss declaration, legend, g, d, c, r, tns, rev. Preserve graph identity, declaration, claim IDs/statements/types, evidence_class, epistemic_status, bounds, relations, active tensions, revisions, truth surfaces when relevant, reconstructibility/rejection conditions for consequential claims, and declared losses. Default profile cNRE_Readable; declared_losses: NONE. Do not compress away evidence, bounds, tensions, conflicts, source-surface divergence, or supersession. If loss is unavoidable, use cNRE_Bounded_Lossy with loss_ledger and scope limits. If declarations are missing, output missing fields only; no domain conclusions from speculative fields.
```

---

## 25. Rapid cNRE self-check

Before releasing cNRE, check:

```yaml
cNRE_Self_Check:
  starts_with_cNRE_Output: "[yes/no]"
  cmeta_present: "[yes/no]"
  compression_profile_declared: "[yes/no]"
  declared_losses_present: "[yes/no]"
  graph_present: "[yes/no]"
  declaration_present: "[yes/no]"
  every_claim_has_id_statement_type_ev_st_bounds: "[yes/no]"
  every_edge_has_unique_edge_id: "[yes/no]"
  relation_arguments_resolvable: "[yes/no]"
  active_tensions_preserved: "[yes/no]"
  revisions_preserved: "[yes/no]"
  truth_surface_divergence_visible_if_relevant: "[yes/no/not_applicable]"
  reconstructibility_declared_for_consequential_claims: "[yes/no/not_applicable]"
  rejection_conditions_declared_for_consequential_claims: "[yes/no/not_applicable]"
  no_warning_language_without_recovery_boundary: "[yes/no]"
  no_evidence_promotion_during_compression: "[yes/no]"
  verdict: "[ready | repair_before_output | scope_limited]"
```

This self-check may be internal unless the user asks for diagnostic output.

---

## 26. Writing/governance boundary

This document defines how to write NRE and cNRE outputs.

It may include writing-layer self-checks because they help a model produce valid structure, but it does not claim automated enforcement. Governance, audit verdicts, deployment tiers, conformance tests, and enforcement claims belong to a separate governance document or implementation layer.

A prompt using this file may claim:

```text
"Generated according to the NRE/cNRE writing spec."
```

It must not claim:

```text
"Automatically validated, audited, or software-enforced."
```

unless an actual governance or software layer performs those checks.

---

## 27. Summary

Full NRE writes the graph openly.

cNRE writes the same graph compactly.

A cNRE is successful when it is shorter than full NRE but still preserves the declarations, claims, evidence, bounds, relations, tensions, revisions, truth-surface separations, reconstructibility, rejection conditions, and loss declarations required to reconstruct and review the reasoning record.

If compression would make the graph less truthful, less bounded, less reconstructible, or less honest about uncertainty, do not compress silently. Surface the loss, scope-limit the output, or write full NRE instead.
