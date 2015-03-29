import scraperwiki
import os

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
print "dogs"
if 'MORPH_SECRET' in os.environ:
  print "woop"
if 'MORPH_SECRETz'in os.environ:
  print "hmm"
