set shell := ["bash", "-euo", "pipefail", "-c"]
set dotenv-load := false

_default:
    @just --list --unsorted

# Prove the pinned canonical package and its env/enc + env/dec regression suite.
env-ci:
    test "$(ores-sops --version)" = "ores-sops 0.3.1"
    nix flake check --no-write-lock-file -L
