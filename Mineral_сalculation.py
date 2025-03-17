import dash
from dash import dcc, html, Input, Output, State
import base64
from PIL import Image
import io
import requests

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Функция для расчета общей стоимости
def calculate_office_salary(num_workers, avg_salary, office_price):
    total_salary = num_workers * avg_salary
    total_office_salary = total_salary + office_price
    return total_salary, total_office_salary

# Функция для расчета стоимости добычи
def extraction_cost(quarry_name, mineral_type, tonnage, extraction_dates, num_workers, work_type, equipment, total_salary, total_office_salary):
    extraction_cost = 0

    # Вид полезного ископаемого
    if "буровой станок" in equipment:
        extraction_cost += 500000
    if "экскаваторы" in equipment:
        extraction_cost += 200000
    if "откатанные машины" in equipment:
        extraction_cost += 100000
    if "конвейер" in equipment:
        extraction_cost += 50000
    if "шахтные подъемники" in equipment:
        extraction_cost += 500000

    # Вид работ
    if work_type == "поиск-розыскные работы":
        extraction_cost += 100000
    if work_type == "добыча полезных ископаемых в карьере":
        extraction_cost += 300000
    if work_type == "добыча полезных ископаемых в шахте":
        extraction_cost += 500000

    # Сумма зарплаты и цены офиса
    extraction_cost += total_salary + total_office_salary

    return extraction_cost

# Загружаем изображение для отображения в приложении
def encode_image(image_url):
    # Скачиваем изображение из интернета
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))  # Открываем изображение как байты
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='PNG')
    return base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

# Преобразование изображений в base64 для использования в приложении
image_data = encode_image("https://raw.githubusercontent.com/AleksandraBabkina/Mineral_calculation/main/Mineral.jpg")

# Создаем layout приложения
app.layout = html.Div([
    html.H1("Calculation of the extraction cost of mineral mass"),

    dcc.Textarea(
        id='quarry_name',
        value="Company Name - LLC 'Landshaft', TIN - 6168107763, OGRN - 1196196028742, Legal address - 344091, Rostov Region, Rostov-on-Don, Kashirskaya st., 9/53a, office 321",
        style={'width': '100%'},
    ),

    html.Div([
        html.Div([
            html.Img(src='data:image/png;base64,{}'.format(image_data), style={'width': '100%'}),
        ], style={'width': '50%'}),
        html.Div([
            dcc.Dropdown(
                id='mineral_type',
                options=[
                    {'label': 'Gravel', 'value': 'gravel'},
                    {'label': 'Limestone', 'value': 'limestone'},
                    {'label': 'Sandstone', 'value': 'sandstone'}
                ],
                value='sandstone',
                style={'width': '100%'}
            ),
            dcc.Input(
                id='tonnage',
                type='number',
                value=100,
                placeholder='Amount of extracted mineral in tons',
                style={'width': '100%'}
            ),
            dcc.RadioItems(
                id='work_type',
                options=[
                    {'label': 'Exploration works', 'value': 'exploration works'},
                    {'label': 'Extraction in quarry', 'value': 'extraction in quarry'},
                    {'label': 'Extraction in mine', 'value': 'extraction in mine'}
                ],
                value='exploration works',
                style={'width': '100%'}
            ),
            dcc.DatePickerRange(
                id='extraction_dates',
                start_date='2025-03-17',
                end_date='2025-03-23',
                display_format='YYYY-MM-DD',
                style={'width': '100%'}
            ),
            dcc.Input(
                id='office_price',
                type='text',
                value='100000',
                placeholder='Office rent cost',
                style={'width': '100%'}
            )
        ], style={'width': '50%'}),
    ], style={'display': 'flex'}),

    html.Div([
        dcc.Slider(
            id='num_workers',
            min=0,
            max=1000,
            step=1,
            value=20,
            marks={i: str(i) for i in range(0, 1001, 100)},
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider-style'
        ),
        dcc.Slider(
            id='avg_salary',
            min=10000,
            max=300000,
            step=1000,
            value=70000,
            marks={i: str(i) for i in range(10000, 300001, 50000)},
            tooltip={"placement": "bottom", "always_visible": True},
            className='slider-style'
        ),
        dcc.Checklist(
            id='equipment',
            options=[
                {'label': 'Drilling rig', 'value': 'drilling rig'},
                {'label': 'Excavators', 'value': 'excavators'},
                {'label': 'Haulage vehicles', 'value': 'haulage vehicles'},
                {'label': 'Conveyor', 'value': 'conveyor'},
                {'label': 'Mine lifts', 'value': 'mine lifts'}
            ],
            value=['drilling rig'],
            style={'width': '100%'}
        )
    ]),

    html.Div([
        html.Button('Recalculate Price', id='calculateBtn', style={'width': '100%'}),
        html.Div(id='result')
    ]),

    html.H6("Note! All metrics are recalculated automatically when changed, except 'Number of workers', 'Average salary of workers', and 'Office rent cost'. Click 'Recalculate Price' to get the final amount after adjusting the metrics.")
])

# Event handler
@app.callback(
    Output('result', 'children'),
    Input('calculateBtn', 'n_clicks'),
    State('quarry_name', 'value'),
    State('mineral_type', 'value'),
    State('tonnage', 'value'),
    State('extraction_dates', 'start_date'),
    State('work_type', 'value'),
    State('equipment', 'value'),
    State('num_workers', 'value'),
    State('avg_salary', 'value'),
    State('office_price', 'value')
)
def update_result(n_clicks, quarry_name, mineral_type, tonnage, extraction_dates, work_type, equipment, num_workers, avg_salary, office_price):
    if n_clicks is None:
        return ''
    office_price = float(office_price)
    total_salary, total_office_salary = calculate_office_salary(num_workers, avg_salary, office_price)
    total_cost = extraction_cost(quarry_name, mineral_type, tonnage, extraction_dates, num_workers, work_type, equipment, total_salary, total_office_salary)
    return f"Extraction cost of the mineral mass: {total_cost} rub."

# Start the server
if __name__ == '__main__':
    app.run_server(debug=True)
