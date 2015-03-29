import scraperwiki
import os

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
print "dogs"
if 'MORPH_SECRET' in os.environ:
  print 'MORPH_SECRET' in os.environ
if 'MORPH_SECRETz'in os.environ:
  print "hmm"
print os.environ
