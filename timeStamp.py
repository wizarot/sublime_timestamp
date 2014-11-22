# -*- coding: utf-8 -*-

from datetime import datetime
import re ,time
import sublime_plugin

#  Sublime Text 2 plug-in to insert TimeStamps into your file.
# Type 'now' 然后按 <tab> 转为当前时间 年-月-日 时:分:秒.
# 'tsnow' + <tab> 显示当前时间戳
# 年-月-日-时-分-秒 转为时间戳

class TimestampCommand(sublime_plugin.EventListener):
    """Expand `now`, `tsnow`
    """

    def on_query_completions(self, view, prefix, locations):
    	#patten1 匹配10为整数时间戳
        pattern1 = re.compile('^\d{10}')
        match = pattern1.match(prefix)
        #pattern2 匹配d20141220235959这样的时间字符串
        pattern2 = re.compile('^(\d{4})-(\d{1,2})-(\d{1,2})-(\d{1,2})-(\d{1,2})-(\d{1,2})')
        match2 = pattern2.match(prefix)

        if prefix in ('now'):  # 2013-06-27T23:34:00
            val = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        elif prefix in ('tsnow','timestamp'):  # 1412092800
            val = str(time.time()).split('.')[0]
        elif match:
            timeStamp = int(match.group(0))
            timeArray = time.localtime(timeStamp)
            val = time.strftime('%Y-%m-%d %H:%M:%S',timeArray)
        elif match2:
            timeStr = match2.group(1) + '-' + match2.group(2) + '-' + match2.group(3) +' ' + match2.group(4)+ ':' + match2.group(5)+ ':' + match2.group(6)
            timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
            val = str(time.mktime(timeArray)).split('.')[0]
        else:
            val = None

        return [(prefix, prefix, val)] if val else []
