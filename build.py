#!/usr/bin/env python3
"""Generates the static pages. Run: python3 build.py"""
# ---- Content that must be confirmed by HybridAI (see README) ----
EMAIL_CONTACT="contact@hybrid.ai"
EMAIL_CAREERS="careers@hybridai.com"   # Figma contact page uses hybrid.ai, careers page uses hybridai.com
PHONE_DISPLAY="1 (833) 247 - 4968";PHONE_TEL="+18332474968"
SOCIAL=[("Facebook",""),("GitHub",""),("Slack",""),("LinkedIn","https://www.linkedin.com/company/hybridai-ai/"),("X","")]  # only the company LinkedIn is verified; empty = shown as placeholder
CONTACT_HREF="contact.html#contact-form"
_n=[0]
def star(size=32):
    _n[0]+=1;i=_n[0]
    pts=[("M16 0c1.400 8 4.600 12.600 0 16C11.400 12.600 14.600 8 16 0z","#2bb3b8"),   # top: teal
         ("M32 16c-8 1.400-12.600 4.600-16 0 3.400-4.600 8-1.400 16 0z","#7a4fb8"),       # right: purple
         ("M16 32c-1.400-8-4.600-12.600 0-16 4.600 3.400 1.400 8 0 16z","#2f5fa8"),        # bottom: blue
         ("M0 16c8-1.400 12.600-4.600 16 0-3.400 4.600-8 1.400-16 0z","#3f8fd0")]          # left: light blue
    paths="".join(f'<path d="{d}" fill="{c}"/>' for d,c in pts)
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 32 32" aria-hidden="true">{paths}'
      '<path fill="#fff" d="M16 10.500c.6 3.300 2.200 4.900 5.500 5.500-3.300.6-4.900 2.200-5.500 5.500-.6-3.300-2.200-4.900-5.500-5.500 3.300-.6 4.900-2.200 5.500-5.500z"/></svg>')
def wordmark():
    lam='<svg class="lam" viewBox="0 0 14 15" aria-hidden="true"><path d="M1.500 14 7 1.500 12.500 14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return f'<span class="wm" aria-label="HybridAI">Hybrid{lam}I</span>'
