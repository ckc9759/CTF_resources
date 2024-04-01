import sys

# Define key codes based on other conversion tables
KEY_CODES = {
    0x04: 'a', 0x05: 'b', 0x06: 'c', 0x07: 'd', 0x08: 'e', 
    0x09: 'f', 0x0A: 'g', 0x0B: 'h', 0x0C: 'i', 0x0D: 'j', 
    0x0E: 'k', 0x0F: 'l', 0x10: 'm', 0x11: 'n', 0x12: 'o', 
    0x13: 'p', 0x14: 'q', 0x15: 'r', 0x16: 's', 0x17: 't', 
    0x18: 'u', 0x19: 'v', 0x1A: 'w', 0x1B: 'x', 0x1C: 'y', 
    0x1D: 'z', 0x1E: '1', 0x1F: '2', 0x20: '3', 0x21: '4', 
    0x22: '5', 0x23: '6', 0x24: '7', 0x25: '8', 0x26: '9', 
    0x27: '0', 0x28: '\n', 0x29: 'esc', 0x2a: 'backspace', 
    0x2b: '\t', 0x2C: ' ', 0x2D: '-', 0x2E: '=', 0x2F: '[', 
    0x30: ']', 0x32: '#', 0x33: ';', 0x34: '\'', 0x36: ',', 
    0x37: '.', 0x38: '/', 0x39: 'capslock', 0x4f: 'right', 
    0x50: 'left', 0x51: 'down', 0x52: 'up'
}
def parse_keystrokes(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    output = []
    prev_chord = None
    backspace_count = 0

    for line in lines:
        parts = line.strip().split(':')
        key_codes = list(filter(None, parts))[2:]
        key_codes = [int(x, 16) for x in key_codes if int(x, 16) != 0]

        chord = [KEY_CODES.get(code, '') for code in key_codes]
        chord_str = ''.join(chord)

        if chord_str == 'backspace':
            backspace_count += 1
        else:
            if backspace_count > 0:
                output.append(f"back{backspace_count}")
                backspace_count = 0

            if chord_str != prev_chord:
                output.append(chord_str)
                prev_chord = chord_str

    return ' '.join(filter(None, output))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    result = parse_keystrokes(file_path)
    print(result.strip())
