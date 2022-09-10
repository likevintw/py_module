
import file_handler
import cv2


def create_image_file_handler(
        input_folder_path,
        search_level,
        path_keep_keyword,
        path_remove_keyword,
        path_replace,
        ROI_file_name,
        export_folder_path,
        export_file_name,
        replace_path):

    handler = ImageFileHandler(input_folder_path)
    handler.search_level = search_level
    handler.path_keep_keyword = path_keep_keyword
    handler.path_remove_keyword = path_remove_keyword
    handler.path_replace = path_replace
    handler.initial_slash_number = handler.check_slash_numbers(
        input_folder_path)
    handler.ROI_file_name = ROI_file_name
    handler.export_folder_path = export_folder_path
    handler.export_file_name = export_file_name
    handler.replace_path = replace_path
    return handler


class ImageFileHandler(file_handler.FilePathHander):
    def __init__(self, input_folder_path) -> None:
        super().__init__(input_folder_path)
        self.ROI_file_name = ""
        self.replace_path = None


class ImageFileStructure():
    def draw_object_area_on_image(self, handler):

        # get ROI data
        ROI_data = handler.import_json(handler.ROI_file_name)
        result = {}
        for i in ROI_data.keys():
            buffer = i.split(handler.replace_path[0])[-1]
            buffer = handler.replace_path[1]+buffer
            result.update({buffer: ROI_data[i]})
        # print(result)

        buffer = ""
        for file_path in result.keys():
            print(file_path)
            img = cv2.imread(file_path)
            for i in result[file_path]:
                cv2.rectangle(img, (i[0], i[1]), (i[2], i[3]), (0, 0, 255), 3)
            buffer = handler.export_folder_path + "/" + file_path.split("/")[-1]
            print(buffer)
            # cv2.imshow('show_image', img)
            # cv2.waitKey(0)
            # cv2.destroyWindow('show_image')
            cv2.imwrite(buffer, img)
            # break
