

import os
from typing import Hashable
import json
import sys
import datetime





class FilePathHander:
    def __init__(self) -> None:
        self.path_remoeve_keywords = None
        self.replace_remove = None
        self.replace_add = None
        self.path_keep_keywords = None
        self.path_replace = None
        self.input_folder_path = None
        self.search_level = None
        self.initial_slash_number = 0
        self.direct_list = None
        self.file_name_list = []
        self.file_path_list = []
        self.export_folder_path = ""
        self.export_file_path = None

    def change_dir(self,path):
        os.chdir(path)

    def pwd(self):
        return os.getcwd()

    def get_file_create_date(self,file_path):
        stat = os.stat(file_path)
        c_timestamp = stat.st_birthtime
        c_time = datetime.datetime.fromtimestamp(c_timestamp)
        mm=""
        if c_time.month<10:
            mm="0"+str(c_time.month)
        else:
            mm=str(c_time.month)
        dd=""
        if c_time.day<10:
            dd="0"+str(c_time.day)
        else:
            dd=str(c_time.day)

        return str(c_time.year)+mm+dd

    def get_file_tail(self,file_path):
        s=file_path.split(".")
        return s[-1]

    def rename_file(self,origin,new):
        os.rename(origin, new)
    
    def check_slash_numbers(self, path):
        numbers = 0
        for i in path:
            if i == "/" or i == "\ ":
                numbers += 1
        return numbers

    def run_single_search(self, folder_path):
        try:
            for file_name in os.listdir(folder_path):
                if os.path.isdir(folder_path+'/'+file_name):
                    self.direct_list.append(folder_path+'/'+file_name)
                else:
                    self.file_name_list.append(file_name)
                    self.file_path_list.append(folder_path+'/'+file_name)
        except:
            return "There is no file " + folder_path

    def run_single_path_search(self, folder_path):

        try:
            os.listdir(folder_path)
        except:
            print("There is no file " + folder_path)
            return None, None, None

        direct_list = []
        file_name_list = []
        file_path_list = []

        for file_name in os.listdir(folder_path):
            if os.path.isdir(folder_path+'/'+file_name):
                direct_list.append(folder_path+'/'+file_name)
            else:
                file_path_list.append(folder_path+'/'+file_name)

        return direct_list, file_path_list

    def get_file_names_and_paths(self, direct_path, level_limitation=1):
        if not os.path.isdir(direct_path):
            sys.exit("{} is not a exist direct".format(direct_path))

        direct_list = [direct_path]
        file_paths = []
        counter = 0
        while True:
            # print(direct_list[counter])
            directs, paths = self.run_single_path_search(
                direct_list[counter])
            if directs:
                direct_list = direct_list+directs
            if paths:
                file_paths = file_paths+paths
            counter += 1
            if counter == len(direct_list):
                break

        return file_paths, direct_list

    def run_path_algorithm(self, folder_path_list, level_limitation=5):
        direct_counter = 0
        level = 0
        while True:
            level = self.check_slash_numbers(
                self.direct_list[direct_counter])-self.initial_slash_number
            if level > level_limitation:
                break
            # print(level, direct_counter)
            self.run_single_search(self.direct_list[direct_counter])
            if direct_counter >= len(self.direct_list)-1:
                break
            direct_counter += 1

    def keep_pathlist_keyword(self, path_list, keyword):
        result = []
        for i in path_list:
            if keyword in i:
                result.append(i)
        return result

    def remove_pathlist_keyword(self, path_list, keyword):
        result = []
        for i in path_list:
            if keyword in i:
                pass
            else:
                result.append(i)
        return result

    def get_file_name_list(self):
        return self.file_name_list

    def show_file_name_list(self):
        for i in self.file_name_list:
            print(i)

    def get_file_path_list(self):
        return self.file_path_list

    def show_file_path_list(self):
        for i in self.file_path_list:
            print(i)
        print("Total: "+str(len(self.file_path_list)))

    def keep_tail_keyword_file_path(self, keep_tail_name=None):
        if not keep_tail_name:
            keep_tail_name = self.keep_tail_keyword
        if not keep_tail_name:
            return self.file_path_list
        length = len(keep_tail_name)
        result = []
        for file_path in self.file_path_list:
            if file_path[-length:] == keep_tail_name:
                result.append(file_path)
        return result

    def save_as_log(self, export_file_name, export_data):
        with open(export_file_name, mode='w') as export_file:
            for data in export_data:
                export_file.write(data+"\n")

    def export_json(self, export_file_name, data):
        with open(export_file_name, 'w') as file:
            json.dump(data, file)

    def import_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def read_ROI_file(self, file_path):
        # print(file_path)
        try:
            with open(file_path, mode='r') as file:
                data = file.read()
                data = data.split()
                # for i in data:
                #     print(float(i))
                return data
        except:
            return " There is no file: " + file_path

    def get_ROI_data(self, image_path, center_x, center_y, dx, dy):
        # img = cv2.imread(image_path)
        # height, width, channel = img.shape
        # center_x = float(center_x)
        # center_y = float(center_y)
        # dx = float(dx)
        # dy = float(dy)
        # left_x = center_x-(dx/2)
        # left_y = center_y-(dy/2)
        # right_x = left_x+dx
        # right_y = left_y+dy
        # left_x *= width
        # left_y *= height
        # right_x *= width
        # right_y *= height
        # return (int(left_x), int(left_y), int(right_x), int(right_y))
        pass

    def replace_path_list_keyword(self, path_list, replaced_data, keyword):
        result = []
        for i in path_list:
            buffer = i.split(replaced_data)[-1]
            result.append(keyword+buffer)
            # print(result[-1])
        return result

    def create_file_dictionary(self, path, prefix):
        result = {}
        for i in path:
            buffer_1 = i.split("jpg")[0]+"txt"
            buffer_2 = prefix[1]+i.split(prefix[0])[-1]
            # print(i.split(prefix[0])[-1])
            # print(buffer_1)
            # print(buffer_2)
            result.update({i.split(prefix[0])[-1]: [buffer_1, buffer_2, i]})
        return result

    def show_image_dictionary(self, image_dict):
        for i in image_dict.keys():
            print(i)
            for j in image_dict[i]:
                print(j)
        print("Total: ", len(image_dict.keys()))

    def get_image_url_and_ROI_points(self, image_dict):
        result = {}
        ROI_points = []
        for file in image_dict.keys():
            data = self.read_ROI_file(image_dict[file][0])
            for j in range(len(data)):
                i = j*5
                try:
                    ROI_points.append(self.get_ROI_data(
                        image_dict[file][2], (data[i+1]), (data[i+2]), (data[i+3]), (data[i+4])))
                except:
                    ROI_points = []
                if i+5 >= len(data):
                    break
            result.update({image_dict[file][1]: ROI_points})
            ROI_points = []
            # break
        return result

    def check_folder_exist(self, folder_path):
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)

    def export_txt_file(self, txt_path, data):
        with open(txt_path, mode='w') as file:
            for i in data:
                file.write(i + '\n')



