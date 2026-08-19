# エンドツーエンド Web 学習プロジェクト

フロントエンド、バックエンド、API、データベース、テスト、Docker Compose の流れがどうつながるのかを学び、実際に確認するための、小さなタスク管理 Web アプリです。

このリポジトリは学習記録として書かれていますが、監督者のレビューでも読みやすいことを意図しています。そのため、ドキュメントでは「今あるもの」「起動方法」「次に何をするか」を中心にまとめています。

## 概要

現在の状態:

- バックエンドは FastAPI、SQLAlchemy、PostgreSQL、そして自動テストまで含めて完成しています。
- フロントエンドは Vue 3 + TypeScript のひな形として存在していますが、まだバックエンドとは接続されていません。
- ローカル開発の主な実行環境は Docker Compose です。

想定しているアプリケーションの流れ:

```text
ユーザー操作
      ↓
Vue フロントエンド
      ↓ HTTP リクエスト
FastAPI バックエンド
      ↓
ビジネスロジックとバリデーション
      ↓
SQLAlchemy ORM
      ↓
PostgreSQL データベース
      ↓
JSON レスポンス
      ↓
Vue の状態更新と UI 更新
```

この図は、後の統合ステージで実現したい全体の流れを表しています。リポジトリにはすでに VS Code の dev container ワークスペースがあり、Docker-outside-of-Docker (DOOD) を使って開発できる状態になっています。

## クイックスタート

1. まだローカルに用意していない場合は、例の環境ファイルをコピーします。

```bash
cp .env.example .env
cp .env.test.example .env.test
```

2. リポジトリを VS Code の dev container で開きます。

```text
Dev Containers: Reopen in Container
```

3. dev container 内のターミナルで、Docker Compose でアプリ全体を起動します。

```bash
docker compose up -d --build
docker compose watch --no-up
```

4. アプリ本体を起動したら、まず migration の状態を確認します。

```bash
docker compose exec backend alembic current
docker compose exec backend alembic heads
```

`alembic heads` が `alembic current` より新しい revision を示している場合は、次を実行します。

```bash
docker compose exec backend alembic upgrade head
docker compose exec backend alembic current
```

5. FastAPI が正しく応答していることを確認します。

```bash
curl http://127.0.0.1:8000/health
```

6. フォーマット、lint、typecheck、テストはワークスペースタスクを使います。これらのタスクは `docker compose exec` 経由で実行されます。

## 現在の状態

```text
環境セットアップ             ✅ 完了
FastAPI CRUD API              ✅ 完了
SQLAlchemy + PostgreSQL       ✅ 完了
Docker Compose ランタイム     ✅ 完了
自動バックエンドテスト       ✅ 完了
CORS 設定                     ✅ 完了
フロントエンドのひな形       ✅ 完了
dev container ワークスペース  ⏳ 検証中
フロントエンド接続           ⏳ 保留
フロントエンド画面            ⏳ 保留
```

バックエンドは SQLAlchemy と PostgreSQL で task データを保存しています。アプリ本体の実行環境は Docker Compose でコンテナ化され、開発時の編集環境は dev container ワークスペースで動いています。フロントエンドのひな形はありますが、API クライアントや task UI はまだこれからです。

## 技術スタック

| 項目 | 技術 |
|---|---|
| フロントエンド | Vue 3, Vite, TypeScript |
| バックエンド | Python, FastAPI |
| データベース | PostgreSQL, SQLAlchemy, Alembic |
| 実行環境 | Docker, Docker Compose |
| テスト | Pytest, FastAPI TestClient, Vitest |
| ツール | Ruff, ESLint, Oxlint, Prettier |
| 開発環境 | Visual Studio Code Dev Container (DOOD) |

## バージョン要件

以下のバージョンは固定または記載済みで、どの環境でも再現しやすいようにしています。

| コンポーネント | バージョン |
|---|---|
| Python | 3.12.10 |
| Node.js | 22.x |
| PostgreSQL | 17.10 |

参照元:

- Python バージョン: [`.python-version`](./.python-version)
- バックエンドイメージ: [`backend/Dockerfile`](./backend/Dockerfile)
- フロントエンドのエンジン要件: [`frontend/package.json`](./frontend/package.json)
- データベースイメージ: [`compose.yaml`](./compose.yaml)

## 実装済み内容

- FastAPI アプリケーションと `/`、`/health`、CRUD の task エンドポイント。
- SQLAlchemy と Alembic を使った PostgreSQL 永続化。
- 分離されたデータベースフィクスチャを使う自動バックエンドテスト。
- バックエンド、フロントエンド、データベースの Docker Compose サービス。
- コンテナ内で format、lint、typecheck、テストを実行する VS Code タスク。
- WSL 上で編集しつつ、アプリ本体はコンテナで動かす開発方式。

## 開発ツール

このプロジェクトでは、バックエンドとフロントエンドで別々の品質チェックコマンドを使います。いくつかは VS Code で保存したときに自動実行され、それ以外はコミット前確認用の VS Code タスクとして用意されています。

### バックエンド

