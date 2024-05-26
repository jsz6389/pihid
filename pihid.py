#!/usr/bin/env python3
from enum import Enum
import time


class key(Enum):
    NULL = '\x00'
    ERRORROLLOVER = '\x01'
    POSTFAIL = '\x02'
    ERRORUNDEFINED = '\x03'
    A = '\x04'
    B = '\x05'
    C = '\x06'
    D = '\x07'
    E = '\x08'
    F = '\x09'
    G = '\x0A'
    H = '\x0B'
    I = '\x0C'
    J = '\x0D'
    K = '\x0E'
    L = '\x0F'
    M = '\x10'
    N = '\x11'
    O = '\x12'
    P = '\x13'
    Q = '\x14'
    R = '\x15'
    S = '\x16'
    T = '\x17'
    U = '\x18'
    V = '\x19'
    W = '\x1A'
    X = '\x1B'
    Y = '\x1C'
    Z = '\x1D'
    ONE = '\x1E'
    TWO = '\x1F'
    THREE = '\x20'
    FOUR = '\x21'
    FIVE = '\x22'
    SIX = '\x23'
    SEVEN = '\x24'
    EIGHT = '\x25'
    NINE = '\x26'
    ZERO = '\x27'
    ENTER = '\x28'
    ESCAPE = '\x29'
    DELETE = '\x2A'
    TAB = '\x2B'
    SPACE = '\x2C'
    DASH = '\x2D'
    EQUAL = '\x2E'
    LEFT_SQUARE_BRACKET = '\x2F'
    RIGHT_SQUARE_BRACKET = '\x30'
    BACK_SLASH = '\x31'
    POUND = '\x32'
    SEMICOLON = '\x33'
    QUOTE = '\x34'
    TILDE = '\x35'
    COMMA = '\x36'
    PERIOD = '\x37'
    FORWARD_SLASH = '\x38'
    CAPS_LOCK = '\x39'
    F1 = '\x3A'
    F2 = '\x3B'
    F3 = '\x3C'
    F4 = '\x3D'
    F5 = '\x3E'
    F6 = '\x3F'
    F7 = '\x40'
    F8 = '\x41'
    F9 = '\x42'
    F10 = '\x43'
    F11 = '\x44'
    F12 = '\x45'
    PRINTSCREEN = '\x46'
    SCROLL_LOCK = '\x47'
    PAUSE = '\x48'
    INSERT = '\x49'
    HOME = '\x4A'
    PAGUP = '\x4B'
    DELETE_FORWARD = '\x4C'
    END = '\x4D'
    PAGEDOWN = '\x4E'
    RIGHTARROW = '\x4F'
    LEFTARROW = '\x50'
    DOWNARROW = '\x51'
    UPARROW = '\x52'
    KEYPAD_NUM_LOCK = '\x53'
    KEYPAD_FORWARD_SLASH = '\x54'
    KEYPAD_STAR = '\x55'
    KEYPAD_MINUS = '\x56'
    KEYPAD_PLUS = '\x57'
    KEYPAD_ENTER = '\x58'
    KEYPAD_ONE = '\x59'
    KEYPAD_TWO = '\x5A'
    KEYPAD_THREE = '\x5B'
    KEYPAD_FOUR = '\x5C'
    KEYPAD_FIVE = '\x5D'
    KEYPAD_SIX = '\x5E'
    KEYPAD_SEVEN = '\x5F'
    KEYPAD_EIGHT = '\x60'
    KEYPAD_NINE = '\x61'
    KEYPAD_ZERO = '\x62'
    KEYPAD_PERIOD = '\x63'
    NON_US_BACKSLASH = '\x64'
    APPLICATION = '\x65'
    POWER = '\x66'
    KEYPAD_EQUALS = '\x67'
    F13 = '\x68'
    F14 = '\x69'
    F15 = '\x6A'
    F16 = '\x6B'
    F17 = '\x6C'
    F18 = '\x6D'
    F19 = '\x6E'
    F20 = '\x6F'
    F21 = '\x70'
    F22 = '\x71'
    F23 = '\x72'
    F24 = '\x73'
    EXECUTE = '\x74'
    HELP = '\x75'
    MENU = '\x76'
    SELECT = '\x77'
    STOP = '\x78'
    AGAIN = '\x79'
    UNDO = '\x7A'
    CUT = '\x7B'
    COPY = '\x7C'
    PASTE = '\x7D'
    FIND = '\x7E'
    MUTE = '\x7F'
    VOLUME_UP = '\x80'
    VOLUME_DOWN = '\x81'
    LOCKING_CAPS_LOCK = '\x82'
    LOCKING_NUM_LOCK = '\x83'
    LOCKING_SCROLL_LOCK = '\x84'
    KEYPAD_COMMA = '\x85'
    KEYPAD_EQUAL_SIGN = '\x86'
    INTERNATIONAL1 = '\x87'
    INTERNATIONAL2 = '\x88'
    INTERNATIONAL3 = '\x89'
    INTERNATIONAL4 = '\x8A'
    INTERNATIONAL5 = '\x8B'
    INTERNATIONAL6 = '\x8C'
    INTERNATIONAL7 = '\x8D'
    INTERNATIONAL8 = '\x8E'
    INTERNATIONAL9 = '\x8F'
    LANG1 = '\x90'
    LANG2 = '\x91'
    LANG3 = '\x92'
    LANG4 = '\x93'
    LANG5 = '\x94'
    LANG6 = '\x95'
    LANG7 = '\x96'
    LANG8 = '\x97'
    LANG9 = '\x98'
    ALTERNATE_ERASE = '\x99'
    SYSREQ = '\x9A'
    CANCEL = '\x9B'
    CLEAR = '\x9C'
    PRIOR = '\x9D'
    RETURN = '\x9E'
    SEPARATOR = '\x9F'
    OUT = '\xA0'
    OPER = '\xA1'
    CLEAR_AGAIN = '\xA2'
    CRSEL = '\xA3'
    EXSEL = '\xA4'
    KEYPAD_00 = '\xB0'
    KEYPAD_000 = '\xB1'
    THOUSANDS_SEPARATOR = '\xB2'
    DECIMAL_SEPARATOR = '\xB3'
    CURRENCY_UNIT = '\xB4'
    CURRENCY_SUBUNIT = '\xB5'
    KEYPAD_LEFT_PARANTHESES = '\xB6'
    KEYPAD_RIGHT_PARANTHESES = '\xB7'
    KEYPAD_LEFT_CURLY_BRACKET = '\xB8'
    KEYPAD_RIGHT_CURLY_BRACKET = '\xB9'
    KEYPAD_TAB = '\xBA'
    KEYPAD_BACKSPACE = '\xBB'
    KEYPAD_A = '\xBC'
    KEYPAD_B = '\xBD'
    KEYPAD_C = '\xBE'
    KEYPAD_D = '\xBF'
    KEYPAD_E = '\xC0'
    KEYPAD_F = '\xC1'
    KEYPAD_XOR = '\xC2'
    KEYPAD_POWER = '\xC3'
    KEYPAD_PERCENT = '\xC4'
    KEYPAD_LESS_THAN = '\xC5'
    KEYPAD_GREATER_THAN = '\xC6'
    KEYPAD_AMPERSAND = '\xC7'
    KEYPAD_DOUBLE_AMPERSAND = '\xC8'
    KEYPAD_PIPE = '\xC9'
    KEYPAD_DOUBLE_PIPE = '\xCA'
    KEYPAD_COLON = '\xCB'
    KEYPAD_POUND = '\xCC'
    KEYPAD_SPACE = '\xCD'
    KEYPAD_AT = '\xCE'
    KEYPAD_EXCLAMATION_POINT = '\xCF'
    KEYPAD_MEMORY_STORE = '\xD0'
    KEYPAD_MEMORY_RECALL = '\xD1'
    KEYPAD_MEMORY_CLEAR = '\xD2'
    KEYPAD_MEMORY_ADD = '\xD3'
    KEYPAD_MEMORY_SUBSTRACT = '\xD4'
    KEYPAD_MEMORY_MULTIPLY = '\xD5'
    KEYPAD_MEMORY_DIVIDE = '\xD6'
    KEYPAD_PLUS_MINUS = '\xD7'
    KEYPAD_CLEAR = '\xD8'
    KEYPAD_CLEAR_ENTRY = '\xD9'
    KEYPAD_BINARY = '\xDA'
    KEYPAD_OCTAL = '\xDB'
    KEYPAD_DECIMAL = '\xDC'
    KEYPAD_HEXADECIMAL = '\xDD'
    LEFTCONTROL = '\xE0'
    LEFTSHIFT = '\xE1'
    LEFTALT = '\xE2'
    LEFT_GUI = '\xE3'
    WIN = '\xE3'
    RIGHTCONTROL = '\xE4'
    RIGHTSHIFT = '\xE5'
    RIGHTALT = '\xE6'
    RIGHT_GUI = '\xE7'


