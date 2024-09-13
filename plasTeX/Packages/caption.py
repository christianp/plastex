# Dummy package to prevent plasTeX from loading the LaTeX version.

from plasTeX.Base.LaTeX.Floats import Caption

class captionof(Caption):
    args = '* float:str self'
