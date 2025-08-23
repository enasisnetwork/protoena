


from pathlib import Path
from subprocess import run
from threading import Event
from threading import Thread
from time import time

from evdev import InputDevice
from evdev import list_devices
from evdev.ecodes import EV_KEY



CNTRLR = (
    'Sony Computer Entertainment'
    ' Wireless Controller')

SCANNING = Event()



def controller() -> None | InputDevice:
    """
    Return the device that is believed to be the controller.
    """

    devices = list_devices()

    for path in devices:

        device = InputDevice(path)

        if device.name == CNTRLR:
            return device

    return None



def scanner() -> None:
    """
    Perform the batch scanning routine outputting to folder.
    """

    PATH = Path(str(int(time())))

    PATH.mkdir()

    run(['aplay',
         'start.wav'],
        check=True)

    try:
        run(['scanimage',
             f'--batch={PATH}/%03d.pnm',
             '--format=pnm'],
            check=True)
    except:
        run(['aplay',
             'failure.wav'],
            check=True)
    else:
        run(['aplay',
             'finish.wav'],
            check=True)

    SCANNING.clear()



def execution() -> None:
    """
    Perform whatever operation is associated with the file.
    """

    device = controller()

    assert device, (
        'Is the controller'
        ' plugged in?')

    loop = device.read_loop()

    codes = {
        304: False,  # east
        308: False}  # south


    for event in loop:

        type = event.type
        code = event.code
        value = bool(event.value)
        allow = (304, 308)

        if SCANNING.is_set():
            continue

        if type != EV_KEY:
            continue

        if code not in allow:
            continue

        codes[code] = value

        if all(codes.values()):

            SCANNING.set()

            thread = Thread(
                target=scanner)

            thread.start()



if __name__ == '__main__':
    execution()
