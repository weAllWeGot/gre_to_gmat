import os
import pandas as pd
"""
Read data from csv and use the first column as the index
This index represents a Quant score in the GRE
The columns represent the Verbal score in the GRE
https://www.mbacrystalball.com/blog/2014/01/23/gre-to-gmat-score-conversion/
"""
TABLE_FILE_NAME = 'data_table.csv'

fullpath = os.path.join(os.path.dirname(__file__), TABLE_FILE_NAME)
score_table = pd.read_csv(fullpath, index_col=0)
score_table.columns = [int(c) for c in score_table.columns]

"""
An old implementation, i know...
"""
# one30 = [200,200,200,200,220,240,260,280,300,320,340,360,390,410,430,450,470,490,510,530,560]
# one32 = [200,200,200,210,230,250,270,290,310,330,360,380,400,420,440,460,480,500,530,550,570]
# one34 = [200,200,200,220,240,260,280,300,330,350,370,390,410,430,450,470,500,520,540,560,580]
# one36 = [200,200,210,230,250,270,300,320,340,360,380,400,420,440,470,490,510,530,550,570,590]
# one38 = [200,200,220,240,270,290,310,330,350,370,390,410,440,460,480,500,520,540,560,580,610]
# one40 = [200,220,240,260,280,300,320,340,360,390,410,430,450,470,490,510,530,560,580,600,620]
# one42 = [210,230,250,270,290,310,330,360,380,400,420,440,460,480,500,530,550,570,590,610,630]
# one44 = [220,240,260,280,300,330,350,370,390,410,430,450,470,500,520,540,560,580,600,620,640]
# one46 = [230,250,270,300,320,340,360,380,400,420,440,470,490,510,530,550,570,590,610,640,660]
# one48 = [250,270,290,310,330,350,370,390,420,440,460,480,500,520,540,560,580,610,630,650,670]
# one50 = [260,280,300,320,340,360,390,410,430,450,470,490,510,530,560,580,600,620,640,660,680]
# one52 = [270,290,310,330,360,380,400,420,440,460,480,500,530,550,570,590,610,630,650,670,700]
# one54 = [280,300,330,350,370,390,410,430,450,470,500,520,540,560,580,600,620,640,670,690,710]
# one56 = [300,320,340,360,380,400,420,440,470,490,510,530,550,570,590,610,640,660,680,700,720]
# one58 = [310,330,350,370,390,420,440,460,480,500,520,540,560,590,610,630,650,670,690,710,730]
# one60 = [320,340,360,390,410,430,450,470,490,510,530,560,580,600,620,640,660,680,700,730,750]
# one62 = [330,360,380,400,420,440,460,480,500,530,550,570,590,610,630,650,670,700,720,740,760]
# one64 = [350,370,390,410,430,450,470,500,520,540,560,580,600,620,640,670,690,710,730,750,770]
# one66 = [360,380,400,420,440,470,490,510,530,550,570,590,610,640,660,680,700,720,740,760,780]
# one68 = [370,390,420,440,460,480,500,520,540,560,590,610,630,650,670,690,710,730,760,780,800]
# one70 = [390,410,430,450,470,490,510,530,560,580,600,620,640,660,680,700,730,750,770,790,800]
# verbal_range = [one30,
# one32,
# one34,
# one36,
# one38,
# one40,
# one42,
# one44,
# one46,
# one48,
# one50,
# one52,
# one54,
# one56,
# one58,
# one60,
# one62,
# one64,
# one66,
# one68,
# one70]

# quant_verb = zip(idx,verbal_range)
# verbal_cols =  {quant_score:vrange[0:21] for quant_score,vrange in quant_verb}
# z = pd.DataFrame(verbal_cols,index=idx)
