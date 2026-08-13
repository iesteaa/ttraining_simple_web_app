# Dev Container (DOOD)

This workspace uses a development container for editing and tooling while Docker Compose remains the runtime for application services.

## Runtime boundaries

- Dev Container: editor, shell, git, Python/Node tooling, Docker CLI.
- Compose services: `backend`, `frontend`, `db`, `db_test` from the root `compose.yaml`.

Docker CLI and Docker Compose CLI are provided by the Dev Containers DOOD feature.

## Why Docker-outside-of-Docker

The Dev Container mounts host Docker socket (`/var/run/docker.sock`) so commands run from the container terminal can control the host Docker daemon:

- `docker compose up`
- `docker compose ps`
- `docker compose logs`
- `docker compose exec`

## Open and verify

1. Reopen the repository in Dev Container.
2. Run `docker compose ps`.
3. Run VS Code tasks `backend: checks` and `frontend: checks`.

## First-Time Setup for New Developers

1. Ensure Docker is running on the host machine.
2. Open the repository in VS Code and run `Dev Containers: Reopen in Container`.
3. Wait until container build and setup commands complete.
4. In the dev container terminal:

```bash
docker compose up -d --build
docker compose ps
```

5. Confirm runtime services are visible:
  - `backend` is running
  - `frontend` is running
  - `db` is healthy
  - `db_test` is healthy

## Verify DOOD Connectivity

Run these commands from inside the dev container terminal:

```bash
docker ps
docker compose ps
docker compose exec backend python -m pytest -q
docker compose exec frontend yarn lint
```

If all commands run successfully, the dev container can control host Docker daemon correctly via mounted socket.

## Verify SSH Agent Forwarding

Git operations such as `git status`, `git add`, and `git commit` work locally inside the Dev Container because the repository and `.git` directory are mounted into the workspace.

However, `git push` over SSH also requires access to the developer's SSH identity.

The intended flow is:

```text
WSL host
│
├── ~/.ssh/id_ed25519
└── ssh-agent
      │
      │ VS Code / Dev Containers forwarding
      ▼
Dev Container
│
├── SSH_AUTH_SOCK
├── git
└── ssh
      │
      ▼
    GitHub
```

The private SSH key must stay on the developer host. Do not copy the private key into the Dev Container, Docker image, or repository.

### Basic verification inside the Dev Container

After rebuilding or reopening the Dev Container, run:

```bash
echo "$SSH_AUTH_SOCK"
ssh-add -l
ssh -T git@github.com
```

Expected behavior:

- `echo "$SSH_AUTH_SOCK"` prints a socket path, often similar to `/tmp/vscode-ssh-auth-....sock`.
- `ssh-add -l` shows the SSH identity forwarded from the host agent.
- `ssh -T git@github.com` authenticates successfully with GitHub.

If all three checks pass, test:

```bash
git push
```

### Common SSH symptoms

#### `Could not open a connection to your authentication agent.`

This means the current shell cannot reach an SSH agent.

Check:

```bash
echo "$SSH_AUTH_SOCK"
```

If the value is empty or points to an invalid socket, make sure the host-side SSH agent is running before reopening the Dev Container.

#### `The agent has no identities.`

This means the SSH agent can be reached, but no SSH key is loaded into that agent.

This was the main problem encountered in this project.

The WSL terminal had a valid SSH key and could authenticate to GitHub, but the Dev Container initially saw an agent with no identities.

Use the layered checks below to find where the identity disappears.

## SSH Troubleshooting: WSL -> VS Code -> Dev Container

Check each layer in order.

### 1. WSL terminal

Run:

```bash
echo "$SSH_AUTH_SOCK"
ssh-add -l
ssh -T git@github.com
```

Expected:

- `SSH_AUTH_SOCK` is not empty.
- `ssh-add -l` shows an SSH identity.
- GitHub authentication succeeds.

For this project, the existing key is:

