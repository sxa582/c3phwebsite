"""Render the selected funding portfolio from verified public award records."""
from html import escape


def render_funding(data, link):
    def e(value):
        return escape(str(value), quote=True)

    def award(project, number):
        records = project['annual_records']
        earlier = project.get('earlier_award', False)
        code = project.get('core_project_number', 'PRESSURE CHECK')
        subproject = f'<span>Subproject {e(project["subproject_id"])}</span>' if project.get('subproject_id') else ''
        period = f'<span class="award-period">Project period {project["period_start"][:4]}–{project["period_end"][:4]}</span>' if project.get('period_start') else '<span class="award-period">Four-city collaborative study</span>'
        if project.get('period_display'):
            period = f'<span class="award-period">{e(project["period_display"])}</span>'
        status = '<span class="award-archive">Earlier award records</span>' if earlier else ''
        leadership = ''
        if project.get('principal_investigators'):
            leadership = f'<div><dt>Principal investigators</dt><dd>{e(" · ".join(project["principal_investigators"]))}</dd></div>'
        partnership = f'<div><dt>Study sites</dt><dd>{e(" · ".join(project["partners"]))}</dd></div>' if project.get('partners') else ''
        history = ''
        latest = ''
        if records:
            latest = f'<div class="award-amount"><span>Latest listed NIH record · FY {records[0]["fiscal_year"]}</span><strong>${records[0]["amount"]:,}</strong><small>Reported annual amount</small></div>'
            rows = ''.join(f'<tr><th scope="row">{r["fiscal_year"]}</th><td>{e(r["project_number"])}</td><td>${r["amount"]:,}</td><td>{link(r["url"],"Record","award-record-link")}</td></tr>' for r in records)
            history = f'''<details class="award-history"><summary>NIH award history <span>{len(records)} {'record' if len(records) == 1 else 'records'}</span></summary><div class="award-table-scroll" tabindex="0" role="region" aria-label="Annual funding records for {e(project['headline'])}"><table><caption class="sr-only">Annual NIH records for {e(code)}</caption><thead><tr><th scope="col">Fiscal year</th><th scope="col">Award number</th><th scope="col">Reported amount</th><th scope="col">Source</th></tr></thead><tbody>{rows}</tbody></table></div></details>'''
        if project.get('study_budget'):
            latest = f'<div class="award-amount"><span>PCORI project budget · Full study</span><strong>${project["study_budget"]:,}</strong><small>Total across study sites</small></div>'
        source_label = 'View NIH RePORTER' if records else 'View PCORI award' 
        source = link(project['url'], source_label, 'text-link')
        if project.get('study_url'):
            source += link(project['study_url'], 'Meet the study team', 'text-link')
        return f'''<article class="funding-award" id="{e(project['id'])}">
<div class="award-index"><span class="award-number">{number:02d}</span><span class="eyebrow">{e(project['funder'])}</span><strong class="award-code">{e(code)}</strong>{subproject}{period}{status}</div>
<div class="award-body"><span class="award-mechanism">{e(project['mechanism'])}</span><h3>{e(project['headline'])}</h3><p class="award-summary">{e(project['summary'])}</p><p class="award-official-title"><span>Project title</span>{e(project['title'])}</p>
<dl class="award-facts"><div><dt>C3PH investigator</dt><dd>{e(project['center_investigator'])}<span>{e(project['role'])}</span></dd></div>{leadership}<div><dt>Recipient institution</dt><dd>{e(project['recipient'])}</dd></div>{partnership}</dl>
<div class="award-bottom"><div class="award-source-links">{source}</div>{latest}</div>{history}</div></article>'''

    projects = data['projects']
    count = len(projects)
    al_kindi = ''.join(award(p, i + 1) for i, p in enumerate(projects) if p['group'] == 'al-kindi')
    nasir = ''.join(award(p, i + 1) for i, p in enumerate(projects) if p['group'] == 'nasir')
    r01 = sum(p['mechanism'] == 'R01' for p in projects)
    return f'''<section class="funding-hero"><div class="wrap"><div class="funding-hero-grid"><div><span class="eyebrow">Funding / Research support</span><h1>Funded questions.<br><span>Shared progress.</span></h1><p>Selected research support involving C3PH investigators and collaborators across institutions. From computational discovery to prevention in the community.</p></div><div class="funding-tally"><span class="eyebrow">A portfolio of possibilities</span><strong>{count:02d}</strong><span>Selected projects &amp; programs</span><div><span>NIH</span><span>PCORI</span></div></div></div><div class="funding-hero-bottom"><nav aria-label="Funding portfolio sections"><a href="#al-kindi">Sadeer Al-Kindi <span aria-hidden="true">↓</span></a><a href="#nasir">Khurram Nasir <span aria-hidden="true">↓</span></a></nav><span>{r01} R01 awards · 1 RF1 award · 1 center core · 1 PCORI study</span></div></div></section>
<section class="funding-portfolio" aria-labelledby="al-kindi-heading" id="al-kindi"><div class="wrap"><div class="funding-group-heading"><span class="eyebrow">01 / Investigator portfolio</span><div><h2 id="al-kindi-heading">Sadeer Al-Kindi</h2><p>Imaging, artificial intelligence, environmental health, and investigator development.</p></div><span class="funding-group-count">05 projects</span></div>{al_kindi}</div></section>
<section class="funding-portfolio funding-portfolio-nasir" aria-labelledby="nasir-heading" id="nasir"><div class="wrap"><div class="funding-group-heading"><span class="eyebrow">02 / Investigator portfolio</span><div><h2 id="nasir-heading">Khurram Nasir</h2><p>Atherosclerosis biology, cardiovascular risk, and community-connected prevention.</p></div><span class="funding-group-count">03 projects</span></div>{nasir}</div></section>
<section class="funding-notes"><div class="wrap"><span class="eyebrow">About this portfolio</span><div><p>NIH records are grouped by core award number and, where applicable, subproject. NIH annual amounts describe the listed award or subproject at its recipient institution. The PCORI amount is the full multisite study budget. These figures do not represent C3PH’s allocation. Earlier award records are identified separately.</p><p>This selected portfolio includes research led by C3PH investigators with collaborating institutions. NIH information comes from RePORTER; Pressure Check funding and investigator roles are linked to PCORI and the study team. Updated October 22, 2026.</p></div></div></section>
<section class="funding-next"><div class="wrap"><h2>See the science<br>this support makes possible.</h2><div>{link('projects.html','Explore our research','button')}{link('collaborations.html','Build a collaboration','text-link')}</div></div></section>'''
