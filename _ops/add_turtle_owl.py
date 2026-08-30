#!/usr/bin/env python3
"""Surgical insertions: turtle in proof grid, tree+owl above Honest Filter, owl in Unlimited card."""
from pathlib import Path
import re

ROOT = Path('/Users/macmini/sites/bootcampfx')
html_path = ROOT / 'index.html'
text = html_path.read_text()

# ---------- SVG snippets ----------
TURTLE_SVG = '''<svg viewBox="0 0 90 42" fill="none">
          <g class="turtle-leg-back">
            <path d="M30 28 C28 34 26 37 28 38 C32 39 36 36 36 30 Z" fill="#9FB0C4"/>
          </g>
          <g class="turtle-leg-front">
            <path d="M56 28 C54 34 52 37 54 38 C58 39 62 36 62 30 Z" fill="#9FB0C4"/>
          </g>
          <g class="turtle-shell">
            <path d="M18 28 L8 26 L16 32 Z" fill="#9FB0C4"/>
            <path d="M72 30 C76 16 62 7 46 7 C30 7 16 16 20 30 C34 32 58 32 72 30 Z" fill="#14291F"/>
            <path d="M46 7 C47 16 46 24 44 30 M46 7 C49 16 50 24 53 30 M26 12 C32 16 34 22 35 29 M66 12 C60 16 58 22 57 29" stroke="#2E5A3F" stroke-width="1.6" fill="none"/>
          </g>
          <g class="turtle-head">
            <path d="M72 25 C80 23 86 23 89 25 C92 27 90 30 85 30 C81 30 76 30 73 29 Z" fill="#9FB0C4"/>
            <circle cx="86" cy="26" r="1.2" fill="#14100A"/>
          </g>
        </svg>'''

TREE_SVG = '''<svg viewBox="0 0 100 300" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <g fill="var(--pine)">
        <path d="M48 4 L60 34 L54 34 L66 62 L48 62 L32 62 L42 34 L36 34 Z"/>
        <path opacity=".96" d="M50 46 L74 90 L60 90 L82 128 L48 128 L18 128 L36 90 L24 90 Z"/>
        <path opacity=".92" d="M52 105 L86 155 L68 155 L92 182 L48 185 L10 185 L30 155 L16 155 Z"/>
        <path opacity=".88" d="M24 168 L52 150 L82 165 L88 188 L50 182 L18 190 Z"/>
        <path opacity=".84" d="M16 185 L50 172 L90 180 L96 208 L52 200 L8 210 Z"/>
        <path opacity=".8" d="M22 200 L54 190 L92 198 L94 218 L50 214 L14 220 Z"/>
      </g>
      <rect x="44" y="205" width="10" height="82" rx="2" fill="var(--ink)" opacity=".85"/>
      <ellipse cx="49" cy="290" rx="20" ry="3.5" fill="var(--ink)" opacity=".12"/>
    </svg>'''

OWL_WISE_SVG = '''<svg viewBox="0 0 64 88" fill="none">
      <path d="M4 78 L60 78" stroke="#6B5B4F" stroke-width="3.5" stroke-linecap="round"/>
      <g class="owl-head">
        <ellipse cx="32" cy="54" rx="18" ry="24" fill="#9FB0C4"/>
        <circle cx="32" cy="30" r="17" fill="#9FB0C4"/>
        <path d="M19 17 L14 3 L22 15 Z" fill="#9FB0C4"/>
        <path d="M45 17 L50 3 L42 15 Z" fill="#9FB0C4"/>
        <g class="owl-eyes">
          <circle cx="25" cy="28" r="6" fill="#F3ECDC"/>
          <circle cx="39" cy="28" r="6" fill="#F3ECDC"/>
          <circle cx="25" cy="28" r="2.2" fill="#14100A"/>
          <circle cx="39" cy="28" r="2.2" fill="#14100A"/>
        </g>
        <path d="M32 33 L28 40 L32 38 L36 40 Z" fill="var(--dawn)"/>
        <path d="M16 40 C12 50 12 62 18 66 L18 44 Z" fill="#7A8A9A"/>
        <path d="M48 40 C52 50 52 62 46 66 L46 44 Z" fill="#7A8A9A"/>
        <path d="M24 74 L24 80 M22 74 L22 80 M26 74 L26 80" stroke="var(--dawn)" stroke-width="2.2" stroke-linecap="round"/>
        <path d="M40 74 L40 80 M38 74 L38 80 M42 74 L42 80" stroke="var(--dawn)" stroke-width="2.2" stroke-linecap="round"/>
      </g>
    </svg>'''

