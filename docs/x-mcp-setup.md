# 本机 X MCP 发推配置（Grok）

> **安全：** 密钥只放环境变量 / GitHub Secrets，不要写进仓库、聊天、截图。  
> 若 Consumer Key 曾泄露，请先到 [Developer Portal](https://developer.x.com/) **Regenerate**。

当前 Grok 会话**默认没有** X 发帖 MCP；配置并重启后，才可以在对话里说「帮我发推…」。

---

## 你需要的 4 个密钥（OAuth 1.0a）

| 名称 | 环境变量建议 | 说明 |
|------|----------------|------|
| API Key (Consumer Key) | `TWITTER_API_KEY` | 应用密钥 |
| API Key Secret | `TWITTER_API_SECRET` | 应用密钥 Secret |
| Access Token | `TWITTER_ACCESS_TOKEN` | **用户**访问令牌 |
| Access Token Secret | `TWITTER_ACCESS_TOKEN_SECRET` | **用户**访问令牌 Secret |

仅有 Consumer Key **不能发帖**。请在 App → **Keys and tokens** 生成 **Access Token and Secret**，App 权限设为 **Read and write**。

可选（周更爬取用，只读）：

| Bearer Token | `TWITTER_BEARER_TOKEN` | `scripts/weekly_x_crawl.py` |

---

## 方案 A：社区 Twitter MCP（推荐，简单）

使用 npm 包 `@enescinar/twitter-mcp`（支持发帖、搜索）。

### 1. 用户级环境变量（PowerShell 永久）

```powershell
# 把下面换成你自己的新密钥（Regenerate 之后的）
[System.Environment]::SetEnvironmentVariable("TWITTER_API_KEY", "你的API_KEY", "User")
[System.Environment]::SetEnvironmentVariable("TWITTER_API_SECRET", "你的API_SECRET", "User")
[System.Environment]::SetEnvironmentVariable("TWITTER_ACCESS_TOKEN", "你的ACCESS_TOKEN", "User")
[System.Environment]::SetEnvironmentVariable("TWITTER_ACCESS_TOKEN_SECRET", "你的ACCESS_TOKEN_SECRET", "User")
```

重新打开终端 / Grok，使变量生效。

### 2. 写入 Grok MCP 配置

编辑 `C:\Users\Sea_Star\.grok\config.toml`，追加（密钥用环境变量引用，不要写死）：

```toml
[mcp_servers.x]
command = "npx"
args = ["-y", "@enescinar/twitter-mcp"]
enabled = true
startup_timeout_sec = 120
env = {
  API_KEY = "${TWITTER_API_KEY}",
  API_SECRET_KEY = "${TWITTER_API_SECRET}",
  ACCESS_TOKEN = "${TWITTER_ACCESS_TOKEN}",
  ACCESS_TOKEN_SECRET = "${TWITTER_ACCESS_TOKEN_SECRET}"
}
```

或用 CLI（仍建议 env 已在系统里）：

```bash
grok mcp add x -e API_KEY=%TWITTER_API_KEY% -e API_SECRET_KEY=%TWITTER_API_SECRET% -e ACCESS_TOKEN=%TWITTER_ACCESS_TOKEN% -e ACCESS_TOKEN_SECRET=%TWITTER_ACCESS_TOKEN_SECRET% -- npx -y @enescinar/twitter-mcp
```

### 3. 诊断

```bash
grok mcp list
grok mcp doctor x
```

### 4. 在 Grok 里发推

新开一轮会话后说：

```text
使用 x MCP 发一条推文（不要改文案）：
🎬 开源了 awesome-kling …
https://github.com/DSeaStar/awesome-kling
```

发帖前建议你在对话里再确认一次。

---

## 方案 B：官方 Hosted X MCP（xurl）

适合已开通 OAuth 2.0 的 App：

```bash
# 需 Node + 官方桥
npx -y @xdevplatform/xurl mcp https://api.x.com/mcp
```

Grok 配置示例（具体参数以 [X 开发者社区 Hosted MCP 公告](https://devcommunity.x.com/t/announcing-the-hosted-x-mcp/269558) 为准）：

```toml
[mcp_servers.x_official]
command = "npx"
args = ["-y", "@xdevplatform/xurl", "mcp", "https://api.x.com/mcp"]
enabled = true
startup_timeout_sec = 120
env = {
  CLIENT_ID = "${X_CLIENT_ID}",
  CLIENT_SECRET = "${X_CLIENT_SECRET}"
}
```

首次通常会走浏览器 OAuth。

---

## 方案 C：本机脚本发推（不经过 MCP 协议）

同一套 4 个环境变量，直接调 X API v2：

```bash
cd C:\Users\Sea_Star\awesome-kling
python scripts/post_to_x.py --text "你好，这是测试。"
python scripts/post_to_x.py --file docs/tweet-awesome-kling.txt
```

说明见脚本头注释。适合 CI/定时任务；MCP 更适合对话式「让 Grok 发」。

---

## 安全清单

- [ ] 已轮换泄露过的 Consumer Key  
- [ ] Access Token 权限为 Read and write  
- [ ] 密钥不在 git 中（检查 `git status`）  
- [ ] `.env` 已在 `.gitignore`  
- [ ] 发帖前人工确认文案  

---

## 故障排除

| 现象 | 处理 |
|------|------|
| 403 / 权限不足 | App 改为 Read and write，重新生成 Access Token |
| doctor 启动超时 | `startup_timeout_sec = 120`，先手动 `npx -y @enescinar/twitter-mcp` 预拉包 |
| `${VAR}` 未展开 | 改成系统环境变量后重启 Grok；或用 `grok mcp add -e KEY=value`（value 仍勿提交） |
| 本会话搜不到 x 工具 | MCP 需重开 Grok 会话后才会加载 |
