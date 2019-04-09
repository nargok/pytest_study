# README

## テストを一つだけ実行する
```
# pytest ファイル名::テスト名
pytest tasks/test_four.py::test_asdict
```

## テストの実行情報を取得する
```
pytest --collect-only
```

実行結果
```
platform darwin -- Python 3.7.0, pytest-4.4.0, py-1.8.0, pluggy-0.9.0
rootdir: /Users/xxx/Projects/pytest_study/ch1
collected 6 items                                                                                                                                                        
<Module test_four.py>
  <Function test_asdict>
  <Function test_replace>
<Module test_one.py>
  <Function test_passing>
<Module test_three.py>
  <Function test_defaults>
  <Function test_member_access>
<Module test_two.py>
  <Function test_passing>
```

## テストの検索
```
pytest -k "asdict or defaults" --collect-only
```

実行結果
```
platform darwin -- Python 3.7.0, pytest-4.4.0, py-1.8.0, pluggy-0.9.0
rootdir: /Users/houxianliangyi/PycharmProjects/pytest_study/ch1
collected 6 items / 4 deselected / 2 selected                                                                                                                            
<Module test_four.py>
  <Function test_asdict>
<Module test_three.py>
  <Function test_defaults>
```

## マークをつけたテストを実行する
```python
@pytest.mark.run_three_please
def test_replace():
  pass
```

```
# pytest -m <マーク名称>
pytest -v -m run_three_please
```

## テストが失敗したらそこで終了にする
```
pytest -x
```
