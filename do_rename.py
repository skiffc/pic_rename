#!/usr/bin/env python
import  os
import  re
import  sys
import  exifread

for root, folders, files in os.walk( sys.argv[1]):
    if root != sys.argv[1]:
        continue
    for f in files:
        if os.path.splitext( f )[1] in ( '.db' ):
            continue
        tags = exifread.process_file( open( os.path.join( root, f), 'rb' ) )
        r = re.sub( ':', '', str(tags['EXIF DateTimeOriginal']).split()[0] ) + '_' + f 
        print f, r 
        os.rename( os.path.join( root, f), os.path.join( root, r ) )

