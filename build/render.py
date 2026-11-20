import json, sys, os
data = json.load(open(sys.argv[1]))['files']
REPO = sys.argv[2]

ALIASES = {'branding': ['брендинг', 'айдентика', 'фирменный стиль', 'brand identity', 'logo', 'логотип', 'брендинговые агентства'], 'product-management': ['product management', 'продакт-менеджмент', 'управление продуктом', 'юнит-экономика', 'unit economics', 'метрики', 'управление проектами', 'project management', 'OKR'], 'brazil': ['Бразилия', 'Brasil'], 'ui-patterns': ['UI-паттерны', 'паттерны интерфейсов'], 'web-galleries': ['галереи сайтов', 'веб-референсы'], 'images-and-moodboards': ['мудборды', 'картинки'], 'color': ['цвет', 'палитры'], 'typography': ['типографика', 'шрифты', 'fonts'], 'motion': ['моушн', 'анимация', 'animation'], 'ux-research': ['UX-исследования'], 'component-libraries': ['библиотеки компонентов', 'UI-киты'], 'photo-archives': ['фотоархивы', 'стоки', 'stock'], 'portugal': ['Португалия'], 'awesome-lists': ['скиллы', 'awesome-списки'], 'icons-and-graphics': ['иконки', 'иллюстрации', 'icons'], 'tools': ['инструменты'], 'off-topic': ['оффтоп'], 'learning': ['обучение', 'книги', 'books'], 'graphic-design-history': ['история графического дизайна'], 'rtl': ['справа налево', 'арабский', 'иврит'], 'architecture': ['архитектура'], 'web-history': ['история веба'], 'ux-curators': ['кураторы', 'LinkedIn'], 'museums-and-galleries': ['музеи', 'галереи'], 'design-schools': ['школы дизайна', 'образование'], 'art-history': ['история искусства', 'художники', 'Гомбрих'], 'egypt': ['Египет'], 'ux-process': ['дизайн-процесс', 'About Face'], 'awards': ['премии', 'награды'], 'cinema': ['кино', 'титры'], 'magazines': ['журналы', 'газеты'], 'publishers': ['издательства'], 'online-learning': ['онлайн-обучение', 'курсы'], 'regions': ['регионы', 'страны'], 'design-systems': ['дизайн-системы', 'киты Figma'], 'design-to-code': ['дизайн в код', 'Figma MCP', 'вайбкодинг'], 'handoff': ['хендофф', 'передача в разработку', 'dev handoff'], 'research-and-testing': ['тестирование', 'исследования'], 'metrics-and-growth': ['метрики', 'рост', 'growth'], 'benchmarks': ['бенчмарк', 'конкуренты', 'competitors'], 'ecommerce': ['e-commerce', 'магазины', 'интернет-магазины', 'электронная коммерция', 'ритейл'], 'forms': ['формы', 'поля ввода'], 'tables-and-dashboards': ['таблицы', 'дашборды', 'data tables'], 'data-visualization': ['визуализация данных', 'графики', 'dataviz'], 'email-design': ['письма', 'email', 'рассылки', 'newsletters'], 'writing': ['тексты', 'UX-writing', 'микрокопи', 'microcopy'], 'accessibility': ['доступность', 'инклюзивность', 'a11y', 'WCAG'], 'mobile-design': ['мобильный дизайн', 'iOS', 'Android'], 'ai-and-creative-tech': ['AI', 'ИИ', '3D', 'креативный код'], 'english-for-designers': ['английский']}
T = {
 'ui-patterns': ('UI Patterns and Real Products','Libraries of screens, flows and patterns from shipped products.',['ui','patterns','mobile','web'],['web-galleries','ux-research','component-libraries']),
 'web-galleries': ('Web Galleries','Curated galleries of websites, landing pages and single page sections.',['web','inspiration','layout'],['ui-patterns','web-history','typography']),
 'images-and-moodboards': ('Images and Moodboards','Moodboard tools, logo archives, shapes and backgrounds.',['images','moodboards','branding'],['photo-archives','icons-and-graphics','color']),
 'color': ('Color','Palette generators and colour tools.',['color'],['images-and-moodboards','typography']),
 'typography': ('Typography and Type Foundries','Type in use, free typefaces and independent Cyrillic and Latin foundries.',['typography','fonts','cyrillic'],['graphic-design-history','rtl','portugal']),
 'motion': ('Motion and Micro-interactions','References for interface motion, delightful details and motion design tools.',['motion','micro-interactions'],['component-libraries','cinema']),
 'ux-research': ('UX Research and Guidelines','Research institutes, guidelines and articles on user experience.',['ux','research'],['ux-curators','ui-patterns']),
 'component-libraries': ('Component Libraries','Copy-paste component libraries for React, Tailwind, shadcn and SwiftUI.',['code','components','react','swiftui'],['motion','ui-patterns','awesome-lists']),
 'photo-archives': ('Photo and Image Archives','Stock photography, open access museums, libraries and specialist archives without AI-generated images.',['photography','archives','public-domain','museums'],['graphic-design-history','portugal','images-and-moodboards']),
 'portugal': ('Portugal','Portuguese design, modernist magazines, azulejos, posters, type, museums, palaces, galleries, publishers and Lisbon Design Week.',['portugal','lisbon','azulejo','modernism'],['architecture','graphic-design-history','photo-archives']),
 'awesome-lists': ('Claude Skills and Awesome Lists','Skills for AI agents and other curated design lists on GitHub.',['ai','skills','github'],['component-libraries','tools']),
 'icons-and-graphics': ('Icons, Illustrations and Graphics','Icon sets, illustration generators and graphic effects.',['icons','illustration'],['images-and-moodboards','tools']),
 'tools': ('Tools','Mockups, inspiration and tools for branding, photo, AI and video.',['tools','mockups','branding'],['icons-and-graphics','motion']),
 'off-topic': ('Off Topic','Learning, utilities, games, radio and small delights for when you are not designing.',['off-topic','radio','games'],['learning']),
 'learning': ('Learning','YouTube channels and books worth owning.',['learning','books','youtube'],['graphic-design-history','ux-curators']),
 'graphic-design-history': ('Graphic Design History','Archives, books and museums for every major movement from medieval manuscripts to Emigre.',['history','graphic-design','avant-garde','modernism'],['typography','rtl','portugal','photo-archives','web-history']),
 'rtl': ('Right-to-Left Scripts','Arabic, Hebrew and Persian typography, RTL interface layout, calligraphy and museums.',['rtl','arabic','hebrew','persian'],['typography','graphic-design-history']),
 'brazil': ('Brazil','Brazilian type foundries, design history archives, museums, architecture, cinema and advertising.',['brazil','latin-america','modernism'],['portugal','regions','typography','architecture']),
 'architecture': ('Architecture','Archives, databases and centres for buildings and architects, starting with Portugal.',['architecture'],['portugal','graphic-design-history']),
 'web-history': ('Early Web History','Museums, archives and books on how the web looked from 1991 onwards.',['web','history','geocities'],['web-galleries','graphic-design-history']),
 'museums-and-galleries': ('Museums, Galleries and Art Media','Museums worldwide, including Scotland and Garage, with their online collections and free publications, galleries, art magazines and fairs.',['museums','collections','art','galleries'],['photo-archives','graphic-design-history','portugal','design-schools']),
 'design-schools': ('Design Schools','Art and design schools in Portugal, the rest of Europe and beyond.',['education','schools','design'],['learning','museums-and-galleries','portugal']),
 'art-history': ('Art History and Artists', "Overviews of art history following Gombrich's The Story of Art, image databases and artists' official resources.", ['art', 'history', 'artists'], ['museums-and-galleries', 'graphic-design-history', 'egypt']),
 'egypt': ('Ancient Egypt', "Museums, primary sources and hieroglyph tools, from Turin's Museo Egizio to free Egyptology PDFs.", ['egypt', 'writing', 'archaeology'], ['art-history', 'museums-and-galleries', 'rtl']),
 'ux-process': ('UX Design Process', 'The design process from About Face: goals and mental models, behaviour, etiquette, and platform and posture.', ['ux', 'process', 'platforms'], ['ux-research', 'ux-curators', 'online-learning']),
 'awards': ('Design Awards', 'International and regional design awards whose winner archives work as reference libraries.', ['awards', 'inspiration'], ['web-galleries', 'magazines', 'regions']),
 'cinema': ('Cinema', 'Title sequences, film typography, frames, posters and film archives.', ['cinema', 'titles', 'posters'], ['motion', 'typography', 'regions']),
 'magazines': ('Magazines and Newspapers', 'Design, architecture and culture magazines in print and online.', ['magazines', 'press'], ['publishers', 'awards', 'graphic-design-history']),
 'publishers': ('Publishers', 'Art, design and typography publishers worth following.', ['books', 'publishers'], ['magazines', 'learning', 'art-history']),
 'online-learning': ('Online Learning', 'Courses and free online books on design, UX and art.', ['learning', 'courses'], ['learning', 'ux-process', 'design-schools']),
 'regions': ('Regions of the World', 'Museums and archives by region: the Americas, Africa, Oceania, East and Southeast Asia.', ['regions', 'museums', 'world'], ['museums-and-galleries', 'art-history', 'cinema']),
 'design-systems': ('Design Systems', 'Corporate design systems, their motion guidelines, official Figma kits and tools for documenting systems.', ['design-systems', 'motion', 'figma'], ['component-libraries', 'design-to-code', 'motion']),
 'design-to-code': ('Design to Code', "Figma Summer School Designer to Builder materials, Figma's official files, MCP and agent tools.", ['figma', 'code', 'ai', 'mcp'], ['design-systems', 'component-libraries', 'handoff']),
 'handoff': ('Developer Handoff', 'Tools for handing designs to engineering.', ['handoff', 'figma'], ['design-to-code', 'design-systems']),
 'research-and-testing': ('Research and Testing Tools', 'Usability testing, recruiting and research repositories, plus secondary research.', ['research', 'testing'], ['ux-research', 'metrics-and-growth', 'ux-process']),
 'metrics-and-growth': ('Metrics and Growth', 'Growth books, product metrics and analytics tools.', ['metrics', 'growth'], ['research-and-testing', 'benchmarks', 'ecommerce']),
 'benchmarks': ('Benchmarks and Competitors', 'Market data and industry players for competitive analysis.', ['benchmark', 'competitors'], ['metrics-and-growth', 'ecommerce']),
 'ecommerce': ('E-commerce', 'Research, patterns and history of online shopping.', ['ecommerce'], ['benchmarks', 'ux-research', 'forms']),
 'forms': ('Forms', 'Form design rules and tools.', ['forms', 'ui'], ['tables-and-dashboards', 'accessibility', 'writing']),
 'tables-and-dashboards': ('Tables and Dashboards', 'Data table and dashboard design.', ['tables', 'dashboards', 'data'], ['data-visualization', 'forms', 'design-systems']),
 'data-visualization': ('Data Visualization', 'Chart inspiration, history and guidelines.', ['dataviz', 'charts'], ['tables-and-dashboards', 'graphic-design-history']),
 'email-design': ('Email Design', 'Email inspiration and newsletter tools.', ['email'], ['writing', 'web-galleries']),
 'writing': ('Writing and UX Writing', 'Content style guides and writing for interfaces.', ['writing', 'content'], ['english-for-designers', 'forms', 'email-design']),
 'accessibility': ('Accessibility and Inclusive Design', 'WCAG guides, accessible patterns and Figma plugins.', ['accessibility', 'inclusive-design', 'wcag'], ['forms', 'design-systems', 'mobile-design']),
 'mobile-design': ('Mobile Design', 'Platform guidelines and mobile UI galleries.', ['mobile', 'ios', 'android'], ['ui-patterns', 'accessibility', 'motion']),
 'ai-and-creative-tech': ('AI and Creative Technology', 'AI tools, generative art, 3D and creative coding.', ['ai', '3d', 'creative-coding'], ['design-to-code', 'motion', 'tools']),
 'english-for-designers': ('English for Designers', 'Pronunciation, writing and speaking in English at work.', ['english', 'communication'], ['writing', 'learning']),
 'product-management': ('Product Management', 'Strategy, metrics, unit economics, finance and delivery, structured after The Product Map.', ['product', 'metrics', 'strategy'], ['metrics-and-growth', 'research-and-testing', 'ux-process']),
 'branding': ('Branding and Identity', 'Established brand agencies in London, New York, Paris and the Netherlands, case-study press, guidelines archives, brand typefaces and books.', ['branding', 'identity'], ['typography', 'graphic-design-history', 'design-systems']),
 'ux-curators': ('UX Curators and Vitaly Friedman','People who publish carefully curated UX material, and Vitaly Friedman\'s resources sorted by topic.',['ux','linkedin','curators'],['ux-research','learning']),
}
GROUPS = [
 ('Visual References',['branding','ui-patterns','web-galleries','images-and-moodboards','color','typography','motion','icons-and-graphics']),
 ('Code and Tools',['design-systems','component-libraries','design-to-code','handoff','tools','ai-and-creative-tech','awesome-lists']),
 ('UX',['ux-research','ux-process','research-and-testing','metrics-and-growth','product-management','benchmarks','ux-curators']),
 ('Interface Topics',['forms','tables-and-dashboards','data-visualization','mobile-design','accessibility','ecommerce','email-design','writing']),
 ('History and Archives',['art-history','egypt','graphic-design-history','web-history','rtl','photo-archives']),
 ('Places and Institutions',['portugal','brazil','architecture','museums-and-galleries','regions','design-schools']),
 ('Media and Culture',['cinema','magazines','publishers','awards']),
 ('Learning',['learning','online-learning','english-for-designers','off-topic']),
]
PLANNED = [('cinema','Cinema'),]