OWL_CARD_SVG = '''<svg viewBox="0 0 64 84" fill="none">
      <g class="owl-head">
        <ellipse cx="32" cy="50" rx="18" ry="24" fill="#9FB0C4"/>
        <circle cx="32" cy="26" r="17" fill="#9FB0C4"/>
        <path d="M19 14 L14 0 L22 12 Z" fill="#9FB0C4"/>
        <path d="M45 14 L50 0 L42 12 Z" fill="#9FB0C4"/>
        <g class="owl-eyes">
          <circle cx="25" cy="24" r="6" fill="#F3ECDC"/>
          <circle cx="39" cy="24" r="6" fill="#F3ECDC"/>
          <circle cx="25" cy="24" r="2.2" fill="#14100A"/>
          <circle cx="39" cy="24" r="2.2" fill="#14100A"/>
        </g>
        <path d="M32 29 L28 36 L32 34 L36 36 Z" fill="var(--dawn)"/>
        <path d="M16 36 C12 46 12 58 18 62 L18 40 Z" fill="#7A8A9A"/>
        <path d="M48 36 C52 46 52 58 46 62 L46 40 Z" fill="#7A8A9A"/>
        <path d="M24 70 L24 76 M22 70 L22 76 M26 70 L26 76" stroke="var(--dawn)" stroke-width="2.2" stroke-linecap="round"/>
        <path d="M40 70 L40 76 M38 70 L38 76 M42 70 L42 76" stroke="var(--dawn)" stroke-width="2.2" stroke-linecap="round"/>
      </g>
    </svg>'''

# ---------- 1. Insert CSS before </head> ----------
css_block = f'''<style>
    /* Turtle, wise owl, and card owl additions */
    .proof-in > div {{ position:relative; }}
    .proof-turtle {{ position:absolute; bottom:8px; right:8px; width:40px; opacity:.9; z-index:1; pointer-events:none; }}
    .proof-turtle svg {{ display:block; width:100%; height:auto; overflow:visible; }}
    .proof-turtle .turtle-head {{ animation:headForage 7s ease-in-out infinite; transform-origin:73px 28px; }}
    .proof-turtle .turtle-leg-front {{ animation:legF 1.6s ease-in-out infinite; transform-origin:58px 30px; }}
    .proof-turtle .turtle-leg-back {{ animation:legB 1.6s ease-in-out infinite; transform-origin:32px 30px; }}
    @keyframes headForage {{ 0%,70%,100%{{ transform:rotate(0);}} 78%,92%{{ transform:rotate(9deg) translateY(2px);}} }}
    @keyframes legF {{ 0%,100%{{ transform:rotate(6deg);}} 50%{{ transform:rotate(-6deg);}} }}
    @keyframes legB {{ 0%,100%{{ transform:rotate(-6deg);}} 50%{{ transform:rotate(6deg);}} }}

    .honest-owl {{ position:absolute; top:18px; right:5%; width:70px; z-index:1; pointer-events:none; }}
    .honest-tree svg {{ display:block; width:100%; height:auto; overflow:visible; }}
    .honest-tree {{ animation:treeSwayC 7s ease-in-out infinite; transform-origin:50% 100%; }}
    @keyframes treeSwayC {{ 0%,100%{{ transform:rotate(0);}} 50%{{ transform:rotate(1.2deg);}} }}
    .owl-wise {{ position:absolute; top:-40px; left:50%; transform:translateX(-50%); width:48px; z-index:2; }}
    .owl-wise svg, .owl-card svg {{ display:block; width:100%; height:auto; overflow:visible; }}
    .owl-head {{ transform-origin:50% 62%; animation:owlTurn 5.4s ease-in-out infinite; }}
    .owl-eyes {{ transform-origin:50% 50%; animation:owlBlink 4.2s ease-in-out infinite; }}
    @keyframes owlTurn {{ 0%,100%{{ transform:rotate(0);}} 28%{{ transform:rotate(6deg);}} 62%{{ transform:rotate(-4deg);}} }}
    @keyframes owlBlink {{ 0%,96%,100%{{ transform:scaleY(1);}} 98%{{ transform:scaleY(0.1);}} }}

    .owl-card {{ position:absolute; top:38px; right:18px; width:40px; z-index:2; pointer-events:none; }}

    @media (max-width:680px){{ .proof-turtle {{ width:34px; bottom:6px; right:6px; }} }}
    @media (max-width:720px){{
      .honest-owl {{ width:52px; right:3%; top:24px; }}
      .owl-wise {{ width:36px; top:-30px; }}
      .owl-card {{ width:32px; top:44px; right:12px; }}
    }}
  </style>

  <!-- Trees fully removed. Deploy marker: 2026-07-27T05:15 -->'''

