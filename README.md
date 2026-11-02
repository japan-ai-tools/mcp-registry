# mcp-registry

Publishes the japan-ai-tools MCP servers to the official [MCP Registry](https://registry.modelcontextprotocol.io/) from GitHub Actions.

| Server | PyPI |
|---|---|
| io.github.japan-ai-tools/nexus-ja-data | [nexus-ja-data](https://pypi.org/project/nexus-ja-data/) |
| io.github.japan-ai-tools/jp-ocr-date-fix | [jp-ocr-date-fix](https://pypi.org/project/jp-ocr-date-fix/) |
| io.github.japan-ai-tools/jp-kansuji-guard | [jp-kansuji-guard](https://pypi.org/project/jp-kansuji-guard/) |
| io.github.japan-ai-tools/jp-invoice-check | [jp-invoice-check](https://pypi.org/project/jp-invoice-check/) |
| io.github.japan-ai-tools/jp-zengin-name | [jp-zengin-name](https://pypi.org/project/jp-zengin-name/) |

## How it works

1. `servers/<name>/server.json` holds the registry entry for each server. The package itself is already on PyPI, and its README carries the matching `mcp-name` line.
2. Actions → "Publish to MCP Registry" → Run workflow.
3. The workflow checks the files (`tests/check_servers.py`), installs the official `mcp-publisher`, logs in with GitHub OIDC (no stored secret), and publishes each server.

Steps follow the official guide: https://modelcontextprotocol.io/registry/github-actions.md

## Limits

- The registry is in preview. Its docs say breaking changes or data resets may occur.
- A version that is already in the registry cannot be published again. Raise the version in the package and in `server.json` first.
- This repository holds no code of the servers. See each server's own repository.
- Independent project. Not affiliated with the MCP Registry maintainers or GitHub.
- The listed tools are not tax, accounting or legal advice. Check results with a qualified professional.

## 日本語

japan-ai-tools の MCP サーバーを、GitHub Actions から公式 MCP Registry に載せるための置き場です。Actions の「Publish to MCP Registry」で Run workflow を押すと、GitHub のサーバー上で登録します(秘密の鍵は置きません)。

License: MIT
