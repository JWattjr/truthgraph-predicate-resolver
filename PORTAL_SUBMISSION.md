# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts  
**Title:** TruthGraph PredicateGraph Resolver  
**Contribution date:** August 12, 2026

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

1. GitHub Repository — https://github.com/JWattjr/truthgraph-predicate-resolver
2. GitHub File — https://github.com/JWattjr/truthgraph-predicate-resolver/blob/main/contracts/TruthGraph.py
3. GitHub File — https://github.com/JWattjr/truthgraph-predicate-resolver/blob/main/tests/test_truth_graph.py
4. GitHub File — https://github.com/JWattjr/truthgraph-predicate-resolver/blob/main/docs/SECURITY_AUDIT.md
5. GitHub File — https://github.com/JWattjr/truthgraph-predicate-resolver/blob/main/docs/TEST_MATRIX.md
6. GitHub File — https://github.com/JWattjr/truthgraph-predicate-resolver/blob/main/deployments/studionet.json
7. GitHub File — https://github.com/JWattjr/truthgraph-predicate-resolver/blob/main/deployments/bradbury.json
8. GenLayer Explorer Contract — https://explorer-bradbury.genlayer.com/address/0x8a0A6D18AF51fBaA0Cf484C86DaB5F7F54A3bB2f
