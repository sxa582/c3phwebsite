#!/usr/bin/env python3
"""Validate generated pages, local assets, navigation, and fragment targets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://sxa582.github.io/c3phwebsite/'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.tags=[]; self.feed(text)
    def handle_starttag(self, tag, attrs): self.tags.append((tag,dict(attrs)))

pages={path.name:Page(path.read_text()) for path in ROOT.glob('*.html')}
errors=[]; refs=0
for name,p in pages.items():
    ids=[attrs['id'] for _,attrs in p.tags if 'id' in attrs]
    duplicates=[key for key,n in Counter(ids).items() if n>1]
    if duplicates: errors.append(f'{name}: duplicate IDs {duplicates}')
    if sum(tag=='h1' for tag,_ in p.tags)!=1: errors.append(f'{name}: needs one h1')
    if not any(tag=='meta' and attrs.get('name')=='description' and attrs.get('content') for tag,attrs in p.tags): errors.append(f'{name}: missing description')
    if not any(tag=='button' and attrs.get('aria-controls')=='site-nav' for tag,attrs in p.tags): errors.append(f'{name}: missing mobile menu')
    if not any(tag=='link' and attrs.get('rel')=='canonical' for tag,attrs in p.tags): errors.append(f'{name}: missing canonical')
    if not any(tag=='main' and attrs.get('id')=='main' for tag,attrs in p.tags): errors.append(f'{name}: missing main landmark')
    for tag,attrs in p.tags:
        if tag=='img' and ('alt' not in attrs or 'width' not in attrs or 'height' not in attrs): errors.append(f'{name}: image missing alt or dimensions')
        if tag=='a' and attrs.get('target')=='_blank' and 'noopener' not in attrs.get('rel',''): errors.append(f'{name}: external target lacks noopener')
        for key in ('href','src'):
            if key not in attrs: continue
            value=attrs[key]
            if value.startswith(BASE): value=value[len(BASE):]
            u=urlsplit(value)
            if u.scheme or u.netloc: continue
            target=unquote(u.path) or name
            refs+=1
            file=ROOT/target
            if not file.is_file(): errors.append(f'{name}: missing local target {target}')
            if u.fragment and target in pages:
                targets={a.get('id') for _,a in pages[target].tags}
                if unquote(u.fragment) not in targets: errors.append(f'{name}: missing fragment {target}#{u.fragment}')
        if tag=='img' and attrs.get('src','').endswith('.gif'): errors.append(f'{name}: heavyweight GIF still referenced')
data=json.loads((ROOT/'content/site.json').read_text())
if len(data['team'])!=16: errors.append('Expected 16 preserved team profiles')
if len(data['publications'])!=15: errors.append('Expected 15 preserved publications')
if len(data['patents'])!=8 or not all(p.get('record') for p in data['patents']): errors.append('Expected eight linked patent records')
for name in ('site.css','site.js','discovery.svg','social-card.png','c3ph-heart-orange.png'):
    if not (ROOT/'assets'/name).is_file(): errors.append(f'Missing shared asset {name}')
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print(f'PASS: {len(pages)} pages, {refs} local references, fragments, shared menus, metadata, images, and preserved records.')
