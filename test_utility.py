import unittest
import utility


'''
python3 -m unittest -v <.py>

don't show docstring
unittest.TestCase.shortDescription = lambda x: None 
'''
unittest.TestCase.shortDescription = lambda x: None


class TestProcess(unittest.TestCase):
    def test_check_sum(self):
        class TestFormat:
            def __init__(self,
                         filename,
                         want) -> None:
                self.filename = filename
                self.want = want

        cases = []
        cases.append(TestFormat(
            filename="export_json_copy.txt",
            want="d2c92ed6f18b45d18ed829dc4b890b5f"
        ))

        for case in cases:
            result = utility.check_sum(case.filename)
            try:
                self.assertEqual(result, case.want)
            except:
                print("\nthe result of {} is {}, want {}".format(
                    case.filename, result, case.want))

    def test_string_to_json(self):  # unfinished
        pass

    def test_json_to_string(self):  # unfinished
        pass

    def test_replace_string_in_list(self):
        class TestFormat:
            def __init__(self,
                         data_list,
                         target,
                         replace,
                         wants) -> None:
                self.data_list = data_list
                self.target = target
                self.replace = replace
                self.wants = wants

        cases = []
        cases.append(TestFormat(
            data_list=["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"],
            target="txt",
            replace="jpg",
            wants=["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
        ))
        cases.append(TestFormat(
            data_list=["Hello World"],
            target="World",
            replace="Good Morning",
            wants=["Hello Good Morning"]
        ))

        for case in cases:
            result = utility.replace_string_in_list(
                case.data_list, case.target, case.replace)
            self.assertEqual(result, case.wants)

    def test_remove_string_in_list(self):
        class TestFormat:
            def __init__(self,
                         data_list,
                         target,
                         wants) -> None:
                self.data_list = data_list
                self.target = target
                self.wants = wants

        cases = []
        cases.append(TestFormat(
            data_list=["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"],
            target="txt",
            wants=[]
        ))

        cases.append(TestFormat(
            data_list=["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"],
            target="2",
            wants=["1.txt", "3.txt", "4.txt", "5.txt"]
        ))

        for case in cases:
            result = utility.remove_string_in_list(
                case.data_list, case.target)
            self.assertEqual(result, case.wants)

    def test_keep_string_in_list(self):
        class TestFormat:
            def __init__(self,
                         data_list,
                         target,
                         wants) -> None:
                self.data_list = data_list
                self.target = target
                self.wants = wants

        cases = []
        cases.append(TestFormat(
            data_list=["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"],
            target="txt",
            wants=["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"]
        ))
        cases.append(TestFormat(
            data_list=["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"],
            target="2",
            wants=["2.txt"]
        ))

        for case in cases:
            result = utility.keep_string_in_list(
                case.data_list, case.target)
            self.assertEqual(result, case.wants)

    def test_import_json_file(self):
        file_path = []
        want = []

        # 1.
        file_path.append("json.txt")
        want.append({'name': 'john', 'age': '50'})

        for i in range(len(file_path)):
            result = utility.import_json_file(file_path[i])
            self.assertEqual(want[i], result)

    def test_export_json_file(self):
        export_file_name = []
        data = []
        want = []

        # 1.
        export_file_name.append("export_json.txt")
        data.append({'name': 'Young', 'age': '44'})
        want.append({'name': 'Young', 'age': '44'})

        for i in range(len(export_file_name)):
            utility.export_json_file(export_file_name[i], data[i])
            result = utility.import_json_file(export_file_name[i])
            self.assertEqual(want[i], result)

    def test_import_file(self):
        file_path = "file.txt"
        want = ['Hello, World', 'Hello,World']

        result = utility.import_file(file_path)

        for i in range(len(result)):
            self.assertEqual(want[i], result[i])

    def test_export_file(self):
        pass

    def test_get_symbol_number_in_string(self):  # update test format
        string = []
        symbol = []
        want = []

        # 1.
        string.append("123/234/134/134/2134")
        symbol.append("/")
        want.append(4)
        # 2.
        string.append("123/234/134/134/2134")
        symbol.append("1")
        want.append(4)
        # 3.
        string.append(
            r"/mnt/c/Users/LDS/Google 雲端硬碟/code_pool/python/module/utility")
        symbol.append("/")
        want.append(9)

        for i in range(len(string)):
            result = utility.get_symbol_number_in_string(string[i], symbol[i])
            self.assertEqual(want[i], result)

    def test_remove_last_slash(self):  # update test format
        string = []
        want = []

        # 1.
        string.append("1/2/3/")
        want.append("1/2/3")
        # 2.
        string.append("1/2/3")
        want.append("1/2/3")
        # 3.
        string.append("1/2/3////////////")
        want.append("1/2/3")
        # 3.
        string.append("//////////")
        want.append("")
        # 4.
        string.append("/8/8/8/8//5//5///")
        want.append("/8/8/8/8//5//5")

        for i in range(len(string)):
            result = utility.remove_last_slash(string[i])
            self.assertEqual(want[i], result)

    def test_get_file_and_direct_path(self):
        folder_path = []
        want_file = []
        want_direct = []

        # 1.
        folder_path.append("folder_test")
        want_file.append(['folder_test/1/11.txt', 'folder_test/2/22.txt'])
        want_direct.append(['folder_test', 'folder_test/1', 'folder_test/2'])
        # 2.
        folder_path.append("folder_test/")
        want_file.append(['folder_test/1/11.txt', 'folder_test/2/22.txt'])
        want_direct.append(['folder_test', 'folder_test/1', 'folder_test/2'])

        for i in range(len(folder_path)):
            file, direct = utility.get_file_and_direct_path(folder_path[i])
            self.assertEqual(want_file[i], file)
            self.assertEqual(want_direct[i], direct)

    def test_read_write_file(self):
        # unfinished
        '''
        write - non append
        write - append
        '''
        pass


if __name__ == '__main__':
    unittest.main()
