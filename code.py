import pandas as pd
import plotly.graph_objects as go
import os, requests
import config


file_xls = requests.get(config.url_site)
df = pd.read_excel('Mobilchips.xls')

def file_load():
    if (requests.head(config.url_site).headers['Content-Length']) != os.path.getsize('Mobilchips.xls'):
        with open("Mobilchips.xls", "wb") as code:
            code.write(file_xls.content)
        df = pd.read_excel('Mobilchips.xls')
        return df


def main_code(model, item_name):
    file_load()

    for i in df.columns:
        if i == 'Наименование' or i =='Спецификация':
            df[i] = df[i].str.upper()
    tmp = df[['Наименование', 'Спецификация', 'Цена']][(df['Спецификация'].str.contains(model).fillna(False))  & (df['Группа'] == item_name) | (df['Наименование'].str.contains(model).fillna(False))  & (df['Группа'] == item_name)]


    #blankIndex = [''] * len(tmp)
    #tmp.index = blankIndex


    tmp_len = len(tmp.index)
    values = tmp.transpose()

    if tmp_len != 0:
        #check_id = True
        fig = go.Figure(data=[go.Table(
            columnorder=[1, 2, 3],
            columnwidth=[800, 800, 220],
            header=dict(
                values=[['<b>НАИМЕНОВАНИЕ</b>'], ['<b>ОПИСАНИЕ</b>'],
                        ['<b>ЦЕНА</b><br>в у.е']],
                line_color='darkslategray',
                fill_color='royalblue',
                align=['center', 'center', 'center'],
                font=dict(color='white', size=12),
                height=40
            ),
            cells=dict(
                values=values,
                line_color='darkslategray',
                fill=dict(color=['white', 'white', 'paleturquoise']),
                align=['left', 'left', 'left'],
                font_size=8,
                height=18)
        )
        ], layout=go.Layout(height=600, width=1000))
        #fig.update_layout(width=fig.width, height=fig.height)
        fig.write_image("table_plotly.png", width=1000, height=600, scale=2)

        #return fig
        return tmp_len
    else:
        return tmp_len
