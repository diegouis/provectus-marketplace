#!/usr/bin/env python3
"""Generate unified catalog, per-practice manifests, and gap analysis from scan reports."""

import json
import os
from collections import defaultdict
from pathlib import Path

BASE_DIR = "/Users/diegofernandomartinezayala/My Drive (dmartinezayala@provectus.com)/Projects/Agentic Coding"
SCAN_DIR = os.path.join(BASE_DIR, "provectus-marketplace/scan-reports")
OUTPUT_DIR = os.path.join(BASE_DIR, "provectus-marketplace/catalog")

PRACTICES = [
    "agentic-engineering", "delivery", "sales", "hr", "finance",
    "devops", "frontend", "backend", "sdlc", "data", "ml-ai",
    "security", "platform", "qa"
]

ASSET_TYPES = [
    "skills", "commands", "agents", "hooks", "mcp_configs",
    "scripts", "docs", "templates", "configs"
]

# Map scan type names to our canonical type names
TYPE_MAP = {
    "skill": "skills",
    "command": "commands",
    "agent": "agents",
    "hook": "hooks",
    "mcp": "mcp_configs",
    "script": "scripts",
    "doc": "docs",
    "template": "templates",
    "config": "configs",
    "claude-file": "configs",
    "api-spec": "docs",
}

# Recommended integrations per practice
PRACTICE_INTEGRATIONS = {
    "agentic-engineering": ["GitHub", "GitLab", "Slack", "Confluence"],
    "delivery": ["Jira", "Slack", "Google Meet", "Google Calendar", "Confluence", "Google Docs"],
    "sales": ["Slack", "Google Docs", "Gmail", "Google Calendar", "Jira"],
    "hr": ["Slack", "Google Docs", "Gmail", "Google Calendar", "Google Meet"],
    "finance": ["Google Docs", "Gmail", "Slack"],
    "devops": ["GitHub", "GitLab", "AWS", "GCP", "Slack", "Jira"],
    "frontend": ["GitHub", "GitLab", "Playwright", "Pencil", "Excalidraw"],
    "backend": ["GitHub", "GitLab", "AWS", "GCP"],
    "sdlc": ["GitHub", "GitLab", "Jira", "Confluence", "Slack"],
    "data": ["AWS", "GCP", "GitHub", "Google Docs"],
    "ml-ai": ["AWS", "GCP", "GitHub", "Google Docs"],
    "security": ["GitHub", "GitLab", "AWS", "GCP", "Slack"],
    "platform": ["GitHub", "GitLab", "Slack", "AWS", "GCP"],
    "qa": ["GitHub", "GitLab", "Playwright", "Jira", "Slack"],
}


def load_scan_reports():
    """Load all scan report batch files."""
    all_repos = []
    for i in range(1, 5):
        path = os.path.join(SCAN_DIR, f"scan-report-batch-{i}.json")
        with open(path, "r") as f:
            data = json.load(f)
            all_repos.extend(data["repos"])
    return all_repos


def build_unified_catalog(repos):
    """Build a deduplicated unified catalog of all assets."""
    catalog = []
    seen = set()  # (repo_name, path) for dedup

    for repo in repos:
        repo_name = repo["name"]
        repo_path = repo["path"]
        repo_desc = repo.get("description", "")

        for asset in repo.get("assets", []):
            key = (repo_name, asset["path"])
            if key in seen:
                continue
            seen.add(key)

            practices = asset.get("practices", [])
            primary_practice = practices[0] if practices else "platform"
            secondary_practices = practices[1:] if len(practices) > 1 else []

            entry = {
                "id": f"{repo_name}::{asset['path']}",
                "repo": repo_name,
                "repo_path": repo_path,
                "path": asset["path"],
                "type": asset.get("type", "unknown"),
                "canonical_type": TYPE_MAP.get(asset.get("type", "unknown"), "configs"),
                "description": asset.get("description", ""),
                "primary_practice": primary_practice,
                "secondary_practices": secondary_practices,
                "all_practices": practices,
                "reuse_potential": asset.get("reuse_potential", "medium"),
            }
            catalog.append(entry)

    return catalog


def build_practice_assets(catalog):
    """Group assets by practice (primary + secondary)."""
    practice_assets = defaultdict(list)

    for entry in catalog:
        for practice in entry["all_practices"]:
            if practice in PRACTICES:
                practice_assets[practice].append(entry)

    return practice_assets


def compute_plugin_readiness(assets_by_type):
    """Determine plugin readiness based on asset types present."""
    has_skills = len(assets_by_type.get("skills", [])) > 0
    has_commands = len(assets_by_type.get("commands", [])) > 0
    has_agents = len(assets_by_type.get("agents", [])) > 0

    if has_skills and has_commands:
        return "ready"
    elif has_skills or has_commands or has_agents:
        return "partial"
    else:
        return "needs-generation"


