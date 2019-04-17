from text import Text
import glob
import json
import config as cfg
counter = 0


    
for filename in glob.glob(cfg.XML_PATH + '*.xml'):
    
    print('reading: ' + filename)
    text = Text(filename = filename)
    text.read()
    
    new_filename = filename[len(cfg.XML_PATH):-8] # removes the original path and the .tcf.xml-suffix
    with open(cfg.JSON_PATH + new_filename + '.json', 'w') as outfile:
        outfile.write(text.toJson())

    counter += 1
    print('file done: ' + str(counter))