from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import sys


def fetch_author(scholar_id):
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    return author


# Google Scholar often blocks GitHub-hosted runners. Try directly with few retries,
# then through free proxies. If both fail, keep the previously published data.
scholar_id = os.environ['GOOGLE_SCHOLAR_ID']
scholarly.set_retries(2)
try:
    author: dict = fetch_author(scholar_id)
except Exception as direct_error:
    print(f'Direct fetch failed: {direct_error!r}. Retrying through free proxies.')
    try:
        proxies = ProxyGenerator()
        if not proxies.FreeProxies():
            raise RuntimeError('no working free proxy found')
        scholarly.use_proxy(proxies)
        scholarly.set_retries(5)
        author = fetch_author(scholar_id)
    except Exception as proxy_error:
        print(f'::warning::Google Scholar could not be reached ({proxy_error!r}); keeping the previous citation data.')
        sys.exit(0)

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(f"{name}: {author['citedby']} citations, {len(author['publications'])} publications")
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
