"""
dxManager 프로젝트용 데이터 검증 유틸리티 함수들.
날짜, 멤버, 아티스트, 값의 존재 여부 확인 함수 포함.
"""


def check_date_exists(json_dicts, task_dict):
    """
    딕셔너리 리스트에서 날짜 존재 여부 확인.
    
    Args:
        json_dicts (list): 날짜 정보 포함된 딕셔너리 리스트
        task_dict (dict): year, month, day 키 포함 딕셔너리
        
    Returns:
        bool: 날짜 존재하면 True, 아니면 False
    """
    for dict_item in json_dicts:
        if (dict_item['year'] == task_dict['year'] and
            dict_item['month'] == task_dict['month'] and
            dict_item['day'] == task_dict['day']):
            return True
    return False


def check_dateMember_exists(json_dicts, task_dict):
    """
    딕셔너리 리스트에서 날짜와 멤버 조합 존재 여부 확인.
    
    Args:
        json_dicts (list): 날짜와 아티스트 정보 포함 딕셔너리 리스트
        task_dict (dict): year, month, day, artist 키 포함 딕셔너리
        
    Returns:
        bool: 날짜와 멤버 존재하면 True, 아니면 False
    """
    for dict_item in json_dicts:
        if (dict_item['year'] == task_dict['year'] and
            dict_item['month'] == task_dict['month'] and
            dict_item['day'] == task_dict['day'] and
            dict_item["artist"] == task_dict["artist"]):
            return True
    return False


def check_artist_exists(json_dicts, task_dict):
    """
    딕셔너리 리스트에서 아티스트 존재 여부 확인.
    
    Args:
        json_dicts (list): 아티스트 정보 포함 딕셔너리 리스트
        task_dict (dict): artist 키 포함 딕셔너리
        
    Returns:
        bool: 아티스트 존재하면 True, 아니면 False
    """
    for dict_item in json_dicts:
        if (dict_item['artist'] == task_dict['artist']):
            return True
    return False


def check_value_in_Dict(dictList, element):
    """
    딕셔너리의 tasks 내 리스트 값들에서 요소 존재 여부 확인.
    
    Args:
        dictList (list): tasks 포함 딕셔너리 리스트
        element: 태스크 리스트에서 찾을 요소
        
    Returns:
        bool: 태스크 리스트에서 요소 발견시 True, 아니면 False
    """
    for dict_item in dictList:
        if dict_item['tasks'] != [{}]:
            for value in dict_item['tasks'][0].values():
                if isinstance(value, list) and element in value:
                    return True
    return False


def check_value_in_lists(dic, value):
    """
    딕셔너리 내 리스트들에서 값 존재 여부 확인.
    
    Args:
        dic (dict): 값으로 리스트 포함 딕셔너리
        value: 리스트에서 찾을 값
        
    Returns:
        tuple: (bool, str) - (True/False, 발견된 키 또는 None)
    """
    for hi in dic:
        if value in dic[hi]:
            return True, hi
    return False, None