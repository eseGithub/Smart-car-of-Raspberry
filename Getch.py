def Getch():
    def _GetchUnix():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def _GetchWindows():
        import msvcrt
        return msvcrt.getch()

    try:
        impl = _GetchWindows()
    except ImportError:
        impl = _GetchUnix()
    return impl