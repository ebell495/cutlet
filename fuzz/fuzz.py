#!/usr/local/bin/python3
import atheris
import sys
with atheris.instrument_imports():
    import cutlet

katsu = cutlet.Cutlet()
kunrei = cutlet.Cutlet("kunrei")
nihon = cutlet.Cutlet("nihon")
nippon = cutlet.Cutlet('nippon')
hepburn = cutlet.Cutlet("hepburn")

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    if len(data) < 1:
        return

    option = fdp.ConsumeBytes(1)[0]
    in_string = fdp.ConsumeUnicodeNoSurrogates(len(data))

    if option % 5 == 0:
        katsu.romaji(in_string)
    elif option % 5 == 1:
        kunrei.romaji(in_string)
    elif option % 5 == 2:
        nihon.romaji(in_string)
    elif option % 5 == 3:
        nippon.romaji(in_string)
    else:
        hepburn.romaji(in_string)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()