"""
Precog High-Level Architecture Diagram Generator
Handwritten, friendly, high-level architecture that anyone can understand.
Uses Caveat and Patrick Hand fonts embedded as base64 for perfect offline headless rendering.
"""

import os
import subprocess
import sys
import urllib.request
import base64
import re

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_PATH = os.path.join(OUTPUT_DIR, "precog-architecture.svg")
PNG_PATH = os.path.join(OUTPUT_DIR, "precog-architecture.png")
HTML_PATH = os.path.join(OUTPUT_DIR, "index.html")

def get_base64_fonts():
    """Download and return base64 encoded TTF fonts for reliable offline rendering."""
    fonts = {}
    font_urls = {
        "CaveatBold": "https://fonts.gstatic.com/s/caveat/v23/WnznHAc5bAfYB2QRah7pcpNvOx-pjRV6SII.ttf",
        "CaveatMedium": "https://fonts.gstatic.com/s/caveat/v23/WnznHAc5bAfYB2QRah7pcpNvOx-pjSx6SII.ttf",
        "PatrickHand": "https://fonts.gstatic.com/s/patrickhand/v25/LDI1apSQOAYtSuYWp8ZhfYeMWQ.ttf",
    }
    
    for name, url in font_urls.items():
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req, timeout=10).read()
            b64 = base64.b64encode(data).decode('ascii')
            fonts[name] = b64
            print(f"Loaded font {name} ({len(data)} bytes)")
        except Exception as e:
            print(f"Warning: could not download font {name}: {e}")
            fonts[name] = None
            
    return fonts

