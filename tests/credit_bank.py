def test_credit_bank(rolf):
    # ���������� body ���������
    request_body_calculation = Calculation.get_random_calculation(rolf)  # ������������ json body ��� �������� ���������
    print(request_body_calculation)

    # ����� �������� �������� ��������� '[additional_service][isn]' �� �������� �� ����� "calculation_test_data.json"
    for param in (calculation_test_data['credit_bank']):
        request_body_calculation['credit']['bank']['isn'] = param

        print("\n" + "�������� ������ : " + str(request_body_calculation['credit']['bank']['isn']))

        # ��������� ������� ��������� �������, ��� ����� ������ � �������� � ��������� ������ 400, StatusCode.ERROR_CODE.value
        calculation = CalculationClientApi(rolf).create_calculation(request_body_calculation, 400, StatusCode.ERROR_CODE.value)


        # ���������
        if param == "":
            assert_calculation_error_text(calculation, 210678,
                                          f'�� ������ ���� ��� credit = True')
        elif type(param) == int:
            assert_calculation_error_text(calculation, 210674,
                                          f'���������� ��������[{param}] �������� [credit.bank.isn] �� �������� ���������� ��������� �������� "���� ��������"')
        else:
            assert_calculation_error_text(calculation, 210671, f'���������� ��������[{param}] ��������[credit.bank.isn] �� �������� �������� ������!')
        request_body_calculation['credit']['bank']['isn'] = param


    # �������� ��� ���� �������� �� �������
    # ���������� ���������� �������� ��� isn �����
    request_body_calculation['credit']['bank']['isn'] = 625561
    # ����� ����� �������� ��� ���� �������� �������
    param = "test"
    request_body_calculation['credit']['agreement']['date'] = param

    print("\n" + "�������� ������ : " + str(request_body_calculation['credit']['agreement']['date']))

    # ��������� ������� ��������� �������, ��� ����� ������ � �������� � ��������� ������ 400, StatusCode.ERROR_CODE.value
    calculation = CalculationClientApi(rolf).create_calculation(request_body_calculation, 400, StatusCode.ERROR_CODE.value)

    # ���������
    assert_calculation_error_text(calculation, 60000,
                                       f'������ ����������� � ���������[{param}]. ���������� ������ �� ��������. ������� ���������� � ���. ���������!')
    assert_calculation_error_text(calculation, 210677,
                                  f'��������[{param}] ��������[credit.bank.agreement.date] �� �������� �������� �����!', count=1)