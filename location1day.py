import subprocess
import time

while True:
    # プロジェクトを再実行する
    subprocess.run(["python", "/Volumes/SSD250/VScode/ALL/location/location.py"])

    # 1日待機する（24時間 * 60分 * 60秒）
    time.sleep(12 * 60 * 60)

#バグらないようにlocation.py自体を1日毎に再実行する。location.py自体は実行する必要がない（重複するため