# エンドツーエンド Web 開発の進捗

**最終更新:** 2026-08-07
**現在のフェーズ:** Dev Container ワークスペースの実装が次

## プロジェクトの進捗

| 項目 | 状態 |
|---|---|
| 環境セットアップ | ✅ 完了 |
| Vue 3 + TypeScript 環境 | ✅ 完了 |
| FastAPI サーバー | ✅ 完了 |
| Task CRUD API | ✅ 完了 |
| Pydantic バリデーション | ✅ 完了 |
| HTTP ステータスとエラー処理 | ✅ 完了 |
| APIRouter リファクタリング | ✅ 完了 |
| SQLAlchemy と PostgreSQL の永続化 | ✅ 完了 |
| バックエンド自動テスト | ✅ 完了 |
| CORS | ✅ 完了 |
| フロントエンドのひな形 | ✅ 完了 |
| Dev Container ワークスペース | ⏳ 保留 |
| フロントエンドのタスク画面 | ⏳ 保留 |
| フロントエンドとバックエンドの接続 | ⏳ 保留 |

## 完了済みのバックエンドチェックポイント

### FastAPI の基礎

- [x] FastAPI のアプリケーションオブジェクトを作成した
- [x] バックエンドの開発サーバーを起動した
- [x] Swagger UI を開いて確認した
- [x] ルートエンドポイントとヘルスチェックを試した
- [x] ルートとエンドポイントの意味を理解した
- [x] HTTP メソッドと URL パスの関係を理解した

### スキーマとバリデーション

- [x] `TaskCreate` を作成した
- [x] `Task` を作成した
- [x] `TaskUpdate` を作成した
- [x] Pydantic の `Field` バリデーションを使った
- [x] 自動で `422` が返ることを確認した
- [x] 入力スキーマとレスポンススキーマの違いを理解した

### Task CRUD

- [x] `POST /tasks`
- [x] `GET /tasks`
- [x] `GET /tasks/{task_id}`
- [x] `PATCH /tasks/{task_id}`
- [x] `DELETE /tasks/{task_id}`
- [x] `201 Created` を使った
- [x] `204 No Content` を使った
- [x] `400 Bad Request` を使った
- [x] `404 Not Found` を使った
- [x] `raise HTTPException(...)` を使った

### Python と部分更新の考え方

- [x] ループで task データを探す方法を使った
- [x] `enumerate()` を使った
- [x] resource ID と list index の違いを理解した
- [x] `model_dump(exclude_unset=True)` を使った
- [x] `model_copy(update=...)` を使った
- [x] `tasks.pop(index)` を使った
- [x] メモリ上のデータが再起動で消える理由を理解した

### Router の整理

- [x] `app/` パッケージを作成した
- [x] `app/routers/` パッケージを作成した
- [x] スキーマを `app/schemas.py` に移した
- [x] task のルートを `app/routers/tasks.py` に移した
- [x] router prefix と tags を追加した
- [x] `main.py` に router を読み込ませた
- [x] リファクタリング後に CRUD を再確認した
- [x] task のパスを `/tasks` に統一した

### データベース永続化

- [x] `app/config.py` で Postgres の設定を作成した
- [x] `app/database.py` で SQLAlchemy の engine と session factory を作成した
- [x] `app/models.py` で Task の ORM モデルを作成した
- [x] `app/routers/tasks.py` を database session を使う形にした
- [x] `GET /health/database` を追加して接続確認できるようにした
- [x] Alembic の migration 用メタデータを接続した

## 現在の API 契約

```text
POST   /tasks
GET    /tasks
GET    /tasks/{task_id}
PATCH  /tasks/{task_id}
DELETE /tasks/{task_id}
GET    /health/database
GET    /health
```

## 直近のチェックポイント — フロントエンド接続

- [x] 分離用に Compose のテスト用データベースサービスがあることを確認した
- [x] Pytest を導入して設定した
- [x] FastAPI TestClient でアプリケーションを呼び出せるようにした
- [x] 独立したテスト DB またはトランザクションベースのテスト構成を作った
- [x] CRUD の正常系をテストした
- [x] バリデーション失敗と対象データなしのケースをテストした
- [x] テストスイートを 1 つのコマンドで実行できるようにした

## 再現性メモ

- アプリ本体は Docker Compose で動かしている。
- VS Code は WSL 側で使っている。
- Python のバージョンは [`.python-version`](./.python-version) で固定している。
- 実行時のバージョン情報は [README.md](./README.md) と Dockerfile に記載している。

## その後のチェックポイント

### 自動バックエンドテスト

- [x] Pytest を導入して設定した
- [x] FastAPI TestClient を使った
- [x] 独立したテスト DB を用意した
- [x] CRUD の正常系をテストした
- [x] バリデーション失敗と対象データなしのケースをテストした

### CORS と設定

- [x] バックエンドの `.env.example` を作成した
- [x] Vue の開発オリジンを許可した
- [x] ブラウザからバックエンドへリクエストできることを確認した