os.makedirs(f'{REPO}/topics', exist_ok=True)
import re
def gslug(t): return re.sub(r'[^\w\- ]','',t.lower()).replace(' ','-')
def esc(s): return s.replace('|','\\|')
for slug,(title,desc,tags,rel) in T.items():
    secs = data.get(slug, {})
    n = sum(len(v) for v in secs.values())
    L = ['---', f'title: {title}', 'aliases: ['+', '.join(ALIASES.get(slug,[]))+']', 'tags: ['+', '.join(tags)+']', f'entries: {n}', '---', '', f'# {title}', '', desc, '']
    rl = [f'[{T[r][0]}]({r}.md)' for r in rel if r in T]
    if rl: L += ['Related: ' + ' · '.join(rl), '']
    L += ['[Back to the index](../README.md)', '', '## Contents', '']
    for s in secs: L.append(f'- [{s}](#{gslug(s)})')
    L.append('')
    for s, items in secs.items():
        L += [f'## {s}', '']
        for name,url,d,acc in items:
            d = d.strip()
            if not d.endswith('.'): d += '.'
            L.append(f'- [{name}]({url}) - {d} *{acc}.*')
        L.append('')
    open(f'{REPO}/topics/{slug}.md','w').write('\n'.join(L))

total = sum(sum(len(v) for v in s.values()) for s in data.values())
R = ['# Awesome Design References [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)', '',
 'Curated references and learning material for product and graphic designers: interface patterns, galleries, type, motion, design systems, design to code, UX research and writing, product management and metrics, art and graphic design history, archives, museums, design schools and regions.', '',
 f'The list holds {total} checked links in {len(T)} topic files. Every topic file links to related topics, so the folder also works as an Obsidian vault with a connected graph.', '',
 '## Contents', '']
