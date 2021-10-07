# импортируем библиотеки для проекта
from fpdf import FPDF
def report(report_measuring):
     # формируем словарь вопросов для приемки оборудования, референсных значений и промежуточных заголовков отчета
    report_headers={'date': ['Дата осмотра оборудования','',''],
                            'type': ['Наименование оборудования','',''],
                            'serial': ['Серийный номер оборудования','',''],
                            # 'Q0': ['Наличие фото оборудования','',''],
                            'Q1': ['Интерактивная панель со встроенным вычислительным блоком','Да','Да','В Н Е Ш Н И Й   В И Д'],
                            'Q2': ['Наличие слота на корпусе для установки дополнительного вычислительного блока, который содержит контакты электропитания системного блока от встроенного блока питания моноблока, контакты для подключения цифрового видеосигнала','Да','Да'],
                            'Q3': ['Наличие встроенной акустической системы','Да','Да'],
                            'Q4': ['Введите количество встроенных громкоговорителей','≥2',2],
                            'Q5': ['Имеются функциональные кнопки на корпусе на лицевой (обращенной к пользователю при работе с экраном) или сенсорной панели: включение / выключение устройства, уменьшение громкости, вызов экранного меню, выбор источника для отображения','Да','Да'],
                            'Q6': ['Введите количество HDMI входов на лицевой панели для подключения внешних устройств','≥1',1],
                            'Q7': ['Введите количество HDMI выходов дополнительного вычислительного блока','≥1',1],
                            'Q8': ['Введите количество портов USB 3.0','≥1',1],
                            'Q9': ['Введите количество портов USB 2.0 дополнительного вычислительного блока','≥2',2],
                            'Q10': ['Введите количество выходов аудиосигнала','≥1',1],
                            'Q11': ['Введите расстояние по горизонтали между крепежными отверстиями для установки моноблока на крепление (мм)','≥600',600,'Х А Р А К Т Е Р И С Т И К И'],
                            'Q12': ['Введите расстояние по вертикали между крепежными отверстиями для установки моноблока на крепление (мм','≥400',400],
                            'Q13': ['Введите базовую тактовую частоту процессора (ГГц)','≥2',2],
                            'Q14': ['Введите количество ядер процессора','≥6',6],
                            'Q15': ['Введите количество потоков процессора','≥6',6],
                            'Q16': ['Введите базовую частоту графической системы (МГц)','≥350',350],
                            'Q17': ['Введите версию оперативной памяти DDR дополнительного вычислительного блока','≥4',4],
                            'Q18': ['Введите частоту оперативной памяти встраиваемого системного блока (МГц)','≥2400',2400],
                            'Q19': ['Введите объем оперативной памяти встроенного вычислительного блока (Гбайт)','≥8',8],
                            'Q20': ['Введите объем накопителя встроенного вычислительного блока (Гбайт)','≥250',250],
                            'Q21': ['Наличие твердотельного накопителя','Да','Да'],
                            'Q22': ['Введите максимальную скорость чтения внутреннего накопителя встраиваемого системного блока (Мбайт/с)','≥2600',2600],
                            'Q23': ['Введите максимальную скорость записи внутреннего накопителя встраиваемого системного блока (Мбайт/с)','≥950',950],
                            'Q24': ['Есть возможность удаленного управления и мониторинга через RS-232','Да','Да'],
                            'Q25': ['Введите поддерживаемую скорость передачи данных на сетевом интерфейсе для подключения дополнительных устройств (режим сетевого коммутатора, в Гбитах/с)','≥1',1],
                            'Q26': ['Есть возможность подключения к сети Ethernet проводным способом','Да','Да'],
                            'Q27': ['Порт для пульта дистанционного управления с возможностью отключения и включения данного порта через RS-232, Ethernet','Да','Да'],
                            'Q28': ['Есть возможность удаленного управления и мониторинга через Ethernet','Да','Да'],
                            'Q29': ['Система охлаждения: вентилятор присутствует только в системном блоке','Да','Да'],
                            'Q30': ['Введите Размер диагонали экрана (Дюйм)','≥85 ≤90',[85,90],'Э К Р А Н'],
                            'Q31': ['Поддерживается разрешение 3840х2160 пикселей (при 60 Гц)','Да','Да'],
                            'Q32': ['Аспектное соотношение сторон экрана: 16:9','Да','Да'],
                            'Q33': ['Тип подсветки экрана: прямая светодиодная','Да','Да'],
                            'Q34': ['Частота обновления экрана при работе от системного блока, установленного в специализированный слот на корпусе моноблока (в Гц)','≥60',60],
                            'Q35': ['Наличие антибликового защитного стекла','Да','Да'],
                            'Q36': ['Наличие интегрированного датчика освещенности для автоматической коррекции яркости подсветки','Да','Да'],
                            'Q37': ['Введите Количество точек касания','≥10',10],
                            'Q38': ['Моноблок поставляется с предварительно откалиброванным экраном','Да','Да'],
                            'Q39': ['Имеются встроенные функции распознавания объектов касания','Да','Да'],
                            'Q40': ['Имеется возможность игнорирования касаний экрана ладонью','Да','Да'],
                            'Q41': ['Имеется возможность использования ладони в качестве инструмента стирания','Да','Да','П Р О Г Р А М М Н О Е   О Б Е С П Е Ч Е Н И Е'],
                            'Q42': ['Операционная система: Microsoft Windows 10 Профессиональная 64-разрядная (требуется для совместимости с используемым ПО и АИС','Да','Да'],
                            'Q43': ['При наличии встроенной операционной системы Android, в ней должны быть заблокированы функции: доступа к рабочему столу данной операционной системы, установки и изменения состава приложений, расширенных настроек операционной системы, отображения экранов мобильных устройств','Да','Да'],
                            'Q44': ['Предустановленное прикладное программное обеспечение должно автоматически запускаться при включении моноблока и блокировать непосредственный доступ пользователей к полному функционалу операционной системы','Да','Да'],
                            'Q45': ['Возможность авторизации пользователей в прикладном программном обеспечении с использованием LDAP каталогов пользователей','Да','Да'],
                            'Q46': ['Возможность ограничения доступа к функциям прикладного программного обеспечения в зависимости от прав пользователя по ролям, определенным службой каталогов','Да','Да'],
                            'Q47': ['Вызов меню расширенных настроек моноблока должен быть доступен только для авторизованных пользователей, в зависимости от прав пользователя по ролям, определенным службой каталогов','Да','Да'],
                            'Q48': ['Встроенная функция создания и сохранения графических пометок поверх произвольных приложений во всех режимах работы прикладного программного обеспечения','Да','Да'],
                            'Q49': ['Возможность для авторизованных пользователей, обладающих правами администратора, управления доступностью установленных приложений в интерфейсе прикладного программного обеспечения','Да','Да'],
                            'Q50': ['Возможность для авторизованных пользователей, обладающих соответствующими правами, выбора источника из подключенных к портам ввода моноблока для отображения на экране','Да','Да'],
                            'Q51': ['Возможность отключения для неавторизованных пользователей функции управления выбором источника для отображения на экране','Да','Да'],
                            'Q52': ['Возможность для авторизованных пользователей, обладающих соответствующими правами, выбора режима работы подсветки экрана (автоматической регулировки яркости либо автоматического уменьшения яркости подсветки экрана при работе с ним) как через графический интерфейс прикладного программного обеспечения, так и удаленно через RS-232, Ethernet','Да','Да'],
                            'Q53': ['Интегрированная функция сбора сведений о состоянии аппаратной части моноблока (из доступных в спецификации протокола управления) и действиях пользователей (в виде журнала выполненных операций)','Да','Да'],
                            'Q54': ['Минимальный набор поддерживаемых встроенными средствами просмотра форматов файлов изображений: .odi, .oti, .png, .jpeg, .bmp','Да','Да'],
                            'Q55': ['Минимальный набор поддерживаемых встроенными средствами просмотра форматов файлов видео: .avi, .mp4','Да','Да'],
                            'Q56': ['Минимальный набор поддерживаемых встроенными средствами просмотра текстовых форматов файлов: .odt, .ott, .txt, .rtf, .doc, .docx','Да','Да'],
                            'Q57': ['Минимальный набор поддерживаемых встроенными средствами просмотра форматов файлов электронных таблиц: .odc, .ots, .xls, xlsx','Да','Да'],
                            'Q58': ['Минимальный набор поддерживаемых встроенными средствами просмотра форматов файлов презентаций: .odp, .otp, .ppt, .pptx','Да','Да'],
                            'Q59': ['Возможность создания индивидуальных для каждого моноблока профилей взаимного расположения на экране элементов интерфейса прикладного программного обеспечения','Да','Да'],
                            'Q60': ['Наличие прикладного программного интерфейса (API) для разработки дополнительных модулей прикладного программного обеспечения и интеграции сторонних приложений в части централизованного мониторинга и обновления','Да','Да'],
                            'Q61': ['API должно предоставляет следующий функционал взаимодействия со сторонними приложениями: в части централизованного мониторинга - предоставление сведений о состоянии аппаратной части моноблока и текущем режиме работы (в том числе о текущем режиме работы подсветки экрана, активном/неактивном состоянии порта для пульта дистанционного управления, состоянии и параметрах системного блока, серийных номерах моноблока, сенсора), действиях пользователей (выполненных операциях в предустановленном прикладном программном обеспечении, запущенных приложениях, времени работы приложений) с привязкой к каждому конкретному пользователю','Да','Да'],
                            'Q62': ['API должно предоставляет следующий функционал взаимодействия со сторонними приложениями: в части централизованного обновления - скачивания и установки обновлений при поступлении внешней управляющей команды, с подтверждением ее исполнения, в следующих режимах: стандартный (установка выполняется при участии пользователя, сведения о состоянии установки выводятся), автоматический режим (установка выполняется автоматически, без участия пользователя, сведения о состоянии установки выводятся), тихий режим (выполняется без участия пользователя, без вывода сведений о состоянии установки), отложенный режим (позволяет пользователю отложить установку обновления до окончания сеанса работы)','Да','Да'],
                            'text':'* Осмотр проведен по представленным характеристикам без использования специального оборудования и лабораторных условий.',
                            'signature':['Дата','Подпись','ФИО специалиста, проводившего осмотр']}

    # формируем массив ключей
    keys=['date', 'serial', 'Q1', 'Q2','Q3', 'Q4', 'Q5','Q6','Q7','Q8',
                                    'Q9', 'Q10', 'Q11', 'Q12', 'Q13','Q14', 'Q15', 'Q16', 'Q17', 'Q18',
                                    'Q19', 'Q20', 'Q21', 'Q22', 'Q23','Q24', 'Q25', 'Q26', 'Q27', 'Q28',
                                    'Q29', 'Q30', 'Q31', 'Q32', 'Q33','Q34', 'Q35', 'Q36', 'Q37', 'Q38',
                                    'Q39', 'Q40', 'Q41', 'Q42', 'Q43','Q44', 'Q45', 'Q46', 'Q47', 'Q48',
                                    'Q49', 'Q50', 'Q51', 'Q52', 'Q53','Q54', 'Q55', 'Q56', 'Q57', 'Q58',
                                    'Q59', 'Q60', 'Q61', 'Q62']
    # формируем массив ключей текстовых данных и числовых
    keys_text=['Q1','Q2','Q3','Q5','Q21','Q24','Q26', 'Q27', 'Q28','Q29', 'Q31', 'Q32',
                         'Q33', 'Q35', 'Q36', 'Q38','Q39', 'Q40', 'Q41', 'Q42', 'Q43','Q44', 'Q45',
                         'Q46', 'Q47', 'Q48','Q49', 'Q50', 'Q51', 'Q52', 'Q53','Q54', 'Q55', 'Q56',
                         'Q57', 'Q58','Q59', 'Q60', 'Q61','Q62']
    keys_number=['Q4','Q6','Q7','Q8','Q9', 'Q10', 'Q11', 'Q12', 'Q13','Q14','Q15', 'Q16',
                             'Q17', 'Q18', 'Q19', 'Q20', 'Q22', 'Q23','Q25', 'Q34','Q37']

    # создаем объект формата pdf
    pdf = FPDF()

    # добавляем страницу и кириллические шрифты
    pdf.add_page()
    pdf.add_font("DejaVu",'', "DejaVuSansMono.ttf", uni=True)
    pdf.add_font("DejaVuB",'', "DejaVuSansMono-Bold.ttf", uni=True)


    # формируем заголовок отчета
    pdf.set_font("DejaVuB",size=13)
    pdf.cell(200, 5, txt='П Р О Т О К О Л',border=0,ln=1, align='C')
    pdf.set_font("DejaVuB",size=12)
    pdf.cell(200, 5, txt='осмотра оборудования № ______',border=0,ln=1, align='C')
    pdf.cell(200, 5, txt='специализированное интерактивное устройство (интерактивная панель)', border=0, ln=1, align='C')
    pdf.ln(5)

    # определяем ширину столбцов отчета
    hight_row = 3.5
    delta_column_1 = 7
    delta_column_2 = 140
    delta_column_3 = 20

    # формируем отчет построчно
    for key in keys:
        if pdf.y > 270:
            pdf.add_page()
        if key in ['Q1','Q11','Q30','Q41']:
            header_text=report_headers[key][3]
            pdf.set_font('DejaVuB', size=11)
            pdf.cell(delta_column_2+delta_column_3*2, 9.5, txt=header_text,border=0, ln=1,align='C')

        # формируем текст для заполнения
        text = [report_headers[key][0], report_headers[key][1], report_measuring[key], report_headers[key][2]]
        pdf.set_font("DejaVu", size=9)

        # определяем начальные координаты курсора документа
        x0=pdf.x
        y0=pdf.y

        # заполняем первые столбец
        if key in ['date', 'type', 'serial', 'photo']:
            pdf.cell(delta_column_3, 4, txt='', border=0, ln=0, align='L')
            pdf.cell(delta_column_3, 4, txt=str(text[1]), ln=0, border=0, align='L')
            pdf.multi_cell(delta_column_2, hight_row, txt=text[0], border=0, align='L')
        else:
            pdf.cell(delta_column_1, hight_row, txt=str(key)[1:] + '.')
            pdf.multi_cell(delta_column_2, hight_row, txt=text[0], border=0, align='L')

        # запонимаем координату курсора в конце столбца
        y1=pdf.y

        # задаем координаты перехода курсора в начало следующего столбца
        pdf.y = y0
        pdf.x = x0 + delta_column_1 + delta_column_2

        # заполняем второй столбец
        pdf.cell(delta_column_3, hight_row, txt=str(text[1]), border=0, align='C')
        pdf.y = y0
        pdf.x = x0 + delta_column_1 + delta_column_2 + delta_column_3

        # заполняем третий столбец и выделяем отклонения
        if (key in keys_text and text[2] != text[3]) or (key in keys_number and float(text[2]) < text[3]) or (key == 'Q30' and (float(text[2]) < text[3][0] or float(text[2]) > text[3][1])):
            pdf.set_draw_color(255, 0, 0)
            pdf.cell(delta_column_3, hight_row, txt=str(text[2]), border=1, align='C')
        else:
            pdf.set_draw_color(255, 255, 255)
            pdf.cell(delta_column_3, hight_row, txt=str(text[2]), border=0, align='C')
        pdf.ln(y1 - y0 + 1)

    # выноска дополнительной информации
    pdf.ln(3)
    pdf.set_font("DejaVu", size=7.5)
    pdf.cell(200, hight_row, txt=report_headers['text'], border=0, align='L')

    # подпись документа сотрудником
    pdf.ln(60)
    y = pdf.y - 0.5
    row = [30, 35, 65]
    for i in range(6):
        if i % 2 == 0:
            pdf.cell(15, hight_row, txt='', border=0, ln=0, align='C')
        else:
            pdf.set_draw_color(0, 0, 0)
            pdf.cell(row[i // 2], hight_row, txt=report_headers['signature'][i // 2], border='T', ln=0, align='C')

    pdf.output(f"reports/reportPanel-{report_measuring['serial']}.pdf")
