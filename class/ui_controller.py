# -*- coding: utf-8 -*-
"""
UI 컨트롤러 클래스
dxManager에서 UI 관리 관련 기능을 분리한 모듈
"""

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import config


class UIController:
    def __init__(self, main_window):
        """
        UI 컨트롤러 초기화
        
        Args:
            main_window: 메인 윈도우 인스턴스
        """
        self.main_window = main_window
        self.ui = main_window.ui
        
    def setup_listview_ui(self):
        """리스트뷰 UI 초기 설정"""
        try:
            # 기본 리스트뷰 설정
            self._setup_basic_listviews()
            print("리스트뷰 UI 설정 완료")
        except Exception as e:
            print(f"리스트뷰 UI 설정 오류: {e}")
    
    def _setup_basic_listviews(self):
        """기본 리스트뷰들의 초기 설정"""
        # 기본적인 리스트뷰 설정 로직
        pass
    
    def refresh_listviews(self, direction=None, schedule_data=None):
        """
        리스트뷰들을 새로고침
        
        Args:
            direction: 방향 (0: 현재, 1: 다음, -1: 이전)
            schedule_data: 스케줄 데이터
        """
        try:
            if direction is not None and schedule_data is not None:
                # 스케줄 데이터를 기반으로 리스트뷰 갱신
                self._update_listviews_with_schedule(direction, schedule_data)
            else:
                # 기본 새로고침
                self._refresh_all_listviews()
        except Exception as e:
            print(f"리스트뷰 새로고침 오류: {e}")
    
    def _update_listviews_with_schedule(self, direction, schedule_data):
        """스케줄 데이터로 리스트뷰 업데이트"""
        # 복잡한 리스트뷰 업데이트 로직은 점진적으로 이동
        pass
    
    def _refresh_all_listviews(self):
        """모든 리스트뷰 새로고침"""
        # 기본 새로고침 로직
        pass
    
    def reload_shot_list(self):
        """샷 리스트뷰 다시 로딩"""
        try:
            QApplication.setOverrideCursor(Qt.WaitCursor)
            
            # 샷 리스트 로딩 로직은 점진적으로 이동
            self._load_shot_data()
            
            QApplication.restoreOverrideCursor()
        except Exception as e:
            print(f"샷 리스트 로딩 오류: {e}")
            QApplication.restoreOverrideCursor()
    
    def _load_shot_data(self):
        """샷 데이터 로딩"""
        # 샷 데이터 로딩 로직
        pass
    
    def update_listview_model(self, listview, model_data):
        """
        리스트뷰 모델 업데이트
        
        Args:
            listview: 대상 리스트뷰
            model_data: 모델 데이터
        """
        try:
            if listview and model_data:
                # 모델 데이터로 리스트뷰 업데이트
                self._apply_model_to_listview(listview, model_data)
        except Exception as e:
            print(f"리스트뷰 모델 업데이트 오류: {e}")
    
    def _apply_model_to_listview(self, listview, model_data):
        """리스트뷰에 모델 적용"""
        # 모델 적용 로직
        pass
    
    def set_listview_view(self, listview, model):
        """
        리스트뷰 뷰 설정
        
        Args:
            listview: 대상 리스트뷰
            model: 모델
        """
        try:
            if listview and model:
                listview.setModel(model)
                self._configure_listview_appearance(listview)
        except Exception as e:
            print(f"리스트뷰 뷰 설정 오류: {e}")
    
    def _configure_listview_appearance(self, listview):
        """리스트뷰 외관 설정"""
        try:
            # 기본 외관 설정
            listview.setAlternatingRowColors(True)
            listview.setSelectionBehavior(QAbstractItemView.SelectRows)
        except Exception as e:
            print(f"리스트뷰 외관 설정 오류: {e}")
    
    def sort_listview(self, listview, model, sort_order, sort_column, date=None):
        """
        리스트뷰 정렬
        
        Args:
            listview: 대상 리스트뷰
            model: 모델
            sort_order: 정렬 순서
            sort_column: 정렬 컬럼
            date: 날짜 (선택적)
        """
        try:
            if model:
                model.sort(sort_column, sort_order)
                listview.sortByColumn(sort_column, sort_order)
        except Exception as e:
            print(f"리스트뷰 정렬 오류: {e}")
    
    def get_listview_selected_items(self, listview):
        """
        리스트뷰 선택된 아이템들 반환 (원본 로직 유지)
        
        Args:
            listview: 대상 리스트뷰
            
        Returns:
            list: 선택된 아이템들
        """
        try:
            selected_indexes = listview.selectedIndexes()
            
            curr_items = []
            for index in selected_indexes:
                item = listview.model().data(index, Qt.DisplayRole)
                
                if item not in curr_items:
                    curr_items.append(item)
            
            return curr_items
        except Exception as e:
            print(f"선택된 아이템 조회 오류: {e}")
            return []
    
    def clear_listview_selection(self, listview):
        """리스트뷰 선택 해제"""
        try:
            if listview and listview.selectionModel():
                listview.selectionModel().clearSelection()
        except Exception as e:
            print(f"리스트뷰 선택 해제 오류: {e}")
    
    def set_listview_filter(self, listview, filter_text):
        """
        리스트뷰 필터 설정
        
        Args:
            listview: 대상 리스트뷰
            filter_text: 필터 텍스트
        """
        try:
            if listview and hasattr(listview.model(), 'setFilterFixedString'):
                listview.model().setFilterFixedString(filter_text)
        except Exception as e:
            print(f"리스트뷰 필터 설정 오류: {e}")
    
    def resize_listview_columns(self, listview):
        """리스트뷰 컬럼 크기 자동 조정"""
        try:
            if listview:
                listview.resizeColumnsToContents()
        except Exception as e:
            print(f"리스트뷰 컬럼 크기 조정 오류: {e}")
    
    def update_team_treeview(self, tree_data):
        """
        팀 트리뷰 업데이트
        
        Args:
            tree_data: 트리 데이터
        """
        try:
            if tree_data:
                self._populate_team_tree(tree_data)
        except Exception as e:
            print(f"팀 트리뷰 업데이트 오류: {e}")
    
    def _populate_team_tree(self, tree_data):
        """팀 트리 데이터 채우기"""
        # 트리 데이터 채우기 로직
        pass
    
    def get_checked_tree_items(self, tree_model):
        """
        체크된 트리 아이템들 반환
        
        Args:
            tree_model: 트리 모델
            
        Returns:
            list: 체크된 아이템들
        """
        try:
            checked_items = []
            if tree_model:
                # 체크된 아이템 수집 로직
                self._collect_checked_items(tree_model.invisibleRootItem(), checked_items)
            return checked_items
        except Exception as e:
            print(f"체크된 아이템 조회 오류: {e}")
            return []
    
    def _collect_checked_items(self, item, checked_items):
        """체크된 아이템들을 재귀적으로 수집"""
        try:
            for row in range(item.rowCount()):
                child = item.child(row)
                if child and child.checkState() == Qt.Checked:
                    checked_items.append(child.text())
                # 하위 아이템들도 확인
                self._collect_checked_items(child, checked_items)
        except Exception as e:
            print(f"체크된 아이템 수집 오류: {e}")
    
    def show_context_menu(self, listview, position):
        """
        컨텍스트 메뉴 표시
        
        Args:
            listview: 대상 리스트뷰
            position: 메뉴 위치
        """
        try:
            if listview:
                menu = QMenu()
                # 컨텍스트 메뉴 아이템들 추가
                self._add_context_menu_items(menu, listview)
                menu.exec_(listview.mapToGlobal(position))
        except Exception as e:
            print(f"컨텍스트 메뉴 표시 오류: {e}")
    
    def _add_context_menu_items(self, menu, listview):
        """컨텍스트 메뉴 아이템들 추가"""
        try:
            # 기본 메뉴 아이템들
            refresh_action = menu.addAction("새로고침")
            refresh_action.triggered.connect(lambda: self.refresh_listviews())
            
            clear_action = menu.addAction("선택 해제")
            clear_action.triggered.connect(lambda: self.clear_listview_selection(listview))
        except Exception as e:
            print(f"컨텍스트 메뉴 아이템 추가 오류: {e}")