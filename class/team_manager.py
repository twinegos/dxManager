"""
TeamManager - 팀 정보 관리 클래스

dxManager에서 팀 관리 관련 기능들을 분리한 클래스입니다.
팀 정보 로드, 팀원 관리, 팀 트리뷰 조작 등의 기능을 담당합니다.
"""

import os
import json
import logging
from utils.validation import check_value_in_lists
from PySide2.QtGui import QStandardItem, QStandardItemModel
from PySide2.QtCore import Qt

class TeamManager:
    def __init__(self, main_window):
        """
        TeamManager 초기화
        
        Args:
            main_window: dxManager 메인 윈도우 인스턴스
        """
        self.main_window = main_window
        self.current_path = os.path.dirname(os.path.abspath(__file__)).replace('/class', '')
        
    def get_team_info(self, member):
        """
        팀 멤버의 정보를 JSON 파일에서 로드합니다.
        
        Args:
            member (str): 팀원의 영문 이름
            
        Returns:
            list: 팀 정보 데이터 리스트 (빈 리스트면 데이터 없음)
        """
        try:
            team_info_path = self.current_path + "/.team_Info"
            team_info_json = os.path.join(team_info_path, f"{member}_teamInfo.json")
            
            team_info_data = []
            
            if os.path.exists(team_info_json):
                with open(team_info_json, 'r', encoding='utf-8') as f:
                    team_info_data = json.load(f)
                    
            return team_info_data
            
        except Exception as e:
            logging.error(f"팀 정보 로드 실패 ({member}): {e}")
            return []
    
    def check_user_info(self, user):
        """
        사용자 정보 파일이 존재하는지 확인하고 없으면 생성합니다.
        
        Args:
            user (str): 사용자 영문 이름
            
        Returns:
            bool: 성공 여부
        """
        try:
            user_info_path = self.current_path + "/.user_Info"
            user_info_json = os.path.join(user_info_path, f"{user}_Info.json")
            
            if not os.path.exists(user_info_json):
                # 사용자 정보 파일이 없으면 기본 구조로 생성
                if not os.path.exists(user_info_path):
                    os.makedirs(user_info_path, exist_ok=True)
                    
                default_user_info = {
                    "nameKr": "",
                    "role": "",
                    "team": "",
                    "job": "",
                    "department": ""
                }
                
                with open(user_info_json, 'w', encoding='utf-8') as f:
                    json.dump(default_user_info, f, ensure_ascii=False, indent=2)
                    
                logging.info(f"사용자 정보 파일 생성: {user_info_json}")
                
            return True
            
        except Exception as e:
            logging.error(f"사용자 정보 확인/생성 실패 ({user}): {e}")
            return False
    
    def get_tree_all_items(self, item, checked_items, unchecked_items, exist_member, hierarchy, hi):
        """
        트리뷰의 모든 아이템을 재귀적으로 순회하며 체크 상태를 수집합니다.
        dxManager의 원본 로직을 그대로 구현합니다.
        """
        try:
            if item is None:
                return hierarchy
                
            hi = hi + 1
            if item.isCheckable() and item.checkState() == Qt.Checked:
                checked_items.append(item.text())
            else:
                unchecked_items.append(item.text())

            if hi not in hierarchy:
                hierarchy[hi] = [item.text()]
            else:
                # 현재 아이템이 전체 멤버하이라키에 존재하는지 확인, 상위 하이라키에 존재하면 하이라키 넘버(dup_hi) 반환
                check_exist, dup_hi = check_value_in_lists(hierarchy, item.text())

                # 상위 하이라키에 존재하는 경우, 가 상위 하이라키에서 멤버 삭제
                if dup_hi is not None: 
                    if hi != dup_hi and dup_hi < hi: 
                        hierarchy[dup_hi].remove(item.text())
                        check_exist = False

                if check_exist == False and (item.text() not in hierarchy[hi]):
                    hierarchy[hi].append(item.text())

            for row in range(item.rowCount()):
                child_item = item.child(row)
                hierarchy = self.get_tree_all_items(child_item, checked_items, unchecked_items, exist_member, hierarchy, hi)    

            return hierarchy
            
        except Exception as e:
            logging.error(f"트리 아이템 순회 실패: {e}")
            return hierarchy
    
    def get_checked_items(self, item, checked_members):
        """
        트리뷰에서 체크된 아이템들을 재귀적으로 수집합니다.
        
        Args:
            item: 현재 순회 중인 트리 아이템
            checked_members (list): 체크된 멤버들을 저장할 리스트
        """
        try:
            if item is None:
                return
                
            # 현재 아이템이 체크되어 있으면 리스트에 추가
            if item.isCheckable() and item.checkState() == Qt.Checked:
                checked_members.append(item.text())
            
            # 하위 아이템들 재귀 처리
            for row in range(item.rowCount()):
                child = item.child(row, 0)
                if child:
                    self.get_checked_items(child, checked_members)
                    
        except Exception as e:
            logging.error(f"체크된 아이템 수집 실패: {e}")
    
    def set_check_items(self, item, checked_list):
        """
        주어진 리스트에 따라 트리뷰 아이템들의 체크 상태를 설정합니다.
        
        Args:
            item: 현재 설정 중인 트리 아이템
            checked_list (list): 체크되어야 할 아이템들의 리스트
        """
        try:
            if item is None:
                return
                
            # 현재 아이템의 체크 상태 설정
            if item.isCheckable():
                item_text = item.text()
                if item_text in checked_list:
                    item.setCheckState(Qt.Checked)
                else:
                    item.setCheckState(Qt.Unchecked)
            
            # 하위 아이템들 재귀 처리
            for row in range(item.rowCount()):
                child = item.child(row, 0)
                if child:
                    self.set_check_items(child, checked_list)
                    
        except Exception as e:
            logging.error(f"아이템 체크 상태 설정 실패: {e}")
    
