import scraperwiki
import os

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
print "dogs"
if 'MORPH_SECRET' in os.environ:
  print os.environ['MORPH_SECRET']
if 'MORPH_SECRETz'in os.environ:
  print "hmm"
