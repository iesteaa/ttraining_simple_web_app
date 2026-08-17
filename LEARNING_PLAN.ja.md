# エンドツーエンド Web 開発の学習計画

このドキュメントは、プロジェクトの学習順序を追うためのものです。個人学習にも監督者のレビューにも使いやすいよう、できるだけ簡潔にまとめています。

## 学習の進め方

各ステージでは、次の順番で進めます。

```text
概念を学ぶ
   ↓
小さな実装を行う
   ↓
手動で確認する
   ↓
失敗ケースを確認する
   ↓
自分の言葉で説明する
   ↓
進捗を更新する
   ↓
Git commit を作成する
```

コードが動いたという理由だけで次に進まないでください。何をしていて、なぜ必要なのかを説明できるようになってから次のステージに進みます。

---

## Phase 0 — 開発環境

**状態:** 完了

### 概念

- プロジェクトルートとフォルダの分離
- Python の仮想環境
- Node.js の依存関係
- Git リポジトリ
- `.gitignore`
- 開発サーバー

### 実装

- `backend/` と `frontend/` を作成する
- Python の `.venv` を作成する
- FastAPI の依存関係をインストールする
- Vue 3 の TypeScript プロジェクトを作成する
- 両方の開発サーバーを起動する

### チェックポイント

- [x] バックエンド環境が動く
- [x] フロントエンド環境が動く
- [x] Git リポジトリが初期化されている
- [x] ローカル依存関係が Git に含まれない

---

## Phase 1 — FastAPI と HTTP の基礎

**状態:** 完了

### 概念

- FastAPI のアプリケーションオブジェクト
- サーバー、リクエスト、レスポンス
- ルートとエンドポイント
- HTTP メソッドと URL パス
- JSON レスポンス
- Swagger UI と OpenAPI

### 実装

```text
GET /
GET /health
```

### チェックポイント

- [x] FastAPI アプリケーションを起動できる
- [x] `/docs` で API を表示できる
- [x] ルートエンドポイントが応答する
- [x] ヘルスチェックエンドポイントが応答する
- [x] method + path = endpoint を説明できる

---

## Phase 2 — リクエスト検証と作成・取得

**状態:** 完了

### 概念

- リクエストボディ
- Pydantic モデル
- 入力スキーマとレスポンススキーマ
- 自動バリデーション
- `201 Created`
- `422 Unprocessable Entity`
- メモリ上の保存

### 実装

```text
POST /tasks
GET  /tasks
GET  /tasks/{task_id}
```

### チェックポイント

- [x] `TaskCreate` スキーマがある
- [x] `Task` レスポンススキーマがある
- [x] 正しい task 作成で `201` が返る
- [x] 不正な入力で `422` が返る
- [x] 全 task を取得できる
- [x] 1件の task を ID で取得できる
- [x] 存在しない task で `404` が返る

---

## Phase 3 — 更新と削除

**状態:** 完了

### 概念

- 部分更新
- `PATCH` と全体置換の違い
- Optional フィールド
- `model_dump(exclude_unset=True)`
- `model_copy(update=...)`
- list index と resource ID の違い
- `204 No Content`

### 実装

```text
PATCH  /tasks/{task_id}
DELETE /tasks/{task_id}
```

### チェックポイント

- [x] `TaskUpdate` スキーマがある
- [x] title を単独で更新できる
- [x] completed を単独で更新できる
- [x] 送っていないフィールドが保持される
- [x] 空の更新は拒否される
- [x] task を ID で削除できる
- [x] 成功時に `204` が返る
- [x] 削除した task は再取得できない

---

## Phase 4 — バックエンドのルーティング整理

**状態:** 完了

### 概念

- 責務の分離
- Python パッケージと `__init__.py`
- FastAPI の `APIRouter`
- router prefix と tags
- `app.include_router(...)`
- 動作を変えずに整理するリファクタリング

### 実装

```text
main.py
app/schemas.py
app/routers/tasks.py
```

### チェックポイント

- [x] スキーマがルートから分離されている
- [x] task エンドポイントが `APIRouter` を使っている
- [x] router が main application に組み込まれている
- [x] CRUD の動作が変わっていない
- [x] エンドポイントのパスが `/tasks` に統一されている

---

## Phase 5 — SQLAlchemy と PostgreSQL による永続化

**状態:** 完了

### 概念

- データベース、テーブル、行、列
- 主キー
- PostgreSQL
- SQLAlchemy ORM
- database engine
- セッションとトランザクション
- `commit`、`refresh`、query
- ORM モデルと Pydantic スキーマの違い
- FastAPI の `Depends` による依存性注入
- 環境変数ベースの設定
- Alembic の metadata 接続

### 予定していた構成

```text
backend/app/
├── database.py
├── models.py
├── schemas.py
└── routers/
    └── tasks.py
```

### 実装目標

- SQLAlchemy を導入する
- PostgreSQL 接続を settings 経由で設定する
- `Task` ORM モデルを作成する
- task テーブルを作成する
- database session の依存関係を作成する
- メモリ上の list を database query に置き換える
- 既存の API 契約を維持する
- live database health check を追加する

### チェックポイント

