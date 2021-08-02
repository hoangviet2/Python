from ssl import Options
import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
data = pandas.read_csv('reviews.csv',parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_course = data.groupby(['Month','Course Name'])['Rating'].count().unstack()

chart_def = """
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""
def app():
    webPage = jp.QuasarPage()
    Head = jp.QDiv(a=webPage,text="A analysis of course review",classes="text-h3 text-center q-pa-md")
    Foot = jp.QDiv(a=webPage,text="Those graphs respresent course review analysis")
    highchart = jp.HighCharts(a=webPage,options=chart_def)
    highchart.options.xAxis.categories = list(month_average_course.index)
    #highchart.options.series[0].data = list(month_average_course['Rating'])
    highchart_data = [{"name":v1,"data":[v2 for v2 in month_average_course[v1]]}  for v1 in month_average_course.columns]
    highchart.options.series = highchart_data
    return webPage

jp.justpy(app)