import plotly.graph_objects as go

fig = go.Figure(data=go.Bar(
                                x=['Bob', 'Boba', 'Boban'],
                                y=[17, 18, 21])
                )

fig.write_html('first_figure.html', auto_open=True)


