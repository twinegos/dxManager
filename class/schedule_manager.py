# -*- coding: utf-8 -*-
"""
스케줄 매니저 클래스
dxManager에서 스케줄 및 맨데이 관리 관련 기능을 분리한 모듈
"""

import os
import json
from datetime import datetime, timedelta
import config


class ScheduleManager:
    def __init__(self, user_id=None):
        """
        스케줄 매니저 초기화
        
        Args:
            user_id (str): 사용자 ID (None일 경우 config에서 자동 획득)
        """
        self.user_id = user_id if user_id else config.get_user_id()
        
    def calculate_mandays(self, start_date, end_date, exclude_weekends=True):
        """
        시작일과 종료일 사이의 맨데이 계산
        
        Args:
            start_date (str): 시작일 (YYYY-MM-DD)
            end_date (str): 종료일 (YYYY-MM-DD)
            exclude_weekends (bool): 주말 제외 여부
            
        Returns:
            int: 계산된 맨데이 수
        """
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            
            if start > end:
                return 0
            
            total_days = (end - start).days + 1
            
            if not exclude_weekends:
                return total_days
            
            # 주말 제외 계산
            mandays = 0
            current_date = start
            while current_date <= end:
                # 주말이 아닌 경우만 카운트 (월요일=0, 일요일=6)
                if current_date.weekday() < 5:  # 월-금
                    mandays += 1
                current_date += timedelta(days=1)
                
            return mandays
        except Exception as e:
            print(f"맨데이 계산 오류: {e}")
            return 0
    
    def validate_schedule_dates(self, start_date, end_date):
        """
        스케줄 날짜 유효성 검증
        
        Args:
            start_date (str): 시작일
            end_date (str): 종료일
            
        Returns:
            tuple: (유효성 여부, 오류 메시지)
        """
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            
            if start > end:
                return False, "시작일이 종료일보다 늦습니다"
            
            # 과거 날짜 체크 (선택적)
            today = datetime.now().date()
            if end.date() < today:
                return False, "종료일이 과거 날짜입니다"
            
            return True, ""
        except ValueError:
            return False, "날짜 형식이 올바르지 않습니다 (YYYY-MM-DD)"
        except Exception as e:
            return False, f"날짜 검증 오류: {e}"
    
    def get_date_range(self, center_date, range_days=7):
        """
        중심 날짜를 기준으로 날짜 범위 계산
        
        Args:
            center_date (str): 중심 날짜
            range_days (int): 범위 일수
            
        Returns:
            tuple: (시작일, 종료일)
        """
        try:
            center = datetime.strptime(center_date, '%Y-%m-%d')
            half_range = range_days // 2
            
            start_date = center - timedelta(days=half_range)
            end_date = center + timedelta(days=half_range)
            
            return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')
        except Exception as e:
            print(f"날짜 범위 계산 오류: {e}")
            today = datetime.now().strftime('%Y-%m-%d')
            return today, today
    
    def get_weekly_dates(self, week_offset=0):
        """
        주간 날짜 목록 반환
        
        Args:
            week_offset (int): 주 오프셋 (0=이번주, 1=다음주, -1=지난주)
            
        Returns:
            list: 주간 날짜 목록 (월-일)
        """
        try:
            today = datetime.now()
            # 이번 주 월요일 찾기
            days_since_monday = today.weekday()
            monday = today - timedelta(days=days_since_monday)
            
            # 오프셋 적용
            target_monday = monday + timedelta(weeks=week_offset)
            
            # 월요일부터 일요일까지 날짜 생성
            weekly_dates = []
            for i in range(7):
                date = target_monday + timedelta(days=i)
                weekly_dates.append(date.strftime('%Y-%m-%d'))
            
            return weekly_dates
        except Exception as e:
            print(f"주간 날짜 계산 오류: {e}")
            return []
    
    def calculate_workload_distribution(self, total_mandays, start_date, end_date):
        """
        총 맨데이를 기간에 따라 분배 계산
        
        Args:
            total_mandays (float): 총 맨데이
            start_date (str): 시작일
            end_date (str): 종료일
            
        Returns:
            dict: 날짜별 맨데이 분배 {날짜: 맨데이}
        """
        try:
            work_days = self.calculate_mandays(start_date, end_date, exclude_weekends=True)
            if work_days <= 0:
                return {}
            
            # 일일 평균 맨데이 계산
            daily_mandays = total_mandays / work_days
            
            # 날짜별 분배
            distribution = {}
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            
            current_date = start
            while current_date <= end:
                # 주말 제외하고 분배
                if current_date.weekday() < 5:
                    date_str = current_date.strftime('%Y-%m-%d')
                    distribution[date_str] = daily_mandays
                current_date += timedelta(days=1)
            
            return distribution
        except Exception as e:
            print(f"워크로드 분배 계산 오류: {e}")
            return {}
    
    def get_schedule_conflicts(self, schedules):
        """
        스케줄 충돌 검사
        
        Args:
            schedules (list): 스케줄 목록 (각각 start_date, end_date 포함)
            
        Returns:
            list: 충돌하는 스케줄 쌍들
        """
        try:
            conflicts = []
            
            for i, schedule1 in enumerate(schedules):
                for j, schedule2 in enumerate(schedules[i+1:], i+1):
                    if self._schedules_overlap(schedule1, schedule2):
                        conflicts.append((i, j))
            
            return conflicts
        except Exception as e:
            print(f"스케줄 충돌 검사 오류: {e}")
            return []
    
    def _schedules_overlap(self, schedule1, schedule2):
        """두 스케줄이 겹치는지 확인"""
        try:
            start1 = datetime.strptime(schedule1['start_date'], '%Y-%m-%d')
            end1 = datetime.strptime(schedule1['end_date'], '%Y-%m-%d')
            start2 = datetime.strptime(schedule2['start_date'], '%Y-%m-%d')
            end2 = datetime.strptime(schedule2['end_date'], '%Y-%m-%d')
            
            # 겹치지 않는 경우: end1 < start2 or end2 < start1
            return not (end1 < start2 or end2 < start1)
        except Exception as e:
            print(f"스케줄 겹침 검사 오류: {e}")
            return False
    
    def calculate_quarterly_workload(self, schedules, year, quarter):
        """
        분기별 워크로드 계산
        
        Args:
            schedules (list): 스케줄 목록
            year (int): 년도
            quarter (int): 분기 (1-4)
            
        Returns:
            dict: 분기별 워크로드 정보
        """
        try:
            # 분기별 시작/종료일 계산
            quarter_start_month = (quarter - 1) * 3 + 1
            quarter_end_month = quarter * 3
            
            quarter_start = datetime(year, quarter_start_month, 1)
            
            # 분기 마지막 날 계산
            if quarter_end_month == 12:
                next_quarter_start = datetime(year + 1, 1, 1)
            else:
                next_quarter_start = datetime(year, quarter_end_month + 1, 1)
            quarter_end = next_quarter_start - timedelta(days=1)
            
            # 분기에 해당하는 스케줄 필터링 및 계산
            quarterly_workload = {
                'quarter': f"{year}Q{quarter}",
                'start_date': quarter_start.strftime('%Y-%m-%d'),
                'end_date': quarter_end.strftime('%Y-%m-%d'),
                'total_mandays': 0,
                'total_tasks': 0,
                'projects': {}
            }
            
            for schedule in schedules:
                if self._schedule_in_quarter(schedule, quarter_start, quarter_end):
                    quarterly_workload['total_tasks'] += 1
                    
                    # 맨데이 계산 (분기 내 기간만)
                    schedule_start = max(
                        datetime.strptime(schedule['start_date'], '%Y-%m-%d'),
                        quarter_start
                    )
                    schedule_end = min(
                        datetime.strptime(schedule['end_date'], '%Y-%m-%d'),
                        quarter_end
                    )
                    
                    mandays = self.calculate_mandays(
                        schedule_start.strftime('%Y-%m-%d'),
                        schedule_end.strftime('%Y-%m-%d')
                    )
                    
                    quarterly_workload['total_mandays'] += mandays
                    
                    # 프로젝트별 집계
                    project = schedule.get('project', 'Unknown')
                    if project not in quarterly_workload['projects']:
                        quarterly_workload['projects'][project] = {
                            'mandays': 0,
                            'tasks': 0
                        }
                    
                    quarterly_workload['projects'][project]['mandays'] += mandays
                    quarterly_workload['projects'][project]['tasks'] += 1
            
            return quarterly_workload
        except Exception as e:
            print(f"분기별 워크로드 계산 오류: {e}")
            return {}
    
    def _schedule_in_quarter(self, schedule, quarter_start, quarter_end):
        """스케줄이 분기 내에 포함되는지 확인"""
        try:
            start = datetime.strptime(schedule['start_date'], '%Y-%m-%d')
            end = datetime.strptime(schedule['end_date'], '%Y-%m-%d')
            
            # 스케줄이 분기와 겹치는지 확인
            return not (end < quarter_start or start > quarter_end)
        except Exception as e:
            print(f"분기 포함 검사 오류: {e}")
            return False
    
    def format_date_for_display(self, date_string, format_type='short'):
        """
        날짜를 표시용으로 포맷
        
        Args:
            date_string (str): 날짜 문자열
            format_type (str): 포맷 타입 ('short', 'long', 'korean')
            
        Returns:
            str: 포맷된 날짜 문자열
        """
        try:
            date = datetime.strptime(date_string, '%Y-%m-%d')
            
            if format_type == 'short':
                return date.strftime('%m/%d')
            elif format_type == 'long':
                return date.strftime('%Y-%m-%d (%A)')
            elif format_type == 'korean':
                weekdays = ['월', '화', '수', '목', '금', '토', '일']
                weekday = weekdays[date.weekday()]
                return f"{date.strftime('%Y년 %m월 %d일')} ({weekday})"
            else:
                return date_string
        except Exception as e:
            print(f"날짜 포맷 오류: {e}")
            return date_string