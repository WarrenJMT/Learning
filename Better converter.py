import PySimpleGUI as sg

layout = [
    [sg.Input(key='-INPUT-'), sg.Spin(['lb to kg', 'km to mile', 'sec to min'], key='-UNITS-'),
     sg.Button('Convert', key='-CONVERT-')],
    [sg.Text('Output', key='-OUTPUT-')]
    # [sg.Button('Clear', key='-CLEAR-')]  # do_not_clear=False)]   How to make clear button clear the input
]

window = sg.Window('Basic Converter', layout)  # Window name and layout

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km(s) is {output} mile(s).'

                    window['-OUTPUT-'].update(output_string)
                case 'lb to kg':
                    output = round(float(input_value) * .45, 2)
                    output_string = f'{input_value} lbs is {output} kgs.'

                    window['-OUTPUT-'].update(output_string)
                case 'sec to min':
                    output = round(float(input_value) / 60)
                    output_string = f'{input_value} seconds is {output} minutes.'

                    window['-OUTPUT-'].update(output_string)

window.close()

'''if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'lb to kg':
                    output = round(float(input_value) * .45, 2)
                    output_string = f'{input_value} lbs is {output} kgs.'

                    window['-OUTPUT-'].update(output_string)


    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'sec to min':
                    output = round(float(input_value) / 60)
                    output_string = f'{input_value} seconds is {output} minutes.'

                    #window['-OUTPUT-'].update(output_string)

        if event == '-CLEAR-':
        #input_value = values['-INPUT-']



window.close()'''
