from project import new_track, open_track, add_row, convert_track

import pytest

""" def test_new_track():
    name = "joan"
    patology = "fever"
    temp = "38.5"
    medicine = "ibuprofen"
    dosis = "150"

    assert new_track(name, patology, temp, medicine, dosis) == None

    temp = "44.5"

    with pytest.raises(ValueError):
        new_track(name, patology, temp, medicine, dosis)


def test_open_track():
    f = "joan_16-07-2022.csv"

    assert open_track(f) == [
        {'Name': 'joan', 'Patology': 'fever', 'Date': '16-07-2022',
        'Hour': '04:09', 'Temperature': '38.5', 'Medicine': 'ibu', 'Dosis': '150'},
        {'Name': '', 'Patology': '', 'Date': '16-07-2022',
        'Hour': '04:11', 'Temperature': '38.5', 'Medicine': '', 'Dosis': ''}
        ]


def test_add_row():
    f = "joan_16-07-2022.csv"
    temp = "38.5"
    medicine = "ibuprofen"
    dosis = "150"

    assert add_row(f, temp, medicine, dosis) == None

    temp = "44.5"

    with pytest.raises(ValueError):
        add_row(f,temp, medicine, dosis) """


def test_convert_track():
    f = "joan_16-07-2022.csv"

    assert convert_track(f) == None