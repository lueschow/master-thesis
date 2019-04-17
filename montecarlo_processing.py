from collection import Collection
from text import Text
import json
import os, random
import multiprocessing
import time
import csv
import gc
import config as cfg


counter = 1
NUM_PROCESSES = 8
processes = []

listdir = os.listdir(cfg.JSON_PATH)

# files that should be skipped can be specified here
# otherwise all files from JSON_PATH are used
filtered_files = set()



def run(identifier):
    filenames = []
    collection = Collection()
    entropies = []
    spellings = []

    start = time.time()
    while True:
        new_filename = random.choice(listdir)
        if new_filename in filenames or new_filename in filtered_files:
            continue
        
        else:

            with open(cfg.JSON_PATH + new_filename, 'r') as readFile:

                text = Text.fromJson(readFile.read())
                
                collection.addText(text)
                
                entropies.append(collection.entropy())
                spellings.append(collection.spellings_count_entropy())

                filenames.append(new_filename)
                
                
                if collection.spellings_count_entropy() >= 10000000: # abort criterion
                    with open(cfg.OUTPUT_PATH + 'montecarlo_thread_%s.csv' % identifier, 'a') as writeFile:
                        writer = csv.writer(writeFile)
                        for i in range(0, len(entropies)): 
                            writer.writerow([spellings[i], entropies[i]])
                    break
    end = time.time()
    return [identifier, (end - start)]

if __name__ == "__main__":
    # Start a Pool with 8 processes
    pool = multiprocessing.Pool(processes=NUM_PROCESSES)
    jobs = []
    for j in range(0, 1000): # number of iterations
        jobs.append(j)

    for res in pool.imap_unordered(run, jobs):
        print "%s: %s" % (res[0], res[1])

    # Safely terminate the pool
    pool.close()
    pool.join()