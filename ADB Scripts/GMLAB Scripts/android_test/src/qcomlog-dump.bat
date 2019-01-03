

@echo ## log dump
@echo ##

@echo ## try to get the root
adb devices
adb root
adb wait-for-device
adb remount

@echo ## make log directory
set date_num=%Date:~0,4%%Date:~5,2%%Date:~8,2%
set t=%Time%
if "%t:~0,1%" ==" " (set t=0%t:~1%)
set date_num=%Date:~0,4%%Date:~5,2%%Date:~8,2%%t:~0,2%%t:~3,2%%t:~6,2%
set dir = qc-log-%date_num%
mkdir qc-log-%date_num%

@echo ## start
@echo ##
@echo ## dump sdcard log
adb pull /mnt/sdcard/log qc-log-%date_num%/log

@echo ## dump One-touch log
adb pull /mnt/sdcard/One-touch qc-log-%date_num%/

@echo ##
@echo ## dump monkey log
adb pull /sdcard/Stability_base.txt qc-log-%date_num%/Stability_base.txt
adb pull /sdcard/Stability_base_err.txt qc-log-%date_num%/Stability_base_err.txt

@echo ##
@echo ## dump Runin log
adb pull /sdcard/runintest2/ qc-log-%date_num%/
adb pull /sdcard/wlan_logs/ qc-log-%date_num%/
adb pull data/data/com.longcheertel.runintest2 qc-log-%date_num%/

@echo ##
@echo ## dump system log
adb shell dmesg > qc-log-%date_num%/dmesg.txt
adb shell cat /proc/iomem >  qc-log-%date_num%/iomem.txt

adb shell dumpsys -t 30 dropbox -p system_server_crash > qc-log-%date_num%/system_server_crash.txt
adb shell dumpsys -t 30 dropbox -p system_app_crash > qc-log-%date_num%/system_app_crash.txt

::@echo ##
::adb shell dumpsys > qc-log-%date_num%/dumpsys.txt
::@echo ##
::adb shell dumpsys window > qc-log-%date_num%/window.txt
@echo ##
adb shell cat /proc/meminfo > qc-log-%date_num%/meminfo.txt
::@echo ##
::adb shell dumpsys meminfo > qc-log-%date_num%/dump_meminfo.txt
::@echo ##
::adb shell free > qc-log-%date_num%/free.txt
::@echo ##
::adb shell dumpstate > qc-log-%date_num%/dumpstate.txt
::@echo ##
::adb shell procrank > qc-log-%date_num%/procrank.txt
::@echo ##
::adb shell vmstat 1 50 > qc-log-%date_num%/vmstat.txt
::@echo ##
::adb shell top -t -d 2 -n 5 > qc-log-%date_num%/top.txt
::@echo ##
::adb shell service list > qc-log-%date_num%/serviceList.txt
@echo ##
adb shell bugreport > qc-log-%date_num%/bugreport.txt
::@echo ##
::adb shell ps -t -p > qc-log-%date_num%/ps.txt


@echo ##
@echo ## dump prop info
adb shell getprop > qc-log-%date_num%/prop.txt

@echo ##
@echo ## dump anr log
adb pull /data/anr qc-log-%date_num%/anr

@echo ##
@echo ## dump dropbox log
adb pull /data/system/dropbox qc-log-%date_num%/dropbox

@echo ##
@echo ## dump tombstones log
adb pull /data/tombstones qc-log-%date_num%/tombstones

@echo ##
@echo ## dump bugreport
adb bugreport qc-log-%date_num%/bugreport.zip

@echo ##
@echo ## done.

move qc-log-%date_num% %cd%/logs
pause