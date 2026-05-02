"""
Sidebar v3: three dot density indicator per tile.
● ● ●  heavy   ● ● ○  medium   ● ○ ○  light
No bars, no count labels.
"""
import re, pathlib

HTML = pathlib.Path(r"c:\Users\Archit Tandon\Desktop\vahdam-dtc-data-engine\reports\strategy.html")
html = HTML.read_text(encoding="utf-8")

# Remove previous density-bar CSS
html = re.sub(r'/\* ── SIDEBAR DENSITY BARS ──[\s\S]+?\.sb-count \{ display: none; \}\n', '', html)

DOTS_CSS = """
/* ── SIDEBAR DENSITY DOTS ── */
.sb-dots {
  display: flex; gap: 3px; margin-left: auto; flex-shrink: 0;
  align-items: center;
}
.sb-d {
  width: 6px; height: 6px; border-radius: 50%;
}
.sb-d.on  { opacity: .7; }
.sb-d.off { background: var(--border) !important; opacity: 1; }
"""
html = html.replace("</style>", DOTS_CSS + "\n</style>", 1)

def dots(n, color):
    """n = 1/2/3 filled dots out of 3."""
    pips = []
    for i in range(3):
        cls = "on" if i < n else "off"
        pips.append(f'<span class="sb-d {cls}" style="background:{color}"></span>')
    return f'<span class="sb-dots">{"".join(pips)}</span>'

def chev():
    return '<svg class="sb-chevron" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="3,5 7,9 11,5"/></svg>'

