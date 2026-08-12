# Security and consensus audit: TruthGraph

Audit date: 2026-08-12
Scope: `contracts/TruthGraph.py`
Method: manual review, GenVM AST lint, SDK schema validation, direct-mode
tests, validator-disagreement tests, and hosted-network receipt inspection.

## Result

No unresolved critical or high-severity issue was found after remediation.
TruthGraph does not custody or transfer funds. Consumers must wait for GenLayer
finality before using an outcome for an irreversible action.

## Remediated findings

| ID | Severity | Finding | Remediation |
| --- | --- | --- | --- |
| TG-01 | Medium | A formula could reference an undeclared atom and silently become unknown. | Validate the complete bounded formula graph against the frozen atom IDs during construction. |
| TG-02 | Medium | All-source outages could reach the LLM. | Return a deterministic all-`UNRESOLVED` atom map before any prompt when no source is available. |
| TG-03 | Medium | Evidence URL checks allowed local/private targets. | Require bounded public HTTPS hosts and reject userinfo, private literal IPs, internal suffixes, and non-default ports. |
| TG-04 | Medium | A bound consensus method captured contract storage in nondeterministic execution. | Snapshot canonical graph and source data before `run_nondet_unsafe`; nested leader/validator closures contain no `self` reference. |
| TG-05 | Low | Source bytes and CLI-decoded JSON needed defensive handling. | Bound bytes, decode with replacement, accept decoded objects, and persist canonical JSON. |
| TG-06 | Low | Validator wrappers accepted objects merely exposing `calldata`. | Require `gl.vm.Return`, independently recompute the complete atom map and derived outcome, and compare both. |

## Residual risks

- DNS rebinding is not eliminated by syntax validation; deploy with reviewed,
  stable domains or add a domain allowlist.
- Public evidence can drift between validator fetches. A substantive mismatch
  intentionally prevents consensus rather than forcing a result.
- HTTPS reachability does not establish publisher authority.
- The graph language is intentionally bounded to 12 atoms and depth 8.

## Verification evidence

- Pinned GenVM runner; GenVM lint and SDK validation pass.
- Standalone direct suite: 3 passed.
- AST regression: no storage reference inside leader/validator closures.
- StudioNet deployment and resolution are finalized; leader execution was
  `SUCCESS`, votes were 3 agree / 2 idle, and no storage warning appeared.
- Live result: both frozen atoms `TRUE`; derived graph outcome `TRUE`.
- Bradbury deployment is recorded separately; its appeal/finality status is
  not represented as final until RPC confirmation.

This is an engineering assessment, not formal verification or a financial or
legal guarantee.