for g,_ in GROUPS: R.append(f'- [{g}](#{g.lower().replace(" ","-")})')
R.append('')
for g, slugs in GROUPS:
    R += [f'## {g}', '']
    for s in slugs:
        t,d,_,_ = T[s]
        n = sum(len(v) for v in data.get(s,{}).values())
        R.append(f'- [{t}](https://github.com/mariyasidorov-create/Reference-Hub/blob/main/topics/{s}.md) - {d[:-1]} ({n} links).')
    R.append('')
R += ['## Contributing', '', 'Suggest a link with the [Suggest a resource form](https://github.com/mariyasidorov-create/Reference-Hub/issues/new?template=suggest-resource.yml), no file editing needed, or open a pull request following the [contribution guidelines](contributing.md).', '',
 '## Footnotes', '', 'This repository is the single home for what used to be two separate collections: the Reference Hub (visual references, galleries, component libraries) and the Knowledge Hub (learning: books, courses, educators, research). Both now live here as topics. See [all resources](all-resources.md) for a single list of every name, and the [knowledge map](knowledge-map.md) for how topics connect. Every entry is also in [references.json](references.json) for scripts and AI agents. Sources include Denis Masharov\'s Facebook albums on graphic design history, Erken Kagarov\'s writing, and posts by Vitaly Friedman.', '']
