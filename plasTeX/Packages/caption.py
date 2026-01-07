"""
The longtable and caption packages add a command \caption*, which produces a caption with no title or reference number, and \captionof, which 

This empty file caption.py exists to prevent plasTeX loading the LaTeX caption package when these packages are used.
"""

from plasTeX.Base.LaTeX.Floats import Caption

class captionof(Caption):
    args = '* float:str self'
