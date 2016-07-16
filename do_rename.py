#!/usr/bin/env python
import  os
import  re
import  sys
import  exifread

fail = []

for root, folders, files in os.walk( sys.argv[1]):
    if root != sys.argv[1]:
        continue
    for f in files:
        if os.path.splitext( f )[1] in ( '.db' ):
            continue
        if re.search( '^20\d{6}$', f.split('_')[0] ):
            s = f.split('_')
            continue

        tags = exifread.process_file( open( os.path.join( root, f), 'rb' ) )
        try:
            r = re.sub( ':', '', str(tags['EXIF DateTimeOriginal']).split()[0] ) + '_' + f 
            print f, r 
            os.rename( os.path.join( root, f), os.path.join( root, r ) )
        except:
            print '[ERROR]', f
            for t in tags:
                if 'DateTime' in t:
                    print '  - tag:', t, '->', tags[t]
            print tags.keys()
             
            fail.append( f )

if fail:
    print 'FAIL:'
    for p in fail:
        print p
   