def build_manifest(practice, assets, practice_integrations):
    """Build a per-practice manifest."""
    assets_by_type = defaultdict(list)
    source_repos = set()

    for asset in assets:
        canonical = asset["canonical_type"]
        assets_by_type[canonical].append({
            "path": asset["path"],
            "repo": asset["repo"],
            "description": asset["description"],
            "reuse_potential": asset["reuse_potential"],
        })
        source_repos.add(asset["repo"])

    readiness = compute_plugin_readiness(assets_by_type)

    has_skill = len(assets_by_type.get("skills", [])) > 0
    has_commands = len(assets_by_type.get("commands", [])) >= 3
    has_agent = len(assets_by_type.get("agents", [])) > 0
    has_hooks = len(assets_by_type.get("hooks", [])) > 0
    has_mcp = len(assets_by_type.get("mcp_configs", [])) > 0

    total = sum(len(v) for v in assets_by_type.values())
    high_reuse = sum(
        1 for asset in assets if asset["reuse_potential"] == "high"
    )

    manifest = {
        "practice": practice,
        "plugin_name": f"proagent-{practice}",
        "plugin_readiness": readiness,
        "assets": {t: assets_by_type.get(t, []) for t in ASSET_TYPES},
        "gaps": {
            "missing_skill": not has_skill,
            "missing_commands": not has_commands,
            "missing_agent": not has_agent,
            "missing_hooks": not has_hooks,
            "missing_mcp": not has_mcp,
            "recommended_integrations": practice_integrations.get(practice, []),
        },
        "statistics": {
            "total_assets": total,
            "high_reuse": high_reuse,
            "source_repos": sorted(list(source_repos)),
        },
    }
    return manifest


def build_gaps(manifests):
    """Build gap analysis JSON."""
    gaps = {}
    for practice, manifest in manifests.items():
        g = manifest["gaps"]
        gaps[practice] = {
            "plugin_name": manifest["plugin_name"],
            "plugin_readiness": manifest["plugin_readiness"],
            "has_skill": not g["missing_skill"],
            "skill_count": len(manifest["assets"]["skills"]),
            "has_3_commands": not g["missing_commands"],
            "command_count": len(manifest["assets"]["commands"]),
            "has_agent": not g["missing_agent"],
            "agent_count": len(manifest["assets"]["agents"]),
            "has_hooks": not g["missing_hooks"],
            "hook_count": len(manifest["assets"]["hooks"]),
            "has_mcp": not g["missing_mcp"],
            "mcp_count": len(manifest["assets"]["mcp_configs"]),
            "total_assets": manifest["statistics"]["total_assets"],
            "high_reuse_count": manifest["statistics"]["high_reuse"],
            "source_repos": manifest["statistics"]["source_repos"],
            "recommended_integrations": g["recommended_integrations"],
            "missing_components": [],
        }
        if g["missing_skill"]:
            gaps[practice]["missing_components"].append("SKILL.md (at least 1)")
        if g["missing_commands"]:
            gaps[practice]["missing_components"].append(f"Commands (need 3, have {len(manifest['assets']['commands'])})")
        if g["missing_agent"]:
            gaps[practice]["missing_components"].append("Agent definition")
        if g["missing_hooks"]:
            gaps[practice]["missing_components"].append("Hook definitions")
        if g["missing_mcp"]:
            gaps[practice]["missing_components"].append("MCP config")

    return gaps


