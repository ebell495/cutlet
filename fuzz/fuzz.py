#!/bin/python3
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
    barray = bytearray(data)
    if len(barray) > 0:
        if barray[0] % 5 == 0:
            del barray[0]
            katsu.romaji(str(barray))
        elif barray[0] % 5 == 1:
            del barray[0]
            kunrei.romaji(str(barray))
        elif barray[0] % 5 == 2:
            del barray[0]
            nihon.romaji(str(barray))
        elif barray[0] % 5 == 3:
            del barray[0]
            nippon.romaji(str(barray))
        else:
            del barray[0]
            hepburn.romaji(str(barray))
    else:
        katsu.romaji(str(barray))

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()