# -*- coding: utf-8 -*-
"""
TACTIC API 클라이언트
dxManager에서 TACTIC 서버와의 API 통신 관련 기능을 분리한 모듈
"""

import requests
import json
import dxConfig
import config


class TacticAPIClient:
    def __init__(self):
        """TACTIC API 클라이언트 초기화"""
        self.api_key = config.TACTIC_API_KEY
        self.tactic_ip = dxConfig.getConf('TACTIC_IP')
        
    def get_task_info(self, name):
        """
        사용자별 태스크 정보 조회
        
        Args:
            name (str): 사용자 이름
            
        Returns:
            dict: 태스크 정보
        """
        request_param = {
            'api_key': self.api_key,
            'login': name
        }
        
        try:
            response = requests.get(
                f"http://{self.tactic_ip}/dexter/search/task.php",
                params=request_param
            )
            return response.json()
        except Exception as e:
            print(f"태스크 정보 조회 오류: {e}")
            return {}
    
    def get_project_list(self):
        """
        활성 프로젝트 목록 조회
        
        Returns:
            dict: 프로젝트 목록 {프로젝트명: [코드, 타이틀]}
        """
        request_param = {
            'api_key': self.api_key,
            'category': 'Active'
        }
        
        try:
            response = requests.get(
                f"http://{self.tactic_ip}/dexter/search/project.php",
                params=request_param
            )
            response_data = response.json()
            
            project_list = {}
            for project in response_data:
                proj_name = project["name"]
                proj_code = project["code"]
                proj_title = project["title"]
                project_list[proj_name] = [proj_code, proj_title]
                
            return project_list
        except Exception as e:
            print(f"프로젝트 목록 조회 오류: {e}")
            return {}
    
    def get_user_info(self, user_code):
        """
        사용자 정보 조회
        
        Args:
            user_code (str): 사용자 코드
            
        Returns:
            tuple: (한글이름, 역할, 팀, 직책, 부서약어)
        """
        request_param = {
            'api_key': self.api_key,
            'code': user_code
        }
        
        try:
            response = requests.get(
                f"http://{self.tactic_ip}/dexter/search/user.php",
                params=request_param
            )
            user_info = response.json()
            
            unicode_name = user_info["name_kr"]
            role = user_info["role"]
            team = user_info["department"]
            job = user_info["job_title"]
            department = user_info["department_short"]
            
            return unicode_name, role, team, job, department
        except Exception as e:
            print(f"사용자 정보 조회 오류: {e}")
            return "", "", "", "", ""