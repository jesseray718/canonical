#!/usr/bin/env python3
import json, urllib.request, datetime
from pathlib import Path
REPOS = ["openroot","aerocement","black-locust-rmh","une","etaledger","und-protocol","fractallattice","agaperesonance","agape-une","agape-primitives","agapenet","agape-coordination","openroot-spoke-template","jesseray718","wisdom-scaffold","agape-ipfs","canonical"]
def fetch(n):
    try:
        with urllib.request.urlopen(f"https://api.github.com/repos/jesseray718/{n}", timeout=10) as r:
            d = json.loads(r.read().decode())
            return {"name":n,"updated":d.get("updated_at","")[:10],"stars":d.get("stargazers_count",0),"archived":d.get("archived",False),"open_issues":d.get("open_issues_count",0),"language":d.get("language") or "-","status":"archived" if d.get("archived") else "active"}
    except Exception as e:
        return {"name":n,"status":"error","error":str(e)[:50]}
now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
results = [fetch(r) for r in REPOS]
active = sum(1 for r in results if r.get("status")=="active")
Path("status.json").write_text(json.dumps({"generated_at":now,"trunk":"openroot","active_count":active,"total_tracked":len(REPOS),"repos":results}, indent=2))
md = [f"# OpenRoot Canonical Dashboard\nGenerated: `{now}`\n\n**Active nodes:** {active} / {len(REPOS)}\n\n| Repo | Updated | Lang | ★ | Issues | Status |\n|------|---------|------|---|--------|--------|"]
for r in sorted(results, key=lambda x: x.get("name","")):
    md.append(f"| {r.get('name')} | {r.get('updated','-')} | {r.get('language','-')} | {r.get('stars',0)} | {r.get('open_issues',0)} | {r.get('status')} |")
md += ["\n## Roles\n- Trunk: openroot\n- Physical: aerocement · black-locust-rmh\n- Computational: une · etaledger · und-protocol · fractallattice · agaperesonance\n- Cooperation: agape-*\n- Meta: canonical · openroot-spoke-template"]
Path("dashboard.md").write_text("\n".join(md))
print(f"Dashboard written — {active} active")
