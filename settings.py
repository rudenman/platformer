import platform


def get_screen_size():
    system = platform.system()

    if system == "Windows":
        import ctypes
        user = ctypes.windll.user32
        screen_width = user.GetSystemMetrics(0)
        screen_height = user.GetSystemMetrics(1)

    elif system == "Darwin":  # macOS
        import Quartz
        main_monitor = Quartz.CGDisplayBounds(Quartz.CGMainDisplayID())
        screen_width = int(main_monitor.size.width)
        screen_height = int(main_monitor.size.height)

    else:
        raise NotImplementedError(f"Unsupported operating system: {system}")

    return screen_width, screen_height


window_width, window_height = get_screen_size()

tile_size = window_width / 30
player_size = tile_size / 8 * 6
enemy_size = tile_size / 4

menu_font_size = window_height // 10
status_font_size = window_height // 20
calc_font_size = window_height // 60 * 4
edu_font1_size = window_height // 60 * 4
edu_font2_size = window_height // 20

object_speed = window_width / 235  # 8
enemy_speed = window_width / 380  # 5

gravity = window_height / 1350
jump_speed = window_height / 49

#

map_width = 30  # * 5
map_height = 17

#########################################

map_background = [
    "                              ",
    "                              ",
    "   S                      S   ",
    "                              ",
    "                              ",
    "                              ",
    "   S                      S   ",
    "                              ",
    "                              ",
    "                              ",
    "   S                      S   ",
    "                              ",
    "                              ",
    "                              ",
    "   S                      S   ",
    "                              ",
    "                              ",
]

