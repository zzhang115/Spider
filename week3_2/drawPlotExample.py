import matplotlib.pyplot as plt
import numpy as np

# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2*np.pi*t)
# plt.plot(t, s)
#
# plt.xlabel('time (s)')
# plt.ylabel('voltage (mV)')
# plt.title('About as simple as it gets, folks')
# plt.grid(True)
# plt.savefig("test.png")
# plt.show()

options = {
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': 'Monthly Average Temperature'},
    'subtitle': {'text': 'Source: WorldClimate.com'},
    'xAxis'   : {'categories': ['周一', '周二', '周三', '周四']},
    'yAxis'   : {'title': {'text': '数量'}}
    }

series = [
    {
    'name': 'OS X',
    'data': [11,2,3,4],
    'type': 'line',
    'y':5
}, {
    'name': 'Ubuntu',
    'data': [8,5,6,7],
    'type': 'line',
    'color':'#ff0066'
}, {
    'name': 'Windows',
    'data': [12,6,7,2],
    'type': 'line'
}, {
    'name': 'Others',
    'data': [29,24,68,23],
    'type': 'line'
}
         ]

# plt.plot(series, options=options)
# plt.plot
