import re
from pathlib import Path


'''
This program reads in a file and searches for imperial system units and
adds the corresponding metric units.

For example: If the original file has the sentence "John is 5 feet 7 inches tall and lives 6 miles away."
That sentence will be changed to "John is 5 feet 7 inches (1.7 meters) tall and lives 6 miles (9.7 kilometers) away." in the new file.
'''

while True:
    try:
        filename = input("Enter a filename: ")
        with open(filename) as fo:
            text = fo.read()
    except FileNotFoundError:
        print("No such file")
        continue
    else:
        break


m_k_pattern = r"(?P<mi>[0-9]+)(?P<wd>\smiles)"
compiled_m_k = re.compile(m_k_pattern)

f_m_i_pattern = r"(?P<me>[0-9]+)(?P<wd2>\s+f(ee)?(oo)?t\s+(?P<in>[0-9]{1,2})(?P<wd3>\sinches\s))"
compiled_f_m_i = re.compile(f_m_i_pattern)


f_m_pattern = r"(?P<me2>[0-9]+)(?P<wd3>\s+fe?e?t\s+(?![0-9]+))"
compiled_f_m = re.compile(f_m_pattern)

i_m_pattern = r"(?<!\sfeet\s)(?P<in2>[0-9]+)(?P<wd4>\s+inches\s+(?!\(\d))"
compiled_i_m = re.compile(i_m_pattern)


def compute_kilo(orig):
    return round(int(orig) * 1.609344,1)

def add_kilo(match_obj):
    new_number = compute_kilo(match_obj.group('mi'))
    return(match_obj.group('mi') + match_obj.group('wd') + " (" + str(new_number) + " kilometers)"  )

def compute_meter_inches(orig):
    return round(int(orig) * 0.0254,1)

def add_meter_inches(match_obj):
    new_group = (int(match_obj.group('me')) * 12) + int(match_obj.group('in'))
    new_meter_inches = compute_meter_inches(new_group)
    return(match_obj.group('me') + match_obj.group('wd2')    + "(" + str(new_meter_inches) + " meters) "  )

def compute_meter(orig):
    return round(int(orig) * 0.3048,1)

def add_meter_only(match_obj):
    new_meter = compute_meter(match_obj.group('me2'))
    return(match_obj.group('me2') + match_obj.group('wd3') + "(" + str(new_meter) + " meters) "  )

def add_inches_only(match_obj):
    new_inches = compute_meter_inches(match_obj.group('in2'))
    return(match_obj.group('in2') + match_obj.group('wd4')    + "(" + str(new_inches) + " meters) "  )



nt = compiled_m_k.sub(add_kilo,text)
text = nt
ni = compiled_i_m.sub(add_inches_only,text)
text = ni
nmi = compiled_f_m_i.sub(add_meter_inches,text)
text = nmi
nm = compiled_f_m.sub(add_meter_only,text)
text = nm


new_file = Path(filename).stem + "_revised.txt"

with open(new_file , "w") as f:
    f.write(text)