- [x] SQLAlchemy が入っている
- [x] PostgreSQL の設定が環境変数から読み込まれている
- [x] `database.py` が engine と session factory を作っている
- [x] `models.py` が Task テーブルを定義している
- [x] `POST /tasks` が database row を作成する
- [x] `GET /tasks` が database を検索する
- [x] `GET /tasks/{task_id}` が主キーで検索する
- [x] `PATCH /tasks/{task_id}` が database row を更新する
- [x] `DELETE /tasks/{task_id}` が database row を削除する
- [x] `GET /health/database` が接続確認を行う
- [x] 再起動後もデータが残る
- [x] スキーマと ORM モデルの違いを説明できる

---

## Phase 6 — バックエンドの自動テスト

**状態:** 完了

### 概念

- 自動テスト
- テストの分離
- Arrange, Act, Assert
- FastAPI の `TestClient`
- Pytest fixture
- 一時的なテスト用データベース
- 回帰テスト

### 実装目標

- `compose.yaml` にすでにある Compose のテスト用 DB サービスを使って分離する

少なくとも次をテストする:

```text
POST の成功とバリデーション失敗
GET 一覧
GET 1件
GET 存在しない task
PATCH の成功と不正入力
DELETE の成功と存在しない task
```

### チェックポイント

- [x] Pytest が入っている
- [x] TestClient で FastAPI application を呼び出せる
- [x] テストが分離された database data を使っている
- [x] 正常系をテストしている
- [x] エラー系をテストしている
- [x] 1つのコマンドで全テストが通る

---

## Phase 7 — 設定と CORS

**状態:** 完了

### 概念

- 環境変数
- application settings
- `.env` と `.env.example`
- ブラウザの origin
- CORS policy
- 許可する frontend origin

### 実装目標

- backend settings を作成する
- `.env.example` を追加する
- Vue の開発オリジンを許可する
- ブラウザから FastAPI にアクセスできることを確認する

### チェックポイント

- [x] backend の設定が必要以上にハードコードされていない
- [x] `.env` が Git に含まれない
- [x] `.env.example` が必要な変数を説明している
- [x] Vue の origin が CORS で許可されている
- [x] ブラウザのリクエストが CORS エラーなしで成功する

---

## Phase 8 — Dev Container ワークスペース

**状態:** 検証中

このプロジェクトはアプリケーション本体を Docker Compose で動かし、エディタのワークスペースは dev container で開いています。このフェーズでは、ワークスペース・ツール・実行環境の境界が正しく機能しているかを検証します。

### 概念

- VS Code dev container
- コンテナ内のワークスペースフォルダ
- コンテナ化されたエディタ用ツール
- 再現性の高い開発環境
- エディタと実行環境でコマンドを共有する考え方

### 実装目標

- このリポジトリ用の dev container 設定を作成する
- プロジェクトを VS Code の dev container ワークスペースとして開けるようにする
- backend と frontend のコマンドがコンテナ化されたワークスペース内でも使えるようにする
- アプリケーションサービス用の既存 Docker Compose 実行環境は維持する

### チェックポイント

- [ ] dev container の設定がある
- [ ] プロジェクトをコンテナワークスペースとして開ける
- [ ] ワークスペースタスクがコンテナ化後も動く
- [ ] backend と frontend の開発コマンドが期待通りの環境で動く

---

## Phase 9 — フロントエンドとバックエンドの最初の接続

**状態:** 保留

Vue のフロントエンドひな形はすでにあります。このフェーズでは、その starter app を backend と会話できる task UI に育てます。

### 概念

- `fetch` または API クライアント関数
- 非同期リクエスト
- loading, success, error の状態管理
- Vue の reactive state
- TypeScript による API response の型付け

### 実装目標

```text
Vue → GET /tasks
Vue → POST /tasks
Vue → PATCH /tasks/{task_id}
Vue → DELETE /tasks/{task_id}
```

### チェックポイント

- [ ] Vue が backend の task を表示する
- [ ] 作成フォームが POST を送る
- [ ] task 完了の切り替えが PATCH を送る
- [ ] 削除ボタンが DELETE を送る
- [ ] 成功後に UI が更新される
- [ ] loading 状態が表示される
- [ ] error フィードバックが表示される

---

## Phase 10 — バックエンド構造の改善

**状態:** 保留

このフェーズは、最初のフロントエンド・バックエンド連携が一通り完成してから始めます。

### 概念

- Router layer
- Service layer
- Repository layer
- 依存性注入
- ビジネスロジックの分離
- 再利用可能な database 操作
- Logging

### チェックポイント

- [ ] route 関数がすべてを直接担当していない
- [ ] ビジネスルールを個別にテストできる
- [ ] database 操作を再利用できる
- [ ] エラー処理が一貫している

---

## Phase 11 — データベース移行と本番向け機能

**状態:** 保留

### 概念

- Alembic migration
- データベース制約
- ページネーションとフィルタリング
- 認証と認可
- パスワードハッシュ
- セキュリティの基礎
- Docker
- デプロイ設定
- 統合テスト

これらのトピックは、基本的な end-to-end アプリの理解が固まってから扱うようにしています。

---

## 完了ステージの定義

あるステージが完了したといえるのは、次を満たしたときです。

- [ ] 機能が動く
- [ ] 正常系をテストした
- [ ] 失敗系をテストした
- [ ] リクエストの流れを説明できる
- [ ] progress ファイルを更新した
- [ ] Git commit を作成した
