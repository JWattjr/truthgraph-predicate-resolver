import json


FUTURE = "2030-01-01T00:00:00Z"


def test_resolves_and_validates_consensus(direct_vm, direct_deploy):
    contract = direct_deploy(
        "contracts/TruthGraph.py",
        "graph-1",
        {
            "atoms": [
                {"id": "a", "claim": "A is true"},
                {"id": "b", "claim": "B is true"},
            ],
            "formula": {"op": "AND", "children": ["a", "b"]},
        },
        ["https://example.org/evidence"],
        FUTURE,
    )
    direct_vm.warp("2031-01-01T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 200, "body": "official evidence"})
    direct_vm.mock_llm(r".*", json.dumps({"atom_statuses": {"a": "TRUE", "b": "TRUE"}}))
    assert contract.resolve()["outcome"] == "TRUE"
    assert direct_vm.run_validator()
    assert not direct_vm.run_validator(leader_result={
        "atom_statuses": {"a": "FALSE", "b": "FALSE"}, "outcome": "FALSE"
    })


def test_all_sources_down_is_unresolved(direct_vm, direct_deploy):
    contract = direct_deploy(
        "contracts/TruthGraph.py",
        "outage",
        {"atoms": [{"id": "a", "claim": "A is true"}], "formula": "a"},
        ["https://example.org/evidence"],
        FUTURE,
    )
    direct_vm.warp("2031-01-01T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 503, "body": "offline"})
    assert contract.resolve()["outcome"] == "UNRESOLVED"
