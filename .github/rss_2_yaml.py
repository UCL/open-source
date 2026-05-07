from argparse import ArgumentParser
import hashlib
from pathlib import Path

import feedparser
import yaml

def grab_funding(output_dir="_data/"):
    """
    Queries CURIOSS RSS feed and creates a yaml file for jekyll to consume.

    Jekyll expect the data files under the `_data` directory.
    """
    output_dir = Path(output_dir)
    h = hashlib.new('sha256')
    feed = feedparser.parse("https://curioss.org/resources/funding-opportunities/index.xml")

    output_dict = dict()

    for entry in feed['entries']:
        h.update(entry['title'].encode())
        output_dict[h.hexdigest()] = {
            'title': entry['title'],
            'url': entry['link'],
            'description': entry['description'].replace('$', '\\$'),
        }

    with open(output_dir/'funding.yaml', 'w') as f:
        yaml.dump(output_dict, stream=f)

if __name__ == '__main__':
   parser = ArgumentParser(description="Grab and generates a yaml file for Jekyll")
   parser.add_argument('--outdir', '-o', default='_data',
                       help='The directory where to save the file')
   arguments= parser.parse_args()
   grab_funding(output_dir=arguments.outdir)