```text
~/.ssh/id_ed25519
```

There is no need to generate a second SSH key if this key already works with GitHub.

### 2. VS Code WSL terminal

Open the project through WSL:

```bash
cd ~/simple-web-app
code .
```

Before reopening in a Dev Container, confirm VS Code is using the **WSL: Ubuntu** context.

Then run from the VS Code integrated terminal:

```bash
echo "$SSH_AUTH_SOCK"
ssh-add -l
ssh -T git@github.com
```

The same identity visible in the normal WSL terminal should also be visible here.

### 3. Dev Container terminal

Reopen or rebuild the Dev Container, then run:

```bash
echo "$SSH_AUTH_SOCK"
ssh-add -l
ssh -T git@github.com
git push
```

The Dev Container may use a different socket path such as:

```text
/tmp/vscode-ssh-auth-xxxxxxxx.sock
```

This is normal. The important point is that `ssh-add -l` must still show the expected identity.

### Do not start another SSH agent inside the Dev Container

Do not run this inside the Dev Container during normal use:

```bash
eval "$(ssh-agent -s)"
```

Doing so creates a new SSH agent inside the container and replaces the `SSH_AUTH_SOCK` provided by VS Code.

That new agent normally has no identities, so SSH authentication will fail even though the WSL agent is correctly configured.

## Make the WSL SSH Agent Available Automatically

After a Windows/WSL restart, the SSH key file still exists, but the previous `ssh-agent` process and its socket no longer exist.

To make the WSL-side agent available before VS Code and Dev Containers start, add the following setup near the bottom of:

```text
~/.bashrc
```

```bash
# --- SSH agent setup ---

SSH_AGENT_ENV="$HOME/.ssh/ssh-agent"

# Try to restore information about an existing ssh-agent.
if [ -z "$SSH_AUTH_SOCK" ] || [ ! -S "$SSH_AUTH_SOCK" ]; then
    if [ -f "$SSH_AGENT_ENV" ]; then
        eval "$(cat "$SSH_AGENT_ENV")" > /dev/null
    fi
fi

# If the saved agent no longer exists, start a new one.
if [ -z "$SSH_AUTH_SOCK" ] || [ ! -S "$SSH_AUTH_SOCK" ]; then
    mkdir -p "$HOME/.ssh"
    ssh-agent -s > "$SSH_AGENT_ENV"
    eval "$(cat "$SSH_AGENT_ENV")" > /dev/null
fi

# Load the existing GitHub SSH key if the agent has no identities.
if ! ssh-add -l > /dev/null 2>&1; then
    ssh-add "$HOME/.ssh/id_ed25519"
fi
```

This project uses an existing Ed25519 key:

```text
~/.ssh/id_ed25519
```

If a developer uses a different key filename, adjust only the final `ssh-add` path accordingly.

Do not copy the same SSH key between developers. Each developer should use their own SSH identity.

### Important `.profile` / `.bashrc` note

On the current Ubuntu setup, `~/.profile` already sources `~/.bashrc`.

Therefore, the SSH-agent setup only needs to exist in `.bashrc`.

Do not make `.bashrc` source `.profile` again, because this can create a recursive loop:

```text
.profile
  -> .bashrc
      -> .profile
          -> .bashrc
          ...
```

## Restart Sequence After SSH Agent Changes

After changing `.bashrc`, SSH-agent state, or VS Code WSL settings, restart the complete chain:

1. Close all VS Code windows.
2. Open Windows PowerShell or Windows Terminal.
3. Run:

```powershell
wsl --shutdown
```

4. Reopen Ubuntu/WSL.
5. Verify the agent is automatically available:

```bash
echo "$SSH_AUTH_SOCK"
ssh-add -l
ssh -T git@github.com
```

6. Open the project through WSL:

```bash
cd ~/simple-web-app
code .
```

7. Confirm VS Code shows **WSL: Ubuntu**.
8. Run **Dev Containers: Rebuild and Reopen in Container**.
9. Verify again inside the Dev Container:

