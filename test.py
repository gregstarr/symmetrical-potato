import pathlib

pin = pathlib.Path(__file__).parent / 'test.txt'
pout = pathlib.Path(__file__).parent / 'out.txt'
print(pin, pout)
pout.write_text(pin.read_text())
