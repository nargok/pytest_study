from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_asdict():
  """_asdict should return a dictionary."""
  t_task = Task('do something', 'okken', True, 21)
  t_dist = t_task._asdict()
  expected = {'summary': 'do something',
              'owner': 'okken',
              'done': True,
              'id': 21 }
  assert t_dist == expected

def test_replace():
  """_replace() should change passed in fields."""
  t_before = Task('finish_book', 'brian', False)
  t_after = t_before._replace(id=10, done=True)
  t_expected = Task('finish_book', 'brian', True, 10)

  assert t_after == t_expected