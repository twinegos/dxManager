# -*- coding: utf-8 -*-
"""
dxManager MongoDB 데이터베이스 매니저
JSON 기반 스케줄 데이터를 MongoDB로 마이그레이션하기 위한 모듈

개발 진행 상태:
- MongoDB 연결 테스트 코드
- JSON 데이터 마이그레이션 로직 개발 중
- 데이터베이스 구조 설계 중
"""

from pymongo import MongoClient
import json
import os


class DatabaseManager:
    def __init__(self, connection_string="mongodb://localhost:27017/"):
        """
        MongoDB 데이터베이스 매니저 초기화
        
        Args:
            connection_string (str): MongoDB 연결 문자열
        """
        self.client = None
        self.db = None
        self.connection_string = connection_string
        
    def connect(self):
        """MongoDB 연결"""
        try:
            self.client = MongoClient(self.connection_string)
            # 연결 테스트
            self.client.admin.command('ping')
            print("MongoDB 연결 성공")
            return True
        except Exception as e:
            print(f"MongoDB 연결 실패: {e}")
            return False
    
    def init_database(self, db_name="SCHEDULE_DATA"):
        """데이터베이스 초기화"""
        if self.client:
            self.db = self.client[db_name]
            return True
        return False
    
    def test_connection(self):
        """
        데이터베이스 연결 테스트 (원본 dxManager.py에서 추출)
        
        원본 코드:
        #db = client['SCHEDULE_test']
        #collection = db['test']
        #collection.insert_one({'a':1})
        #client.drop_database('SCHEDULE_test')
        """
        try:
            # 테스트 데이터베이스 생성
            test_db = self.client['SCHEDULE_test']
            test_collection = test_db['test']
            
            # 테스트 데이터 삽입
            result = test_collection.insert_one({'a': 1, 'test': True})
            print(f"테스트 데이터 삽입 성공: {result.inserted_id}")
            
            # 테스트 데이터베이스 삭제
            self.client.drop_database('SCHEDULE_test')
            print("테스트 데이터베이스 삭제 완료")
            
            return True
        except Exception as e:
            print(f"데이터베이스 테스트 실패: {e}")
            return False
    
    def migrate_json_to_mongodb(self, json_data):
        """
        JSON 데이터를 MongoDB로 마이그레이션 (원본 dxManager.py에서 추출)
        
        원본 코드:
        for data in jsonData:
            artist_name = data['artist']
            collection_name = artist_name
            collection = db[collection_name]
            collection.insert_one(data)
        
        Args:
            json_data (list): 마이그레이션할 JSON 데이터 리스트
        """
        if not self.db:
            print("데이터베이스가 초기화되지 않았습니다.")
            return False
            
        try:
            migrated_count = 0
            for data in json_data:
                if 'artist' in data:
                    artist_name = data['artist']
                    collection_name = artist_name
                    collection = self.db[collection_name]
                    
                    # 데이터 삽입
                    result = collection.insert_one(data)
                    migrated_count += 1
                    print(f"아티스트 {artist_name} 데이터 마이그레이션 완료: {result.inserted_id}")
            
            print(f"총 {migrated_count}개 데이터 마이그레이션 완료")
            return True
            
        except Exception as e:
            print(f"데이터 마이그레이션 실패: {e}")
            return False
    
    def get_artist_schedule(self, artist_name):
        """특정 아티스트의 스케줄 데이터 조회"""
        if not self.db:
            return None
            
        try:
            collection = self.db[artist_name]
            return list(collection.find())
        except Exception as e:
            print(f"아티스트 {artist_name} 데이터 조회 실패: {e}")
            return None
    
    def update_artist_schedule(self, artist_name, schedule_data):
        """아티스트 스케줄 데이터 업데이트"""
        if not self.db:
            return False
            
        try:
            collection = self.db[artist_name]
            # 기존 데이터 삭제 후 새 데이터 삽입 (단순 구현)
            collection.delete_many({})
            if isinstance(schedule_data, list):
                collection.insert_many(schedule_data)
            else:
                collection.insert_one(schedule_data)
            return True
        except Exception as e:
            print(f"아티스트 {artist_name} 데이터 업데이트 실패: {e}")
            return False
    
    def close_connection(self):
        """MongoDB 연결 종료"""
        if self.client:
            self.client.close()
            print("MongoDB 연결 종료")


# 사용 예시 및 테스트 함수들
def test_database_manager():
    """데이터베이스 매니저 테스트"""
    db_manager = DatabaseManager()
    
    # 연결 테스트
    if db_manager.connect():
        db_manager.init_database("SCHEDULE_DATA")
        
        # 연결 테스트 실행
        db_manager.test_connection()
        
        # 연결 종료
        db_manager.close_connection()
    else:
        print("데이터베이스 연결 실패")


if __name__ == "__main__":
    test_database_manager()