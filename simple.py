from ssl import Options
from typing import Text
import justpy as jp
from justpy.chartcomponents import HighCharts
from justpy.htmlcomponents import Option
from pandas.core.dtypes.common import classes
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: true
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""
def app():
    webPage = jp.QuasarPage()
    Head = jp.QDiv(a=webPage,text="A analysis of course review",classes="text-h3 text-center q-pa-md")
    Foot = jp.QDiv(a=webPage,text="Those graphs respresent course review analysis")
    Hc = jp.HighCharts(a=webPage,options = chart_def)
    Hc.options.title.text = "Average by rating"
    Hc.options.series[0].data = [[0,12],[45,60]]
    
    return webPage

jp.justpy(app)