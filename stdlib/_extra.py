# For libhelp command because it's not working on main file

def stdlibhelp():
  import stdlib.__init__
  help(stdlib)
  
