"""
FileManager - 파일 입출력 관리 클래스

dxManager에서 파일 관련 기능들을 분리한 클래스입니다.
JSON 파일 입출력, 백업 관리, 엑셀 파일 처리 등의 기능을 담당합니다.
"""

import os
import json
import logging
from datetime import datetime
from data_manager import DataManager

class FileManager:
    def __init__(self, main_window):
        """
        FileManager 초기화
        
        Args:
            main_window: dxManager 메인 윈도우 인스턴스
        """
        self.main_window = main_window
        self.current_path = os.path.dirname(os.path.abspath(__file__)).replace('/class', '')
        self.data_manager = DataManager(main_window)
        
    def get_latest_file(self, path):
        """최신 파일 가져오기 및 프리뷰 실행"""
        try:
            if not os.path.exists(path):
                latest_file = ""
            else:
                patterns = ["thumb", "_icon_", "_web_"]
                all_items = [
                    os.path.join(path, item)
                    for item in os.listdir(path)
                    if not any(pattern in item for pattern in patterns)
                ]
                if not all_items:
                    latest_file = ""
                else:
                    latest_file = max(all_items, key=os.path.getmtime)
        except Exception as e:
            latest_file = ""

        if not latest_file:
            from PySide2.QtWidgets import QMessageBox
            QMessageBox.information(None, "알 림", "프리뷰가 존재하지 않습니다.")
            return

        # 프리뷰 실행
        import subprocess

        if os.path.isdir(latest_file):
            subprocess.run(["xdg-open", str(latest_file)], check=True)
        elif os.path.isfile(latest_file) and latest_file.lower().endswith((".mov", ".mp4", ".jpg", "jpeg", "png", "exr")):
            cmd = ["/backstage/dcc/DCC", "rez-env", "rv-1.0.0", "--", "rv", latest_file]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
    
    def import_Json(self, path, name):
        """JSON 파일 가져오기"""
        try:
            json_file = os.path.join(path, name)
            if os.path.exists(json_file):
                with open(json_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"JSON 파일 임포트 실패 ({path}/{name}): {e}")
            return []
    
    def import_Json_Thread(self, path, name):
        """쓰레드용 JSON 파일 가져오기"""
        try:
            json_file = os.path.join(path, name)
            if os.path.exists(json_file):
                with open(json_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"스레드 JSON 파일 임포트 실패 ({path}/{name}): {e}")
            return []
    
    def export_Json(self, path, name, data):
        """JSON 파일 내보내기"""
        try:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)

            json_file = os.path.join(path, name)
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"JSON 파일 익스포트 실패 ({path}/{name}): {e}")
            return False
    
    def export_Json_Thread(self, path, name, data):
        """쓰레드용 JSON 파일 내보내기"""
        try:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)

            json_file = os.path.join(path, name)
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"스레드 JSON 파일 익스포트 실패 ({path}/{name}): {e}")
            return False
    
    def backup_schedule(self, save_data, user, backup_dir, backup_name):
        """스케쥴 데이터 백업"""
        try:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = os.path.join(self.current_path, ".backup", backup_dir)
            backup_file = f"{backup_name}_{timestamp}.json"

            if not os.path.exists(backup_path):
                os.makedirs(backup_path, exist_ok=True)

            success = self.export_Json(backup_path, backup_file, save_data)

            if success:
                self.cleanup_old_backups(backup_path, user, 10)

            return success

        except Exception as e:
            print(f"스케쥴 백업 실패: {e}")
            return False
    
    def cleanup_old_backups(self, backup_dir, user, max_backups=10):
        """오래된 백업 파일 정리"""
        try:
            if not os.path.exists(backup_dir):
                return

            backup_files = sorted(
                [f for f in os.listdir(backup_dir) if f.startswith(user) and f.endswith('.json')],
                key=lambda x: os.path.getmtime(os.path.join(backup_dir, x))
            )

            if len(backup_files) > max_backups:
                files_to_delete = backup_files[:-max_backups]
                for file_to_delete in files_to_delete:
                    file_path = os.path.join(backup_dir, file_to_delete)
                    os.remove(file_path)

        except Exception as e:
            print(f"백업 파일 정리 실패: {e}")
    
    def save_file_with_backup(self, data, user_id):
        """
        파일 저장과 동시에 백업을 생성합니다.
        
        Args:
            data: 저장할 데이터
            user_id (str): 사용자 ID
            
        Returns:
            bool: 저장 성공 여부
        """
        try:
            # 메인 파일 저장
            json_file_path = os.path.join(self.current_path, f"{user_id}_Data.json")
            main_save_success = self.data_manager.save_json_data(data, json_file_path)
            
            if main_save_success:
                # 백업 생성
                backup_success = self.backup_schedule(
                    data, 
                    user_id, 
                    "schedule_backup", 
                    f"{user_id}_schedule"
                )
                
                if not backup_success:
                    logging.warning(f"메인 저장 성공, 백업 실패: {user_id}")
                    
                return True
            else:
                logging.error(f"메인 파일 저장 실패: {user_id}")
                return False
                
        except Exception as e:
            logging.error(f"파일 저장 및 백업 실패: {e}")
            return False
    
    def get_backup_list(self, user_id, backup_dir="schedule_backup"):
        """
        사용자의 백업 파일 목록을 가져옵니다.
        
        Args:
            user_id (str): 사용자 ID
            backup_dir (str): 백업 디렉토리명
            
        Returns:
            list: 백업 파일 정보 리스트 (파일명, 생성날짜 포함)
        """
        try:
            backup_path = os.path.join(self.current_path, ".backup", backup_dir)
            
            if not os.path.exists(backup_path):
                return []
                
            backup_files = [
                f for f in os.listdir(backup_path) 
                if f.startswith(user_id) and f.endswith('.json')
            ]
            
            backup_info = []
            for backup_file in backup_files:
                file_path = os.path.join(backup_path, backup_file)
                mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                
                backup_info.append({
                    'filename': backup_file,
                    'filepath': file_path,
                    'created_date': mod_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'size': os.path.getsize(file_path)
                })
            
            # 생성날짜 역순으로 정렬 (최신 파일이 위에)
            backup_info.sort(key=lambda x: x['created_date'], reverse=True)
            
            return backup_info
            
        except Exception as e:
            logging.error(f"백업 목록 조회 실패: {e}")
            return []
    
    def restore_from_backup(self, backup_file_path, user_id):
        """
        백업 파일에서 데이터를 복원합니다.
        
        Args:
            backup_file_path (str): 백업 파일의 전체 경로
            user_id (str): 사용자 ID
            
        Returns:
            dict: 복원된 데이터 (실패 시 None)
        """
        try:
            if not os.path.exists(backup_file_path):
                logging.error(f"백업 파일이 존재하지 않음: {backup_file_path}")
                return None
                
            # 백업 파일 로드
            with open(backup_file_path, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
                
            logging.info(f"백업 파일 복원 완료: {backup_file_path}")
            return backup_data
            
        except Exception as e:
            logging.error(f"백업 복원 실패 ({backup_file_path}): {e}")
            return None