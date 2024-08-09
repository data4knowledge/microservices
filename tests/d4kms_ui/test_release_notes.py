from d4kms_ui.release_notes import ReleaseNotes

def test_create_no_dir(mocker):
  mock_read = mocker.patch('d4kms_ui.release_notes.ReleaseNotes._read')
  rn = ReleaseNotes()
  assert rn is not None
  assert rn._dir == ReleaseNotes.DIR
  assert rn._text == ''
  assert mock_read.call_count == 1
  mock_read.assert_has_calls([mocker.call()])

def test_create_dir(mocker):
  mock_read = mocker.patch('d4kms_ui.release_notes.ReleaseNotes._read')
  rn = ReleaseNotes('some/path')
  assert rn is not None
  assert rn._dir == 'some/path'
  assert rn._text == ''
  assert mock_read.call_count == 1
  mock_read.assert_has_calls([mocker.call()])

def test_notes(mocker):
  mocker.patch('builtins.open', mocker.mock_open(read_data='test'))  
  rn = ReleaseNotes('some/path')
  assert rn.notes() == '<p>test</p>'

def test__read(mocker):
  mocker.patch('builtins.open', mocker.mock_open(read_data='test'))  
  rn = ReleaseNotes('some/path')
  assert rn._text == 'test'
