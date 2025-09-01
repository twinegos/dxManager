from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


# progressBar 의 블러킹 현상을 해결하기 위해 쓰레드를 분리하여 show_team_status 메서드내의 get_child_items가 이 쓰레드상에서 실행되도록 함
class ProgressBar_Thread(QThread):
    progress_signal = Signal(int)
    finished_signal = Signal()
    result_ready_signal = Signal(list)


    def __init__(self, index, total_app_tasks, total_tasks, total_act_mandays, total_mandays, team_projManday, team_shotStatus, team_wipStatus, orderList, dxManager, parent=None):
        super().__init__(parent)
        #self.task_time = task_time
        self.index = index
        self.total_app_tasks = total_app_tasks
        self.total_tasks = total_tasks
        self.total_act_mandays = total_act_mandays
        self.total_mandays = total_mandays
        self.team_projManday = team_projManday
        self.team_shotStatus = team_shotStatus
        self.team_wipStatus = team_wipStatus
        self.orderList = orderList

        self.all_app = 0
        self.all_tasks = 0
        self.all_actManday = ""
        self.all_manday = 0 
        self.projManday = {}
        self.projShotStatus = {}
        self.teamWipStatus = {}
        self.dxManager = dxManager
        self.results = []

        self.dxManager.update_progress = self.report_progress

    def report_progress(self, value):
        self.progress_signal.emit(value)


    def run(self):
        total_steps = 100
        self.all_app, self.all_tasks, self.all_actManday, self.all_manday, self.projManday, self.projShotStatus, self.teamWipStatus = self.dxManager.get_child_items(self.index, self.total_app_tasks, self.total_tasks, self.total_act_mandays, self.total_mandays, self.team_projManday, self.team_shotStatus, total_steps, self.team_wipStatus, self.orderList)
        self.results = [self.all_app, self.all_tasks, self.all_actManday, self.all_manday, self.projManday, self.projShotStatus, self.teamWipStatus]
        
        self.result_ready_signal.emit(self.results)
        self.finished_signal.emit()

