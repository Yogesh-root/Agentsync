# agentsync

**One `AGENTS.md`. Every AI coding agent.**

Claude Code reads `CLAUDE.md`. Gemini wants `GEMINI.md`. Cursor wants `.cursor/rules`. Copilot, Windsurf, Codex... each has its own file, and they drift apart within a week.

`agentsync` keeps **one source of truth** and generates the rest. Zero dependencies, offline, one command.

```console
$ pip install agentsync
$ agentsync init          # adopts your existing CLAUDE.md if you have one
$ agentsync sync
  wrote   CLAUDE.md
  wrote   GEMINI.md
  wrote   .github/copilot-instructions.md
  wrote   .windsurfrules
  wrote   .cursor/rules/agents.mdc
  wrote   .claude/skills/example
```

## Why you'll like it

- **Safe by default.** Never overwrites a file it didn't generate (use `--force` once to take over).
- **Drift detection in CI.** `agentsync sync --check` exits 1 if anyone hand-edited a generated file.
- **Skills too.** `.agents/skills/*` is synced to `.claude/skills/*`.
- **`agentsync doctor`** lints your setup: token bloat, leaked API keys, malformed skills, drift.
- **Local-first.** No network, no account, no telemetry, no dependencies.

## Commands

| Command | What it does |
|---|---|
| `agentsync init` | Create `AGENTS.md`, or adopt an existing agent file |
| `agentsync sync` | Generate all agent files (`--dry-run`, `--only claude,cursor`, `--force`) |
| `agentsync sync --check` | CI mode: fail on drift |
| `agentsync doctor` | Health check for your agent setup |

## CI

```yaml
- run: pip install agentsync && agentsync sync --check
```

## Roadmap

- [ ] `watch` mode
- [ ] Per-agent overrides (`AGENTS.claude.md`)
- [ ] More targets (Aider, Zed, Amp)
- [ ] Pre-commit hook

PRs welcome. Adding a target is one line in `TARGETS`.

## License

MIT