def logo():return f'<a class="logo" href="index.html">{star()}{wordmark()}</a>'
SPARK='<svg class="spark" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 0c.8 7 3.400 9.600 12 12-8.600 2.400-11.200 5-12 12-.8-7-3.400-9.600-12-12C8.600 9.600 11.200 7 12 0z"/></svg>'
SPARK_O='<svg class="sparko" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M12 2c.9 6.500 3.500 9.100 10 10-6.500.9-9.100 3.500-10 10-.9-6.500-3.500-9.100-10-10 6.500-.9 9.100-3.500 10-10z"/></svg>'
ICO={
"fb":'<path d="M13.500 21v-8h2.700l.4-3.200h-3.100V7.800c0-.9.3-1.500 1.600-1.500h1.700V3.400c-.3 0-1.300-.1-2.400-.1-2.400 0-4.100 1.500-4.100 4.200v2.300H7.500V13h2.800v8z"/>',
"gh":'<path d="M12 .5C5.650.5.500 5.650.500 12c0 5.080 3.290 9.390 7.860 10.910.58.100.79-.25.79-.56v-2c-3.200.7-3.870-1.370-3.870-1.370-.52-1.330-1.280-1.690-1.280-1.690-1.050-.71.080-.7.080-.7 1.160.08 1.770 1.190 1.770 1.190 1.030 1.770 2.700 1.260 3.360.96.1-.75.4-1.260.73-1.550-2.550-.29-5.240-1.280-5.240-5.690 0-1.260.45-2.280 1.190-3.090-.12-.29-.52-1.460.11-3.050 0 0 .97-.31 3.170 1.180a11 11 0 0 1 5.760 0c2.200-1.490 3.170-1.180 3.170-1.180.63 1.590.23 2.760.11 3.050.74.81 1.190 1.830 1.190 3.090 0 4.420-2.690 5.390-5.250 5.680.41.36.78 1.060.78 2.140v3.170c0 .31.21.67.8.56A11.500 11.500 0 0 0 23.500 12C23.500 5.650 18.350.5 12 .5z"/>',
"sl":'<g fill="none" stroke="currentColor" stroke-width="2.200" stroke-linecap="round"><path d="M9.500 3.500v17M14.500 3.500v17M3.500 9.500h17M3.500 14.500h17"/></g>',
"in":'<path d="M20.450 20.450h-3.560v-5.570c0-1.330-.03-3.040-1.850-3.040-1.860 0-2.140 1.450-2.140 2.940v5.670H9.350V9h3.410v1.560h.05c.48-.9 1.640-1.850 3.370-1.850 3.600 0 4.270 2.370 4.270 5.460v6.280zM5.340 7.430a2.060 2.060 0 1 1 0-4.120 2.060 2.060 0 0 1 0 4.120zM7.120 20.450H3.560V9h3.560v11.450z"/>',
"x":'<path d="M18.244 2.250h3.308l-7.227 8.260 8.502 11.240H16.170l-5.214-6.817L4.990 21.750H1.680l7.730-8.835L1.254 2.250H8.080l4.713 6.231zm-1.161 17.520h1.833L7.084 4.126H5.117z"/>'}
def ico(k,cls="ico"):return f'<svg class="{cls}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{ICO[k]}</svg>'
SOC_KEYS=["fb","gh","sl","in","x"]
def socials():
    out=[]
    for (n,u),k in zip(SOCIAL,SOC_KEYS):
        if u:out.append(f'<a href="{u}" target="_blank" rel="noopener noreferrer" aria-label="HybridAI on {n}">{ico(k)}</a>')
        else:out.append(f'<span class="ph" title="{n} URL to be supplied" aria-label="{n} (URL to be supplied)">{ico(k)}</span>')
    return '<div class="soc">'+"".join(out)+'</div><p class="tbc-note">Facebook, GitHub, Slack and X links: URL to be supplied.</p>'