### フロントエンド接続

- [ ] 型付きの frontend API サービスを作る
- [ ] `GET /tasks` の内容を画面に表示する
- [ ] `POST /tasks` で task を作成する
- [ ] `PATCH /tasks/{task_id}` で task を更新する
- [ ] `DELETE /tasks/{task_id}` で task を削除する
- [ ] ローディング表示を追加する
- [ ] エラー表示を追加する

## 作業セッション記録のテンプレート

各学習セッションのあとに、このセクションをコピーして使う。

```markdown
## Session: YYYY-MM-DD — Stage Name

### Goal

- 何を学ぶ、または実装する予定だったか？

### Changes Made

- 変更したファイル:
- 追加したエンドポイントや機能:
- 変更した設定:

### Concepts Learned

- Concept 1:
- Concept 2:

### Tests Performed

- [ ] 正常系を確認した
- [ ] 不正入力を確認した
- [ ] 対象なしのケースを確認した
- [ ] 必要なら再起動後の挙動も確認した

### Problems and Debugging

- 起きたエラーや想定外の挙動:
- 原因:
- 修正内容:

### Result

- [ ] Completed
- [ ] Partially completed
- [ ] Needs review

### Next Action

- 次にやる最小の作業は:
```

## Session: 2026-08-07 — Documentation Sync for Supervisor Review

### Goal

- Human-facing documentation を、現在の「バックエンド完了・フロントエンドひな形のみ」の状態に合わせる。

### Changes Made

- File changed: `README.md`
- File changed: `LEARNING_PLAN.md`
- File changed: `PROGRESS.md`
- File changed: `frontend/README.md`
- FastAPI, SQLAlchemy, PostgreSQL, Docker Compose, Vue ひな形の状態が、実装どおりに読めるようにした。

### Concepts Learned

- README は、完了したバックエンド作業と未完了のフロントエンド接続を分けて書くと分かりやすい。
- 進捗ログは、理想ではなく実際の実装状態を追うほうが役に立つ。

### Tests Performed

- [x] `backend/main.py`、`backend/app/routers/tasks.py`、`backend/app/schemas.py`、`compose.yaml`、frontend の package scripts と照合した
- [x] 参照している VS Code task 名が `.vscode/tasks.json` と一致するか確認した

### Problems and Debugging

- エラーや想定外の挙動: ドキュメント上では frontend がすでに backend とつながっているように見えていた。
- 原因: backend 作業完了後に文書が追従していなかった。
- 修正: すでに実装済みの backend と、これからやる frontend 接続をはっきり分けて書き直した。

### Result

- [x] Completed

### Next Action

- 次にやる最小の作業は: typed frontend API service と task UI を実装すること。

---

## Session: 2026-07-30 — Documentation Sync for Persistence Layer

### Goal

- 学習ドキュメントを、現在の backend アーキテクチャと完了済みの進捗に合わせる。

### Changes Made

- File changed: `README.md`
- File changed: `LEARNING_PLAN.md`
- File changed: `PROGRESS.md`
- 追加した内容: ドキュメントが SQLAlchemy + PostgreSQL の永続化と `/health/database` を反映するようになった。
- 変更した設定: progress と学習フェーズの状態を、実際の backend に合わせた。

### Concepts Learned

- PostgreSQL ベースの永続化が、いまの実データの保存先になっている。
- FastAPI の route handler は SQLAlchemy session に依存している。
- Alembic は route コードではなく ORM の metadata を追跡する。

### Tests Performed

- [x] 現在の backend ファイルを見てアーキテクチャを確認した
- [x] Compose ベースの PostgreSQL 構成とドキュメントを照合した
- [ ] 正常系を確認した
- [ ] 不正入力を確認した
- [ ] 対象なしのケースを確認した
- [ ] 必要なら再起動後の挙動も確認した

### Problems and Debugging

- エラーや想定外の挙動: 学習ドキュメントがまだ SQLite とメモリ上の保存を説明していた。
- 原因: 実装は PostgreSQL 永続化に進んでいたが、文書が更新されていなかった。
- 修正: 現在の backend 実装と進捗状態に合わせて、ドキュメントを同期した。

### Result

- [x] Completed

### Next Action

- 次にやる最小の作業は: PostgreSQL ベースの CRUD API に対する自動 backend テストを追加すること。

## 更新ルール

各ステージごとに次を行う。

1. **最終更新** 日付を変更する。
2. **現在のフェーズ** を更新する。
3. 完了したチェック項目には `[x]` を付ける。
4. 新しく学んだ概念を追加する。
5. 重要なエラーや修正内容をセッション記録に残す。
6. 未完了の項目はチェックしない。
7. ドキュメントは、関連するコード変更と一緒にコミットする。

コミット例:

```bash
git add README.md LEARNING_PLAN.md PROGRESS.md backend
git commit -m "Document backend progress and database learning plan"
```