class FilePathStructure:
    def __init__(self) -> None:
        pass

    def run_file_path_collection(self, handler):
        counter = 0
        while(counter < len(handler.direct_list)):
            if handler.check_slash_numbers(handler.direct_list[counter]) > handler.serach_level:
                break
            # print("path:{}, level:{}".format(handler.direct_list[counter],
            #     handler.check_slash_numbers(handler.direct_list[counter])))
            handler.get_file_path(handler.direct_list[counter])
            counter += 1

    # keep tail_name and keep keyword file path
    def run_script_3(self, handler):
        self.run_file_path_collection(handler)
        handler.file_path_list = handler.filter_tail_name_file_path()
        handler.file_path_list = handler.filter_specific_keyword_path_list()
        return None

    def run_script_old(self, handler, keep_tail=None, keep_key_word=None, remove_key_word=None):
        self.run_file_path_collection(handler)
        handler.file_path_list = handler.keep_tail_keyword_file_path(keep_tail)
        handler.file_path_list = handler.keep_keyword_path_list(keep_key_word)
        handler.file_path_list = handler.remove_keyword_path_list(
            remove_key_word)

    def run_accuracy_ROI_test(self, handler):
        data = handler.import_json(self.url_ROI_json_path)
        buffer = []
        test_counter = 0
        for i in data.keys():
            buffer = []
            for j in data[i]:
                buffer.append(tuple(j))
                if len(buffer) > 3:  # max is 4
                    break
            handler.send_ROI_accurace_request_post(
                handler.ai_id,
                None,
                i,
                handler.project_name,
                buffer
            )

            # break
            test_counter += 1
            if test_counter > 20:
                break

    def export_image_url_and_ROI_points_tuple(self, handler):
        # get file path list of self.input_folder_path
        handler.run_path_algorithm(handler.search_level)

        # path remove keyword
        for i in handler.path_remoeve_keywords:
            handler.file_path_list = handler.remove_pathlist_keyword(
                path_list=handler.file_path_list,
                keyword=i)

        # path keep keyword
        for i in handler.path_keep_keyword:
            handler.file_path_list = handler.keep_pathlist_keyword(
                path_list=handler.file_path_list,
                keyword=i)

        # get dictionary
        image_path_dict = handler.create_file_dictionary(
            handler.file_path_list, handler.path_replace)
        # handler.show_file_path_list()

        url_data = handler.get_image_url_and_ROI_points(
            image_path_dict)
        handler.show_image_dictionary(url_data)

        handler.check_folder_exist(handler.export_folder_path)
        handler.export_json(handler.export_folder_path +
                            handler.export_file_name, url_data)

    def export_image_url(self, handler):

        # get file name and path
        files_path, directs_path = handler.get_file_names_and_paths(
            direct_path=handler.input_folder_path,
            level_limitation=10)

        # remove keywords
        for keyword in handler.path_remoeve_keywords:
            files_path = handler.remove_pathlist_keyword(files_path, keyword)

        # keep keywords
        if handler.path_keep_keywords:
            for keyword in handler.path_keep_keywords:
                files_path = handler.keep_pathlist_keyword(files_path, keyword)

        # replace keywords
        if handler.replace_remove and handler.replace_add:
            files_path = handler.replace_path_list_keyword(
                files_path,
                handler.replace_remove,
                handler.replace_add)

        # export image url file
        handler.export_txt_file(
            txt_path=handler.export_file_path,
            data=files_path)

    def rename_by_create_date(self, handler, folder_path):
        file_name,direct_list=handler.get_file_names_and_paths(folder_path)
        handler.change_dir(folder_path)
        repeat=0
        new_name=""
        for i in file_name:
            print(repeat,i)
            t=handler.get_file_tail(i)
            d=handler.get_file_create_date(i)
            i=s=i.split("/")[-1]
            repeat=0
            while True:
                new_name=d+" "+str(repeat)+"."+t
                if os.path.exists(new_name):
                    repeat+=1
                else:
                    handler.rename_file(i,new_name)
                    break
