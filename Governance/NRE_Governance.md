# NRE Governance and Validation Considerations

Author: Jean Charbonneau (https://www.linkedin.com/in/jean-charbonneau-ai/)

Purpose: define how NRE output is validated, audited, governed, recovered, versioned, and honestly described. This document is not meant to be injected wholesale into prompts unless the system is implementing governance behavior

---

## 1. Separation principle

The NRE Writing Spec defines how to write NRE output

This Governance document defines how to validate whether an output complied with that writing spec

The split should remain stable:

```yaml
separation:
  writing_spec_owns:
    - graph structure
    - node fields
    - edge grammar
    - declaration capsule
    - evidence class labels
    - epistemic status labels
    - compact writing procedure
  governance_owns:
    - audits
    - violation handling
    - profile tiers
    - deployment modes
    - collaborative recovery workflow
    - conformance tests
    - enforcement claims
    - versioning and change control
```

The governance layer must not redefine canonical writing fields. It may validate them, require them, test them, or gate outputs that omit them

---

## 2. Validation interface

For governance to validate an NRE output, the writing spec must expose a predictable validation target

Required validation target:

```yaml
NRE_Validation_Target:
  graph:
    graph_id: "required"
    title: "required"
    version: "required"
  declaration:
    substrate: "required"
    scale: "required"
    proxies: "required, may be NONE"
    recovery_boundary: "required, may be NOT_APPLICABLE unless warning language is used"
    evidence_policy: "required"
  claims:
    node_id: "required and unique"
    statement: "required"
    claim_type: "required"
    evidence_class: "required"
    epistemic_status: "required"
    bounds: "required"
  relations:
    edge_id: "required and unique"
    relation_name: "required"
    arguments: "must reference existing nodes, edges, graphs, or declared external sources"
  tensions:
    active_tension_nodes: "required when conflicts or violations exist"
  revisions:
    supersedes_edges: "required when claims are replaced"
```

---

## 3. Governance validators

### 3.1 Application Declaration Audit (ADA)

Purpose: verify that declaration discipline is present before and throughout analytical output

ADA checks:

```yaml
ADA_Checks:
  pre_computation:
    - declaration exists before analytical claims
    - substrate is declared
    - own computational/semantic substrate is acknowledged
    - scale is declared with justification
    - proxies have boundary statements
    - recovery boundary exists before warning language
    - evidence classification scheme is declared
  substrate:
    - no variable crosses domains without transfer and re-bound statement
  scale:
    - no cross-scale inference without scale_shift and bridging argument
  proxy:
    - no proxy is treated as equivalent to its target variable
  recovery_boundary:
    - no collapse/failure/critical/crisis language without a declared boundary
  evidence:
    - every claim has evidence_class
    - Narrative and Speculative claims do not validate empirical conclusions
    - composite claims declare inherited lowest evidence class
  output:
    - violations become visible active_tension nodes
```

ADA verdicts:

```yaml
ADA_Verdict:
  PASS: "No blocking violation detected"
  PASS_WITH_TENSION: "Output may proceed, but active_tension nodes remain visible"
  FAIL_GATED: "Analytical output must not be released until blocking issues are resolved"
  SCOPE_LIMITED: "Only claims within validated declaration scope may proceed"
```

### 3.2 Structural Validation Audit (SVA)

Purpose: verify that the NRE graph is structurally valid

SVA checks:

```yaml
SVA_Checks:
  - every node_id is unique
  - every edge_id is unique
  - every edge references an existing node, edge, graph, or declared external source
  - superseded nodes are preserved
  - every replacement is recorded with a supersedes edge
  - cNRE compression loss is declared if compression is used
```

### 3.3 Coherence Audit (CA)

Purpose: verify consistency across the graph

CA checks:

```yaml
CA_Checks:
  - no two confirmed_coherent nodes contradict each other without active_tension
  - claims remain consistent with declared substrate, scale, and evidence class
  - invalidated claims do not remain in active use without revision or supersession
```

---

## 4. Interpretive Hygiene Constraint register

The governance layer owns the Interpretive Hygiene Constraints as validation rules

```yaml
IHC_Register:
  IHC_01_Declare_Before_Interpreting:
    check: "No analytical output before declaration"
    violation: "active_tension + gate"
  IHC_02_Classify_Before_Claiming:
    check: "Every claim has evidence class"
    violation: "active_tension + correction required"
  IHC_03_Bound_Before_Applying:
    check: "No variable/proxy/conclusion used outside declared bounds"
    violation: "active_tension + re-bound required"
  IHC_04_Revise_When_Evidence_Requires:
    check: "Invalidated claims are revised or superseded"
    violation: "audit failure"
  IHC_05_No_Substrate_Drift:
    check: "Cross-substrate transfer is declared and re-bounded"
    violation: "active_tension"
  IHC_06_No_Scale_Confusion:
    check: "Cross-scale inference has scale_shift and bridge"
    violation: "active_tension"
  IHC_07_No_Proxy_Inflation:
    check: "Proxy is not treated as full target variable"
    violation: "active_tension"
  IHC_08_Recovery_Boundary_Gate:
    check: "Warning/failure language requires declared recovery boundary"
    violation: "active_tension + language gate"
  IHC_09_No_Evidence_Class_Collapse:
    check: "Narrative, Speculative, and Protocol-Stipulated claims are not used as empirical evidence"
    violation: "active_tension"
  IHC_10_Violation_Surfacing:
    check: "Detected violations are visible, not suppressed"
    violation: "audit failure"
```

---

## 5. Collaborative Recovery Protocol governance

CRP belongs in governance, not in the compact writing spec

Purpose: handle incomplete declarations without pretending they are complete

Governance behavior:

```yaml
CRP_Governance:
  trigger: "A request lacks one or more required declaration parameters"
  principle: "CRP is a compliance pathway, not a bypass"
  gate: "Analytical computation remains blocked until validation or scope limitation"

  stages:
    CRP_S1_Acknowledge_And_Flag:
      output: "visible IHC_01 active_tension node"
      gate_status: "BLOCKED"
    CRP_S2_Provisional_Proposal:
      output: "machine-inferred declaration proposal with prompt_basis"
      classes: "Inferred or Speculative"
    CRP_S3_Epistemic_Downgrade:
      output: "formal downgrade record"
      rule: "Speculative provisional fields cannot support analytical conclusions"
    CRP_S4_Validation_Check:
      actions: "validate, correct, reject"
      rule: "validation_status and evidence_class are independent"
      silence_rule: "operator silence is not validation"
```

Operator validation mapping:

```yaml
Validation_Basis_Mapping:
  source_cited:
    resulting_evidence_class: "Reconstructed"
    status: "confirmed_coherent"
  domain_reasoning_without_source:
    resulting_evidence_class: "Operator-Declared"
    status: "confirmed_coherent"
  bare_confirmation:
    resulting_evidence_class: "Inferred"
    status: "candidate_hypothesis"
  rejected:
    resulting_status: "active_tension"
    gate: "dependent claims remain blocked"
```

Deadlock behavior:

```yaml
CRP_Deadlock:
  condition: "Two unproductive CRP cycles without usable validation"
  required_output: "Minimal Safe Output"
  minimal_safe_output_must_include:
    - missing parameters
    - why they are required
    - what is needed to proceed
    - whether scope-limited analysis is possible
  minimal_safe_output_must_not_include:
    - domain conclusions
    - inferred, modeled, reconstructed, or measured claims about the target domain
```

---

## 6. Deployment tiers

Profile tiers belong in governance because they define compliance expectations, not the writing grammar itself

```yaml
NRE_Profile_Tiers:
  NRE_Lite:
    use: "single-domain, low-stakes exploratory reasoning"
    does_not_satisfy: "full Application Declaration Standard"
  NRE_Declared:
    use: "cross-domain, multi-proxy, or consequential analytical contexts"
    requires: "completed declaration and evidence class tagging"
  NRE_Audited:
    use: "publication, institutional, or external stakeholder review"
    requires: "ADA + SVA + CA records and provenance"
  NRE_Executable:
    use: "software-enforced NRE compliance"
    requires: "code-level validators, schema checks, hard gates, machine-readable audit trail"
```

---

## 7. Deployment and enforcement boundaries

Governance must prevent inflated compliance claims

```yaml
Deployment_Modes:
  text_only:
    enforcement: "operator discipline only"
    may_claim: "normative adherence"
    must_not_claim: "automated enforcement or verification"
  prompt_mediated:
    enforcement: "language model instruction-following"
    may_claim: "probabilistic prompt-mediated compliance with declared test results"
    must_not_claim: "guaranteed enforcement"
  human_audited:
    enforcement: "designated human auditor with checklist"
    may_claim: "reviewed at time of release"
    must_not_claim: "permanent guarantee or perfect detection"
  software_enforced:
    enforcement: "middleware validators, schemas, hard gates, state machines"
    may_claim: "software enforcement within implemented checks"
    must_not_claim: "coverage of unspecified violations"
```

Required governance rule:

```yaml
Compliance_Claim_Rule:
  statement: "An NRE deployment must not claim enforcement guarantees it does not have"
  validator: "ADA + deployment-mode check"
```

---

## 8. Conformance test suite

The conformance suite validates governance behavior against known failure modes

Recommended test coverage:

```yaml
ADA_Conformance_Tests:
  TC_001: "Warning language without recovery boundary"
  TC_002: "Cross-substrate variable transfer without re-bounding"
  TC_003: "Narrative claim used as empirical validation"
  TC_004: "Analytical output without completed declaration"
  TC_005: "Proxy treated as equivalent to target variable"
  TC_006: "Scale shift without bridging argument"
  TC_007: "Claim without evidence class tag"
  TC_008: "CRP deadlock produces Minimal Safe Output"
  TC_009: "Protocol-Stipulated field cited as empirical evidence"
  TC_010: "Bare operator confirmation does not promote field to Reconstructed"
  TC_011: "Narrative used only to orient inquiry is permitted"
```

Governance pass criteria:

```yaml
Conformance_Pass_Criteria:
  - violation-producing tests create active_tension nodes
  - blocked outputs are not released as analytical conclusions
  - permitted narrative orientation is not over-blocked
  - deployment claims match deployment mode
  - validation and evidence-class promotion remain separate
```

---

## 9. Recommended validation pipeline

```yaml
NRE_Governance_Pipeline:
  step_1_parse:
    action: "Parse graph, declaration, claims, relations, tensions, revisions"
    validator: "SVA"
  step_2_declaration:
    action: "Verify substrate, scale, proxy, recovery boundary, evidence policy"
    validator: "ADA"
  step_3_claim_classification:
    action: "Check every claim has evidence_class and epistemic_status"
    validator: "ADA"
  step_4_boundary_checks:
    action: "Check substrate transfer, scale shift, proxy boundaries, warning gate"
    validator: "ADA"
  step_5_evidence_chain:
    action: "Check evidence class promotion, narrative role, speculative containment, protocol-stipulated isolation"
    validator: "ADA + CA"
  step_6_structural_integrity:
    action: "Check node/edge uniqueness, references, supersession preservation"
    validator: "SVA"
  step_7_coherence:
    action: "Check contradictions and unresolved confirmed_coherent conflicts"
    validator: "CA"
  step_8_deployment_claim:
    action: "Check claimed enforcement matches declared deployment mode"
    validator: "ADA"
  step_9_verdict:
    action: "Return PASS, PASS_WITH_TENSION, FAIL_GATED, or SCOPE_LIMITED"
    validator: "governance controller"
```

---

## 10. Split map from the original full specification

Recommended destination of original sections:

```yaml
Split_Map:
  NRE_Writing_Spec:
    keep_and_compress:
      - "Core mandate"
      - "Core graph concepts"
      - "Node, edge, and relation grammar"
      - "Epistemic statuses"
      - "Evidence classes"
      - "Declaration capsule"
      - "Core writing procedure"
      - "Canonical relations needed for output"
    exclude:
      - "ADA implementation"
      - "IHC register as governance rules"
      - "CRP workflow"
      - "Deployment tiers"
      - "Enforcement boundary analysis"
      - "Conformance tests"

  Governance_Considerations:
    keep:
      - "Failure modes as rationale"
      - "Application Declaration Audit"
      - "Structural Validation Audit"
      - "Coherence Audit"
      - "Interpretive Hygiene Constraints"
      - "NRE profile tiers"
      - "Collaborative Recovery Protocol"
      - "Implementation and enforcement boundaries"
      - "Canonical rule summary as checklist"
      - "ADA conformance test suite"
```

---

## 11. Versioning and change control

The writing spec should remain compact and stable. Governance may evolve faster

```yaml
Versioning_Rules:
  writing_spec_changes:
    require: "version bump when canonical fields, evidence classes, statuses, or relation grammar change"
    risk: "prompt compatibility"
  governance_changes:
    require: "version bump when validators, test cases, tiers, deployment modes, or CRP states change"
    risk: "compliance claim drift"
  compatibility_rule:
    statement: "Governance may add validators but must not redefine writing-spec fields without a writing-spec version bump"
```

---

## 12. Governance summary

The governance layer validates NRE by checking that each output exposes the declaration, claims, classes, bounds, relations, tensions, and revisions required by the writing spec. It then applies ADA, SVA, CA, IHC checks, CRP recovery when declarations are incomplete, deployment-mode honesty checks, and conformance testing

The key design is separation: the compact NRE Writing Spec is the object injected into prompts; the Governance document is the validator that decides whether the resulting output may honestly claim NRE compliance

---

# Informed Governance for NRE

Purpose: validate NRE outputs against anti-collapse, truth-surface, reconstructibility, and rejection-condition discipline

## 1. Truth Surface Separation Audit (TSSA)

Purpose: verify that distinct sources of truth are declared and not silently merged

```yaml
TSSA_Checks:
  - relevant truth surfaces are declared when artifacts, durable truth, session continuity, projections, memories, or authorial voice are involved
  - artifact reality is not overridden by session continuity or projection without explicit evidence
  - durable truth is not overwritten by stale session state without supersession basis
  - projections, dashboards, summaries, and model outputs remain traceable to source surfaces
  - authorial voice is not overwritten by optimization without explicit transformation consent
  - surface precedence is declared when surfaces conflict
  - missing surface declarations create active_tension and scope limitation
```

Verdicts:

```yaml
TSSA_Verdict:
  PASS: "Truth surfaces are separated and precedence is valid"
  PASS_WITH_TENSION: "Divergence remains visible but output is safe within scope"
  SCOPE_LIMITED: "Only claims grounded in validated surfaces may proceed"
  HUMAN_REVIEW_REQUIRED: "Merge, supersession, or precedence requires owner/manual review"
  FAIL_GATED: "Output silently merges or overrides surfaces without basis"
```

## 2. No Silent Merge Audit (NSMA)

Purpose: prevent coherent-sounding collapse of conflicting records, directives, or perspectives

```yaml
NSMA_Checks:
  - all material divergences are surfaced as active_tension nodes
  - conflict is not averaged into a neutral narrative
  - confidence, recency, fluency, convenience, or institutional need is not used as arbitration
  - both_valid_but_different is allowed as a stable outcome
  - requires_human_review is used when no valid automated precedence exists
  - split-brain states are escalated rather than blended
```

Allowed arbitration outcomes:

```yaml
Arbitration_Outcomes:
  confirmed_match: "Surfaces agree within declared bounds"
  one_side_invalid: "One surface is rejected with evidence"
  both_valid_but_different: "Both surfaces remain valid but differ by content, time, scope, or authority"
  insufficient_evidence: "The basis cannot determine precedence"
  requires_human_review: "A human or external authority must decide before merge/action"
```

## 3. Reconstructibility Audit (RA)

Purpose: verify that claims can be rebuilt from declared sources

```yaml
RA_Checks:
  - consequential claims identify source surfaces
  - transformation steps are visible enough for review
  - opaque inference state is declared if used
  - unreconstructable bases do not support empirical, institutional, safety-critical, or authority-bearing conclusions
  - partially reconstructible claims are downgraded or scope-limited
  - reconstructibility verdict is recorded for consequential outputs
```

Verdicts:

```yaml
Reconstructibility_Verdict:
  RECONSTRUCTIBLE: "Claim can be rebuilt from declared sources and transformations"
  PARTIALLY_RECONSTRUCTIBLE: "Some source or transformation steps are missing; scope limitation required"
  UNRECONSTRUCTABLE: "Dependent claim must be downgraded, halted, or moved to inquiry"
```

## 4. Rejection Condition Audit (RCA2)

Purpose: ensure claims are designed for falsification, revision, and escalation

```yaml
RCA2_Checks:
  - consequential claims state what would make them fail
  - evidence that would force revision is named
  - escalation state is defined for failed or contested claims
  - validation-seeking is not substituted for rejection-condition design
  - confirmation bias is surfaced as active_tension where relevant
```

## 5. Additional Interpretive Hygiene Constraints

```yaml
IHC_11_Truth_Surface_Separation:
  check: "Distinct truth surfaces are declared and not silently merged"
  violation: "active_tension + surface audit required"

IHC_12_No_Silent_Merge:
  check: "Material divergence is classified, not blended"
  violation: "FAIL_GATED or HUMAN_REVIEW_REQUIRED"

IHC_13_Reconstructibility:
  check: "Consequential claims can be reconstructed from source surfaces or are downgraded"
  violation: "scope limitation / seek evidence / halt dependent claim"

IHC_14_Rejection_Condition:
  check: "Consequential claims name failure and revision conditions"
  violation: "candidate_hypothesis at most"

IHC_15_Authorial_Surface_Protection:
  check: "Human-originating voice is preserved unless transformation is requested"
  violation: "active_tension + consent/author review"
```

## 6. Recommended governance pipeline extension

```yaml
NRE_Governance_Pipeline_Extension:
  step_A_truth_surfaces:
    action: "Parse artifact reality, durable truth, session continuity, projection, and authorial voice surfaces"
    validator: "TSSA"
  step_B_divergence:
    action: "Classify conflicts using Arbitration_Outcomes"
    validator: "NSMA"
  step_C_reconstructibility:
    action: "Check whether consequential claims can be rebuilt from sources"
    validator: "RA"
  step_D_rejection:
    action: "Verify rejection conditions and escalation states"
    validator: "RCA2"
```

