# REA in OpenCode: usage, verification, and maintenance

## Installed shape

| Component | Current value |
| --- | --- |
| Upstream | `morluto/rea` |
| npm package | `rea-agents@6.7.0` |
| Global CLI | `C:\Users\Vishal\AppData\Roaming\npm\rea.cmd` |
| MCP server name | `rea` |
| MCP registration | `C:\Users\Vishal\.config\opencode\opencode.jsonc` |
| Managed skill | `C:\Users\Vishal\.agents\skills\reverse-engineer-anything` |
| OpenCode front door | `C:\Users\Vishal\.agents\skills\rea` |
| Global command | `C:\Users\Vishal\.config\opencode\commands\rea.md` |
| Catalog size | 207 MCP tools, 153 CLI commands, 6 MCP prompts |
| Managed skill version | 42 |
| Node runtime | 24.19.0 (supported) |

The skill is instructions only. The MCP server and CLI do the analysis. Native
analysis engines are optional and separate.

## The two invocation styles

### `@rea`

Type `@rea` in the composer, or name it in a prompt:

```text
@rea explain how offline search works in the app at C:\Apps\Example
```

OpenCode loads the skill whose path-derived ID is `rea`. That skill then loads
the full upstream `reverse-engineer-anything` workflow. `@rea` does not grant
new permissions and does not start an analysis by itself.

### `/rea`

```text
/rea understand how offline search works in C:\Apps\Example
```

The command expands to a prompt that loads the `rea` skill and applies it to the
argument. With no argument it asks for the target and the question first.

REA's MCP prompts are exposed as commands when the server advertises them:

```text
/rea:investigate_feature "offline search"
/rea:compare_application_versions "v1 path" "v2 path"
/rea:verify_reconstruction "reconstruction spec"
/rea:trace_crash "crash symptom"
/rea:audit_residual_unknowns
/rea:prepare_bounded_process_capture "process experiment"
```

Exact command names come from the live MCP catalog. If a prompt is not exposed
in the current session, use `/rea` and describe the same investigation.

## Capability map

| Target | Start with | Notes |
| --- | --- | --- |
| Native executable, library, or database | `open_binary` | Needs Ghidra, IDA, or Kuna on Windows; Hopper is not supported on `win32`. |
| JavaScript / Electron / ASAR | `analyze_javascript_application` | Static; no native engine. |
| .NET PE/CLI assembly | `inspect_managed_artifact` | Static; no native engine. |
| ZIP, APK, IPA, MSIX, DMG, PyInstaller | `open_binary`, then `inspect_artifact` | Use `detail: "summary"` for large inventories. |
| Apple bundle resources | `open_bundle_resources` | Plists, asset catalogs, keyed archives. |
| Android APK code | `inspect_android_package` | Needs caller-supplied JADX and JDK. |
| APK signature | `inspect_apk_signature` | Identity and integrity, not a trust verdict. |
| Firmware | `inspect_firmware_regions` / `extract_firmware` | Needs Binwalk or Unblob on Linux. |
| Browser page or scenario | `list_browser_targets` / `capture_browser_scenario` | Runtime actions execute in the declared scope. |
| Electron runtime | `list_electron_targets` | Check fuses before `--inspect` attempts. |
| HAR, SAZ, qlog, PCAP | `inspect_web_network_capture` / `inspect_packet_capture` | Recorded evidence, not live capture. |
| SQLite snapshot | `inspect_sqlite_database` | Needs a suitable Node.js SQLite runtime. |
| Go, Rust, ELF notes, PE certs, WASM, EVM, BEAM, PYC | Dedicated `inspect_*` tools | Mostly built-in static inspection. |
| Model artifacts, IL2CPP, GPU code | Dedicated `inspect_*` tools | Static metadata, not model behavior. |
| Process behavior | Bounded process capture | Linux/macOS PTY; explicit actions only. |

The upstream skill has the complete route table and each guide's prerequisites.
Use the live tool catalog and `binary_session` availability, not this table
alone, to decide whether an operation is possible.

## Investigation loop

1. **Frame the question.** Target, version, feature, and what evidence would
   answer it. Resolve paths from the conversation and workspace first.