def build_summary_md(catalog, manifests, gaps):
    """Build human-readable summary markdown."""
    lines = []
    lines.append("# Provectus Asset Catalog Summary")
    lines.append(f"\n**Generated:** 2026-02-16")
    lines.append(f"**Total Assets:** {len(catalog)}")
    lines.append(f"**Source Repos:** {len(set(e['repo'] for e in catalog))}")
    lines.append(f"**Practices:** {len(PRACTICES)}")
    lines.append("")

    # Overall stats
    type_counts = defaultdict(int)
    reuse_counts = defaultdict(int)
    for e in catalog:
        type_counts[e["canonical_type"]] += 1
        reuse_counts[e["reuse_potential"]] += 1

    lines.append("## Asset Type Distribution\n")
    lines.append("| Type | Count |")
    lines.append("|------|-------|")
    for t in ASSET_TYPES:
        lines.append(f"| {t} | {type_counts.get(t, 0)} |")

    lines.append(f"\n## Reuse Potential Distribution\n")
    lines.append("| Rating | Count |")
    lines.append("|--------|-------|")
    for r in ["high", "medium", "low"]:
        lines.append(f"| {r} | {reuse_counts.get(r, 0)} |")

    # Per-practice overview table
    lines.append("\n## Per-Practice Overview\n")
    lines.append("| Practice | Plugin | Readiness | Skills | Commands | Agents | Hooks | MCP | Total | High Reuse |")
    lines.append("|----------|--------|-----------|--------|----------|--------|-------|-----|-------|------------|")
    for p in PRACTICES:
        m = manifests.get(p)
        if m:
            a = m["assets"]
            s = m["statistics"]
            lines.append(
                f"| {p} | proagent-{p} | {m['plugin_readiness']} | "
                f"{len(a['skills'])} | {len(a['commands'])} | {len(a['agents'])} | "
                f"{len(a['hooks'])} | {len(a['mcp_configs'])} | {s['total_assets']} | {s['high_reuse']} |"
            )

    # Gap analysis summary
    lines.append("\n## Gap Analysis Summary\n")
    lines.append("| Practice | Readiness | Missing Components |")
    lines.append("|----------|-----------|-------------------|")
    for p in PRACTICES:
        g = gaps.get(p, {})
        missing = g.get("missing_components", [])
        status = g.get("plugin_readiness", "needs-generation")
        missing_str = "; ".join(missing) if missing else "None - complete"
        lines.append(f"| {p} | {status} | {missing_str} |")

    # Detailed per-practice sections
    lines.append("\n## Detailed Practice Breakdown\n")
    for p in PRACTICES:
        m = manifests.get(p)
        if not m:
            continue
        lines.append(f"### {p} (proagent-{p})\n")
        lines.append(f"**Readiness:** {m['plugin_readiness']}")
        lines.append(f"**Source Repos:** {', '.join(m['statistics']['source_repos'])}")
        lines.append(f"**Recommended Integrations:** {', '.join(m['gaps']['recommended_integrations'])}")
        lines.append("")

        for t in ASSET_TYPES:
            items = m["assets"].get(t, [])
            if items:
                lines.append(f"**{t}** ({len(items)}):")
                for item in items[:10]:  # Cap at 10 for readability
                    reuse_badge = f"[{item['reuse_potential']}]"
                    lines.append(f"- {reuse_badge} `{item['repo']}` / `{item['path']}`")
                if len(items) > 10:
                    lines.append(f"- ... and {len(items) - 10} more")
                lines.append("")

    return "\n".join(lines)


def main():
    repos = load_scan_reports()
    print(f"Loaded {len(repos)} repos from scan reports")

    catalog = build_unified_catalog(repos)
    print(f"Unified catalog: {len(catalog)} assets (deduplicated)")

    practice_assets = build_practice_assets(catalog)

    # Build manifests
    manifests = {}
    for practice in PRACTICES:
        assets = practice_assets.get(practice, [])
        manifests[practice] = build_manifest(practice, assets, PRACTICE_INTEGRATIONS)

    # Build gap analysis
    gaps = build_gaps(manifests)

    # Write catalog.json
    catalog_path = os.path.join(OUTPUT_DIR, "catalog.json")
    with open(catalog_path, "w") as f:
        json.dump({
            "generated": "2026-02-16",
            "total_assets": len(catalog),
            "total_repos": len(repos),
            "practices": PRACTICES,
            "assets": catalog,
        }, f, indent=2)
    print(f"Wrote {catalog_path}")

    # Write gaps.json
    gaps_path = os.path.join(OUTPUT_DIR, "gaps.json")
    with open(gaps_path, "w") as f:
        json.dump(gaps, f, indent=2)
    print(f"Wrote {gaps_path}")

    # Write per-practice manifests
    for practice in PRACTICES:
        manifest_path = os.path.join(OUTPUT_DIR, f"proagent-{practice}-manifest.json")
        with open(manifest_path, "w") as f:
            json.dump(manifests[practice], f, indent=2)
        print(f"Wrote {manifest_path}")

    # Write catalog-summary.md
    summary_md = build_summary_md(catalog, manifests, gaps)
    summary_path = os.path.join(OUTPUT_DIR, "catalog-summary.md")
    with open(summary_path, "w") as f:
        f.write(summary_md)
    print(f"Wrote {summary_path}")

    # Summary stats
    print("\n=== SUMMARY ===")
    for p in PRACTICES:
        m = manifests[p]
        print(f"  {p}: {m['plugin_readiness']} ({m['statistics']['total_assets']} assets, {m['statistics']['high_reuse']} high-reuse)")


if __name__ == "__main__":
    main()