def build_svg(fonts):
    width = 2400
    height = 1350
    
    font_face_css = ""
    if fonts.get("CaveatBold"):
        font_face_css += f"""
        @font-face {{
            font-family: 'Caveat';
            font-weight: 700;
            font-style: normal;
            src: url(data:font/truetype;charset=utf-8;base64,{fonts['CaveatBold']}) format('truetype');
        }}
        """
    if fonts.get("CaveatMedium"):
        font_face_css += f"""
        @font-face {{
            font-family: 'Caveat';
            font-weight: 600;
            font-style: normal;
            src: url(data:font/truetype;charset=utf-8;base64,{fonts['CaveatMedium']}) format('truetype');
        }}
        """
    if fonts.get("PatrickHand"):
        font_face_css += f"""
        @font-face {{
            font-family: 'Patrick Hand';
            font-weight: 400;
            font-style: normal;
            src: url(data:font/truetype;charset=utf-8;base64,{fonts['PatrickHand']}) format('truetype');
        }}
        """
        
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&amp;family=Patrick+Hand&amp;display=swap');
      
      {font_face_css}
      
      * {{
        box-sizing: border-box;
      }}
      
      .hand-title {{
        font-family: 'Caveat', cursive, sans-serif;
        font-weight: 700;
        text-rendering: geometricPrecision;
      }}
      
      .hand-body {{
        font-family: 'Patrick Hand', 'Caveat', cursive, sans-serif;
        font-weight: 400;
        text-rendering: geometricPrecision;
      }}
      
      .card-shadow {{
        filter: drop-shadow(0 12px 24px rgba(15, 23, 42, 0.06));
      }}
      
      .hero-shadow {{
        filter: drop-shadow(0 20px 35px rgba(79, 70, 229, 0.12));
      }}
    </style>
    
    <!-- Marker for hand-drawn style arrows -->
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284C7" />
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#16A34A" />
    </marker>
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#9333EA" />
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#D97706" />
    </marker>

    <!-- Subtle Dot Pattern for Whiteboard / Notebook look -->
    <pattern id="dot-grid" x="0" y="0" width="36" height="36" patternUnits="userSpaceOnUse">
      <circle cx="18" cy="18" r="1.5" fill="#E2E8F0" />
    </pattern>
  </defs>

  <!-- Background Canvas -->
  <rect width="{width}" height="{height}" fill="#FAF9F6" />
  <rect width="{width}" height="{height}" fill="url(#dot-grid)" />

  <!-- Outer Hand-Drawn Sketch Border -->
  <rect x="25" y="25" width="2350" height="1300" rx="28" fill="none" stroke="#CBD5E1" stroke-width="2.5" stroke-dasharray="16 10" />

  <!-- ==================== HEADER ==================== -->
  <g transform="translate(100, 65)">
    <!-- Pill Badge -->
    <rect x="0" y="0" width="340" height="46" rx="23" fill="#EEF2FF" stroke="#818CF8" stroke-width="2" />
    <text x="170" y="30" text-anchor="middle" class="hand-title" font-size="24" fill="#4338CA">⚡ HIGH-LEVEL ARCHITECTURE</text>
    
    <!-- Main Title -->
    <text x="0" y="112" class="hand-title" font-size="62" fill="#0F172A">
      How Precog Works: <tspan fill="#4F46E5">Predictive Caching in Go</tspan>
    </text>
    
    <!-- Subtitle -->
    <text x="0" y="156" class="hand-body" font-size="30" fill="#475569">
      It doesn’t just cache API responses — it learns navigation habits and preloads what users click next!
    </text>

    <!-- GitHub / Repo Tag in top right -->
    <g transform="translate(1820, 15)">
      <rect x="0" y="0" width="380" height="58" rx="16" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5" class="card-shadow" />
      <text x="190" y="38" text-anchor="middle" class="hand-title" font-size="28" fill="#0F172A">
        ★ github.com/adam-Sar/precog
      </text>
    </g>
  </g>

  <!-- ==================== 4 STEP CARDS (HORIZONTAL FLOW) ==================== -->
  
  <!-- STEP 1: USER REQUEST -->
  <g transform="translate(100, 270)" class="card-shadow">
    <!-- Card Container -->
    <rect x="0" y="0" width="490" height="520" rx="24" fill="#FFFFFF" stroke="#0284C7" stroke-width="3.5" />
    <!-- Top Accent Bar -->
    <path d="M 0 24 Q 0 0 24 0 L 466 0 Q 490 0 490 24 L 490 60 L 0 60 Z" fill="#E0F2FE" />
    <text x="30" y="42" class="hand-title" font-size="30" fill="#0369A1">STEP 1: USER ACTION</text>
    
    <!-- Card Content -->
    <g transform="translate(32, 100)">
      <!-- Big Handwritten Header -->
      <text x="0" y="25" class="hand-title" font-size="44" fill="#0F172A">User visits "/products"</text>
      
      <!-- Visual Sketch Box -->
      <rect x="0" y="55" width="426" height="120" rx="16" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="2" />
      <text x="213" y="105" text-anchor="middle" class="hand-title" font-size="34" fill="#0284C7">GET /api/v1/products</text>
      <text x="213" y="145" text-anchor="middle" class="hand-body" font-size="24" fill="#0369A1">Session ID: #user-8492</text>
      
      <!-- Explanation bullets -->
      <text x="0" y="225" class="hand-body" font-size="26" fill="#334155">• Normal HTTP request hits your server</text>
      <text x="0" y="270" class="hand-body" font-size="26" fill="#334155">• Precog middleware intercepts request</text>
      <text x="0" y="315" class="hand-body" font-size="26" fill="#334155">• Reads session cookie or token</text>
      
      <!-- Bottom Badge -->
      <rect x="0" y="345" width="220" height="42" rx="12" fill="#E0F2FE" />
      <text x="110" y="374" text-anchor="middle" class="hand-title" font-size="24" fill="#0369A1">Standard Traffic</text>
    </g>
  </g>

  <!-- ARROW 1 -> 2 -->
  <g transform="translate(595, 510)">
    <path d="M 10 0 C 40 -15, 60 15, 90 0" fill="none" stroke="#0284C7" stroke-width="4.5" stroke-linecap="round" marker-end="url(#arrow-blue)" />
    <text x="50" y="-22" text-anchor="middle" class="hand-body" font-size="24" fill="#0284C7">Intercepts</text>
  </g>

  <!-- STEP 2: LIGHTNING CACHE & SHIELD -->
  <g transform="translate(700, 270)" class="card-shadow">
    <!-- Card Container -->
    <rect x="0" y="0" width="490" height="520" rx="24" fill="#FFFFFF" stroke="#16A34A" stroke-width="3.5" />
    <!-- Top Accent Bar -->
    <path d="M 0 24 Q 0 0 24 0 L 466 0 Q 490 0 490 24 L 490 60 L 0 60 Z" fill="#DCFCE7" />
    <text x="30" y="42" class="hand-title" font-size="30" fill="#15803D">STEP 2: SUPERFAST CACHE</text>
    
    <!-- Card Content -->
    <g transform="translate(32, 100)">
      <text x="0" y="25" class="hand-title" font-size="44" fill="#0F172A">Instant Check (<tspan fill="#16A34A">&lt; 5ns</tspan>)</text>
      
      <!-- Visual Sketch Box -->
      <rect x="0" y="55" width="426" height="120" rx="16" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="2" />
      <text x="213" y="105" text-anchor="middle" class="hand-title" font-size="32" fill="#15803D">⚡ Atomic In-Memory Hit</text>
      <text x="213" y="145" text-anchor="middle" class="hand-body" font-size="24" fill="#166534">0 Heap Allocations • Zero GC Overhead</text>
      
      <!-- Bullets -->
      <text x="0" y="225" class="hand-body" font-size="26" fill="#334155">• In Cache? Served in 5 nanoseconds!</text>
      <text x="0" y="270" class="hand-body" font-size="26" fill="#334155">• Cache Miss? Coalesces duplicate traffic:</text>
      <text x="20" y="312" class="hand-body" font-size="25" fill="#15803D">50 simultaneous users = 1 database call!</text>
      
      <!-- Badge -->
      <rect x="0" y="345" width="260" height="42" rx="12" fill="#DCFCE7" />
      <text x="130" y="374" text-anchor="middle" class="hand-title" font-size="24" fill="#15803D">🛡️ Stampede Protected</text>
    </g>
  </g>

  <!-- ARROW 2 -> 3 -->
  <g transform="translate(1195, 510)">
    <path d="M 10 0 C 40 -15, 60 15, 90 0" fill="none" stroke="#16A34A" stroke-width="4.5" stroke-linecap="round" marker-end="url(#arrow-green)" />
    <text x="50" y="-22" text-anchor="middle" class="hand-body" font-size="24" fill="#16A34A">Analyze</text>
  </g>

  <!-- STEP 3: MARKOV PREDICTOR -->
  <g transform="translate(1300, 270)" class="card-shadow">
    <!-- Card Container -->
    <rect x="0" y="0" width="490" height="520" rx="24" fill="#FFFFFF" stroke="#9333EA" stroke-width="3.5" />
    <!-- Top Accent Bar -->
    <path d="M 0 24 Q 0 0 24 0 L 466 0 Q 490 0 490 24 L 490 60 L 0 60 Z" fill="#F3E8FF" />
    <text x="30" y="42" class="hand-title" font-size="30" fill="#7E22CE">STEP 3: AI "CRYSTAL BALL"</text>
    
    <!-- Card Content -->
    <g transform="translate(32, 100)">
      <text x="0" y="25" class="hand-title" font-size="44" fill="#0F172A">Predicts Next Click</text>
      
      <!-- Speech bubble / Thought box -->
      <rect x="0" y="55" width="426" height="120" rx="16" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="2" />
      <text x="213" y="102" text-anchor="middle" class="hand-title" font-size="28" fill="#7E22CE">"85% chance this user will</text>
      <text x="213" y="142" text-anchor="middle" class="hand-title" font-size="30" fill="#9333EA">click '/checkout' next!"</text>
      
      <!-- Bullets -->
      <text x="0" y="225" class="hand-body" font-size="26" fill="#334155">• Markov chain tracks route transitions</text>
      <text x="0" y="270" class="hand-body" font-size="26" fill="#334155">• Extremely fast lock-free matrix</text>
      <text x="0" y="315" class="hand-body" font-size="26" fill="#334155">• Runs on backend &amp; browser (WASM!)</text>
      
      <!-- Badge -->
      <rect x="0" y="345" width="240" height="42" rx="12" fill="#F3E8FF" />
      <text x="120" y="374" text-anchor="middle" class="hand-title" font-size="24" fill="#7E22CE">🔮 Smart Prediction</text>
    </g>
  </g>

  <!-- ARROW 3 -> 4 -->
  <g transform="translate(1795, 510)">
    <path d="M 10 0 C 40 -15, 60 15, 90 0" fill="none" stroke="#9333EA" stroke-width="4.5" stroke-linecap="round" marker-end="url(#arrow-purple)" />
    <text x="50" y="-22" text-anchor="middle" class="hand-body" font-size="24" fill="#9333EA">Pre-fetch</text>
  </g>

  <!-- STEP 4: SPECULATIVE PRE-WARMER -->
  <g transform="translate(1900, 270)" class="card-shadow">
    <!-- Card Container -->
    <rect x="0" y="0" width="400" height="520" rx="24" fill="#FFFFFF" stroke="#D97706" stroke-width="3.5" />
    <!-- Top Accent Bar -->
    <path d="M 0 24 Q 0 0 24 0 L 376 0 Q 400 0 400 24 L 400 60 L 0 60 Z" fill="#FEF3C7" />
    <text x="25" y="42" class="hand-title" font-size="30" fill="#B45309">STEP 4: PRE-WARMER</text>
    
    <!-- Card Content -->
    <g transform="translate(26, 100)">
      <text x="0" y="25" class="hand-title" font-size="42" fill="#0F172A">Loads in Background</text>
      
      <!-- Sketch box -->
      <rect x="0" y="55" width="348" height="120" rx="16" fill="#FFFBEB" stroke="#FDE68A" stroke-width="2" />
      <text x="174" y="105" text-anchor="middle" class="hand-title" font-size="30" fill="#B45309">Workers Pre-warm</text>
      <text x="174" y="145" text-anchor="middle" class="hand-body" font-size="24" fill="#D97706">GET /api/v1/checkout</text>
      
      <!-- Bullets -->
      <text x="0" y="225" class="hand-body" font-size="25" fill="#334155">• Background workers execute route</text>
      <text x="0" y="270" class="hand-body" font-size="25" fill="#334155">• Response placed directly into cache</text>
      <text x="0" y="315" class="hand-body" font-size="25" fill="#334155">• User hasn't even clicked yet!</text>
      
      <!-- Badge -->
      <rect x="0" y="345" width="220" height="42" rx="12" fill="#FEF3C7" />
      <text x="110" y="374" text-anchor="middle" class="hand-title" font-size="24" fill="#B45309">🚀 Ahead of Time</text>
    </g>
  </g>

  <!-- ==================== BIG BOTTOM HERO PAYOFF BANNER ==================== -->
  <g transform="translate(100, 840)" class="hero-shadow">
    <!-- Main Result Card -->
    <rect x="0" y="0" width="2200" height="410" rx="28" fill="#FFFFFF" stroke="#4F46E5" stroke-width="4" />
    
    <!-- Top Decorative Gradient Header -->
    <path d="M 0 28 Q 0 0 28 0 L 2172 0 Q 2200 0 2200 28 L 2200 70 L 0 70 Z" fill="#EEF2FF" />
    <text x="50" y="48" class="hand-title" font-size="34" fill="#4338CA">
      🎉 THE BIG PAYOFF: WHAT THE USER EXPERIENCES
    </text>

    <!-- Content Columns inside Payoff Card -->
    <g transform="translate(50, 110)">
      <!-- Left: Big Punchline Message -->
      <text x="0" y="45" class="hand-title" font-size="52" fill="#0F172A">
        When the user finally clicks "/checkout" ➔ <tspan fill="#16A34A" font-size="58">0ms Load Time!</tspan> ⚡
      </text>
      <text x="0" y="98" class="hand-body" font-size="32" fill="#475569">
        The response is already waiting in memory. No database query. No network spinner. Instant page transition.
      </text>
      
      <!-- Horizontal divider -->
      <line x1="0" y1="135" x2="2100" y2="135" stroke="#E2E8F0" stroke-width="2" stroke-dasharray="10 8" />

      <!-- 5 Key Metric / Value Cards -->
      <!-- Card 1 -->
      <g transform="translate(0, 160)">
        <rect x="0" y="0" width="390" height="105" rx="18" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
        <text x="25" y="42" class="hand-title" font-size="36" fill="#0284C7">&lt; 5 ns Hit</text>
        <text x="25" y="80" class="hand-body" font-size="24" fill="#64748B">Zero-alloc lock-free L1 cache</text>
      </g>
      
      <!-- Card 2 -->
      <g transform="translate(425, 160)">
        <rect x="0" y="0" width="390" height="105" rx="18" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
        <text x="25" y="42" class="hand-title" font-size="36" fill="#16A34A">100% Defense</text>
        <text x="25" y="80" class="hand-body" font-size="24" fill="#64748B">Coalesces traffic spikes</text>
      </g>

      <!-- Card 3 -->
      <g transform="translate(850, 160)">
        <rect x="0" y="0" width="390" height="105" rx="18" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
        <text x="25" y="42" class="hand-title" font-size="36" fill="#9333EA">Markov Prediction</text>
        <text x="25" y="80" class="hand-body" font-size="24" fill="#64748B">Real-time session learning</text>
      </g>

      <!-- Card 4 -->
      <g transform="translate(1275, 160)">
        <rect x="0" y="0" width="390" height="105" rx="18" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
        <text x="25" y="42" class="hand-title" font-size="36" fill="#D97706">W3C Speculation</text>
        <text x="25" y="80" class="hand-body" font-size="24" fill="#64748B">Browser cache &amp; WASM client</text>
      </g>

      <!-- Card 5 -->
      <g transform="translate(1700, 160)">
        <rect x="0" y="0" width="400" height="105" rx="18" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="2" />
        <text x="25" y="42" class="hand-title" font-size="36" fill="#4338CA">1 Line of Go</text>
        <text x="25" y="80" class="hand-body" font-size="24" fill="#4F46E5">http.ListenAndServe(engine(mux))</text>
      </g>
    </g>
  </g>

