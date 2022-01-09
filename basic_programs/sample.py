import pandas as pd

lst = [['sch_1', '!@sc_1', 'english math chemistry'],
       ['sch_2', '))sc_2', 'english pyhsics chemistry'],
       ['sch_3', '!@sc_2', 'maths biology'],
       ['sch_4', 'sc_2)_', 'french'],
       ['sch_5','sc_1#@', 'social_studies maths literature'],
       ['sch_6', 'sc_10#@', 'english maths history']
       ]
df = pd.DataFrame(lst, columns=['school_id', 'state_code', 'subjects'])
