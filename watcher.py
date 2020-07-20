from riotwatcher import LolWatcher
from datetime import datetime, timedelta
import time

lol_watcher = LolWatcher('RGAPI-b34c9615-2352-439e-8324-4326e28fbee1')

my_region = 'kr'
target = input('검색할 닉네임을 입력하세요:\n')

me = lol_watcher.summoner.by_name(my_region, target)

spectator = None

while True:
    print('[*] Checking...', "'"+target+"'", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    try:
        spectator = lol_watcher.spectator.by_summoner(my_region, me['id'])

        start_time = datetime.fromtimestamp(spectator['gameStartTime'] / 1000)

        if datetime.now() - start_time < timedelta(minutes=60):
            print('[!] My son is playing LoL!', start_time.strftime('%Y-%m-%d %H:%M:%S'))
    except:
        pass

    time.sleep(5)
