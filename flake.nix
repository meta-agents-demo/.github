{
  description = "Meta Agents organization proof of the canonical ores-sops contract";

  inputs.ores-sops.url =
    "github:ORESoftware/ores-sops/bcedd169490775d58f418a59248a3e2354451cf2";

  outputs = { ores-sops, ... }: {
    devShells = ores-sops.devShells;
    packages = ores-sops.packages;
    checks = ores-sops.checks;
    formatter = ores-sops.formatter;
  };
}
