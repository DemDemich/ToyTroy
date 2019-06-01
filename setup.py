
from distutils.core import setup
import py2exe
    
setup(
    windows=[{"script":"key_client.py"}],
    #options={"py2exe": {"includes":["sip"]}}
)
