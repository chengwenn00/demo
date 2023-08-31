import glob
import os
import pandas as pd
from datetime import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.models import BasicTickFormatter, ColumnDataSource, DatetimeTickFormatter, HoverTool

PATH=r'C:\Users\keileong\Desktop\PMlogfiles\Navi 21 log files\PCS122 (card 12)'
date_today=datetime.now().strftime("%Y-%m-%d") 

df=pd.read_csv(r'C:\Users\keileong\Desktop\PMlogfiles\Navi 21 log files\PCS122 (card 12)\OUTPUT_clean.csv')
df['TimeStamp']=pd.to_datetime(df['TimeStamp'], format='%Y-%m-%d %H:%M:%S.%f')
print(df.dtypes)



graph1 = figure(title = "Maximum Socket Power",
               x_axis_type='datetime', 
               x_axis_label = "Date Time",
               y_axis_label = "Socket Power(W)",
               width = 1000)

graph2 = figure(title = "Maximum Temperature Hotspot",
               x_axis_type='datetime', 
               x_axis_label = "Date Time",
               y_axis_label = "Temperature Hotspot(deg)",
               width = 1000)

graph3 = figure(title = "Maximum Temperature Gradient(deg)",
               x_axis_type='datetime', 
               x_axis_label = "Date Time",
               y_axis_label = "Temperature Gradient",
               width = 1000)

source = ColumnDataSource(df)

graph1.line(x='TimeStamp', y='GPU0PowerTGPPower',
         source=source)
graph1.y_range.start = 0
# graph1.xaxis.formatter=DatetimeTickFormatter('%Y-%m-%d %H:%M:%S.%f')
graph1.title.text_font_size = "20pt"
graph1.axis.axis_label_text_font_size = "20pt"
graph1.axis.major_label_text_font_size = "20pt"

graph2.line(x='TimeStamp', y='GPU0TemperatureHotspot',
         source=source)
graph2.y_range.start = 0
# graph2.xaxis.formatter=BasicTickFormatter(use_scientific=False)
graph2.title.text_font_size = "20pt"
graph2.axis.axis_label_text_font_size = "20pt"
graph2.axis.major_label_text_font_size = "20pt"

graph3.line(x='TimeStamp', y='GPU0TemperatureGradientMaximumMaxToMin',
         source=source)
graph3.y_range.start = 0
# graph3.xaxis.formatter=BasicTickFormatter(use_scientific=False)
graph3.title.text_font_size = "20pt"
graph3.axis.axis_label_text_font_size = "20pt"
graph3.axis.major_label_text_font_size = "20pt"

graph1.add_tools(HoverTool(
    tooltips=[
    ('Cycle','@cyclecount{o}'),
    ('date','@TimeStamp{%F %T}'),
    ('Cycle Max Socket Power(W)','@GPU0PowerTGPPower')],
    formatters={'@TimeStamp':'datetime'},
    mode='vline'
))

graph2.add_tools(HoverTool(
    tooltips=[
    ('Cycle','@cyclecount{o}'),
    ('date','@TimeStamp{%F %T}'),
    ('Temperature Hotspot(deg)','@GPU0TemperatureHotspot')],
    formatters={'@TimeStamp':'datetime'},
    mode='vline'
))

graph3.add_tools(HoverTool(
    tooltips=[
    ('Cycle','@cyclecount{o}'),
    ('date','@TimeStamp{%F %T}'),
    ('Temperature Gradient','@GPU0TemperatureGradientMaximumMaxToMin')],
    formatters={'@TimeStamp':'datetime'},
    mode='vline'
))


output_file(os.path.join(PATH, 'NV21_PC timestamp plotting'+ date_today + '.html'), title="Power Cycling Timestamp Plot")

graph_list = [graph1, graph2, graph3]             # if you added or removed graphs, change the list accordingly

show(gridplot(graph_list, ncols=1, width=1000))