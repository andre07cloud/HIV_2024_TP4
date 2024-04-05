from poly_llm.to_test.file_name_check import file_name_check

def test_file_name_check():
    assert file_name_check("example.txt") == "Yes", "Should pass basic check"
    assert file_name_check("1example.dll") == "No", "Name shouldn't start with digit"
    assert file_name_check(".exe") == "No", "Empty prefix"
    assert file_name_check("myfile.") == "No", "Missing suffix"
    assert file_name_check("myfile.doc") == "No", "Wrong suffix"
    assert file_name_check("thisisaverylongfilenamewhichistoolongandshouldfail.txt") == "No", "Too long prefix"
    assert file_name_check("hello world!.txt") == "No", "Spaces in filename"
    assert file_name_check("myfile.TXT") == "No", "Suffix must be lowercase"