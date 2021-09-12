import sqlite3
mv = sqlite3.connect(movies.db)
c= mv.cursor()
movie_list = [('INCEPTION','LEONARDO DICAPRIO','MARION COTILLARD','2010','CHRISTOPHER NOLAN'),
              ('SPIDER-MAN','TOBEY MAGUIRE','KIRSTEN DUNST','2002','SAM RAIMI'),
              ('MEMENTO','GUY PEARCE','CARRIE-ANNE MOSS','2000','CHRISTOPHER NOLAN'),
              ('I, ROBOT','WILL SMITH','BRIDGET MOYNAHAN','2004','ALEX PROYAS'),
              ('THE HANGOVER','BRADLEY COOPER','HEATHER GRAHAM','2009','TODD PHILLIPS'),
              ('MISSION: IMPOSSIBLE - FALLOUT','TOM CRUISE','REBECCA FERGUSON','2018','CHRISTOPHER MCQUARRIE'),
              ('JURASSIC PARK','SAM NEILL','LAURA DERN','1993','STEVEN SPIELBERG'),
              ('VENOM','TOM HARDY','MICHELLE WILLIAMS','2018','RUBEN FLEISCHER'),
              ]

c.executemany( """INSERT INTO movies VALUES(?,?,?,?,?,?)""",movie_list)
mv.commit()
mv.close