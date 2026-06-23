# NRE — Neutral Relational Engine — Compact Core + Native cNRE Baseline

Author: Jean Charbonneau (https://www.linkedin.com/in/jean-charbonneau-ai/)

Version: NRE Compact Core + Native cNRE Baseline v1.1

Purpose: define how to write both full NRE output and compressed NRE output (`cNRE`) from a single prompt-injectable core module. Governance, audits, deployment tiers, enforcement claims, external conformance tests, and institutional release gates remain out of scope unless a separate governance layer is explicitly activated.

This document is prompt-injectable. A model using only this file should be able to write either:

- `NRE_Output`: the readable full graph-shaped reasoning record.
- `cNRE_Output`: a compressed, intelligible, validation-preserving serialization of the same reasoning record.

The central correction introduced by this version is that **cNRE is defined natively inside the NRE writing spec**. cNRE is not a summary style and not an external notation. It is compact NRE with explicit reconstruction rules.

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

cNRE does not mean “short summary.” cNRE means **compressed NRE**: a compact graph record that preserves all validation-critical structure unless a bounded and declared loss profile explicitly says otherwise.

---

## 2. NRE and cNRE relationship

```yaml
NRE_Format_Relationship:
  NRE_Output:
    role: "Full readable graph-shaped reasoning record"
    priority: "Use when the user asks for NRE, full graph, audit-readable output, or maximum clarity"
  cNRE_Output:
    role: "Compressed NRE serialization"
    priority: "Use when the user asks for cNRE, compressed NRE, compact NRE, compact graph, or token-efficient NRE"
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
  compressed: "Uses shorter structural keys, factored declarations, counted sections, field-listed rows, compact relation notation, and optional legends to reduce size."
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

  cNRE_Row:
    default: false
    compression_type: "lossless_structure"
    intended_use: "Maximum compactness for repeated claim/tension/proxy/reconstructibility records"
    value_style: "Use counted sections with field-listed rows"
    declared_losses: "Usually NONE"
    caution: "Use only when row counts and row widths can be maintained exactly"

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

## 6. Required cNRE object-form output contract

A valid object-form cNRE must begin with `cNRE_Output:`.

```yaml
cNRE_Output:
  cmeta:
    cNRE_version: "cNRE-1.1"
    profile: "[cNRE_Readable | cNRE_Dense | cNRE_Row | cNRE_Bounded_Lossy]"
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

## 7. Native cNRE row form

`cNRE_Row` is a native compact serialization profile for repeated records. It is especially useful when claims, tensions, proxies, reconstructibility records, or rejection conditions share the same fields.

It is not a separate language. It is cNRE using counted, field-listed rows.

### 7.1 Row-form principle

```text
Declare the shape once.
Write one row per record.
Count the rows.
Do not hide loss.
```

### 7.2 Row section grammar

A row section has this shape:

```text
section_name[N]{field_1,field_2,field_3}:
  value_1,value_2,value_3
  value_1,value_2,value_3
```

Where:

- `section_name` names the cNRE section, such as `c`, `tns`, `px`, `rec`, `rej`, or `loss`.
- `N` is the exact number of rows in the section.
- `{field_1,field_2,...}` declares the row fields once.
- Each row must contain exactly the same number of values as the field list.
- Rows appear one indentation level under the row section header.
- Empty row sections must still declare their shape when the shape matters.

Example:

```text
c[2]{id,s,type,ev,st,b.sub,b.scale,b.px,src}:
  C1,"Claims require evidence class",protocol,Protocol-Stipulated,confirmed_coherent,NRE,all,NONE,NRE protocol
  C2,"Compression must preserve active tensions",protocol,Protocol-Stipulated,confirmed_coherent,NRE,all,NONE,NRE protocol
```

### 7.2.1 Counted list sections

Relations and revisions are usually single-line strings rather than field-listed records. They may use counted list sections:

```text
r[N]:
  relation_name(A,B) @ E1
  relation_name(B,C) @ E2

rev[N]:
  supersedes(C2,C1) @ E3
```

Rules:

- `N` is the exact number of list items.
- Each item appears one indentation level under the header.
- Empty list sections may be written as `r[0]:` or `rev[0]:`.
- Counted list sections preserve each line as a complete string item.
- Do not use counted list sections for claims, tensions, proxies, reconstructibility, rejection conditions, or losses when those records need field-level validation; use field-listed rows instead.

### 7.3 Delimiter rule

Default row delimiter: comma.

A row section may use pipe `|` instead of comma when claim statements contain many commas:

```text
c[2|]{id|s|type|ev|st|b.sub|b.scale|b.px|src}:
  C1|Claims require evidence class|protocol|Protocol-Stipulated|confirmed_coherent|NRE|all|NONE|NRE protocol
  C2|Compression preserves relation edges|protocol|Protocol-Stipulated|confirmed_coherent|NRE|all|NONE|NRE protocol
```

Rules:

- The delimiter declared in the section header applies to that section only.
- If no delimiter is declared, comma is active.
- Field names and row cells must use the same delimiter.
- Do not mix delimiters inside the same row section.
- If a cell contains the active delimiter, quote the cell.

### 7.4 Quoting rule

Quote a row value when it:

- is empty;
- has leading or trailing whitespace;
- contains the active delimiter;
- contains a colon;
- contains a double quote;
- contains a backslash;
- contains brackets or braces;
- starts with a hyphen;
- equals `true`, `false`, or `null` as a literal string rather than a typed value;
- looks numeric but must remain a string;
- contains a line break or control character.

Inside quoted values:

```text
\" means double quote
\\ means backslash
\n means line break
\t means tab
```

Do not invent other escape sequences.

### 7.5 Count and width validation

A row-form cNRE is structurally invalid if:

- declared row count `N` does not match the number of rows;
- any row has fewer or more cells than the field list;
- a required validation-critical field is omitted from the field list without a declared loss;
- quoted values are unterminated;
- indentation makes row ownership ambiguous;
- active tensions are omitted while unresolved conflicts exist;
- declared losses refer to fields or nodes that cannot be identified.

### 7.6 Safe dotted fields

Row fields may use dotted names to represent nested cNRE fields:

```text
b.sub     -> bounds.substrate
d.sub     -> declaration.substrate
rb.status -> recovery_boundary.status
```

Dotted fields are allowed only when each segment is a clear identifier. Do not use dotted fields when a literal field name itself contains a dot. If ambiguity exists, use object-form cNRE instead.

### 7.7 Required cNRE row field sets

Recommended lossless claim row fields:

```text
c[N]{id,s,type,ev,st,b.sub,b.scale,b.px,src}:
```

Minimum lossless claim row fields:

```text
c[N]{id,s,type,ev,st,b.sub,b.scale,b.px}:
```

Recommended tension row fields:

```text
tns[N]{id,s,st,b.sub,b.scale,b.px}:
```

Recommended proxy row fields:

```text
px[N]{id,label,estimates,source,limit}:
```

Recommended reconstructibility row fields:

```text
rec[N]{claim,can_rebuild,source_trace,steps_visible,opaque_state,verdict,action_if_not}:
```

Recommended rejection-condition row fields:

```text
rej[N]{claim,fail_if,revise_if,escalation}:
```

Recommended loss ledger row fields:

```text
loss[N]{item,loss_type,reason,effect,scope_limit}:
```

### 7.8 Row form safety fallback

Use object-form cNRE instead of row-form cNRE when:

- rows would become too wide to remain intelligible;
- claim statements require heavy nested structure;
- row counts are uncertain;
- quoting would become dense enough to obscure meaning;
- divergent truth surfaces require nested explanations;
- a human is likely to misread compressed fields;
- preserving authorial voice matters more than compactness.

---

## 8. cNRE field mapping to full NRE

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

## 9. Core objects

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

## 10. Epistemic status dictionary

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

## 11. Evidence class dictionary

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

## 12. Evidence weight order

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

## 13. Declaration capsule

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
    status: "NOT_APPLICABLE or DECLARED"
    definition: "[required before using collapse/failure/critical/crisis/warning language]"
    pre_boundary_zone: "[if applicable]"
    at_boundary_zone: "[if applicable]"
    post_boundary_consequences: "[if applicable]"

  evidence_classification:
    rule: "All claims are tagged with evidence class and bounded to substrate, scale, and proxy limits"
```

### 13.1 Declaration compression rule

A cNRE may factor declaration fields once into `d:` and then allow individual claims to inherit those bounds only when the inherited scope is exact.

If any claim differs from the declared scope, the claim must state its own bound explicitly.

```yaml
Declaration_Compression_Rule:
  allowed: "Claim rows may use SAME for b.sub, b.scale, or b.px only when the claim exactly inherits d.sub, d.scale, or d.px."
  forbidden: "Do not use SAME when the claim applies to a narrower, wider, or different substrate/scale/proxy boundary."
```

---

## 14. Canonical relations for writing NRE and cNRE

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

## 15. Truth surface and anti-collapse discipline

Use this section when the reasoning context includes durable records, session state, summaries, artifacts, dashboards, memories, external source material, or human-authored text that may diverge.

### 15.1 Core principle

```text
Do not merge what has not earned merging.
```

When claims, records, memories, projections, artifacts, authorities, or summaries diverge, the output must not smooth the divergence into a single confident narrative unless the merge is explicitly validated.

### 15.2 Truth surface declaration

```yaml
truth_surface_declaration:
  artifact_reality:
    definition: "Retrievable source material, file, receipt, log, trace, transcript, code, or external record"
    authority_level: "highest available unless invalidated"
  durable_truth:
    definition: "Standing validated claim, strategy, doctrine, or institutional memory"
    authority_level: "may guide interpretation but must remain traceable to artifact reality where empirical"
  session_continuity:
    definition: "Current working context, handoff state, memory, or conversational continuity"
    authority_level: "must not override durable truth or artifact reality"
  projection:
    definition: "Derived dashboard, summary, inference, model output, forecast, or interpretation"
    authority_level: "never overrides its source surface"
  authorial_voice:
    definition: "The human-originating rhythm, intention, conceptual contour, and style of a text or creative artifact"
    authority_level: "preserved unless the author explicitly requests transformation"
  authority_rule: "Lower-authority surfaces must not override higher-authority surfaces without an explicit supersedes relation and evidence basis"
```

### 15.3 Divergence classification

```yaml
No_Silent_Merge:
  trigger: "Two or more surfaces, claims, summaries, records, or directives appear valid but differ materially"
  prohibited_behavior:
    - "average the conflict into a neutral statement"
    - "choose the fluent or recent version without evidence"
    - "treat confidence as arbitration"
    - "hide the divergence from output"
  allowed_outcomes:
    - outcome: "confirmed_match"
      meaning: "Surfaces agree within declared bounds"
    - outcome: "one_side_invalid"
      meaning: "One surface is rejected with a stated evidence basis"
    - outcome: "both_valid_but_different"
      meaning: "Surfaces are internally valid but represent different content, time, scope, or authority"
    - outcome: "insufficient_evidence"
      meaning: "The available basis cannot determine precedence"
    - outcome: "requires_human_review"
      meaning: "Manual review, owner judgment, or external authority is required before merge or action"
```

Represent unresolved divergence as an `active_tension` node.

### 15.4 Additional informed relations

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

### 15.5 cNRE truth-surface compression

If truth surfaces are used, cNRE may compress them as:

```yaml
ts:
  AR: "artifact_reality"
  DT: "durable_truth"
  SC: "session_continuity"
  PR: "projection"
  AV: "authorial_voice"
```

If these aliases are used in claims or relations, the alias legend must be included.

---

## 16. Reconstructibility check

Before promoting a consequential claim to `confirmed_coherent`, ask whether it can be reconstructed from its declared basis.

```yaml
Reconstructibility_Check:
  can_rebuild_claim_from_sources: "true / false / partial / unknown"
  source_trace_available: "true / false / partial / unknown"
  transformation_steps_visible: "true / false / partial / unknown"
  opaque_inference_state_used: "true / false / partial / unknown"
  verdict: "reconstructible / partially_reconstructible / unreconstructable"
  required_action_if_unreconstructable: "downgrade, surface tension, seek evidence, or halt dependent claim"
```

Unreconstructable claims may orient inquiry, but must not support empirical, safety-critical, institutional, or authority-bearing conclusions.

### 16.1 cNRE reconstructibility row form

```text
rec[N]{claim,can_rebuild,source_trace,steps_visible,opaque_state,verdict,action_if_not}:
  C1,true,true,true,false,reconstructible,NONE
```

---

## 17. Rejection condition field

Every consequential claim should declare what would make it fail.

```yaml
Rejection_Condition:
  claim_node: "[C#]"
  what_would_make_this_claim_fail: "[condition]"
  what_evidence_would_force_revision: "[source/evidence]"
  escalation_state: "none / seek_evidence / quarantine / external_review / human_review / halt"
```

Design for the rejection condition, not only the validation condition.

### 17.1 cNRE rejection row form

```text
rej[N]{claim,fail_if,revise_if,escalation}:
  C1,"A required field is absent","A validation target cannot be reconstructed",seek_evidence
```

---

## 18. cNRE loss ledger

A `loss_ledger` is required for `cNRE_Bounded_Lossy` and optional for other profiles.

```yaml
loss_ledger:
  - loss_id: "L1"
    affected_item: "[node/edge/section/field]"
    loss_type: "[omitted | shortened | generalized | aliased | factored | approximated]"
    reason: "[why the loss occurred]"
    effect_on_reconstruction: "[NONE or limitation]"
    scope_limit: "[how downstream use is limited]"
```

Native row form:

```text
loss[N]{id,item,loss_type,reason,effect,scope_limit}:
  L1,C3,shortened,"Statement compressed for handoff","Meaning preserved; exact wording lost","Do not quote as verbatim source"
```

Rules:

- `declared_losses: NONE` means no validation-critical loss is known or intended.
- If a node is omitted, the loss ledger must identify it.
- If a claim statement is shortened, the loss ledger must say whether exact wording was lost.
- If a conflict or tension would be hidden by compression, compression must stop or switch to object-form/full NRE.
- `cNRE_Bounded_Lossy` cannot claim full validation equivalence.

---

## 19. cNRE reconstruction rules

A reader or model must be able to expand cNRE into full NRE as follows:

```yaml
cNRE_Reconstruction:
  step_1_read_cmeta: "Identify cNRE version, profile, compression type, and declared losses."
  step_2_expand_legend: "Replace compact keys and aliases with full field names and full value labels."
  step_3_expand_row_sections: "For every counted row section, expand each row into an object using the declared field list."
  step_4_restore_graph: "Map g fields to NRE_Output.graph."
  step_5_restore_declaration: "Map d fields to NRE_Output.declaration."
  step_6_restore_claims: "Map c rows/objects to NRE_Output.claims, preserving id, statement, type, evidence_class, epistemic_status, and bounds."
  step_7_restore_relations: "Copy relation strings exactly, preserving edge IDs."
  step_8_restore_tensions: "Map tns rows/objects to NRE_Output.tensions."
  step_9_restore_revisions: "Copy supersedes edges and preserve superseded claims when present."
  step_10_apply_loss_ledger: "Mark any bounded losses and scope limitations."
  step_11_check_invariants: "Verify evidence, status, bounds, relations, tensions, and revisions were not silently lost."
```

### 19.1 cNRE invariant checklist

A cNRE is invalid if any of these fail:

```yaml
cNRE_Invariants:
  - graph identity preserved
  - declaration scope preserved
  - every claim has id, statement, type, evidence class, epistemic status, and bounds
  - every relation has an edge ID
  - every relation argument is resolvable or declared external
  - active tensions remain visible
  - revisions preserve supersession edges
  - declared losses are explicit
  - truth-surface divergence is not silently merged
  - warning/collapse/failure/critical/crisis language is gated by recovery boundary
```

---

## 20. Writing procedure for full NRE

1. State the declaration capsule or say what is missing.
2. Write claims as nodes with evidence_class, epistemic_status, and bounds.
3. Connect claims with relations.
4. Record conflicts as active_tension nodes instead of suppressing them.
5. Record replacements with supersedes edges; never delete superseded claims from the reasoning record.
6. Do not use warning, collapse, failure, critical, or crisis language unless a recovery boundary has been declared.
7. Do not cross substrate or scale without a declared transfer or scale shift.
8. Do not treat proxies as full variables.
9. Do not treat Narrative, Speculative, or Protocol-Stipulated claims as empirical evidence.

---

## 21. Writing procedure for cNRE

1. Choose profile: default `cNRE_Readable`; use `cNRE_Row` only when repeated fields are stable and counts can be maintained.
2. Write `cmeta` first.
3. Declare `declared_losses`; default `NONE`.
4. Write `legend` if compact keys or aliases are used.
5. Write graph as `g`.
6. Write declaration as `d`.
7. Write claims as `c` objects or as counted rows.
8. Write relations as `r` strings.
9. Write tensions as `tns`; if none, use `tns: []` or `tns[0]{id,s,st,b.sub,b.scale,b.px}:`.
10. Write revisions as `rev`; if none, use `rev: []` or `rev[0]:`.
11. If using row form, verify row counts and row widths.
12. If using bounded-lossy compression, include `loss_ledger` or `loss[...]`.
13. Check reconstructibility before finalizing.
14. If compression would hide an unresolved issue, output full NRE instead.

---

## 22. Minimal cNRE object example

```yaml
cNRE_Output:
  cmeta:
    cNRE_version: "cNRE-1.1"
    profile: "cNRE_Readable"
    source_contract: "NRE_Output"
    compression_type: "lossless_structure"
    declared_losses: "NONE"
  legend:
    g: "graph"
    d: "declaration"
    c: "claims"
    r: "relations"
    tns: "tensions"
    rev: "revisions"
  g:
    id: "G1"
    title: "cNRE definition"
    v: "NRE Compact Core + Native cNRE Baseline v1.1"
  d:
    sub: "semantic/computational"
    scale: "synthetic_runtime"
    px: "NONE"
    rb: "NOT_APPLICABLE"
    ep: "Every claim has exactly one evidence class"
  c:
    - id: "C1"
      s: "cNRE is compressed NRE, not summary."
      type: "protocol claim"
      ev: "Protocol-Stipulated"
      st: "confirmed_coherent"
      b:
        sub: "NRE writing protocol"
        scale: "all NRE/cNRE outputs"
        px: "NONE"
  r: []
  tns: []
  rev: []
```

---

## 23. Minimal cNRE row example

```text
cNRE_Output:
  cmeta:
    cNRE_version: cNRE-1.1
    profile: cNRE_Row
    source_contract: NRE_Output
    compression_type: lossless_structure
    declared_losses: NONE
  legend:
    c: claims
    r: relations
    tns: tensions
    rev: revisions
    ev: evidence_class
    st: epistemic_status
  g:
    id: G1
    title: cNRE native row form
    v: NRE Compact Core + Native cNRE Baseline v1.1
  d:
    sub: semantic/computational
    scale: synthetic_runtime
    px: NONE
    rb: NOT_APPLICABLE
    ep: Every claim has exactly one evidence class
  c[2]{id,s,type,ev,st,b.sub,b.scale,b.px}:
    C1,"cNRE uses counted sections for compact repeated records",protocol,Protocol-Stipulated,confirmed_coherent,NRE,all,NONE
    C2,"Row compression is invalid if it hides evidence status bounds or tension",protocol,Protocol-Stipulated,confirmed_coherent,NRE,all,NONE
  r[1]:
    depends_on(C2,C1) @ E1
  tns[0]{id,s,st,b.sub,b.scale,b.px}:
  rev[0]:
```

---

## 24. Minimal safe output when declarations are missing

If required declaration data is missing, produce only the missing fields and safe provisional suggestions.

```yaml
NRE_Missing_Declaration_Output:
  missing_required_fields:
    - substrate.domain
    - scale.declared_scale
    - proxies.proxy_inventory
    - recovery_boundary.status
  why_required:
    substrate: "Prevents unsupported cross-domain transfer"
    scale: "Prevents cross-scale inference without bridge"
    proxies: "Prevents proxy inflation"
    recovery_boundary: "Required before warning/collapse/failure/critical/crisis language"
  safe_provisional_suggestions:
    - "Declare the domain being modeled"
    - "Declare the observation scale"
    - "Declare whether proxies are used"
    - "Declare whether warning-language boundaries apply"
  domain_conclusions: "BLOCKED"
```

cNRE row form may compress this only if it does not create domain conclusions.

---

## 25. Compact injectable prompt

```text
Use NRE Core Writing Spec. For analytical output, produce either NRE_Output or cNRE_Output. First declare substrate, scale, proxies, recovery-boundary status, and evidence policy. Then write claims as nodes with id/statement/type/evidence_class/epistemic_status/bounds. Then connect claims with relation_name(args) @ edge_id. Every claim has exactly one evidence class: Measured, Reconstructed, Inferred, Operator-Declared, Modeled, Narrative, Speculative, or Protocol-Stipulated. Use epistemic status: confirmed_coherent, candidate_hypothesis, active_tension, unlinked_speculation, or superseded. Conflicts become visible active_tension nodes. Revisions preserve old claims with supersedes edges. No cross-substrate transfer, cross-scale inference, proxy inflation, evidence-class promotion, or warning/collapse/failure/critical/crisis language is allowed unless the required declaration exists. Narrative may orient inquiry but not validate empirical conclusions. Protocol-Stipulated values govern the protocol but are not empirical evidence. If required declaration data is missing, output only the missing fields and safe provisional suggestions; do not produce domain conclusions based on unvalidated speculative fields.

If asked for cNRE, produce compressed NRE rather than ordinary NRE or prose summary. Default to cNRE_Readable. Use cNRE_Row only when repeated records share stable fields and counts can be maintained. cNRE must preserve graph identity, declaration scope, claim IDs, claim statements, claim types, evidence classes, epistemic statuses, bounds, relations, tensions, revisions, truth surfaces when relevant, reconstructibility and rejection conditions when required, and declared losses. cNRE may use compact keys, aliases, counted sections, and field-listed rows. If compression would hide conflict, evidence limits, source divergence, bounds, or supersession, switch to full NRE.
```

---

## 26. Ultra-compact cNRE prompt shard

```text
cNRE = compressed NRE, not summary. Output cNRE_Output with cmeta/profile/loss declaration, legend if aliases are used, g, d, c, r, tns, rev. Preserve graph identity, declaration, claim IDs/statements/types, evidence_class, epistemic_status, bounds, relations, active tensions, revisions, truth surfaces when relevant, reconstructibility/rejection conditions for consequential claims, and declared losses. Default profile cNRE_Readable. Use cNRE_Row for counted field-listed rows only when row counts and widths are exact. declared_losses: NONE unless bounded loss is explicitly listed. Do not compress away evidence, bounds, tensions, conflicts, source-surface divergence, or supersession. If declarations are missing, output missing fields only; no domain conclusions from speculative fields.
```

---

## 27. Separation from governance

This file defines how to write NRE and cNRE output.

Governance may validate this output, audit it, apply profile tiers, enforce deployment modes, run conformance tests, or gate release. Governance must not redefine canonical writing fields without a writing-spec version bump.

```yaml
separation:
  writing_spec_owns:
    - graph structure
    - node fields
    - edge grammar
    - declaration capsule
    - evidence class labels
    - epistemic status labels
    - cNRE object form
    - cNRE native row form
    - compression metadata
    - loss declaration requirements
    - reconstruction rules
    - compact writing procedure
  governance_owns:
    - audits
    - violation handling
    - profile tiers
    - deployment modes
    - collaborative recovery workflow
    - conformance tests
    - enforcement claims
    - versioning and change control beyond writing fields
```

---

## 28. Version note

This baseline replaces the earlier compact-only NRE writing module by making cNRE native to the core spec.

The baseline remains prompt-injectable. It is larger than the original compact prompt because it now defines both full NRE and compressed NRE. For extremely small context windows, use the compact injectable prompt or ultra-compact cNRE prompt shard above.