class mod(Enum):
    LEFT_GUI = '\x08'
    LEFT_WIN = '\x08'
    RIGHT_GUI = '\x80'
    RIGHT_WIN = '\x80'
    LEFT_CONTROL = '\x01'
    RIGHT_CONTROL = '\x10'
    LEFT_SHIFT = '\x02'
    RIGHT_SHIFT = '\x20'
    LEFT_ALT = '\x04'
    RIGHT_ALT = '\x40'


keymap = {
    '`':[key.TILDE],
    '~':[mod.LEFT_SHIFT,key.TILDE],
    '1':[key.ONE],
    '!':[mod.LEFT_SHIFT,key.ONE],
    '2':[key.TWO],
    '@':[mod.LEFT_SHIFT,key.TWO],
    '3':[key.THREE],
    '#':[mod.LEFT_SHIFT,key.THREE],
    '4':[key.FOUR],
    '$':[mod.LEFT_SHIFT,key.FOUR],
    '5':[key.FIVE],
    '%':[mod.LEFT_SHIFT,key.FIVE],
    '6':[key.SIX],
    '^':[mod.LEFT_SHIFT,key.SIX],
    '7':[key.SEVEN],
    '&':[mod.LEFT_SHIFT,key.SEVEN],
    '8':[key.EIGHT],
    '*':[mod.LEFT_SHIFT,key.EIGHT],
    '9':[key.NINE],
    '(':[mod.LEFT_SHIFT,key.NINE],
    '0':[key.ZERO],
    ')':[mod.LEFT_SHIFT,key.ZERO],
    '-':[key.DASH],
    '_':[mod.LEFT_SHIFT,key.DASH],
    '=':[key.EQUAL],
    '+':[mod.LEFT_SHIFT,key.EQUAL],
    '[':[key.LEFT_SQUARE_BRACKET],
    '{':[mod.LEFT_SHIFT,key.LEFT_SQUARE_BRACKET],
    ']':[key.RIGHT_SQUARE_BRACKET],
    '}':[mod.LEFT_SHIFT,key.RIGHT_SQUARE_BRACKET],
    '\\':[key.BACK_SLASH],
    '|':[mod.LEFT_SHIFT,key.BACK_SLASH],
    ';':[key.SEMICOLON],
    ':':[mod.LEFT_SHIFT,key.SEMICOLON],
    "'":[key.QUOTE],
    '"':[mod.LEFT_SHIFT,key.QUOTE],
    ',':[key.COMMA],
    '<':[mod.LEFT_SHIFT,key.COMMA],
    '.':[key.PERIOD],
    '>':[mod.LEFT_SHIFT,key.PERIOD],
    '/':[key.FORWARD_SLASH],
    '?':[mod.LEFT_SHIFT,key.FORWARD_SLASH],
    'a':[key.A],
    'A':[mod.LEFT_SHIFT,key.A],
    'b':[key.B],
    'B':[mod.LEFT_SHIFT,key.B],
    'c':[key.C],
    'C':[mod.LEFT_SHIFT,key.C],
    'd':[key.D],
    'D':[mod.LEFT_SHIFT,key.D],
    'e':[key.E],
    'E':[mod.LEFT_SHIFT,key.E],
    'f':[key.F],
    'F':[mod.LEFT_SHIFT,key.F],
    'g':[key.G],
    'G':[mod.LEFT_SHIFT,key.G],
    'h':[key.H],
    'H':[mod.LEFT_SHIFT,key.H],
    'i':[key.I],
    'I':[mod.LEFT_SHIFT,key.I],
    'j':[key.J],
    'J':[mod.LEFT_SHIFT,key.J],
    'k':[key.K],
    'K':[mod.LEFT_SHIFT,key.K],
    'l':[key.L],
    'L':[mod.LEFT_SHIFT,key.L],
    'm':[key.M],
    'M':[mod.LEFT_SHIFT,key.M],
    'n':[key.N],
    'N':[mod.LEFT_SHIFT,key.N],
    'o':[key.O],
    'O':[mod.LEFT_SHIFT,key.O],
    'p':[key.P],
    'P':[mod.LEFT_SHIFT,key.P],
    'q':[key.Q],
    'Q':[mod.LEFT_SHIFT,key.Q],
    'r':[key.R],
    'R':[mod.LEFT_SHIFT,key.R],
    's':[key.S],
    'S':[mod.LEFT_SHIFT,key.S],
    't':[key.T],
    'T':[mod.LEFT_SHIFT,key.T],
    'u':[key.U],
    'U':[mod.LEFT_SHIFT,key.U],
    'v':[key.V],
    'V':[mod.LEFT_SHIFT,key.V],
    'w':[key.W],
    'W':[mod.LEFT_SHIFT,key.W],
    'x':[key.X],
    'X':[mod.LEFT_SHIFT,key.X],
    'y':[key.Y],
    'Y':[mod.LEFT_SHIFT,key.Y],
    'z':[key.Z],
    'Z':[mod.LEFT_SHIFT,key.Z],
    ' ':[key.SPACE]
    # TODO Generate complete keymap for string conversions
    }


