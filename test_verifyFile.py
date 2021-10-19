from Control.classFileSrt import File_Srt

def test_File_srt():
    test = File_Srt()
    test_argument = "OutraLegenda"
    expected = True
    actual = test.verifyFile(test_argument)
    message = f'verifyFile(OutraLegenda) precisa retornar True mas retornou {actual}'
    assert actual == expected, message

    