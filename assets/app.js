const $=(s,r=document)=>[...r.querySelectorAll(s)];
$('.menu').forEach(b=>b.onclick=()=>{const n=document.querySelector('nav');b.setAttribute('aria-expanded',n.classList.toggle('open'))});
const io=new IntersectionObserver(e=>e.forEach(x=>x.isIntersecting&&(x.target.classList.add('in'),io.unobserve(x.target))),{threshold:.1});
$('.reveal').forEach(el=>io.observe(el));
$('[role=tablist]').forEach(l=>{const tabs=$('[role=tab]',l);tabs.forEach((t,i)=>{t.onclick=()=>sel(t);t.onkeydown=e=>{if(e.key==='ArrowRight')sel(tabs[(i+1)%tabs.length],1);if(e.key==='ArrowLeft')sel(tabs[(i-1+tabs.length)%tabs.length],1)}});
function sel(t,f){tabs.forEach(x=>x.setAttribute('aria-selected',x===t));if(f)t.focus();const g=l.dataset.group;$(`[data-g=${g}]`).forEach(p=>{const on=p.dataset.k===t.dataset.k;p.classList.toggle('on',on);p.hidden=!on&&p.classList.contains('job')})}});
const f=document.querySelector('form');
if(f){const q=new URLSearchParams(location.search);
const set=(id,v)=>{const e=document.getElementById(id);if(e&&v)e.value=v};
set('d',q.get('dept'));set('s',q.get('subject'));
f.onsubmit=e=>{e.preventDefault();const ok=document.querySelector('.ok');
if(!f.checkValidity()){f.reportValidity();return}
const v=id=>document.getElementById(id).value.trim(),to=v('d')==='Careers'?f.dataset.careers:f.dataset.contact;
const body=`${v('m')}\n\n— ${v('f')} ${v('l')} (${v('e')}) · ${v('d')}`;
ok.style.display='block';ok.textContent='';ok.append('Opening your email app to send this to ',Object.assign(document.createElement('a'),{href:'mailto:'+to,textContent:to}),'. If nothing opens, write to that address directly.');
location.href=`mailto:${to}?subject=${encodeURIComponent(v('s'))}&body=${encodeURIComponent(body)}`}}
