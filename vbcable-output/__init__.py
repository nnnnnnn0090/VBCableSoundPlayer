# vbcable_output/__init__.py

from .vbcable_output import vbcable_output

vbcable_output.init_player()

play = vbcable_output.play
wait = vbcable_output.wait

__version__ = "0.1.0"
__all__ = ['play', 'wait']