```bash
echo "$SSH_AUTH_SOCK"
ssh-add -l
ssh -T git@github.com
git push
```

## Optional VS Code WSL Setting

If Dev Containers still appears to use the wrong host context for SSH-agent discovery, this local VS Code User Setting can be tested:

```json
"dev.containers.executeInWSL": true
```

This belongs in local **VS Code User Settings**, not in the project's workspace settings or `devcontainer.json`.

After changing it, repeat the full restart sequence above.

## Inspect Dev Containers SSH Forwarding

If the WSL terminal and VS Code WSL terminal both show the correct identity, but the Dev Container still reports:

```text
The agent has no identities.
```

open:

```text
Dev Containers: Show Container Log
```

and search for:

```text
ssh-agent
SSH_AUTH_SOCK
```

This helps identify how the Dev Containers helper created the forwarding socket and whether it fell back to another agent endpoint.

## Manual SSH Socket Mount Warning

A manual mount such as:

```json
"source=${localEnv:SSH_AUTH_SOCK},target=/ssh-agent,type=bind"
```

was tested during troubleshooting but was not reliable in this environment.

The Dev Containers CLI resolved the source to an empty value:

```text
--mount source=,target=/ssh-agent,type=bind
```

which caused Docker to fail with:

```text
invalid value for 'source': value is empty
```

For this project, prefer:

```text
WSL ssh-agent initialization
+
VS Code built-in SSH-agent forwarding
```

instead of manually mounting `${localEnv:SSH_AUTH_SOCK}`.

## SSH Troubleshooting Reference

A useful practical reference used while resolving this issue:

- Qiita: **Dev ContainerでGitHubにSSH接続する手順**
  - https://qiita.com/ZuyaTepo/items/7beb120346210353bbe5

The article demonstrates:

- starting `ssh-agent` automatically from `.bashrc`
- loading an SSH private key into the agent
- checking GitHub SSH connectivity
- forwarding SSH authentication into a Dev Container

The article generates a new RSA key (`id_rsa`), while this project already had a working Ed25519 key from its existing SSH-based repository setup.

Therefore, the project adapts the idea by using:

```bash
ssh-add "$HOME/.ssh/id_ed25519"
```

instead of generating and loading a new `id_rsa` key.

## Expected Runtime Boundary

- Dev container: editor, terminal, git, local tooling.
- Compose runtime: `backend`, `frontend`, `db`, `db_test`.
- Application services remain defined in root `compose.yaml`.

## Common issues

- Permission denied for Docker socket:
  - Check host socket group: `ls -l /var/run/docker.sock`
  - Rebuild the Dev Container after UID/GID changes.
- Compose services not running:
  - Start stack from Dev Container terminal with `docker compose up -d --build`.
- Missing local tooling commands:
  - Re-run `postCreateCommand` manually:
    - `python3 -m pip install --user -r backend/requirements-dev.txt`
    - `npm ci --prefix frontend`
- Host port conflicts (`5432`, `5433`, `8000`, `5173`):
  - Stop conflicting process or container, then rerun `docker compose up -d --build`.
- Outdated container setup after configuration changes:
  - Run `Dev Containers: Rebuild Container`.

## References

- Qiita — Dev ContainerでGitHubにSSH接続する手順  
  https://qiita.com/ZuyaTepo/items/7beb120346210353bbe5
- VS Code — Sharing Git credentials with your container  
  https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials

## Space for Improvement : 
- frontend container couldnt be builded if we build with docker CLI in dev container -> this part of limitation from DooD concept, when we use bind mount. Problem statement "Docker Compose runs within the Dev Container's filesystem namespace, whereas the Docker daemon that actually creates the application container resides outside the Dev Container. Consequently, a bind-mount source path that is valid within the Dev Container is not necessarily valid for the Docker daemon."
- build application container using host Docker compose instead. 
