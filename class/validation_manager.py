# encoding:utf-8

class ValidationManager:
    def __init__(self, main_window):
        """
        데이터 검증 및 유효성 검사를 담당하는 클래스
        """
        self.main_window = main_window

    def check_date_exists(self, json_dicts, task_dict):
        """딕셔너리 리스트에서 날짜 존재 여부 확인"""
        for dict_item in json_dicts:
            if (dict_item['year'] == task_dict['year'] and
                dict_item['month'] == task_dict['month'] and
                dict_item['day'] == task_dict['day']):
                return True
        return False

    def check_dateMember_exists(self, json_dicts, task_dict):
        """딕셔너리 리스트에서 날짜와 멤버 조합 존재 여부 확인"""
        for dict_item in json_dicts:
            if (dict_item['year'] == task_dict['year'] and
                dict_item['month'] == task_dict['month'] and
                dict_item['day'] == task_dict['day'] and
                dict_item["artist"] == task_dict["artist"]):
                return True
        return False

    def check_value_in_lists(self, dic, value):
        """딕셔너리 내 리스트들에서 값 존재 여부 확인"""
        for hi in dic:
            if value in dic[hi]:
                return True, hi
        return False, None

    def check__Task_data(self, taskData, filterDate_tasks, jsonData):
        """태스크 데이터 검증"""
        if taskData["tasks"][0]:
            for proj in taskData["tasks"][0]:
                for task in taskData["tasks"][0][proj]:
                    for filterData in filterDate_tasks:
                        for filterProj in filterData["tasks"][0]:
                            if task in filterData["tasks"][0][filterProj]:
                                delAssign = filterData["artist"]
                                newAssign = taskData["artist"]
                                if (delAssign != newAssign) and filterData["department"] == taskData["department"]:
                                    self.main_window.updateAssignment(delAssign, newAssign, taskData)
                                    jsonData.remove(filterData)
                                    return True
        return False