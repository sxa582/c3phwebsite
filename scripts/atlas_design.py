"""Editorial homepage and original code-native visual assets for C3PH."""
from html import escape
from pathlib import Path
import math
import random

def render_home(data, link, head, cta):
    projects=data['projects']
    def url(p): return 'project-'+p['id']+'.html'
    lead=projects[1]
    side=[projects[0],projects[2]]
    rows=''.join(f'''<article class="research-brief"><div class="brief-number">0{i+2}</div><div><span class="label">{escape(p['topic'])}</span><h3><a href="{url(p)}">{escape(p['title'])}</a></h3><p>{escape(p['summary'])}</p>{link(url(p),'Inside the research')}</div><a class="brief-art" href="{url(p)}" aria-hidden="true" tabindex="-1"><img src="assets/{p['art']}.svg" alt="" width="600" height="320" loading="lazy"></a></article>''' for i,p in enumerate(side))
    programs=''.join(f'''<details class="program-disclosure" {'open' if i==0 else ''}><summary><span class="program-index">0{i+1}</span><span>{escape(title)}</span><span class="disclosure-icon" aria-hidden="true"></span></summary><div class="program-content"><p>{escape(desc)}</p>{link('focus-areas.html#'+pid,'Explore this program')}</div></details>''' for i,(pid,title,desc,_) in enumerate(data['programs']))
    people=''.join(f'''<article class="director"><a href="team.html#{person['name'].split(',')[0].lower().replace(' ','-')}" tabindex="-1" aria-hidden="true"><img src="{person['image']}" width="400" height="460" alt="" loading="lazy"></a><span class="label">{escape(person['role'])}</span><h3><a href="team.html#{person['name'].split(',')[0].lower().replace(' ','-')}">{escape(person['name'])}</a></h3></article>''' for person in data['team'][:2])
    publications=''.join(f'''<article class="record-row"><span class="record-year">{p['year']}</span><div><span class="label">{escape(p['journal'])}</span><h3><a href="{p['url']}" target="_blank" rel="noopener noreferrer">{escape(p['title'])}</a></h3></div><a class="record-arrow" href="{p['url']}" target="_blank" rel="noopener noreferrer" aria-label="Read {escape(p['title'])} on PubMed">↗</a></article>''' for p in [data['publications'][6],data['publications'][8],data['publications'][0]])
    return f'''
<section class="atlas-hero" aria-labelledby="hero-title"><div class="wrap hero-editorial"><div class="hero-copy"><span class="eyebrow">The science of seeing more</span><h1 id="hero-title">A new view<br>of <span>prevention.</span></h1><p>Human health is written in many signals.<br>We bring them together.</p><div class="actions">{link('projects.html','Discover our research','button')}{link('collaborations.html','Work with C3PH','text-link')}</div><div class="hero-signature"><span class="signature-rule"></span>Center for Cardiovascular Computational<br>&amp; Precision Health</div></div><figure class="atlas-stage" data-mode="imaging"><div class="atlas-coordinate coordinate-top"><span>THE CARDIOVASCULAR ATLAS</span><span>01 / 04</span></div><div class="atlas-art-wrap"><img class="heart-art" src="assets/atlas-heart.svg" width="680" height="700" alt="Conceptual point-cloud reconstruction of cardiac anatomy" fetchpriority="high"><div class="slice-marker" aria-hidden="true"></div></div><span class="specimen-tag">STRUCTURE + SIGNAL + CONTEXT</span><figcaption>Conceptual artwork. No patient data.</figcaption></figure></div><div class="wrap hero-floor"><span><span class="live-dot" aria-hidden="true"></span>Houston Methodist · DeBakey Heart &amp; Vascular Center</span><a href="#perspective">Explore the center <span aria-hidden="true">↓</span></a></div></section>
<section class="section perspective" id="perspective"><div class="wrap"><div class="editorial-intro"><span class="section-code">01 / OUR PERSPECTIVE</span><div><h2>One person.<br><span class="muted-title">Many dimensions of health.</span></h2><div class="intro-columns"><p>We connect clinicians, scientists, and engineers around a shared question: what can the data we already collect reveal about the disease we hope to prevent?</p><p>Imaging. ECGs. Clinical history. Environment. Different perspectives become a more complete picture of cardiovascular health.</p></div></div></div><div class="scale-strip"><div class="scale-anchor"><strong>3<span>M+</span></strong><span>Longitudinal patients</span></div><div class="scale-item"><strong>8M+</strong><span>ECGs</span></div><div class="scale-item"><strong>200K+</strong><span>Cardiac CT studies</span></div><div class="scale-item"><strong>60K+</strong><span>CMR studies</span></div><div class="scale-item"><strong>500K+</strong><span>Echocardiograms</span></div></div><div class="scale-footnote"><span>Approximate center-reported research holdings</span>{link('resources.html#ecosystem','Explore the data ecosystem')}</div></div></section>
<section class="section selected-section" id="selected"><div class="wrap">{head('02 / Selected research','Questions worth looking closer at.','','projects.html','All research')}<div class="research-spread"><article class="lead-research"><a class="lead-art" href="{url(lead)}" tabindex="-1" aria-hidden="true"><img src="assets/atlas-heart.svg" width="680" height="700" alt="" loading="lazy"><span class="image-reference">01 / OPPORTUNISTIC CT</span><span class="image-cross" aria-hidden="true">+</span></a><div class="lead-caption"><span class="label">{escape(lead['topic'])} · Heart failure</span><h3><a href="{url(lead)}">A calcium scan.<br>A wider view of risk.</a></h3><p>{escape(lead['summary'])}</p>{link(url(lead),'Explore the study')}</div></article><div class="research-briefs">{rows}<a class="portfolio-note" href="projects.html"><span>Six published study spotlights.<br>Explore the questions behind the work.</span><span aria-hidden="true">↗</span></a></div></div></div></section>
<section class="signal-section" aria-labelledby="signal-heading"><div class="wrap signal-layout"><div class="signal-intro"><span class="section-code">03 / EXPLORE A SIGNAL</span><h2 id="signal-heading">The data is<br>only the beginning.</h2><p>Select a perspective to explore what it can reveal.</p><div class="signal-tabs" role="tablist" aria-label="Clinical data perspectives"><button type="button" role="tab" id="tab-imaging" aria-selected="true" aria-controls="signal-panel" data-signal="imaging">01 <span>Imaging</span> ↗</button><button type="button" role="tab" id="tab-ecg" aria-selected="false" aria-controls="signal-panel" tabindex="-1" data-signal="ecg">02 <span>ECG &amp; biosignals</span> ↗</button><button type="button" role="tab" id="tab-ehr" aria-selected="false" aria-controls="signal-panel" tabindex="-1" data-signal="ehr">03 <span>Health records</span> ↗</button><button type="button" role="tab" id="tab-environment" aria-selected="false" aria-controls="signal-panel" tabindex="-1" data-signal="environment">04 <span>Environment</span> ↗</button></div></div><div class="signal-panel" role="tabpanel" id="signal-panel" aria-labelledby="tab-imaging" tabindex="0"><div class="signal-image"><img id="signal-image" src="assets/ct.svg" alt="Conceptual illustration of computational imaging" width="600" height="320" loading="lazy"><span class="signal-visual-label">ILLUSTRATIVE VISUALIZATION</span></div><div class="signal-panel-copy"><span class="label" id="signal-kicker">Structure &amp; composition</span><h3 id="signal-title">More than an image.</h3><p id="signal-description">Quantifying anatomy, tissue composition, and disease burden from imaging acquired during routine care.</p><a class="text-link" id="signal-link" href="focus-areas.html#imaging">Explore imaging research <span aria-hidden="true">↗</span></a></div></div></div></section>
<section class="programs-section"><div class="wrap programs-layout"><div class="programs-title"><span class="section-code">04 / RESEARCH PROGRAMS</span><h2>Six lenses.<br><span>One purpose.</span></h2><p>Earlier insight.<br>More precise prevention.<br>Better cardiovascular health.</p></div><div class="program-accordions">{programs}</div></div></section>
<section class="section people-section"><div class="wrap people-editorial"><div class="people-statement"><span class="section-code">05 / THE PEOPLE</span><h2>Different disciplines.<br><span class="muted-title">Shared curiosity.</span></h2><p>Our team brings together clinical medicine, computational science, engineering, and population health.</p>{link('team.html','Meet the full team')}<div class="people-count"><strong>16</strong><span>Investigators, scientists,<br>engineers &amp; fellows</span></div></div><div class="director-grid">{people}</div></div></section>
<section class="section research-record"><div class="wrap">{head('06 / The research record','From discovery to the published page.','','publications.html','Search publications')}<div class="record-list">{publications}</div></div></section>{cta()}'''

