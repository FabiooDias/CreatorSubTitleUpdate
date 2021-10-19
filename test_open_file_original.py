from Control.classCreateFile import Create_Open_File

def test_open_file_original():
    test = Create_Open_File()
    test_argument = "Legenda"
    expected = "<_io.TextIOWrapper name='Legenda.srt' mode='rt' encoding='utf8'>"
    actual = str(test.open_file_original(test_argument))
    message = f'open_file_original(Legenda) precisa retornar um Text I/O, mais esta retornando {actual}'
    assert actual == expected, message