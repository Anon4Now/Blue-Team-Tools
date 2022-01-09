from url_decoder import URLDefenseDecoder
from tkinter_gui import DecoderGUIInput, DecoderGUIOutput

if __name__ == '__main__':
    # Instantiate Objects
    decoderInput = DecoderGUIInput()
    decoderOutput = DecoderGUIOutput()
    defenseDecoder = URLDefenseDecoder()

    # Start the tkinter GUI
    result = decoderInput.binding()

    # Attempt to decode the users input/display output
    try:
        output = defenseDecoder.decode(result)
        decoderOutput.displayResult(output)
    except ValueError as e:
        decoderOutput.displayResult(e)
