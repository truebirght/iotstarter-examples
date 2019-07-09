import firebase_admin
import schedule
import time
import datetime
import random
import sys
from time import sleep
from random import randint

from firebase_admin import credentials
from firebase_admin import db

# 자동급식/수동급식 실행시 Firebase로 정보 전송
def add_action(type):
    db.reference('/queue').push({
        "startAt": round(datetime.datetime.now().timestamp()),
        "status": "pending",
        "type": type,
        "action": "feed"
    })


# Web에서 자동급식정보가 수정됬을때 수행
def on_batch_modified(evt):
    #설정된 자동급식정보가 하나도 없을경우 아무것도 안함
    if evt.path == '/' and evt.data == None:
        return
    
    if evt.path == '/':
        for job in evt.data.values():
            set_schedule_job(job)
    else:
        if evt.data != None:
            set_schedule_job(evt.data)
        else:
            
            schedule.clear(evt.path[1:])    

# 급식정보가 추가됬을때 수행
def on_action_added(evt):
    if evt.path == '/' or evt.data == None:
        return

    data = evt.data
    try:
        #TODO :: 실제 서보모터를 돌려야함
        delay = randint(1, 5)
        print('[sleep {0}sec] - {1}'.format(delay, data))
        sleep(delay)
        
        if bool(random.choice([True, False])):
            raise IOError('운명은 신에게 맡기세요..')

        data['status'] = 'complete'
    except Exception as ex:
        data['status'] = 'incomplete'
        data['exception'] = str(ex)
    finally:
        data['endAt'] = round(datetime.datetime.now().timestamp())
        db.reference('/history').push(data)

def set_schedule_job(job):
    time_str = str(job['hour']) + ':' + str(job['minute'])
    if job['everyday'] == True:
        schedule.every().day.at(time_str).do(add_action, type='batch').tag(job['key'])
        print("batch_job_added : everyday " + time_str)
    else:
        for k in ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']:
            if job[k] == True:
                print("batch_job_added : " + k + " " + time_str)
                if k == 'mon':
                    schedule.every().monday.at(time_str).do(add_action, type='batch').tag(job['key'])
                if k == 'tue':
                    schedule.every().tuesday.at(time_str).do(add_action, type='batch').tag(job['key'])
                if k == 'wed':
                    schedule.every().wednesday.at(time_str).do(add_action, type='batch').tag(job['key'])
                if k == 'thu':
                    schedule.every().thursday.at(time_str).do(add_action, type='batch').tag(job['key'])
                if k == 'fri':
                    schedule.every().friday.at(time_str).do(add_action, type='batch').tag(job['key'])
                if k == 'sat':
                    schedule.every().saturday.at(time_str).do(add_action, type='batch').tag(job['key'])
                if k == 'sun':
                    schedule.every().sunday.at(time_str).do(add_action, type='batch').tag(job['key'])


if __name__ == '__main__':
    ql = None
    bl = None

    try:
        # Firebase 인증정보 연결 및 초기화
        cred = credentials.Certificate(
            'C:\\Users\\GgamMang\\Downloads\\fb-adminsdk.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://iotstarter-smartfeeder.firebaseio.com'
        })

        ql = db.reference('/queue').listen(on_action_added)
        bl = db.reference('/batch').listen(on_batch_modified)

        while True:
            schedule.run_pending()
            time.sleep(1)

    except FileNotFoundError:
        print('인증정보 파일 위치가 올바르지 않습니다.')
    except KeyboardInterrupt:
        print('사용자가 프로그램을 종료하였습니다.')  
    finally:
        schedule.clear()
        ql.close()
        bl.close()
        firebase_admin.delete_app(firebase_admin.get_app())
        sys.exit(0)
    