assert '<!-- Trees fully removed. Deploy marker: 2026-07-27T05:15 -->' in text, 'marker not found'
text = text.replace('<!-- Trees fully removed. Deploy marker: 2026-07-27T05:15 -->', css_block, 1)

# ---------- 2. Insert turtle in 4.9★ proof cell ----------
old_proof_cell = '<div role="listitem" class="reveal" style="--rd:.16s"><b><span class="count" data-count="4.9" data-dec="1">0</span><i>★</i></b><span>Average Rating</span></div>'
new_proof_cell = f'''<div role="listitem" class="reveal" style="--rd:.16s"><b><span class="count" data-count="4.9" data-dec="1">0</span><i>★</i></b><span>Average Rating</span>
        <div class="proof-turtle" aria-hidden="true">{TURTLE_SVG}</div>
      </div>'''
assert old_proof_cell in text, '4.9 proof cell not found'
text = text.replace(old_proof_cell, new_proof_cell, 1)

# ---------- 3. Insert tree + owl above Honest Filter heading ----------
old_honest_h2 = '<h2 class="display k reveal" style="text-align:center;">This works for almost everyone. <em>It\'s not for everyone.</em></h2>'
new_honest_h2 = f'''<div class="honest-owl" aria-hidden="true">
      <div class="honest-tree">{TREE_SVG}</div>
      <div class="owl owl-wise">{OWL_WISE_SVG}</div>
    </div>
    <h2 class="display k reveal" style="text-align:center;">This works for almost everyone. <em>It\'s not for everyone.</em></h2>'''
assert old_honest_h2 in text, 'honest h2 not found'
text = text.replace(old_honest_h2, new_honest_h2, 1)

# ---------- 4. Insert owl inside Unlimited tier card ----------
old_tier = '<div class="tier featured reveal" id="tier-unlimited" style="--rd:.1s">'
new_tier = f'''<div class="tier featured reveal" id="tier-unlimited" style="--rd:.1s;">
      <div class="owl owl-card" aria-hidden="true">{OWL_CARD_SVG}</div>'''
assert old_tier in text, 'unlimited tier not found'
text = text.replace(old_tier, new_tier, 1)

# ---------- 5. Reduced motion additions ----------
old_rm = '''.sq-proof { opacity:.8; transform:none !important; }
      .sq-proof .sq-inner, .sq-proof .sq-tail { transform:none !important; }
    }'''
new_rm = '''.sq-proof { opacity:.8; transform:none !important; }
      .sq-proof .sq-inner, .sq-proof .sq-tail { transform:none !important; }
      .proof-turtle, .proof-turtle * { animation:none !important; }
      .honest-owl, .honest-tree, .owl, .owl-head, .owl-eyes, .owl-card { animation:none !important; transform:none !important; }
    }}'''
assert old_rm in text, 'reduced motion block not found'
text = text.replace(old_rm, new_rm, 1)

html_path.write_text(text)
print('Inserted turtle, honest owl/tree, and card owl into index.html')
