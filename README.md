# TruthGraph PredicateGraph Resolver

A standalone GenLayer Intelligent Contract for prediction markets and quests
whose outcome depends on a graph of public claims rather than one event.

It freezes 1-12 atomic claims, an `AND`, `OR`, `NOT`, or `K_OF_N` expression,
public HTTPS evidence URLs, and a deadline. The leader and validators
independently fetch evidence and classify each atom as `TRUE`, `FALSE`, or
`UNRESOLVED`; deterministic code evaluates the graph. Unknown formula atoms,
missing sources, malformed model output, and validator disagreement fail
closed.

## GenLayer-native decision

The consequential decision is the canonical atom-status map and its derived
graph outcome. Validators recompute those fields from the same public evidence
through a custom equivalence function. No frontend or single oracle decides the
result.

## Verify

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/TruthGraph.py
pytest tests -v
```

See `docs/SECURITY_AUDIT.md`, `docs/TEST_MATRIX.md`, and
`PORTAL_SUBMISSION.md` for reviewer evidence.
