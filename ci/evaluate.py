"""Validate scanner output and evaluate the classroom security policy."""
import json
import sys
from pathlib import Path

tool, filename, raw_status = sys.argv[1:]
status = int(raw_status)
if status not in ({0, 1, 2} if tool == "zap" else {0, 1}):
    raise SystemExit(f"Scanner execution failed with exit code {status}")
data = json.loads(Path(filename).read_text())
if tool == "bandit":
    if data.get("errors"):
        raise SystemExit("Bandit could not analyse all input files")
    findings = len(data["results"])
elif tool == "trivy":
    if "SchemaVersion" not in data or "ArtifactName" not in data:
        raise SystemExit("Invalid Trivy report")
    findings = sum(
        item.get("Severity") in {"HIGH", "CRITICAL"}
        for result in data.get("Results", [])
        for item in result.get("Vulnerabilities", [])
    )
else:
    if not data.get("site"):
        raise SystemExit("ZAP did not report any target sites")
    findings = sum(
        str(alert["pluginid"]) in {"10020", "10021"}
        for site in data["site"] for alert in site["alerts"]
    )
print(f"Classroom policy findings: {findings}")
Path(filename + ".count").write_text(str(findings))