PH='<svg class="li" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.500 1.500a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>'
ML='<svg class="li" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
NAV=[("index.html","Home"),("team.html","Meet Our Team"),("platform.html","Platform Overview"),("careers.html","Careers")]
def page(file,title,desc,body):
    nav="".join(f'<li><a href="{h}"{" aria-current=page" if h==file else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · HybridAI</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Poppins:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css"></head><body><a class="skip" href="#main">Skip to content</a>
<header><div class="wrap nav">{logo()}
<button class="menu" aria-label="Menu" aria-expanded="false">☰</button><nav aria-label="Main"><ul>{nav}<li class="mob"><a class="btn fill" href="{CONTACT_HREF}">Contact Us</a></li></ul></nav><a class="btn out" href="{CONTACT_HREF}">Contact Us</a></div></header>
<main id="main">{body}</main>
<footer><div class="wrap"><div class="fgrid"><div>{logo()}<p>HybridAI is a cutting-edge SaaS and on-premise platform designed to revolutionize how companies manage and optimize their IT and AI infrastructure resources through the datacenter lifecycle.</p>
{socials()}</div>
<div><h4>SUPPORT</h4><ul><li><a href="{CONTACT_HREF}">Contact Us</a></li></ul></div>
<div><h4>RESOURCES</h4><ul><li><a href="careers.html">Careers</a></li><li><a href="blog.html">Blog</a></li></ul></div>
<div><h4>COMPANY</h4><ul><li><a href="team.html">Our Team</a></li><li><a href="platform.html">Our Platform</a></li><li><a href="privacy.html">Privacy Policy</a></li><li><a href="terms.html">Terms &amp; Conditions</a></li></ul></div></div>
<p class="copy">Copyright © 2025 Hybrid AI</p></div></footer><script src="assets/app.js"></script></body></html>'''
def ic(p):return f'<svg viewBox="0 0 48 48">{p}</svg>'
I={"plan":ic('<rect x="10" y="6" width="26" height="36" rx="3"/><rect x="16" y="14" width="14" height="10" rx="2"/><path d="M20 28h6M23 10v4"/>'),
"auto":ic('<circle cx="30" cy="14" r="6"/><path d="M30 5v3M30 20v3M21 14h3M36 14h3M6 36h10l8-4h10"/>'),
"cost":ic('<circle cx="24" cy="24" r="17"/><path d="M28 17c-1-2-7-3-8 0s8 3 8 6-7 4-9 1M24 11v26"/>'),
"pred":ic('<circle cx="28" cy="20" r="12"/><path d="M19 29 8 40M24 16h8v8h-8z"/>'),
"clock":ic('<circle cx="24" cy="24" r="18"/><path d="M24 12v13h10"/>'),
"users":ic('<circle cx="16" cy="14" r="6"/><path d="M5 38c0-8 5-12 11-12s11 4 11 12M32 10a6 6 0 0 1 0 10M36 30c3 2 5 5 5 8"/>'),
"chart":ic('<rect x="6" y="32" width="8" height="8"/><rect x="20" y="24" width="8" height="16"/><rect x="34" y="14" width="8" height="26"/><path d="M26 4h12v12M38 4 20 20"/>'),
"ease":ic('<rect x="6" y="6" width="34" height="28" rx="2"/><path d="M12 14h14M12 20h10M30 26l2 14 4-5 5 2z"/>'),
"flex":ic('<path d="M24 42V24M24 24 10 14M24 24l14-10M6 18l4-6 6 3M42 18l-4-6-6 3M20 10l4-6 4 6"/>'),
"bulb":ic('<path d="M16 34V30C10 26 8 22 8 17a16 16 0 1 1 32 0c0 5-2 9-8 13v4zM16 40h16M20 44h8M26 12l-6 10h8l-6 10"/>')}
def feat(k,t,d,full=False):return f'<div class="feat reveal{" full" if full else ""}">{I[k]}<h3>{t}</h3><p>{d}</p></div>'
home=f'''<section class="hero wrap"><span class="sp s1">{SPARK}</span><span class="sp s2">{SPARK}</span><span class="sp s3">{SPARK}</span><span class="sp s4">{SPARK}</span><h1 class="reveal">Empower your AI strategy — accelerate enterprise agility with Agentic AI workflow automation and enhance performance tuning across clouds with Predictive AI.</h1>
<p class="reveal">Juggling on-premises and cloud resources? Scattered infrastructure and mismatched services slowing you down? HybridAI uses advanced AI to analyze and integrate your entire infrastructure, optimizing performance, eliminating waste, and slashing resource needs. Get a streamlined, efficient system that works smarter, not harder.</p>
<div class="cta reveal"><a class="btn fill" href="{CONTACT_HREF}">{SPARK_O}Book a Demo</a><a class="btn out" href="{CONTACT_HREF}">Enquire Now</a></div></section>
<section class="s wrap"><p class="eyebrow">About Us</p><h2>Who We Are</h2><p class="lead reveal">HybridAI empowers enterprises to accelerate AI innovation and deployment while reducing operational costs by transforming how AI and IT infrastructure resources are planned, automated, and optimized. By intelligently aligning resource allocation with workload demands and utilization, it delivers measurable improvements in performance, energy efficiency, and total cost of ownership (TCO).</p><a class="btn fill" href="team.html">Meet Our Team</a></section>
<section class="s wrap"><p class="eyebrow">Our Process</p><h2>How We Work</h2><p class="lead reveal">HybridAI’s patented innovation, Automating the Resource Lifecycle – Plan, Orchestrate, Predict, and Optimize, is driven by the xPU Resource Engine, which intelligently models and provisions AI infrastructure resources based on workload characteristics, including compute intensity, latency sensitivity, and power constraints. Utilizing agentic AI, it orchestrates end-to-end AI data center workflows—from AI model frameworks to heterogeneous infrastructure components such as GPUs, CPUs, memory, and storage. The engine continuously optimizes resource allocation through real-time telemetry, predictive analytics, and utilization data to maximize performance density, power efficiency, and system throughput.</p></section>
<section class="s wrap"><p class="eyebrow">Our Solution</p><h2>What Our Customers Can Expect</h2><div class="grid">
{feat("plan","Plan and Design","Recommends type of AI infra resource based on workload and model characteristics, including compute intensity, latency sensitivity, and power constraints.")}
{feat("auto","Automation","Automate the deployment and management of AI/IT workloads across various environments, including K8, Openshift, VMware, on-premise, and cloud.")}
{feat("cost","Continuous Optimization","Maximize efficiency and cost savings with dynamic resource allocation that adapts to your evolving needs.")}
{feat("pred","Predictive Foresights","Anticipate future resource demands based on workload resource utilization patterns, preventing bottlenecks and ensuring seamless scalability.")}</div></section>
<section class="s wrap"><p class="eyebrow">Platform Overview</p><h2>Learn About Our Platform</h2><p class="lead">The HybridAI platform is purpose built for enterprise customers, underpinned by the four key capabilities of Prediction, Optimization, Recommendation, and Orchestration.</p><a class="btn fill" href="platform.html">Learn More</a></section>
<section class="s wrap"><p class="eyebrow">Why Choose Us</p><h2>The HybridAI Advantage</h2><p class="lead">Managing resources efficiently is paramount in today's complex IT landscape. HybridAI simplifies this complexity, allowing you to focus on your core business while we ensure your infrastructure operates at peak performance, power efficiency, and optimal cost. Our experienced team has a strong presence in Asia-Pacific and USA and is dedicated to your success.</p><div class="grid">
{feat("clock","Months to Minutes","Experience the power of fully automated end-to-end orchestration, performance testing, and validation of AI &amp; IT workloads. Reduce deployment time from months to mere minutes, accelerating your time to market.")}
{feat("users","Multi-Vendor Support","Enjoy unparalleled flexibility with our vendor-agnostic platform. Choose the best hardware solutions for your unique needs, avoiding vendor lock-in and maximizing your investment.")}
{feat("chart","AI-Powered Optimization","Leveraging the latest advancements in AI and machine learning, HybridAI continuously analyses and optimizes infrastructure performance, ensuring peak efficiency and cost savings. Alerting you to ensure you maximise your investments.",True)}
{feat("ease","Ease of Use","Designed with user-friendliness in mind, HybridAI simplifies complex infrastructure optimization. Its intuitive interface makes it easy for your team to adopt and realize its benefits quickly.")}
{feat("flex","Flexible Deployment Options","Deploy HybridAI on-premises or in the cloud, tailoring the solution to your specific requirements and preferences.")}</div></section>'''
def gicon(k,body):
    return (f'<svg viewBox="0 0 96 96" role="img" aria-label="{k} icon"><defs><linearGradient id="gi-{k}" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#2f5fa8"/><stop offset="1" stop-color="#3fb5c0"/></linearGradient></defs>'
            f'<g fill="none" stroke="url(#gi-{k})" stroke-width="3.500" stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>')
def label(k,t,y=53,size=17):return f'<text x="48" y="{y}" text-anchor="middle" font-family="Montserrat,sans-serif" font-weight="700" font-size="{size}" fill="url(#gi-{k})" stroke="none">{t}</text>'
pins=lambda xs,y0,y1:"".join(f"M{x} {y0}v{y1-y0}" for x in xs)
pinsx=lambda ys,x0,x1:"".join(f"M{x0} {y}h{x1-x0}" for y in ys)
I["bulb"]=gicon("predict",'<path d="M36 72v-6C26 60 22 52 22 43a26 26 0 1 1 52 0c0 9-4 17-14 23v6z"/><path d="M36 79h24M40 86h16"/><path d="M53 28 41 48h9l-5 17 14-21h-9z"/>')
I["xpu"]=gicon("optimize",'<rect x="24" y="24" width="48" height="48" rx="4"/>'+f'<path d="{pins([36,44,52,60],12,24)}{pins([36,44,52,60],72,84)}{pinsx([36,44,52,60],12,24)}{pinsx([36,44,52,60],72,84)}"/>'+'<path d="M32 40v-8h8M64 32h-0M56 32h8v8M32 56v8h8M64 56v8h-8"/>'+label("optimize","xPU"))
I["server"]=gicon("plan",''.join(f'<rect x="12" y="{y}" width="58" height="20" rx="5"/><path d="M20 {y+7}h.1M26 {y+7}h.1M32 {y+7}h.1M20 {y+13}h.1M26 {y+13}h.1M32 {y+13}h.1M52 {y+10}h10"/>' for y in (8,32,56))+'<path fill="var(--bg)" d="M54 66v14c0 4 7 7 16 7s16-3 16-7V66c0-4-7-7-16-7s-16 3-16 7z"/><path d="M54 66c0 4 7 7 16 7s16-3 16-7M54 73c0 4 7 7 16 7s16-3 16-7"/>')
I["gpu"]=gicon("orchestrate",'<rect x="16" y="26" width="64" height="44" rx="5"/>'+f'<path d="{pins([28,38,48,58,68],14,26)}{pins([28,38,48,58,68],70,82)}"/>'+'<path d="M32 36h32l6 6v12l-6 6H32l-6-6V42z"/>'+label("orchestrate","GPU",53,15))
PL=[("predict","Predict","Predict with Confidence",["Illuminate future workloads and anticipate infrastructure demands.","Smart foresight unlocked, HybridAI maps, predicts, and optimizes your infrastructure."],"bulb"),
("optimize","Optimize","Optimize with Precision",["Elevate efficiency and unleash your infrastructure’s full potential.","From prediction to performance, HybridAI maps, maximizes, and accelerates your infrastructure."],"xpu"),
("plan","Plan &amp; Design","Recommend with Intelligence",["Right-sized infrastructure, every time, no guesswork, no overspending, no delays.","HybridAI Recommendations pinpoints the perfect infrastructure, using what you have, adding only what you need."],"server"),
("orch","Orchestrate","Orchestrate with Speed",["From months to minutes, seamless execution, instant deployment, effortless orchestration.","Bring new resources online quickly or reconfigure existing resource to reduce time to value."],"gpu")]
tabs="".join(f'<button class="tab" role="tab" data-k="{k}" aria-selected="{str(i==0).lower()}">{n}</button>' for i,(k,n,_,_,_) in enumerate(PL))
panels="".join(f'<div class="panel{" on" if i==0 else ""}" data-g="pl" data-k="{k}" role="tabpanel"><div><h2 style="font-size:26px">{h}</h2><ul>{"".join(f"<li>{x}</li>" for x in b)}</ul></div>{I[ic]}</div>' for i,(k,_,h,b,ic) in enumerate(PL))
platform=f'<section class="band"><div class="wrap"><h1>Platform Overview</h1><p>The HybridAI platform is purpose built for enterprise customers, underpinned by the four key capabilities of Prediction, Optimization, Recommendation, and Orchestration.</p></div></section><div class="wrap" style="max-width:760px;padding-bottom:40px"><div class="tabs" role="tablist" data-group="pl">{tabs}</div>{panels}</div>'
TEAM=[("Rajesh Chainani","CPO and Co-Founder","rajesh"),("Ramesh Ramnath","CDO, Co-Founder","ramesh"),("Udaya Kondameedi","","udaya")]
LINKEDIN={}  # personal profiles unverified; TODO: {"Rajesh Chainani": "https://www.linkedin.com/in/..."}; icon is not linked until a URL is supplied
def li(n):
    u=LINKEDIN.get(n)
    if u:return f'<a href="{u}" aria-label="{n} on LinkedIn" target="_blank" rel="noopener noreferrer">{ico("in","li-ico")}</a>'
    return f'<span class="ph" title="LinkedIn URL to be supplied" aria-label="{n} LinkedIn (URL to be supplied)">{ico("in","li-ico")}</span>'
def card(n,r,img):
    role=f"<small>{r}</small>" if r else ""
    return f'<div class="card reveal"><img src="assets/{img}.jpg" alt="Portrait of {n}" width="432" height="576" loading="lazy"><div><span>{n}{role}</span>{li(n)}</div></div>'
team=f'''<section class="band"><div class="wrap"><h1 class="teamh">The <span class="grad">HybridAI</span> Team</h1><p>At the helm of our company is a dynamic leadership team committed to fostering growth, innovation, and excellence. With deep industry expertise and a shared passion for driving meaningful change, our leaders are dedicated to guiding our organization with vision, integrity, and strategic insight. Learn more about the individuals who inspire our direction and lead us toward a successful future.</p></div></section>
<div class="wrap"><div class="team">{"".join(card(*t) for t in TEAM)}</div></div><div class="stat"><b>100</b> years domain expertise<small class="tbc-note" style="display:block">Pending confirmation from HybridAI</small></div>
<p class="tbc-note" style="text-align:center;margin-top:16px">Team LinkedIn links: URL to be supplied.</p>
<div class="wrap"><section class="s"><h2 style="font-weight:500">Wish To Join Our Team?</h2><a class="btn fill" href="careers.html">View Vacancies</a></section></div>'''
JOBS=[("Engineering","Senior Frontend Developer"),("Engineering","Senior Backend Developer"),("Engineering","ML Platform Engineer"),("Design","Product Designer"),("Marketing","Growth Marketing Manager"),("Finance","Financial Analyst")]
jt="".join(f'<button class="tab" role="tab" data-k="{c}" aria-selected="{str(c=="Engineering").lower()}">{c}</button>' for c in ["Engineering","Design","Marketing","Finance"])
jobs="".join(f'<article class="job" data-g="jb" data-k="{c}"{"" if c=="Engineering" else " hidden"}><header><div><h3>{t}</h3><small>{c} · Remote · Full-time</small></div><a class="btn fill sm" href="contact.html?dept=Careers&amp;subject={t.replace(" ","+")}+application#contact-form">Apply Now</a></header><p style="margin:.6em 0 0">We\'re looking for an experienced {t.lower()} to join our team and help build the future of AI infrastructure.</p></article>' for c,t in JOBS)
for _ in [0]:jobs=jobs.replace('class="job" data-g="jb"','class="job on" data-g="jb"')
careers=f'''<section style="background:linear-gradient(rgba(10,20,40,.7),rgba(10,20,40,.8)),linear-gradient(135deg,#2f5fa8,#0b1220);color:#fff;text-align:center;padding:96px 20px"><h1 style="font-size:clamp(32px,5vw,48px)">JOIN OUR TEAM</h1><p style="max-width:640px;margin:auto">We are looking for talented individuals who are excited to shape the future of IT and AI infrastructure optimization.</p></section>
<div class="wrap"><div class="about"><p>At HybridAI, we are revolutionizing the way companies manage and optimize their IT and AI infrastructure. Our innovative SaaS and on-premise platform harnesses cutting-edge AI to drive efficiency, cost savings, and performance improvements. If you're passionate about technology, optimization, and making an impact in the AI-driven world, we want you on our team.</p>
<div class="perks"><div class="perk p1"><h3>Innovative Environment</h3><p>Work at the forefront of AI-driven IT infrastructure optimization.</p></div><div class="perk p2"><h3>Growth &amp; Development</h3><p>Expand your skills and expertise with access to cutting-edge tools and a collaborative team.</p></div><div class="perk p3"><h3>Trust and Transparency</h3><p>The best ideas emerge when teams collaborate with honesty, integrity, and the confidence to challenge the status quo.</p></div><div class="perk p4"><h3>Global Perspectives. Unified Vision.</h3><p>Our global team unites diverse voices, creating an inclusive environment where innovation thrives.</p></div></div></div>
<section class="s" style="padding-top:24px"><h2>Current Openings</h2><div class="tabs" role="tablist" data-group="jb" style="justify-content:flex-start">{jt}</div><div style="border-top:1px solid var(--line)">{jobs}</div></section>
<section class="s"><h2>How To Apply</h2><p class="lead">If you are excited to be part of our team, send your resume and a cover letter to <a href="mailto:{EMAIL_CAREERS}" style="color:var(--blue)">{EMAIL_CAREERS}</a> <small class="tbc">address unconfirmed</small>. Tell us about your experience, passion for AI and IT infrastructure, and how you can contribute to HybridAI.</p></section></div>'''
contact=f'''<div class="wrap contact"><div><h1>Get In Touch With Us</h1><p>At HybridAI, we optimize your IT infrastructure with AI-driven precision, ensuring smarter IT, lower costs, and greener operations. Whether you're an enterprise, cloud provider, server vendor, or consulting firm, our automated platform helps you reduce waste, enhance efficiency, and optimize resources across any infrastructure.<br>Have questions about AI costs, underutilized resources, or vendor lock-in?<br>Let's talk about right-sizing your workloads for peak performance.</p>
<ul class="cl"><li>{PH}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li><li>{ML}<a href="mailto:{EMAIL_CONTACT}">{EMAIL_CONTACT}</a> <small class="tbc">address unconfirmed</small></li></ul></div>
<form id="contact-form" data-contact="{EMAIL_CONTACT}" data-careers="{EMAIL_CAREERS}" novalidate><div><label for="f">First Name <i>*</i></label><input id="f" required autocomplete="given-name"></div><div><label for="l">Last Name <i>*</i></label><input id="l" required autocomplete="family-name"></div>
<div class="w"><label for="e">Email <i>*</i></label><input id="e" type="email" required placeholder="you@domain.com" autocomplete="email"></div>
<div class="w"><label for="d">Department <i>*</i></label><select id="d" required><option value="">- Select -</option><option>Sales</option><option>Support</option><option>Partnerships</option><option>Careers</option></select></div>
<div class="w"><label for="s">Subject <i>*</i></label><input id="s" required></div><div class="w"><label for="m">Message <i>*</i></label><textarea id="m" rows="4" required placeholder="Write your message"></textarea></div>
<div class="w"><button class="btn fill" type="submit">SUBMIT</button></div><div class="w ok" role="status"></div></form></div>'''
blog=f'''<section class="band"><div class="wrap"><h1>Blog</h1><p>Notes from the HybridAI team on AI infrastructure, resource optimization, and what we learn building a platform that plans, orchestrates, predicts, and optimizes it.</p></div></section>
<div class="wrap"><section class="s"><h2>Topics We Write About</h2><div class="grid" style="max-width:900px;grid-template-columns:repeat(3,1fr)">
{feat("pred","Predictive AI","How workload telemetry becomes forecasts of capacity, power, and cost.")}
{feat("auto","Agentic Automation","Orchestrating AI and IT workloads across Kubernetes, OpenShift, VMware, and cloud.")}
{feat("cost","Infrastructure Efficiency","Right-sizing GPUs, CPUs, memory, and storage to cut waste and total cost of ownership.")}</div>
<p class="lead" style="margin-top:40px">Our first posts are on the way. Want to hear when they land, or have a topic you would like covered?</p><a class="btn fill" href="{CONTACT_HREF}">Contact Us</a></section></div>'''
def legal(t,w,v='is'):return f'<section class="band"><div class="wrap"><h1>{t}</h1><p>The full {w} {v} being finalised and will be published here. For questions in the meantime, contact <a href="mailto:{EMAIL_CONTACT}" style="color:var(--blue)">{EMAIL_CONTACT}</a>.</p></div></section>'
for f,t,d,b in [("blog.html","Blog","Notes from the HybridAI team.",blog),("privacy.html","Privacy Policy","HybridAI privacy policy.",legal("Privacy Policy","privacy policy")),("terms.html","Terms &amp; Conditions","HybridAI terms and conditions.",legal("Terms &amp; Conditions","terms and conditions","are")),("index.html","Home","AI-driven IT infrastructure optimization.",home),("team.html","Meet Our Team","The HybridAI leadership team.",team),("platform.html","Platform Overview","Predict, optimize, plan and orchestrate.",platform),("careers.html","Careers","Join the HybridAI team.",careers),("contact.html","Contact Us","Get in touch with HybridAI.",contact)]:
    open(f,"w").write(page(f,t,d,b))
