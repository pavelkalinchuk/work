def test_credit_bank(rolf):
    # Генерируем body котировки
    request_body_calculation = Calculation.get_random_calculation(rolf)  # генерируется json body для создания котировки
    print(request_body_calculation)

    # Далее заменяем значение параметра '[additional_service][isn]' на значения из файла "calculation_test_data.json"
    for param in (calculation_test_data['credit_bank']):
        request_body_calculation['credit']['bank']['isn'] = param

        print("\n" + "Тестовые данные : " + str(request_body_calculation['credit']['bank']['isn']))

        # Попробуем создать котировку ожидаем, что будет ошибка и передаем в параметры методы 400, StatusCode.ERROR_CODE.value
        calculation = CalculationClientApi(rolf).create_calculation(request_body_calculation, 400, StatusCode.ERROR_CODE.value)


        # Проверяем
        if param == "":
            assert_calculation_error_text(calculation, 210678,
                                          f'Не предан Банк при credit = True')
        elif type(param) == int:
            assert_calculation_error_text(calculation, 210674,
                                          f'Переданное значение[{param}] элемента [credit.bank.isn] не является допустимым значением оговорки "Банк кредитор"')
        else:
            assert_calculation_error_text(calculation, 210671, f'Переданное значение[{param}] элемента[credit.bank.isn] не является валидным Числом!')
        request_body_calculation['credit']['bank']['isn'] = param


    # Проверка для даты договора по кредиту
    # Возвращаем корректное значение для isn банка
    request_body_calculation['credit']['bank']['isn'] = 625561
    # Задаём новое значение для даты договора кредита
    param = "test"
    request_body_calculation['credit']['agreement']['date'] = param

    print("\n" + "Тестовые данные : " + str(request_body_calculation['credit']['agreement']['date']))

    # Попробуем создать котировку ожидаем, что будет ошибка и передаем в параметры методы 400, StatusCode.ERROR_CODE.value
    calculation = CalculationClientApi(rolf).create_calculation(request_body_calculation, 400, StatusCode.ERROR_CODE.value)

    # Проверяем
    assert_calculation_error_text(calculation, 60000,
                                       f'Ошибка конвертации в ДатаВремя[{param}]. Дальнейшая работа не возможна. Просьба обратиться в тех. поддержку!')
    assert_calculation_error_text(calculation, 210677,
                                  f'Значение[{param}] элемента[credit.bank.agreement.date] не является валидной Датой!', count=1)