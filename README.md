# kokutwi-backend

kokutwi の API

## poetry

```
$ poetry config --list
```

`virtualenvs.in-project`が true でない場合以下を実行

```
$ poetry config virtualenvs.in-project true
```

インストールする

```
$ poetry install
```

## API を起動する

```
$ poetry run task start
```

## テストを実行する

```
$ poetry run pytest
```