open(f'{REPO}/README.md','w').write('\n'.join(R))

# knowledge map
M = ['# Knowledge Map', '', 'How the topics connect. GitHub renders the diagram below; Obsidian builds the same graph automatically from the links between topic files.', '', '```mermaid', 'graph LR']
seen=set()
for s,(t,_,_,rel) in T.items():
    M.append(f'  {s.replace("-","_")}["{t}"]')
for s,(t,_,_,rel) in T.items():
    for r in rel:
        if r in T and (r,s) not in seen:
            seen.add((s,r)); M.append(f'  {s.replace("-","_")} --- {r.replace("-","_")}')
M += ['```', '', '## Open as an Obsidian Vault', '', '1. Clone the repository.', '2. In Obsidian choose Open folder as vault and pick the cloned folder.', '3. Open Graph view: every topic file is a node, and the Related links are the edges.', '', 'Tags in each file\'s front matter (for example `history`, `portugal`, `rtl`) show up in the tag pane and can colour the graph.', '', '## Planned Topics', '', '- Archive of saved Instagram posts with transcripts', '', '[Back to the index](README.md)', '']
open(f'{REPO}/knowledge-map.md','w').write('\n'.join(M))
A=['# All Resources','','Every resource in the hub by name, grouped by topic. Authors are in brackets where the resource is a book or a person\'s work. Descriptions and links are in the topic files.','']
for g,slugs in GROUPS:
    A+=[f'## {g}','']
    for sl in slugs:
        A.append(f'### [{T[sl][0]}](topics/{sl}.md)')
        A.append('')
        A.append(' · '.join(sorted({n for items in data.get(sl,{}).values() for n,_,_,_ in items}, key=str.lower)))
        A.append('')
A+=['[Back to the index](README.md)','']
open(f'{REPO}/all-resources.md','w').write('\n'.join(A))
print('total', total)