# Write raw data to the hid device
def write_report(report):
    for c in report:
        print(hex(ord(c)),'',end='')
    print()
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


def write_single(k):
    match k:
        case mod():
            write_report(k.value+key.NULL.value*7) # modifier keys are written to the first byte of the hid report
        case key():
            write_report(key.NULL.value*2+k.value+key.NULL.value*5) # modifier keys are written to the third byte of the hid report


# TODO Test this function
def write_list(l):
    m = '\x00' # modifier
    ks = [] # list of keys to place in the HID report
    # NOTE HID reports can contain a maximum of 6 key presses, not counting modifiers
    for k in l:
        match k:
            case mod():
                m = chr(ord(m)|ord(k.value)) # update the modifier byte with the new modifier
            case key():
                ks.append(k.value)

    report = m+key.NULL.value+''.join(ks)+key.NULL.value*(6-len(ks)) # Build the final hid report
    write_report(report)


def write_string(s,delay):
    for c in s:
        write_list(keymap[c])
        write_single(key.NULL)
        time.sleep(delay)


# Determine the type of the argument and pass it to the proper helper function
def write(hid_input,delay=0):
    match hid_input:
        case str(): # If the user passes a string
            write_string(hid_input,delay)
        case list(): # If the user passes a list of keys
            write_list(hid_input)
        case key(): # If the user passes a single key from the key enum
            write_single(hid_input)
        case mod():
            write_single(hid_input)

    # release all keys
    write_report(key.NULL.value*8)


def main():
    # Test all strings
    # write('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG~!@#$%^&*()_+{}|:"<>?') 
    # write("the quick brown fox jumps over the lazy dog`1234567890-=[]\;',./")

    write(mod.LEFT_WIN) # Press the windows key
    time.sleep(0.2)
    write('notepad',delay=0.05)# Type 'notepad' to the keyboard
    time.sleep(0.2)
    write(key.ENTER) # Press the enter key to open notepad
    time.sleep(0.3)
    write([mod.LEFT_CONTROL,key.N]) # Create a new document
    time.sleep(0.2)
    write('Hello world!') # Document contents
    write([mod.LEFT_CONTROL,key.S]) # Saving the document
    time.sleep(0.2)
    write('hello.txt') # naming the document
    time.sleep(0.2)
    write(key.ENTER)


if __name__=='__main__':
    main()


