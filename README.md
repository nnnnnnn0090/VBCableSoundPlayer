# vbcable_output

This package outputs audio to the VBCable virtual audio device.   
https://vb-audio.com/Cable/

## Installation

You can install the package using pip:

```
pip install vbcable_output
```

## Usage
```python
import vbcable_output

vbcable_output.play(data, rate)
vbcable_output.wait()
```

## Parameters
    data: The audio data you want to play.
    rate: The sample rate of the audio.

## License
MIT License. See the LICENSE file for details.