# -*- coding: utf-8 -*-
"""
데이터 매니저 클래스
dxManager에서 JSON 데이터 관리 관련 기능을 분리한 모듈
"""

import os
import json
import pandas as pd
from datetime import datetime
import config


class DataManager:
    def __init__(self, user_id=None):
        """
        데이터 매니저 초기화
        
        Args:
            user_id (str): 사용자 ID (None일 경우 config에서 자동 획득)
        """
        self.user_id = user_id if user_id else config.get_user_id()
        self.json_file_path = config.SCHEDULE_DATA_PATH
        self.json_file = config.get_schedule_data_file(self.user_id)
        self.mirror_file = config.get_schedule_mirror_file(self.user_id)
        
    def load_json_data(self, file_path=None, default_value=None):
        """
        JSON 데이터 파일 로딩 (기존 import_Json 로직과 동일)
        
        Args:
            file_path (str): JSON 파일 경로 (None일 경우 기본 경로 사용)
            default_value: 파일이 없을 경우 반환할 기본값 (None일 경우 빈 리스트)
            
        Returns:
            JSON 데이터 (파일이 없으면 default_value 또는 빈 리스트)
        """
        if file_path is None:
            file_path = self.json_file
            
        if default_value is None:
            default_value = []
            
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return data
            else:
                return default_value
        except Exception as e:
            print(f"JSON 데이터 로딩 오류: {e}")
            return default_value
    
    def save_json_data(self, data, file_path=None, backup=False):
        """
        JSON 데이터 파일 저장 (기존 export_Json 로직과 동일)
        
        Args:
            data: 저장할 JSON 데이터
            file_path (str): 저장할 파일 경로 (None일 경우 기본 경로 사용)
            backup (bool): 백업 생성 여부
            
        Returns:
            bool: 저장 성공 여부
        """
        if file_path is None:
            file_path = self.json_file
            
        try:
            # 백업 생성 (필요시)
            if backup and os.path.exists(file_path):
                self._create_backup(file_path)
            
            # 디렉토리 생성 (존재하지 않는 경우)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            # JSON 데이터 저장 (기존 로직과 동일하게)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())
            
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False
    
    def get_dataframe_schedule(self, file_path=None, search_empty_proj_func=None):
        """
        JSON 파일을 DataFrame으로 변환 (기존 로직 유지)
        
        Args:
            file_path (str): JSON 파일 경로
            search_empty_proj_func (function): 빈 프로젝트 검색 함수
            
        Returns:
            pandas.DataFrame: 스케줄 데이터프레임
        """
        if file_path is None:
            file_path = self.json_file
            
        try:
            df = pd.read_json(file_path)
            
            if not df.empty:
                # searchEmptyProj 함수가 제공된 경우에만 적용
                if search_empty_proj_func:
                    df['tasks'] = df['tasks'].apply(lambda x: search_empty_proj_func(x))
                    df_imported_json = df.loc[df['tasks'].apply(lambda x: x != [{}])]
                    return df_imported_json
                else:
                    return df
            else:
                # 스케쥴이 존재하지 않는 멤버의 경우 빈 데이터프레임 반환
                return df
                
        except Exception as e:
            print(f"DataFrame 변환 오류: {e}")
            return pd.DataFrame()
    
    def validate_schedule_data(self, data):
        """
        스케줄 데이터 유효성 검증
        
        Args:
            data (list): 검증할 스케줄 데이터
            
        Returns:
            tuple: (유효성 여부, 오류 메시지 리스트)
        """
        errors = []
        
        if not isinstance(data, list):
            return False, ["데이터가 리스트 형식이 아닙니다"]
        
        required_fields = ['artist', 'project', 'task', 'start_date', 'end_date']
        
        for i, item in enumerate(data):
            if not isinstance(item, dict):
                errors.append(f"항목 {i}: 딕셔너리 형식이 아닙니다")
                continue
                
            for field in required_fields:
                if field not in item:
                    errors.append(f"항목 {i}: 필수 필드 '{field}'가 누락되었습니다")
        
        return len(errors) == 0, errors
    
    def merge_schedule_data(self, base_data, new_data):
        """
        기존 스케줄 데이터와 새 데이터를 병합
        
        Args:
            base_data (list): 기존 스케줄 데이터
            new_data (list): 새로운 스케줄 데이터
            
        Returns:
            list: 병합된 데이터
        """
        try:
            merged_data = base_data.copy()
            
            for new_item in new_data:
                # 중복 검사 로직 (artist, project, task 조합으로)
                is_duplicate = False
                for i, existing_item in enumerate(merged_data):
                    if (existing_item.get('artist') == new_item.get('artist') and
                        existing_item.get('project') == new_item.get('project') and
                        existing_item.get('task') == new_item.get('task')):
                        # 중복 발견 시 기존 데이터 업데이트
                        merged_data[i] = new_item
                        is_duplicate = True
                        break
                
                # 중복이 아니면 새로 추가
                if not is_duplicate:
                    merged_data.append(new_item)
            
            return merged_data
        except Exception as e:
            print(f"데이터 병합 오류: {e}")
            return base_data
    
    def create_mirror_data(self, schedule_data):
        """
        스케줄 데이터의 미러 백업 생성
        
        Args:
            schedule_data (list): 원본 스케줄 데이터
            
        Returns:
            bool: 미러 생성 성공 여부
        """
        try:
            mirror_data = {
                'created_at': datetime.now().isoformat(),
                'user_id': self.user_id,
                'data': schedule_data
            }
            
            return self.save_json_data(mirror_data, self.mirror_file, backup=False)
        except Exception as e:
            print(f"미러 데이터 생성 오류: {e}")
            return False
    
    def load_mirror_data(self):
        """
        미러 데이터 로딩
        
        Returns:
            list: 미러 데이터의 스케줄 부분
        """
        try:
            mirror_data = self.load_json_data(self.mirror_file)
            if mirror_data and 'data' in mirror_data:
                return mirror_data['data']
            return []
        except Exception as e:
            print(f"미러 데이터 로딩 오류: {e}")
            return []
    
    def _create_backup(self, file_path):
        """
        파일 백업 생성 (내부 메소드)
        
        Args:
            file_path (str): 백업할 파일 경로
        """
        try:
            backup_name = f"{file_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            with open(file_path, 'r', encoding='utf-8') as src:
                with open(backup_name, 'w', encoding='utf-8') as dst:
                    dst.write(src.read())
            print(f"백업 생성: {backup_name}")
        except Exception as e:
            print(f"백업 생성 오류: {e}")
    
    def get_user_schedule_summary(self, user_id=None):
        """
        사용자별 스케줄 요약 정보 반환
        
        Args:
            user_id (str): 조회할 사용자 ID
            
        Returns:
            dict: 스케줄 요약 정보
        """
        if user_id is None:
            user_id = self.user_id
            
        try:
            file_path = config.get_schedule_data_file(user_id)
            data = self.load_json_data(file_path)
            
            if not data:
                return {'total_tasks': 0, 'projects': [], 'date_range': None}
            
            projects = list(set(item.get('project', '') for item in data))
            
            # 날짜 범위 계산
            dates = []
            for item in data:
                if 'start_date' in item:
                    dates.append(item['start_date'])
                if 'end_date' in item:
                    dates.append(item['end_date'])
            
            date_range = None
            if dates:
                dates.sort()
                date_range = {'start': dates[0], 'end': dates[-1]}
            
            return {
                'total_tasks': len(data),
                'projects': projects,
                'date_range': date_range
            }
        except Exception as e:
            print(f"스케줄 요약 오류: {e}")
            return {'total_tasks': 0, 'projects': [], 'date_range': None}