</svg>"""
    return svg

def build_html_preview():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Precog High-Level Architecture</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Patrick+Hand&display=swap" rel="stylesheet">
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: #0F172A;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      font-family: 'Patrick Hand', 'Caveat', cursive, sans-serif;
    }}
    .container {{
      width: 2400px;
      height: 1350px;
      max-width: 100%;
      height: auto;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }}
    svg {{
      width: 100%;
      height: 100%;
      display: block;
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- SVG will be loaded here -->
    <img src="precog-architecture.svg" alt="Precog High-Level Architecture" style="width:100%; height:100%;" />
  </div>
</body>
</html>"""

def main():
    print("Loading fonts...")
    fonts = get_base64_fonts()
    
    print("Generating SVG...")
    svg_content = build_svg(fonts)
    with open(SVG_PATH, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG written to: {SVG_PATH}")

    # Also build index.html
    html_content = build_html_preview()
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML preview written to: {HTML_PATH}")

    # Render PNG using headless Chrome
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    temp_png = r"C:\Users\adams\AppData\Local\Temp\precog_arch_temp.png"
    if os.path.exists(temp_png):
        os.remove(temp_png)

    print("Rendering high-resolution PNG (2400 x 1350) via headless Chrome...")
    # Render SVG directly via file URL so embedded fonts render perfectly
    svg_file_url = f"file:///{SVG_PATH.replace(os.sep, '/')}"
    cmd = [
        chrome_path,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--window-size=2400,1350",
        "--hide-scrollbars",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=2000",
        f"--screenshot={temp_png}",
        svg_file_url
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Chrome screenshot failed: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    import shutil
    if os.path.exists(temp_png):
        shutil.copyfile(temp_png, PNG_PATH)
        os.remove(temp_png)
        print(f"Successfully generated high-resolution PNG: {PNG_PATH}")
    else:
        print(f"Error: Screenshot file was not created at {temp_png}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