NEW_SIDEBAR = f"""<aside id="sidebar">
  <div class="sb-brand">VAHDAM &nbsp;<strong>DTC Analytics</strong></div>

  <!-- KEY QUESTIONS -->
  <details class="sb-sec" open>
    <summary>
      <span class="sb-sec-icon">❓</span>
      <span class="sb-sec-label">Key Questions</span>
      {dots(3,'#7c3aed')}
      {chev()}
    </summary>
    <div class="sb-sec-body">
      <a class="sb-link sb-top" href="#questions">All Questions</a>
      <div class="sb-divider"></div>
      <a class="sb-link" href="#qg-revenue">💰 Revenue &amp; Margin {dots(2,'#d97706')}</a>
      <a class="sb-link" href="#qg-economics">📐 Customer Economics {dots(2,'#0d9488')}</a>
      <a class="sb-link" href="#qg-retention">🔁 Retention &amp; Churn {dots(3,'#7c3aed')}</a>
      <a class="sb-link" href="#qg-channel">📧 Channel &amp; Email {dots(1,'#16a34a')}</a>
      <a class="sb-link" href="#qg-conversion">🛒 Conversion &amp; Mix {dots(2,'#2563eb')}</a>
    </div>
  </details>

  <!-- METRICS FRAMEWORK -->
  <details class="sb-sec" open>
    <summary>
      <span class="sb-sec-icon">📊</span>
      <span class="sb-sec-label">Metrics Framework</span>
      {dots(3,'#d97706')}
      {chev()}
    </summary>
    <div class="sb-sec-body">
      <a class="sb-link sb-top" href="#overview">Overview &amp; Pyramid</a>
      <div class="sb-divider"></div>
      <div class="sb-tier-row"><span class="sb-tier-dot" style="background:#d97706"></span>Tier 1 — Business Health</div>
      <a class="sb-link" href="#metric-m1"><span class="sb-dot" style="background:#d97706"></span>M1 · Net Revenue by Market</a>
      <a class="sb-link" href="#metric-m2"><span class="sb-dot" style="background:#d97706"></span>M2 · New vs Returning</a>
      <a class="sb-link" href="#metric-m3"><span class="sb-dot" style="background:#0d9488"></span>M3 · LTV:CAC by Channel</a>
      <a class="sb-link" href="#metric-m4"><span class="sb-dot" style="background:#7c3aed"></span>M4 · Repeat Rate 90d</a>
      <a class="sb-link" href="#metric-m5"><span class="sb-dot" style="background:#d97706"></span>M5 · Gross Margin %</a>
      <div class="sb-tier-row"><span class="sb-tier-dot" style="background:#0d9488"></span>Tier 2 — Growth Levers</div>
      <a class="sb-link" href="#metric-m6"><span class="sb-dot" style="background:#0d9488"></span>M6 · CAC by Channel</a>
      <a class="sb-link" href="#metric-m7"><span class="sb-dot" style="background:#7c3aed"></span>M7 · Email Revenue %</a>
      <a class="sb-link" href="#metric-m8"><span class="sb-dot" style="background:#d97706"></span>M8 · AOV Trend MoM</a>
      <a class="sb-link" href="#metric-m9"><span class="sb-dot" style="background:#2563eb"></span>M9 · Checkout Funnel</a>
      <a class="sb-link" href="#metric-m10"><span class="sb-dot" style="background:#e11d48"></span>M10 · Subscription Mix</a>
      <div class="sb-tier-row"><span class="sb-tier-dot" style="background:#7c3aed"></span>Tier 3 — Retention Intel</div>
      <a class="sb-link" href="#metric-m11"><span class="sb-dot" style="background:#7c3aed"></span>M11 · Cohort Retention</a>
      <a class="sb-link" href="#metric-m12"><span class="sb-dot" style="background:#7c3aed"></span>M12 · Time to 2nd Purchase</a>
      <a class="sb-link" href="#metric-m13"><span class="sb-dot" style="background:#7c3aed"></span>M13 · Churn Risk</a>
      <a class="sb-link" href="#metric-m14"><span class="sb-dot" style="background:#e11d48"></span>M14 · At-Risk Revenue</a>
      <a class="sb-link" href="#metric-m15"><span class="sb-dot" style="background:#e11d48"></span>M15 · Product Repeat Rate</a>
      <a class="sb-link" href="#metric-bonus"><span class="sb-dot" style="background:#0d9488"></span>BONUS · LTV by Market</a>
    </div>
  </details>

  <!-- STRATEGIES -->
  <details class="sb-sec" open>
    <summary>
      <span class="sb-sec-icon">🗺</span>
      <span class="sb-sec-label">Strategies</span>
      {dots(3,'#e11d48')}
      {chev()}
    </summary>
    <div class="sb-sec-body">
      <a class="sb-link sb-top" href="#s1"><span class="sb-strat" style="background:#7c3aed">S1</span>Retention Engine {dots(2,'#7c3aed')}</a>
      <a class="sb-link sb-top" href="#s2"><span class="sb-strat" style="background:#0d9488">S2</span>Channel Efficiency {dots(3,'#0d9488')}</a>
      <a class="sb-link sb-top" href="#s3"><span class="sb-strat" style="background:#d97706">S3</span>Geo Expansion {dots(2,'#d97706')}</a>
      <a class="sb-link sb-top" href="#s4"><span class="sb-strat" style="background:#e11d48">S4</span>Subscription Flywheel {dots(3,'#e11d48')}</a>
      <a class="sb-link sb-top" href="#s5"><span class="sb-strat" style="background:#2563eb">S5</span>Funnel Conversion {dots(3,'#2563eb')}</a>
    </div>
  </details>

  <div class="sb-divider"></div>
  <a class="sb-standalone" href="#arch">🏗 &nbsp;Data Architecture {dots(3,'#2563eb')}</a>
  <a class="sb-standalone" href="#roadmap">🗓 &nbsp;Roadmap {dots(2,'#d97706')}</a>
</aside>"""

old = re.search(r'<aside id="sidebar">[\s\S]+?</aside>', html)
if not old:
    print("ERROR: sidebar not found"); exit(1)

html = html[:old.start()] + NEW_SIDEBAR + html[old.end():]
HTML.write_text(html, encoding="utf-8")

d = len(re.findall(r'class="sb-dots"', html))
print(f"Done. {d} dot indicators. {round(len(html)/1024,1)} KB")
