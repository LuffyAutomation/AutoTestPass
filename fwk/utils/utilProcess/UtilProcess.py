import os


class UtilProcess:
    @staticmethod
    def kill_process(name):
        if os.name == "nt":
            # windows OS
            if not name.endswith('.exe'):
                name = name + '.exe'
            os.system("taskkill /f /im {}".format(name))
            # os.system(r"start /b pcs.exe 2>&1")
            # with os.popen("tasklist | findstr \"pcs.exe\"") as f:
            #     temp_content = f.read()
            # if len(temp_content) == 0:
            #     pass
        else:
            if name.endswith('.exe'):
                name = name.replace('.exe', '')
            os.system("killall -9 {} 2>&1".format(name))
            # os.system("pcs &")
            # with os.popen("ps -aux | grep pcs | grep -v grep") as f:
            #     temp_content = f.read()
            # if len(temp_content) == 0:
            #     pass
    # os.system("taskkill /im /f")
#
# import subprocess
#
# handle = subprocess.Popen("", shell=False)
# subprocess.Popen("taskkill /F /T /PID %i" % handle.pid, shell=True)
#
#
# import subprocess
#
# process = subprocess.Popen(['', '-c', 'while 1: pass'])
#

