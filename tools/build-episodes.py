"""Render the shared EP02 data into static, indexable page slots. No runtime dependency."""
import json, re, html
from pathlib import Path
root=Path(__file__).resolve().parent.parent
e=json.loads((root/'data/episodes.json').read_text())['latest']
esc=html.escape
def slot(file,name,markup):
 p=root/file;s=p.read_text();start=f'<!-- {name}:start -->';end=f'<!-- {name}:end -->'
 s,n=re.subn(re.escape(start)+r'.*?'+re.escape(end),lambda _:start+'\n'+markup+'\n'+end,s,flags=re.S)
 assert n==1,(file,name,n)
 p.write_text(s)
def feature():
 return f'''<article class="featured-card">
<div class="scenario-number">#02</div><div class="featured-copy">
<div class="meta">{esc(e['series'])} · EP02 · {esc(e['duration'])} · 廣東話 · 主持 {esc(e['host'])}</div>
<h3>{esc(e['title'])}</h3>{''.join('<p>'+esc(p)+'</p>' for p in e['summary'])}
<div class="listen-row"><a class="btn dark" href="{e['path']}">睇情境 + 收聽</a><span>Spotify · YouTube</span></div></div>
<a class="episode-artwork" href="{e['path']}" aria-label="EP02：{esc(e['title'])}"><img src="{e['image']}" width="1280" height="720" alt="WedHQ EP02 封面：結完婚先知呢幾件事，超伏、超後悔！" loading="lazy"></a>
</article>'''
slot('index.html','latest-episode',feature())
slot('episodes.html','latest-episode',f'<div class="eyebrow">Latest Episode</div>'+feature())
slot('episodes.html','ep02-card',f'''<article class="small-card episode-card" data-series="scenario" data-search="EP02 Q蚊 六個情境 預算 父母 推薦 海外婚禮 Destination Wedding 時間表 後悔 Full-time Job">
<a class="episode-card-image" href="{e['path']}" aria-label="EP02：{esc(e['title'])}"><img src="{e['image']}" width="1280" height="720" alt="WedHQ EP02 封面" loading="lazy"></a>
<div class="meta">EP02 · {esc(e['series'])} · {e['duration']} · 廣東話 · Q蚊</div><h3>{esc(e['title'])}</h3><p>{esc(' '.join(e['summary']))}</p><a href="{e['path']}">Read / Listen →</a></article>''')
slot('episode-002.html','episode-header',f'''<div class="episode-kicker">{esc(e['series'])} · EP02</div><h1>{esc(e['title'])}</h1><p class="meta">主持 Q蚊 · 廣東話 · 27:26</p><p class="lead">{esc(e['summary'][0])}</p><img class="episode-cover" src="{e['image']}" width="1280" height="720" alt="WedHQ EP02 封面：結完婚先知呢幾件事，超伏、超後悔！">''')
slot('episode-002.html','episode-summary',f'<div class="section-label">SCENARIO</div><h2>今集情境</h2>'+''.join('<p>'+esc(p)+'</p>' for p in e['summary']))
apple_control = (f'<a href="{esc(e["apple"])}" target="_blank" rel="noopener">在 Apple Podcasts 收聽 ↗</a>' if e.get('apple') else '<button type="button" disabled aria-disabled="true" aria-describedby="apple-pending">在 Apple Podcasts 收聽 ↗</button>')
apple_note = '' if e.get('apple') else '<p class="platform-note" id="apple-pending">Apple Podcasts 更新中，連結稍後提供。</p>'
slot('episode-002.html','episode-listen',f'''<div class="section-label">LISTEN</div><h2>收聽今集</h2>
<div class="spotify-embed-wrap"><iframe style="border-radius:12px" src="https://open.spotify.com/embed/episode/5VqY9FhWxVZeArgrLMx1Bx" width="100%" height="232" frameborder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy" title="Spotify player — WedHQ EP02 {esc(e['title'])}"></iframe></div>
<div class="platforms"><a href="{esc(e['spotify'])}" target="_blank" rel="noopener">在 Spotify 收聽 ↗</a>{apple_control}<a href="{esc(e['youtube'])}" target="_blank" rel="noopener">在 YouTube 收聽 ↗</a></div>{apple_note}''')
summary=' '.join(e['summary'])
schema={'@context':'https://schema.org','@type':'PodcastEpisode','@id':'https://wedhq.ca/episode-002#episode','name':e['title'],'episodeNumber':2,'description':summary,'inLanguage':'yue-Hant','url':'https://wedhq.ca/episode-002','image':'https://wedhq.ca/'+e['image'],'timeRequired':e['durationISO'],'actor':{'@type':'Person','name':'Q蚊'},'partOfSeries':{'@type':'PodcastSeries','name':'WedHQ Podcast','url':'https://wedhq.ca/episodes'},'sameAs':[e['spotify'],e['youtube']]+([e['apple']] if e.get('apple') else [])}
meta=f'''<title>{esc(e['title'])}｜EP02 婚禮 Scenario｜WedHQ</title>
<meta name="description" content="{esc(summary)}"><link rel="canonical" href="https://wedhq.ca/episode-002">
<meta property="og:type" content="article"><meta property="og:title" content="{esc(e['title'])}｜EP02｜WedHQ"><meta property="og:description" content="{esc(summary)}"><meta property="og:url" content="https://wedhq.ca/episode-002"><meta property="og:image" content="https://wedhq.ca/{e['image']}"><meta property="og:image:width" content="1280"><meta property="og:image:height" content="720"><meta property="og:image:alt" content="WedHQ EP02 封面"><meta property="og:locale" content="zh_HK"><meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>'''
slot('episode-002.html','episode-meta',meta)
for file,url in [('index.html','https://wedhq.ca/'),('episodes.html','https://wedhq.ca/episodes')]:
 slot(file,'latest-meta',f'<meta property="og:type" content="website"><meta property="og:title" content="WedHQ · 最新 EP02：{esc(e["title"])}"><meta property="og:description" content="{esc(summary)}"><meta property="og:url" content="{url}"><meta property="og:image" content="https://wedhq.ca/{e["image"]}"><meta name="twitter:card" content="summary_large_image">')
print('Rendered EP02 homepage, Podcast / episodes, and episode landing page.')