2. **Check existing state.** Inspect the current session and retained Evidence
   before opening a duplicate analysis.
3. **Start small.** Use a summary or inventory, then follow one concrete gap.
4. **Trace with evidence.** Link each conclusion to an Evidence ID. Keep
   observations, inferences, and unknowns distinct.
5. **Corroborate.** Add runtime observation only when static evidence cannot
   answer the question and the runtime is authorized and available.
6. **Finish.** Revisit the question list, export needed Evidence, and close an
   opened native session with `close_binary`.

## CLI fallback

The CLI uses the same workflows and Evidence contracts:

```powershell
rea analyze-javascript-application "C:\Apps\Example" --json
rea analyze "C:\Apps\Example" --json
rea inspect-managed-artifact "C:\Apps\Example.dll" --json
rea inspect-sqlite-database "C:\data\app.db" --table notes --row-limit 20 --json
rea doctor --client opencode --json
rea doctor --skill --json
```

Large results should be written to a file and paged:

```powershell
rea analyze-javascript-application "C:\Apps\Example" --json > app-evidence.json
rea inspect-analysis-view app-view.json
```

Use `npx -y rea-agents@latest ...` only when the global CLI is unavailable.
The installed global CLI is the faster and more predictable path.

## Verification

```powershell
opencode mcp list
rea doctor --client opencode --json
rea doctor --skill --json
npx skills ls -g -a opencode
```

Expected signs:

- `opencode mcp list` shows `rea` as connected.
- `rea doctor --client opencode --json` reports `healthy: true` for the OpenCode
  registration. `environment_healthy` can be false when native engines are
  missing; that does not block static JavaScript, .NET, or artifact work.
- `rea doctor --skill --json` reports `identity.skill.state: "aligned"`.
- The skill list includes `rea` and `reverse-engineer-anything`.
- `@rea` loads both skills, and `/rea` expands into a prompt.

## Troubleshooting

| Symptom | Check | Action |
| --- | --- | --- |
| REA tools missing | `opencode mcp list` | Reconnect in `/mcps`; restart the session if the registration is aligned. |
| Server slow to start | `rea --version` | The global CLI works; the config may still launch through `npx`. Keep it unless you deliberately re-run setup. |
| `npx` cache error | `npm cache verify` | Clear the broken `_npx` entry or use the global `rea` CLI. |
| Native analysis unavailable | `rea doctor --client opencode --json` | Install or point REA at Hopper, Ghidra, IDA, JADX, or Kuna only with approval. |
| Skill out of date | `rea doctor --skill --json` | Run `rea setup --skill-client opencode --yes --json` after reviewing the plan. |
| MCP returns a huge result | Tool result | Use the retained `parent_evidence_id` with `inspect_analysis_view`, or export a bundle. |

Do not repeat an identical analysis call just to get a smaller response. Page
the retained Evidence instead.

## Maintenance

```powershell
rea update
rea doctor --client opencode --json
rea setup --client opencode --dry-run --json
rea setup --client opencode --yes
```

Review the dry-run paths and backups before applying setup. Setup is broader
than this wrapper: it can refresh MCP registration and replace the managed
`reverse-engineer-anything` skill. The local `rea` wrapper is not managed by
REA setup and stays in place unless you remove it.

Uninstall only the REA-owned pieces when you mean to remove the integration:

```powershell
rea uninstall
rea uninstall --purge-data
```

Uninstall preserves Hopper, Node.js, Evidence files, captures, unrelated skills,
and other MCP servers. To remove only the OpenCode alias, delete
`~/.agents/skills/rea` and `~/.config/opencode/commands/rea.md` after removing
the MCP registration.

## Sources

- <https://github.com/morluto/rea>
- <https://github.com/morluto/rea/blob/main/docs/installation.md>
- <https://github.com/morluto/rea/blob/main/docs/cli.md>
- <https://github.com/morluto/rea/blob/main/docs/mcp-contracts.md>
- <https://github.com/morluto/rea/blob/main/docs/mcp-prompts.md>
- <https://opencode.ai/v2/docs/skills/>
- <https://opencode.ai/v2/docs/commands/>
- <https://opencode.ai/v2/docs/mcp-servers/>
