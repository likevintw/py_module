from typing import Union
import unittest
from unittest.case import skip
import file_handler

# python3 -m unittest -v


class TestFolderPathHandler(unittest.TestCase):

    def test_get_file_create_date(self):
        handler=file_handler.FilePathHander()
        result=handler.get_file_create_date("file_handler.py")
        self.assertEqual(result,"20220909")

    def test_get_file_tail(self):
        handler=file_handler.FilePathHander()
        result=handler.get_file_tail("file_handler.py")
        self.assertEqual(result,"py")

    # @unittest.skip("finished")
    def test_rename_by_date(self):
        '''
        problem, same date for several files
        '''
        handler=file_handler.FilePathHander()
        structure=file_handler.FilePathStructure()
        structure.rename_by_create_date(handler,"/Users/kevin/Desktop/rename_folder")

    @unittest.skip("")
    def test_replace(self):
        input_folder_path = "/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_human"
        output_image_path = "./image_path/human_positive_path_list.txt"
        keep_keyword = [".jpg", "positive"]

        handler = file_handler.create_file_handler(
            input_folder_path=input_folder_path,
            search_level=5
        )
        handler.run_path_algorithm(handler.search_level)
        handler.file_path_list = handler.remove_pathlist_keyword(
            handler.file_path_list, "aws")
        for i in keep_keyword:
            handler.file_path_list = handler.keep_pathlist_keyword(
                path_list=handler.file_path_list,
                keyword=i)
        handler.show_file_path_list()
        handler.file_path_list=handler.replace_path_list_keyword(
            handler.file_path_list,
            "/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_human",
            "http://192.168.5.130/upload/Human/Human/"
        )
        # handler.show_file_path_list()
        # handler.save_as_log(
        #     export_file_name=output_image_path,
        #     export_data=handler.file_path_list
        # )
        self.assertEqual(len(handler.file_path_list), 188)

    @unittest.skip("")
    def test_ROI_points(self):
        input_folder_path = "/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_human"
        output_image_path = "./image_path/"
        keep_keyword = [".txt", "positive"]
        remove_keyword = ["aws", "class"]

        handler = file_handler.create_file_handler(
            input_folder_path=input_folder_path,
            search_level=5
        )
        handler.run_path_algorithm(handler.search_level)
        for i in keep_keyword:
            handler.file_path_list = handler.keep_pathlist_keyword(
                path_list=handler.file_path_list,
                keyword=i)

        for i in remove_keyword:
            handler.file_path_list = handler.remove_pathlist_keyword(
                path_list=handler.file_path_list,
                keyword=i)
        # handler.show_file _path_list()

        for i in handler.file_path_list:
            data = handler.read_ROI_file(i)
            for j in range(len(data)):
                i = j*5
                ROI_points = handler.get_ROI_data(
                    (data[i+1]), (data[i+2]), (data[i+3]), (data[i+4]))
                print(ROI_points)
                if i+5 >= len(data):
                    break
            break
        # handler.save_as_log(
        #     export_file_name=output_image_path,
        #     export_data=handler.file_path_list
        # )

    @unittest.skip("")
    def test_get_image_path_list(self):
        input_folder_path = "/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_human"
        output_image_path = "./image_path/human_positive_path_list.txt"
        keep_keyword = [".jpg", "positive"]

        handler = file_handler.create_file_handler(
            input_folder_path=input_folder_path,
            search_level=5
        )
        handler.run_path_algorithm(handler.search_level)
        for i in keep_keyword:
            handler.file_path_list = handler.keep_pathlist_keyword(
                path_list=handler.file_path_list,
                keyword=i)
        # handler.show_file_path_list()
        handler.save_as_log(
            export_file_name=output_image_path,
            export_data=handler.file_path_list
        )
        self.assertEqual(len(handler.file_path_list), 483)

    @unittest.skip("")
    def test_remove_tail(self):
        handler = file_handler.create_file_handler(
            input_folder_path="input_folder",
            search_level=2
        )
        handler.run_path_algorithm(handler.search_level)
        handler.file_path_list = handler.remove_pathlist_keyword(
            handler.file_path_list, ".txt")
        # handler.show_file_path_list()
        self.assertEqual(handler.file_path_list, [
                         'input_folder/t3/test.md', 'input_folder/t3/test.py'])

    @unittest.skip("")
    def test_keep_tail(self):
        handler = file_handler.create_file_handler(
            input_folder_path="input_folder",
            search_level=2
        )
        handler.run_path_algorithm(handler.search_level)
        handler.file_path_list = handler.keep_pathlist_keyword(
            handler.file_path_list, ".md")
        # handler.show_file_path_list()
        self.assertEqual(handler.file_path_list, ['input_folder/t3/test.md'])

    @unittest.skip("")
    def test_first_level(self):
        handler = file_handler.create_file_handler(
            input_folder_path="input_folder",
            search_level=5
        )
        handler.run_single_search(handler.input_folder_path)
        # handler.show_file_path_list()
        self.assertEqual(handler.get_file_path_list(), [
                         'input_folder/1.txt', 'input_folder/2.txt'])

    @unittest.skip("")
    def test_not_exist_folder(self):
        handler = file_handler.create_file_handler(
            input_folder_path="not_exist",
            search_level=5
        )

        self.assertEqual(handler.run_single_search(
            handler.input_folder_path), "There is no file not_exist")


if __name__ == '__main__':
    unittest.main()
