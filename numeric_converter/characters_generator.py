import unicodedata


ISO_15924 = [(0x0041, 0xFF5A)] # Latin
EMOJI = [(0x1F601, 0x1F64F), (0x2702, 0x27B0), (0x1F680, 0x1F6C0)]
SPACES = ['NO-BREAK SPACE']


def generate_characters_map() -> None:
    characters_ranges = ISO_15924 + EMOJI
    characters_map = {}
    character_code = 10

    for cr in characters_ranges:
        for i in range(cr[0], cr[1] + 1):
            unicode_char_exist = unicodedata.name(chr(i), False)

            if not unicode_char_exist or unicode_char_exist in SPACES:
                continue

            characters_map[character_code] = i
            character_code += 1

    with open('src/base_character.py', "w") as f:
        f.write(f"base_map = {str(characters_map)}")


if __name__ == '__main__':
    generate_characters_map()