def build_visual_assets(root):
    dest=Path(root)/'assets'
    rng=random.Random(413)
    points=[]
    # A stylized ventricular surface and outflow vessels, intended as editorial art.
    for row in range(78):
        y=-.98+row/77*1.96
        radius=math.sqrt(max(0,1-y*y))*(.76+.16*y)
        for col in range(70):
            a=col/70*math.tau+row*.025
            x=radius*math.cos(a)+.24*y
            z=radius*.68*math.sin(a)
            points.append((x+rng.uniform(-.007,.007),y,z,False))
    def tube(start,end,bend,radius,count=34):
        for i in range(count):
            t=i/(count-1)
            x=start[0]*(1-t)+end[0]*t+bend[0]*math.sin(t*math.pi)
            y=start[1]*(1-t)+end[1]*t+bend[1]*math.sin(t*math.pi)
            z=start[2]*(1-t)+end[2]*t
            for j in range(20):
                a=j/20*math.tau
                points.append((x+radius*math.cos(a),y,z+radius*math.sin(a),False))
    tube((-.05,.72,.04),(.61,1.22,.02),(-.35,.45),.15,50)
    tube((.27,.78,-.1),(.86,1.02,-.1),(-.05,.12),.12,32)
    tube((-.38,.58,.0),(-.49,1.19,.0),(.01,.0),.15,30)
    for x in (.0,.23,.43): tube((x,1.35,.02),(x-.08,1.66,.02),(0,0),.055,16)
    # Project with a fixed oblique camera; no diagnostic or patient coordinates.
    projected=[]
    for x,y,z,_ in points:
        xx=x*math.cos(-.35)+z*math.sin(-.35)
        zz=-x*math.sin(-.35)+z*math.cos(-.35)
        yy=y*.97-zz*.22
        px=335+xx*218; py=396-yy*218
        depth=(zz+1)/2
        projected.append((zz,f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{.65+depth*.5:.2f}" fill="#e4e1d7" opacity="{.14+depth*.58:.2f}"/>'))
    projected.sort(key=lambda v:v[0])
    dots=''.join(s for _,s in projected)
    arteries='<g fill="none" stroke="#e9815c" stroke-linecap="round"><path d="M366 229C350 280 337 309 344 357S363 445 318 548" stroke-width="2.4"/><path d="M351 310C307 324 268 347 251 390M344 361C393 363 424 393 446 431M353 408C318 416 291 443 282 473M342 469C370 476 390 489 396 510" stroke-width="1.4"/></g>'
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 700"><defs><radialGradient id="h"><stop stop-color="#36413f" stop-opacity=".38"/><stop offset="1" stop-color="#101c23" stop-opacity="0"/></radialGradient></defs><ellipse cx="350" cy="370" rx="260" ry="300" fill="url(#h)"/>{dots}{arteries}<g stroke="#e9815c" opacity=".45"><path d="M207 315H93m0-7v14M411 499h143m0-7v14"/><circle cx="207" cy="315" r="3" fill="#e9815c"/><circle cx="411" cy="499" r="3" fill="#e9815c"/></g></svg>'''
    (dest/'atlas-heart.svg').write_text(svg)
    # Reuse the established schematic drawings in the new, restrained palette.
    for name in ('ecg','ct','retina','ehr','environment'):
        path=dest/(name+'.svg')
        s=path.read_text()
        for old,new in {'#21747a':'#24312e','#0b2a45':'#142329','#0c2d48':'#142329','#71d6bd':'#e88c69','#70d8bb':'#e88c69','#9ec7c6':'#d1d2c6','#8bd8c3':'#e88c69','#195b6b':'#344740','#193d55':'#293b3b','#143c52':'#293b3b','#c3e4d2':'#e88c69','#418391':'#76857c','#4a8c98':'#566b62','#9bb2c2':'#a2aca2','#89a7b6':'#b7bbb0','#82b7d0':'#a4b3a7','#88bed1':'#a4b3a7','#577f93':'#52685c','#466d82':'#52685c'}.items(): s=s.replace(old,new)
        path.write_text(s)
