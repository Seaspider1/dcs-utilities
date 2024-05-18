from pathlib import Path
import re
import os

def parse_assets(lua_file, score=0):
    with open(Path(lua_file)) as fid:
        txt = fid.read()

    # Use regex to extract names
    start_str = 'ShapeName	 =   "'
    end_str = '",'

    pattern = f'{start_str}(.*?){end_str}'

    matches = re.findall(pattern, txt)

    dict_out = {key.lower(): score for key in matches}

    return dict_out

if __name__ == "__main__":

    lua_file = Path(os.environ['USERPROFILE']) / "Saved Games/DCS.openbeta/Mods/tech/Massun92-Asset Pack/Database/db_M92_Assets.lua"

    output = parse_assets(lua_file)

    print(("{" + "\n    ".join("{!r}: {!r},".format(k, v) for k, v in output.items()) + "}").replace("'", '"'))