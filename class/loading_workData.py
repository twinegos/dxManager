from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *




class loading_workData(QRunnable):

    def __init__(self, task_id, member, taskInfo, projs, editedTasks_json, signals, conn_shot_sche, loading_tatic, dxManager):
        super().__init__()
        self.task_id = task_id
        self.member = member
        self.taskInfo = taskInfo
        self.projs = projs
        self.editedTasks_json = editedTasks_json
        self.conn_shot_sche = conn_shot_sche
        self.loading_tatic = loading_tatic
        self.dxManager = dxManager
        self.signals = signals#load_workData_Signals()
        self.is_finished = False


    def run(self):

        QApplication.setOverrideCursor(Qt.WaitCursor)
        global connect_shot_schedule

        if self.loading_tatic == 0:
            if self.member in list(self.dxManager.taskInfoJson.keys()):
                self.taskInfo[self.member] = self.dxManager.taskInfoJson[self.member]                    

            elif self.member not in list(self.dxManager.taskInfoJson.keys()): 
                self.taskInfo[self.member] = self.dxManager.getTaskInfo(self.member)
                self.dxManager.taskInfoJson[self.member] = self.taskInfo[self.member]
                #self.dxManager.export_Json(currentPath+"/.task_info", userID+"_task_info.json", self.dxManager.taskInfoJson)        

        elif self.loading_tatic == 1:
                self.taskInfo[self.member] = self.dxManager.getTaskInfo(self.member)
                self.dxManager.taskInfoJson[self.member] = self.taskInfo[self.member]


        member_shot = {}
        project_tasks = {}
        member_task = {}

        memberData = {}
        memberData_taskInfo = []

        task_schedule_dic = {}


        for sel_proj in self.projs:

            #self.project_tasks.append(sel_proj)
            #self.project_tasks.append(self.member)

            progressRate = 0
            shot_manday_list = []
            shot_manday_status_list = []

            #task_schedule_dic = {}

            shotList=[]
            process=""
            for i in range(len(self.taskInfo[self.member])):
                projCode = self.taskInfo[self.member][i]["project_code"]

                if projCode == self.dxManager.projects[sel_proj.lower()][0]:

                    shot = self.taskInfo[self.member][i]["extra_code"]
                    bd_manday = (self.taskInfo[self.member][i]["bid_manday"])
                    act_manday = self.taskInfo[self.member][i]["active_manday"]
                    status = self.taskInfo[self.member][i]["status"]
                    process = self.taskInfo[self.member][i]["process"]
                    start_date = self.taskInfo[self.member][i]["start_date"]
                    end_date = self.taskInfo[self.member][i]["end_date"]

                    if act_manday == None:
                        act_manday = "None"

                    if bd_manday == None:
                        bd_manday = "None"                            

                    progressRate = str(act_manday) + "/" + str(bd_manday)


                    context = self.taskInfo[self.member][i]["context"]
                    #if  context.find('/') != -1:
                    #    contextList = context.split('/')
                    #    shot = shot + "/" + contextList[1]

                    numContext=context.count("/")
                    if numContext>0:
                        contextList = context.split('/')

                        full_context = ""
                        for i in range(len(contextList)):
                            if i>0:
                                full_context += "/"+contextList[i]
                        shot=shot+full_context


                    shot_manday = (shot, progressRate)
                    shot_manday_list.append(shot_manday)


                    # 파트 지정
                    part=""
                    if process == "matchmove":
                        part = "M"

                    elif process == "animation":
                        part = "A"

                    elif process == "creature":
                        part = "R"


                    for editTask in self.editedTasks_json:

                        editTask_proj = ""
                        for proj_low in self.dxManager.projects:
                            if proj_low[1] == editTask[3]:
                                editTask_proj = proj_low[1]                                    

                        if editTask[0] == shot and editTask[2] == part and editTask_proj==sel_proj:
                            act = progressRate.split("/")[0]
                            progressRate = act+"/"+editTask[1]

                            
                    #shot_manday_status = (grade, shot, progressRate, status, part)

                    shot_manday_status = (sel_proj.upper(), shot, progressRate, status, part)
                    shot_manday_status_list.append(shot_manday_status)
                    task_schedule = [start_date, end_date]
                    task_schedule_dic[shot_manday_status] = task_schedule


            # connect_shot_schedule 와 새로 생성된 task_schedule_dic 을 합치기
            self.conn_shot_sche = {**self.conn_shot_sche, **task_schedule_dic}

            # conn_shot_sche 의  태스크중 task_schedule_dic 와 태스크 이름은 같지만 맨데이나 스테이터스가 다른 태스크의 경우 
            # conn_shot_sche 의 원래 태스크를 삭제하고 task_schedule_dic의 태스크로 대체시킴
            del_tasks = []
            add_tasks = []
            for connTask in self.conn_shot_sche:
                for editTask in task_schedule_dic:
                    if connTask[0] == editTask[0] and connTask[1] == editTask[1] and connTask[4] == editTask[4] and connTask[2] != editTask[2]:
                        del_tasks.append(connTask)
                        add_tasks.append(editTask)

            for del_task in del_tasks:
                del self.conn_shot_sche[del_task]

            for add_task in add_tasks:
                self.conn_shot_sche[add_task] = task_schedule_dic[add_task]


            # conn_shot_sche의 태스크들중 비디 맨데이가 수정된 태스크는 수정된 맨데이를 적용
            taskList_connectSchedule = list(self.conn_shot_sche.keys())
            editedTasks = [editTask for editTask in self.editedTasks_json for task in taskList_connectSchedule  if task[1]==editTask[0] and task[4]==editTask[2] and self.dxManager.projects[task[0].lower()][1] ==  editTask[3]]

            for taskName in editedTasks:
                scheduleTask = [scheduleTaskName for scheduleTaskName in self.conn_shot_sche if scheduleTaskName[1]== taskName[0] and scheduleTaskName[4]== taskName[2] and self.dxManager.projects[scheduleTaskName[0].lower()][1] ==  taskName[3]]

                if len(scheduleTask) == 1:
                    list_scheduleTask = list(scheduleTask[0])
                    bidManday = taskName[1]
                    mandayStatus = list_scheduleTask[2].split('/')[0] + "/" + bidManday
                    list_scheduleTask[2] = mandayStatus
                    tuple_scheduleTask = tuple(list_scheduleTask)

                    if scheduleTask[0] in self.conn_shot_sche:
                        schedule = self.conn_shot_sche[scheduleTask[0]]
                        del self.conn_shot_sche[scheduleTask[0]]

                    else:
                        schedule = [None, None]

                    self.conn_shot_sche[tuple_scheduleTask] = schedule

            project_tasks[sel_proj] = shot_manday_status_list


        memberData[self.member] = project_tasks
        memberData_taskInfo.append(memberData)
        memberData_taskInfo.append(self.taskInfo)
        memberData_taskInfo.append(self.conn_shot_sche)
        memberData_taskInfo.append(task_schedule_dic)

        result = memberData_taskInfo

        self.result  = result
        self.is_finished = True

        QApplication.restoreOverrideCursor()


class load_workData_Signals(QObject):
    result = Signal(object) # 각 worker가 개별적으로 결과를 emit 할때
    finished = Signal(dict) # 모든 worker 이 끝나고 전체 결과를 한번에 emit 할때
