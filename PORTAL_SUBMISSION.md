# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts  
**Title:** TruthGraph PredicateGraph Resolver  
**Contribution date:** Use the actual date of the submitted release.

## Notes / Description

Built and deployed an MIT-licensed TruthGraph PredicateGraph Resolver, a
standalone reusable GenLayer Intelligent Contract for markets and quests whose
outcome depends on multiple public claims. The constructor freezes bounded atom
claims, an AND/OR/NOT/K-of-N formula, evidence URLs, and a deadline. The leader
fetches public evidence and classifies atoms; validators independently re-fetch
and compare the full canonical atom-status map and derived outcome through a
custom equivalence function. Deterministic code evaluates the graph and stores
TRUE, FALSE, or UNRESOLVED. Unknown atom references, source outages, malformed
model output, private-network URLs, premature resolution, replays, and validator
disagreement fail closed. Includes pinned GenVM source, direct consensus tests,
a dated security audit, test matrix, and StudioNet/Bradbury deployment records.
It is an oracle primitive only and does not custody funds or execute payouts.

## Evidence to add

1. GitHub Repository — replace with the private repository URL.
2. GitHub File — `contracts/TruthGraph.py`.
3. GitHub File — `tests/test_truth_graph.py`.
4. GitHub File — `docs/SECURITY_AUDIT.md`.
5. GitHub File — `docs/TEST_MATRIX.md`.
6. GitHub File — `deployments/studionet.json`.
7. GitHub File — `deployments/bradbury.json`.
8. GenLayer Explorer Contract — replace with the finalized Bradbury address URL.