- 保存時の format: Python ファイルを保存すると、VS Code が Ruff で自動フォーマットします。
- 保存時の import 整理: Python ファイルでは `source.organizeImports` も適用されるので、import の整理も一緒に行われます。
- format check: `docker compose exec backend env RUFF_CACHE_DIR=/tmp/ruff-cache python -m ruff format --check .`
- lint: `docker compose exec backend python -m ruff check .`
- type check: `docker compose exec backend python -m mypy .`
- テスト: `docker compose exec backend python -m pytest -q`

使い方:

1. バックエンドの Python ファイルを開きます。
2. 変更して保存すると、Ruff による format と import 整理が自動で行われます。

`Ctrl + Shift + P` -> `Tasks: Run Task` からも実行できます。
1. コミット前に `backend: format check` を実行して、フォーマッタと一致しているか確認します。
2. バックエンド全体を確認したいときは `backend: checks` を実行します。

### フロントエンド

- format check: `docker compose exec frontend yarn format:check`
- lint: `docker compose exec frontend yarn lint`
- type check: `docker compose exec frontend yarn type-check`
- unit tests: `docker compose exec frontend yarn test:unit`

`frontend/package.json` では、ローカル実行用のコマンドも定義されています。

- `yarn dev`
- `yarn build`
- `yarn lint`
- `yarn format:check`
- `yarn test:unit`

### ワークスペースタスク

- `backend: checks` は backend の format、lint、typecheck、tests を順番に実行します。
- `frontend: checks` は frontend の format、lint、typecheck を順番に実行します。

## 実装済み API

| 操作 | メソッド | エンドポイント | 期待される結果 |
|---|---|---|---|
| task を作成 | `POST` | `/tasks` | `201 Created` |
| task 一覧を取得 | `GET` | `/tasks` | `200 OK` |
| task 1件を取得 | `GET` | `/tasks/{task_id}` | `200 OK` または `404` |
| task を更新 | `PATCH` | `/tasks/{task_id}` | `200 OK` または `404` |
| task を削除 | `DELETE` | `/tasks/{task_id}` | `204 No Content` または `404` |
| データベースヘルス | `GET` | `/health/database` | `200 OK` または DB エラー |
| ヘルスチェック | `GET` | `/health` | `200 OK` |

## Docker Compose でアプリを起動する

このリポジトリでは、アプリ本体は Docker Compose で動かし、VS Code は dev container ワークスペースで使います。いつも通りワークスペースで編集したら、プロジェクトルートから次を実行します。

```bash
docker compose up --build
```

backend と frontend は `develop.watch` を使っているので、dev container 側のファイル変更はそのまま実行中のコンテナへ反映されます。

バックエンドは、ルートの `.env` ファイルから PostgreSQL の接続情報を読み込みます。Compose 内では `db` というサービス名でデータベースに接続します。

```text
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
POSTGRES_HOST
POSTGRES_PORT
CORS_ORIGINS
```

テスト実行時の Compose 用テストデータベースサービス名は `db_test` です。

開発フローのまとめ:

- dev container 上で編集して、そのまま保存する。
- アプリ本体は `docker compose up -d --build` と `docker compose watch --no-up` で起動する。
- チェックは [`.vscode/tasks.json`](./.vscode/tasks.json) の VS Code タスクを使う。
- `.env` と `.env.test` は Compose のサービス名と合わせておく。

アプリのアドレス:

```text
API:          http://127.0.0.1:8000
Swagger UI:   http://127.0.0.1:8000/docs
OpenAPI JSON: http://127.0.0.1:8000/openapi.json
Frontend:     http://localhost:5173
```

バックエンドとフロントエンドのチェックには、[`.vscode/tasks.json`](./.vscode/tasks.json) のタスクを使います。これらは `docker compose exec` 経由で実行されます。

再現性のメモ:

- `docker compose up --build` がアプリ実行の主な入口です。
- バックエンドとフロントエンドの依存関係は、ホストではなくイメージ内にインストールされます。
- Python と Node のバージョンは固定または記載済みで、どの環境でも同じ実行結果を得やすくしています。
- PostgreSQL は Compose の `db` サービスとして起動し、テストでは `db_test` を使います。

## ドキュメント

- [`LEARNING_PLAN.md`](./LEARNING_PLAN.md): ステージごとのロードマップと学習チェックポイント。
- [`PROGRESS.md`](./PROGRESS.md): 現在の進捗、完了済みチェックポイント、次の作業。

## 次のステージ

次の作業は **フロントエンドとバックエンドの最初の接続** です。

目的は、Vue のフロントエンドを FastAPI バックエンドに接続し、task 一覧と作成・更新・削除の最初の UI を作ることです。

予定している内容:

```text
Vue → GET /tasks
Vue → POST /tasks
Vue → PATCH /tasks/{task_id}
Vue → DELETE /tasks/{task_id}
```

このワークスペースの段階が終わったら、task 一覧、task フォーム、完了切り替え、削除操作、ローディング表示、エラー表示を実装していきます。

## リポジトリの考え方

このリポジトリでは、速度よりも理解を優先します。

目的はアプリを動かすことだけではなく、次の点を理解することです。

- データがどこから来るのか
- リクエストがどのようにバックエンドに届くのか
- 入力がどう検証されるのか
- ビジネスロジックがどこで実行されるのか
- データがどのように保存されるのか
- フロントエンドがレスポンスをどう受け取り表示するのか
- エラーをどう見つけ、どうテストするのか