# new
map_start = [
    "                              ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X S SX S S XX SS XX S SXS S SX",
    "XSXXXXXXSXXXSXXXXSXSXX XXX XXX",
    "X S SXXX XXX S  S X S SXXXSXXX",
    "XXXX XXXSXXXSXXXXSXS XXXXX XXX",
    "XXXXSXXX XXX XXXX X XSXXXXSXXX",
    "XS S XXXSXXXSXXXXSXSXXSXXX XXX",
    "XXXXXXXXXXSXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXX  SXX               ",
    "XS S S S S   SX               ",
    "XXXXXXXXXX  SXXP              ",
    "XXXXXXXXXXSXXXXXXXXXXX        ",
    "XXXXXXXXXXXXXXXXXXXXXXXXX     ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

# new
map_end = [
    "                              ",
    "XXXXXXXXXXXXXXXXXXXXXXXX      ",
    "XXXXXXXXXXXXXXXXXXXXXXXX      ",
    "XXS SXSXSXXSXSXS SXSXSXX      ",
    "XX XXX X XX X X XXX X XX      ",
    "XXSSXXSXSSXSXSXS SXSSSXX      ",
    "XX XXX X XS X XXX X X XX      ",
    "XXSXXXSXSXXSXSXS SXSXSXX      ",
    "XXXXXXXXXXXXXXXXXXXXXXXX      ",
    "XXXXXXXXXXXXXXXXXXXXXXXX      ",
    "                       X      ",
    "                       X      ",
    "                       X      ",
    "             F         X      ",
    "             X         X      ",
    "XXXXXXXXXXXXXXXXXXXXXXXX      ",
    "XXXXXXXXXXXXXXXXXXXXXXXX      ",
]

# new
map1 = [
    "                              ",
    "                   XXXXXXXXXX ",
    "                   X   V      ",
    "                   X          ",
    "                   X      X   ",
    "              V    X      X   ",
    "                   X      X   ",
    "                   XXX V  X   ",
    "         V                X   ",
    "    V               V     X   ",
    "           XX             X   ",
    "                         XX   ",
    "                          X   ",
    "      XX                  X   ",
    "                      XXXXX   ",
    "XXX             XXX       XXXX",
    "XXX                        XXX",
]

# new
map2 = [
    "                              ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX ",
    "X                      X    X ",
    "X                      X    X ",
    "X                      X  X X ",
    "X   X  H     H         X  X X ",
    "X V XXXXXXXXXXXXXXXXX  XX X   ",
    "X   X                  X  X   ",
    "XX  X                  X  X   ",
    "X   X V    H           X  X   ",
    "X   X   XXXXXXXXXXXXXXXX XX   ",
    "X   X   X   H    H        X   ",
    "   XX   X  X  X  X  X  X  X   ",
    "    X   X XX  X XX  X XX  X   ",
    "    X   X  X  X  X  X  XX X   ",
    "XXXXX      X     X     X  X XX",
    "XXXXXXXXXXXXXXXXXXXXXXXX  X XX",
]

# new
map3 = [
    "                              ",
    "                              ",
    "              XXXX            ",
    "                 X            ",
    "                 X            ",
    "                 X            ",
    "          H      X            ",
    "               X X            ",
    "               X              ",
    "               X              ",
    "               X              ",
    "              XX              ",
    "               X              ",
    "               X              ",
    "  H     H      XH     H       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

# new
map4 = [
    "                              ",
    "                              ",
    "                              ",
    "                      V       ",
    "                      V       ",
    "                      V       ",
    "                      V       ",
    "                      V       ",
    "  V  VV  VVVVVVVVV    V       ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "   X   X          X           ",
    "XXXXXXXXXXXXXXXXXXXX     XXXXX",
    "XXXXXXXXXXXXXXXXXXXX     XXXXX",
]

# new
map5 = [
    "                              ",
    "                              ",
    "                  VV   X      ",
    "                       X      ",
    "         VV            X      ",
    "                       X      ",
    "      VV   H         VV   X   ",
    "           XXXXXXX        X   ",
    "                        VVX   ",
    "        X           X     X   ",
    "    V                         ",
    "                              ",
    "     X                 X      ",
    "                              ",
    "   X                      X   ",
    "XXX                        XXX",
    "XXX                        XXX",
]

map6 = [
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "   VVVVVVVVVVVVVVVVVVVVVVVV   ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "     H      H      H          ",
    "    XXXX XXXXX   XXXXX XXX    ",
    "   XXXXXXXXXXXXXXXXXXXXXXXX   ",
    "  X                        X  ",
    "XX                          XX",
    "XX                          XX",
]

map7 = [
    "                              ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X     X                   VV  ",
    "X V X X   V                   ",
    "X  XX X   V                   ",
    "X   X X   V                   ",
    "X   X X   V  X    X    X      ",
    "X V X X   V             X     ",
    "XX  X X                  X    ",
    "X   X  XXX                X   ",
    "X   X                      X  ",
    "X   X                      X  ",
    "X  XX      X               X  ",
    "    X                      X  ",
    "    XH                     X  ",
    "XXXXX  XXX                  XX",
    "XX                          XX",
]

map8 = [
    "                              ",
    "          XXXXXXXXX           ",
    "                  X           ",
    "                  X           ",
    "         X     V  X           ",
    "        X VVVXX   X           ",
    "        X     X  XX           ",
    "         X    X               ",
    "         X    X               ",
    "        X    X                ",
    "        X    X                ",
    "         X    XX   H          ",
    "              X    XXXXXXX    ",
    "              X               ",
    "  HH         XX               ",
    "XXXXXXXXXX                  XX",
    "XX                          XX",
]

map9 = [
    "                              ",
    "           VXXXXX             ",
    "       V        X             ",
    "                X             ",
    "           V    X             ",
    "             X  X             ",
    "   V   V     X  X             ",
    "             X  X    VVV      ",
    "         X   X  XVV           ",
    "             X  X             ",
    "   V        X  X              ",
    "     X     X  X               ",
    "          X  X           X    ",
    "         X  X                 ",
    "        X  X   X    X         ",
    "XX     XXH                  XX",
    "XX     XXXXXXXXX            XX",
]

map10 = [
    "                              ",
    "         XXXXXXXXXXXXX V      ",
    "           V   X   V   V      ",
    "           V   X   V   V      ",
    "      V    V   X   V   V      ",
    "      V    V   X   V   V      ",
    "      V    VX  X  XV   V      ",
    "      V     X  X  X    V      ",
    "      V     X  X XX    V      ",
    "      V X   X  X  X  X V      ",
    "      V     X  X  X    V      ",
    "            X  X  X           ",
    "    X       X  XX X      X    ",
    "            X  X  X           ",
    "            X     X           ",
    "XX          XXXXXXX         XX",
    "XX                          XX",
]

map_parts = [map1, map2, map3, map4, map5, map6, map7, map8, map9, map10]
