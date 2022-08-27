""" Python string coloring.

Thank you for using pycolor!
Color codes:
  1 - Black
  2 - Red
  3 - Green
  4 - Yellow
  5 - Blue
  6 - Violet
  7 - Beige
  8 - White
  9 - Grey
  10 - Red2
  11 - Green2
  12 - Yellow2
  13 - Blue2
  14 - Violet2
  15 - Beige2
  16 - White2
  20 - Black BG
  22 - Red BG
  23 - Green BG
  24 - Yellow BG
  25 - Blue BG
  26 - Violet BG
  27 - Beige BG
  28 - White BG
  29 - Grey BG
  30 - Red2 BG
  31 - Green2 BG
  32 - Yellow2 BG
  33 - Blue2 BG
  34 - Violet2 BG
  35 - Beige2 BG
  36 - White2 BG
"""

__version__ = ("v1.0.4")


class colors:
  """ Color codes!"""
  HEADER    = '\033[95m'
  OKBLUE    = '\033[94m'
  OKCYAN    = '\033[96m'
  OKGREEN   = '\033[92m'
  WARNING   = '\033[93m'
  FAIL      = '\033[91m'
  ENDC      = '\033[0m'
  BOLD      = '\033[1m'
  UNDERLINE = '\033[4m'

  CEND      = '\33[0m'
  CBOLD     = '\33[1m'
  CITALIC   = '\33[3m'
  CURL      = '\33[4m'
  CBLINK    = '\33[5m'
  CBLINK2   = '\33[6m'
  CSELECTED = '\33[7m'

  CBLACK    = '\33[30m'
  CRED      = '\33[31m'
  CGREEN    = '\33[32m'
  CYELLOW   = '\33[33m'
  CBLUE     = '\33[34m'
  CVIOLET   = '\33[35m'
  CBEIGE    = '\33[36m'
  CWHITE    = '\33[37m'

  CBLACKBG  = '\33[40m'
  CREDBG    = '\33[41m'
  CGREENBG  = '\33[42m'
  CYELLOWBG = '\33[43m'
  CBLUEBG   = '\33[44m'
  CVIOLETBG = '\33[45m'
  CBEIGEBG  = '\33[46m'
  CWHITEBG  = '\33[47m'

  CGREY     = '\33[90m'
  CRED2     = '\33[91m'
  CGREEN2   = '\33[92m'
  CYELLOW2  = '\33[93m'
  CBLUE2    = '\33[94m'
  CVIOLET2  = '\33[95m'
  CBEIGE2   = '\33[96m'
  CWHITE2   = '\33[97m'

  CGREYBG   = '\33[100m'
  CREDBG2   = '\33[101m'
  CGREENBG2 = '\33[102m'
  CYELLOWBG2= '\33[103m'
  CBLUEBG2  = '\33[104m'
  CVIOLETBG2= '\33[105m'
  CBEIGEBG2 = '\33[106m'
  CWHITEBG2 = '\33[107m'

""" This functions is for testing logs, use can use them"""
def info(str):
  """ Shows an info"""
  print(colors.CGREY + "[INFO] - " + str + colors.CEND)

def warning(str):
  """ Shows an warning"""
  print(colors.WARNING + "[WARNING] - " + str + colors.CEND)

def error(str):
  """ Shows an error"""
  print(colors.CRED2 + "[ERROR] - " + str + colors.CEND)

def success(str):
  """ Shows an success"""
  print(colors.CGREEN2 + "[SUCCESS] - " + str + colors.CEND)

def fatal(str):
  """ Shows an fatal error"""
  print(colors.CRED + colors.CBOLD + "[FATAL ERROR] - " + str + colors.CEND)

def selected(str):
  """ Mark a string as selected"""
  print(colors.CSELECTED + str + colors.CEND)
# thank you stackoverflow.com for the color codes!