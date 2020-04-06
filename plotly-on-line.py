import chart_studio

chart_studio.tools.set_credentials_file(username='tereshchenko.igor', api_key='1n8yuJXEUn51pPnR3ecW')


import plotly.graph_objects as go

import chart_studio.plotly as py


trace0 = go.Scatter(

    x = [1,2,3,4],
    y = [1,4,9,16]
)

trace1 = go.Scatter(

    x=[1, 2, 3, 4],
    y=[1, 8, 27, 256]
)


data = [trace0, trace1]

py.plot(data, auto_open= True, filename='test')


