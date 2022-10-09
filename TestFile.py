# from openpyxl import load_workbook
#
# file = "Information.xlsx"
# wb = load_workbook(file)
# wb.active = 0
# sheet = wb.active
#
# num = 0
# for i in range(3, len(sheet['A']) + 1):
#     id = str(sheet['A' + str(i)].value)
#     area = str(sheet['B' + str(i)].value)
#     medOrganization = str(sheet['C' + str(i)].value)
#     numKard = str(sheet['D' + str(i)].value)
#     age = str(sheet['E' + str(i)].value)
#     gender = str(sheet['F' + str(i)].value)
#     dataHospital = str(sheet['G' + str(i)].value)
#     datadischarge = str(sheet['H' + str(i)].value)
#     mkb = str(sheet['I' + str(i)].value)
#     diagnosis = str(sheet['J' + str(i)].value)
#     resultHealth = str(sheet['K' + str(i)].value)
#     healtIshod = str(sheet['L' + str(i)].value)
#     typeOfAssistance = str(sheet['L' + str(i)].value)
#     resultKVI = str(sheet['L' + str(i)].value)
#     dataResultKVI = str(sheet['L' + str(i)].value)
#     if area == "Восточно-Казахстанская область":
#         num += 1
#         print(area, num)
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly import graph_objs as go
import pandas as pd
from openpyxl import load_workbook

file = "Information.xlsx"
wb = load_workbook(file)
wb.active = 0
sheet = wb.active

init_notebook_mode(connected = True)

def plotly_df(df, title = ''):
    data = []

    for column in df.columns:
        trace = go.Scatter(
            x = df.index,
            y = df[column],
            mode = 'lines',
            name = column
        )
        data.append(trace)

    layout = dict(title = title)
    fig = dict(data = data, layout = layout)
    iplot(fig, show_link=False)

# for i in range(3, len(sheet['A']) + 1):
#     dataHospital = str(sheet['G' + str(i)].value)
#     plotly_df(dataHospital, title="Data Hospitalization")

# dataset = pd.read_csv('hour_online.csv', index_col=['Time'], parse_dates=['Time'])
# plotly_df(dataHospital, title="Online users")