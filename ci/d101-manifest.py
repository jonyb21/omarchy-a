#!/usr/bin/env python3
"""Write the d101 install manifest beside the j71b one; same platform root and recovery."""
from pathlib import Path
import re
import sys

release = Path(sys.argv[1])
source = (release / 'j71b-checkm8-pongo.toml').read_text()
result = re.sub(r'(?m)^("?device"?\s*=\s*)"j71b"', r'\1"d101"', source)
if result == source:
    sys.exit('No device line in the j71b manifest')
(release / 'd101-checkm8-pongo.toml').write_text(result)
print(result)
