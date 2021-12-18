from openpyxl import *
from openpyxl.styles.colors import *
from openpyxl.styles.alignment import *
from openpyxl.styles import *
from openpyxl.utils import *
from pyshorteners import *
from Scraper.Constants import *
from pathlib import Path
from pyshorteners.exceptions import ShorteningErrorException

shortener = Shortener()
expStringLi = []
eduStringLi = []
expTempString = ""
eduTempString = ""
downloadsPath = str(Path.home() / "Downloads")