import base64

with open('/mnt/user-data/uploads/Screenshot-from-2025-07-01-13-24-06-e1751356886820.png','rb') as f:
    img_b64 = base64.b64encode(f.read()).decode()
dataurl = "data:image/jpeg;base64," + img_b64

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>ScholarBrain v2.0 — Live AI Dashboard</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css"/>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js"></script>
<style>
:root{
  --gold:#F5A623;--red:#E24B4A;--green:#4CAF82;--blue:#4A9EE0;--purple:#A99FE8;
  --surface:rgba(10,12,20,0.83);--surface2:rgba(255,255,255,0.055);
  --border:rgba(255,255,255,0.10);--text:#F0EDE6;--muted:rgba(240,237,230,0.52);
  --fh:'Syne',sans-serif;--fb:'DM Sans',sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;font-family:var(--fb);color:var(--text);overflow-x:hidden;background:#080A10}
body.panic-urgent{--gold:#E24B4A}
body.panic-urgent .logo,body.panic-urgent #brandSpan{color:var(--red)}

.hero-bg{
  position:fixed;inset:0;z-index:0;
  background-image:url('CAMPUS_IMG_HERE');
  background-size:cover;background-position:center;background-repeat:no-repeat;
  filter:brightness(0.26) saturate(0.5) contrast(1.08);
}
.hero-overlay{
  position:fixed;inset:0;z-index:1;
  background:linear-gradient(155deg,rgba(8,10,18,0.97) 0%,rgba(8,10,18,0.65) 45%,rgba(8,10,18,0.92) 100%);
}
#app{position:relative;z-index:2;min-height:100vh}
.app{display:grid;grid-template-columns:72px 1fr;min-height:100vh}

.sidebar{background:rgba(6,8,14,0.93);border-right:1px solid var(--border);display:flex;flex-direction:column;align-items:center;padding:20px 0;gap:6px;position:sticky;top:0;height:100vh;backdrop-filter:blur(20px);z-index:10}
.logo{width:40px;height:40px;background:var(--gold);border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:var(--fh);font-weight:800;font-size:17px;color:#0D0F14;margin-bottom:14px;flex-shrink:0;transition:background 0.4s}
.nav-btn{width:44px;height:44px;border-radius:10px;border:none;background:transparent;color:var(--muted);font-size:20px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all 0.2s;position:relative;flex-shrink:0}
.nav-btn:hover,.nav-btn.active{background:rgba(245,166,35,0.14);color:var(--gold)}
.tooltip{position:absolute;left:58px;background:rgba(6,8,14,0.96);color:var(--text);font-size:12px;padding:4px 10px;border-radius:6px;white-space:nowrap;pointer-events:none;opacity:0;transition:opacity 0.18s;border:1px solid var(--border);font-family:var(--fb);z-index:200}
.nav-btn:hover .tooltip{opacity:1}
.nav-sep{width:32px;height:1px;background:var(--border);margin:6px 0}
.nav-bottom{margin-top:auto}

.main{display:flex;flex-direction:column;overflow:hidden;min-height:100vh}
.topbar{padding:12px 22px;display:flex;align-items:center;gap:14px;border-bottom:1px solid var(--border);background:rgba(6,8,14,0.76);backdrop-filter:blur(16px);position:sticky;top:0;z-index:50}
.topbar-title{font-family:var(--fh);font-weight:800;font-size:19px;color:var(--text);white-space:nowrap;display:flex;align-items:center;gap:6px}
.topbar-title span{color:var(--gold);transition:color 0.4s}
.search-bar{flex:1;max-width:440px;position:relative;display:flex;gap:6px}
.search-bar input{flex:1;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:8px 14px 8px 36px;color:var(--text);font-size:13px;font-family:var(--fb);outline:none;transition:border-color 0.2s}
.search-bar input:focus{border-color:rgba(245,166,35,0.45)}
.search-bar input::placeholder{color:var(--muted)}
.search-bar .si{position:absolute;left:10px;top:50%;transform:translateY(-50%);color:var(--muted);font-size:16px;pointer-events:none}
.voice-btn{width:34px;height:34px;border-radius:8px;border:1px solid var(--border);background:var(--surface2);color:var(--muted);cursor:pointer;font-size:16px;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:all 0.2s}
.voice-btn:hover,.voice-btn.listening{background:rgba(226,75,74,0.15);border-color:rgba(226,75,74,0.4);color:#F09595}
.voice-btn.listening{animation:micPulse 1s infinite}
@keyframes micPulse{0%,100%{box-shadow:0 0 0 0 rgba(226,75,74,0.3)}50%{box-shadow:0 0 0 6px rgba(226,75,74,0)}}
.topbar-right{margin-left:auto;display:flex;align-items:center;gap:8px}
.standup-btn{background:rgba(245,166,35,0.11);border:1px solid rgba(245,166,35,0.28);color:var(--gold);padding:7px 12px;border-radius:8px;font-size:12px;font-family:var(--fb);cursor:pointer;font-weight:500;display:flex;align-items:center;gap:5px;transition:all 0.2s;white-space:nowrap}
.standup-btn:hover{background:rgba(245,166,35,0.20)}
.panic-btn{background:rgba(226,75,74,0.14);border:1px solid rgba(226,75,74,0.32);color:#F09595;padding:7px 12px;border-radius:8px;font-size:12px;font-family:var(--fb);cursor:pointer;font-weight:500;display:flex;align-items:center;gap:5px;transition:all 0.2s;white-space:nowrap}
.panic-btn:hover{background:rgba(226,75,74,0.24)}
.avatar{width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--gold),#C87919);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:11px;color:#0D0F14;cursor:pointer;flex-shrink:0;user-select:none}

.content{padding:18px 22px;display:flex;flex-direction:column;gap:16px;overflow-y:auto;flex:1}
.content::-webkit-scrollbar{width:4px}
.content::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.1);border-radius:2px}

.greeting-bar{display:flex;align-items:center;gap:16px;padding:14px 18px;background:var(--surface);border:1px solid var(--border);border-radius:14px;backdrop-filter:blur(10px)}
.date-label{font-size:11px;color:var(--muted);margin-bottom:3px}
.greet-heading{font-family:var(--fh);font-size:21px;font-weight:700;line-height:1.2}
.greet-heading .gold{color:var(--gold)}
.greet-sub{font-size:12px;color:var(--muted);margin-top:3px}
.energy-chip{margin-left:auto;display:flex;align-items:center;gap:7px;background:rgba(76,175,130,0.11);border:1px solid rgba(76,175,130,0.24);padding:6px 12px;border-radius:20px;font-size:11px;color:var(--green);font-weight:500;white-space:nowrap;flex-shrink:0}
.energy-dot{width:7px;height:7px;border-radius:50%;background:var(--green);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:0.4;transform:scale(0.75)}}

.stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.stat-box{background:var(--surface2);border-radius:10px;padding:14px 16px;border:1px solid var(--border);backdrop-filter:blur(8px)}
.stat-box .val{font-family:var(--fh);font-size:28px;font-weight:700}
.stat-box .lbl{font-size:11px;color:var(--muted);margin-top:4px}
.val.red{color:var(--red)}.val.gold{color:var(--gold)}.val.green{color:var(--green)}

.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:18px;backdrop-filter:blur(10px)}
.card-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.card-head h3{font-family:var(--fh);font-size:13px;font-weight:600;display:flex;align-items:center;gap:7px}
.badge{font-size:10px;font-weight:600;padding:2px 8px;border-radius:10px;font-family:var(--fb)}
.badge-red   {background:rgba(226,75,74,0.14);  color:#F09595;      border:1px solid rgba(226,75,74,0.2)}
.badge-gold  {background:rgba(245,166,35,0.11);  color:var(--gold);  border:1px solid rgba(245,166,35,0.2)}
.badge-green {background:rgba(76,175,130,0.11);  color:var(--green); border:1px solid rgba(76,175,130,0.2)}
.badge-blue  {background:rgba(74,158,224,0.11);  color:var(--blue);  border:1px solid rgba(74,158,224,0.2)}
.badge-purple{background:rgba(169,159,232,0.11); color:var(--purple);border:1px solid rgba(169,159,232,0.2)}
.live-tag{font-size:10px;color:var(--green);font-weight:700;margin-left:4px;vertical-align:middle}

.scheduler-blocks{display:flex;flex-direction:column;gap:5px}
.time-block{display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:8px;border:1px solid var(--border);cursor:pointer;transition:all 0.2s}
.time-block:hover{border-color:rgba(245,166,35,0.3)}
.time-label{font-size:10px;color:var(--muted);width:58px;flex-shrink:0;font-weight:500}
.block-bar{height:26px;border-radius:6px;flex:1;display:flex;align-items:center;padding:0 10px;font-size:12px;font-weight:500}
.block-bar.high  {background:rgba(226,75,74,0.11); border:1px solid rgba(226,75,74,0.2);   color:#F09595}
.block-bar.med   {background:rgba(245,166,35,0.09); border:1px solid rgba(245,166,35,0.18); color:#F5C475}
.block-bar.low-b {background:rgba(76,175,130,0.08); border:1px solid rgba(76,175,130,0.16); color:var(--green)}
.block-bar.empty {background:transparent;border:1px dashed var(--border);color:var(--muted);font-style:italic}
.block-weight{font-size:10px;color:var(--muted);flex-shrink:0;width:34px;text-align:right}

.cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;margin-bottom:10px}
.cal-day-header{font-size:10px;color:var(--muted);text-align:center;padding:3px 0;font-weight:500}
.cal-day{aspect-ratio:1;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:11px;cursor:pointer;transition:all 0.15s;position:relative}
.cal-day:hover{background:var(--surface2)}
.cal-day.today{background:rgba(245,166,35,0.2);color:var(--gold);font-weight:700}
.cal-day.has-event::after{content:'';position:absolute;bottom:2px;left:50%;transform:translateX(-50%);width:4px;height:4px;border-radius:50%;background:var(--red)}
.cal-day.other-month{color:rgba(240,237,230,0.18)}
.event-list .ev{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border)}
.event-list .ev:last-child{border-bottom:none}
.ev-time{font-size:11px;color:var(--muted);width:52px;flex-shrink:0;font-weight:500}
.ev-bar{width:3px;border-radius:2px;flex-shrink:0;align-self:stretch;min-height:26px}
.ev-text .name{font-size:13px;font-weight:500}
.ev-text .loc{font-size:11px;color:var(--muted);margin-top:1px}

.bot-chat{display:flex;flex-direction:column;gap:8px;max-height:190px;overflow-y:auto}
.bot-chat::-webkit-scrollbar{width:3px}
.bot-chat::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.1);border-radius:2px}
.msg{padding:9px 12px;border-radius:8px;font-size:13px;line-height:1.5}
.msg.incoming{background:rgba(245,166,35,0.07);border:1px solid rgba(245,166,35,0.14)}
.msg.parsed  {background:rgba(76,175,130,0.07);border:1px solid rgba(76,175,130,0.14)}
.parse-tag{display:inline-block;background:rgba(76,175,130,0.15);color:var(--green);font-size:10px;font-weight:700;padding:1px 6px;border-radius:4px;margin-bottom:5px;letter-spacing:0.06em}
.parse-body{color:var(--text);font-size:12px;line-height:1.6}
.bot-input-row{display:flex;gap:8px;margin-top:10px}
.bot-input-row input{flex:1;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:8px 12px;color:var(--text);font-size:13px;font-family:var(--fb);outline:none}
.bot-input-row input:focus{border-color:rgba(245,166,35,0.4)}
.bot-input-row input::placeholder{color:var(--muted)}
.bot-input-row button{background:rgba(245,166,35,0.13);border:1px solid rgba(245,166,35,0.28);color:var(--gold);padding:8px 14px;border-radius:8px;cursor:pointer;font-size:12px;font-family:var(--fb);font-weight:500;display:flex;align-items:center;gap:5px;transition:all 0.2s;white-space:nowrap}
.bot-input-row button:hover{background:rgba(245,166,35,0.22)}

.ocr-zone{border:1.5px dashed rgba(245,166,35,0.3);border-radius:10px;padding:22px;text-align:center;cursor:pointer;transition:all 0.2s}
.ocr-zone:hover,.ocr-zone.drag-over{border-color:rgba(245,166,35,0.65);background:rgba(245,166,35,0.04)}
.ocr-zone i{font-size:28px;color:rgba(245,166,35,0.5);display:block;margin-bottom:8px}
.ocr-zone p{font-size:13px;color:var(--muted)}
.ocr-zone small{font-size:11px;color:rgba(245,166,35,0.5);margin-top:4px;display:block}
.ocr-progress{margin-top:10px;font-size:12px;color:var(--gold)}
.ocr-bar-wrap{height:3px;background:rgba(245,166,35,0.15);border-radius:2px;margin-top:8px;overflow:hidden}
.ocr-bar-fill{height:100%;background:var(--gold);border-radius:2px;transition:width 0.3s;width:0%}
.ocr-result{margin-top:12px}
.ocr-result-label{font-size:11px;color:var(--green);font-weight:700;letter-spacing:0.06em;margin-bottom:8px}
.ocr-raw{font-size:11px;color:var(--muted);line-height:1.6;max-height:60px;overflow-y:auto;background:var(--surface2);border:1px solid var(--border);border-radius:6px;padding:8px;margin-bottom:8px;white-space:pre-wrap}
.task-item{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border)}
.task-item:last-child{border-bottom:none;padding-bottom:0}
.task-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}
.task-dot.urgent{background:var(--red)}.task-dot.medium{background:var(--gold)}.task-dot.low{background:var(--green)}
.task-info .t-title{font-size:13px;font-weight:500}
.task-info .t-meta{font-size:11px;color:var(--muted);margin-top:2px}
.task-del{margin-left:auto;background:transparent;border:none;color:var(--muted);cursor:pointer;font-size:16px;padding:2px 4px;transition:color 0.2s;flex-shrink:0}
.task-del:hover{color:var(--red)}

.audio-player{background:rgba(245,166,35,0.05);border:1px solid rgba(245,166,35,0.18);border-radius:10px;padding:14px;display:flex;flex-direction:column;gap:10px}
.audio-waveform{display:flex;align-items:center;gap:3px;height:40px;justify-content:center}
.wave-bar{width:4px;background:rgba(245,166,35,0.28);border-radius:2px;transition:height 0.22s,background 0.22s}
.audio-controls{display:flex;align-items:center;gap:12px}
.play-btn{width:36px;height:36px;border-radius:50%;background:var(--gold);border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;color:#0D0F14;font-size:16px;flex-shrink:0;transition:transform 0.15s}
.play-btn:hover{transform:scale(1.08)}
.audio-info .a-title{font-size:13px;font-weight:500}
.audio-info .a-sub{font-size:11px;color:var(--muted);margin-top:1px}
.audio-time{font-size:12px;color:var(--muted);white-space:nowrap}
.audio-progress{width:100%;height:4px;background:rgba(245,166,35,0.14);border-radius:2px;cursor:pointer}
.audio-fill{height:100%;background:var(--gold);border-radius:2px;transition:width 0.4s linear}
.briefing-text{background:rgba(245,166,35,0.04);border:1px solid rgba(245,166,35,0.1);border-radius:8px;padding:12px;font-size:12px;color:var(--muted);line-height:1.75;margin-top:8px}

.capsule-list{display:flex;flex-direction:column;gap:8px}
.capsule-item{display:flex;align-items:center;gap:10px;padding:10px;border-radius:8px;background:var(--surface2);border:1px solid var(--border);cursor:pointer;transition:all 0.2s}
.capsule-item:hover{border-color:rgba(169,159,232,0.38);background:rgba(169,159,232,0.05)}
.capsule-icon{width:34px;height:34px;border-radius:8px;background:rgba(169,159,232,0.13);display:flex;align-items:center;justify-content:center;font-size:16px;color:var(--purple);flex-shrink:0}
.capsule-info .c-name{font-size:13px;font-weight:500}
.capsule-info .c-tabs{font-size:11px;color:var(--muted);margin-top:2px}
.capsule-launch{margin-left:auto;font-size:11px;font-weight:500;color:var(--purple);background:rgba(169,159,232,0.1);padding:3px 8px;border-radius:6px;border:1px solid rgba(169,159,232,0.2);white-space:nowrap}
.cap-actions{display:flex;gap:8px;margin-top:12px}
.cap-btn{flex:1;background:var(--surface2);border:1px solid var(--border);color:var(--muted);padding:7px;border-radius:8px;font-size:12px;cursor:pointer;font-family:var(--fb);display:flex;align-items:center;justify-content:center;gap:5px;transition:all 0.2s}
.cap-btn:hover{border-color:rgba(245,166,35,0.3);color:var(--text)}
.cap-btn.purple{background:rgba(169,159,232,0.07);border-color:rgba(169,159,232,0.2);color:var(--purple)}
.cap-btn.purple:hover{background:rgba(169,159,232,0.14)}

.search-input-row{display:flex;gap:8px;margin-bottom:12px}
.search-input-row input{flex:1;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:8px 12px;color:var(--text);font-size:13px;font-family:var(--fb);outline:none}
.search-input-row input:focus{border-color:rgba(74,158,224,0.4)}
.search-input-row input::placeholder{color:var(--muted)}
.search-input-row button{background:rgba(74,158,224,0.1);border:1px solid rgba(74,158,224,0.25);color:var(--blue);padding:8px 14px;border-radius:8px;cursor:pointer;font-size:13px;font-family:var(--fb);font-weight:500;transition:all 0.2s;white-space:nowrap}
.search-input-row button:hover{background:rgba(74,158,224,0.18)}
.search-result-item{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid var(--border)}
.search-result-item:last-child{border-bottom:none}
.result-source{font-size:10px;font-weight:700;letter-spacing:0.05em;padding:2px 6px;border-radius:4px;flex-shrink:0;margin-top:2px}
.source-wa  {background:rgba(76,175,130,0.14);color:var(--green)}
.source-lms {background:rgba(74,158,224,0.14);color:var(--blue)}
.source-mail{background:rgba(245,166,35,0.14);color:var(--gold)}
.r-text{font-size:13px;line-height:1.5}
.r-text .highlight{color:var(--gold);font-weight:500}
.r-text .when{font-size:11px;color:var(--muted);margin-top:2px}
.nlp-hint{font-size:12px;color:var(--muted);padding:10px 0;font-style:italic}

.webhook-item{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid var(--border)}
.webhook-item:last-child{border-bottom:none}
.wh-icon{width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.wh-icon.placement{background:rgba(245,166,35,0.13);color:var(--gold)}
.wh-icon.deadline {background:rgba(226,75,74,0.11); color:#F09595}
.wh-icon.schedule {background:rgba(74,158,224,0.11);color:var(--blue)}
.wh-body .wh-title{font-size:13px;font-weight:500}
.wh-body .wh-from {font-size:11px;color:var(--muted);margin-top:2px}
.wh-time{margin-left:auto;font-size:11px;color:var(--muted);white-space:nowrap;flex-shrink:0}
.urgent-dot{width:7px;height:7px;border-radius:50%;background:var(--red);margin-top:5px;flex-shrink:0;animation:pulse 1.5s infinite}

.chart-wrap{position:relative;height:175px;width:100%}
.heatmap-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:4px}
.hm-cell{padding:12px 10px;border-radius:8px;text-align:center;cursor:default;transition:transform 0.15s}
.hm-cell:hover{transform:scale(1.03)}
.hm-label{font-size:10px;color:rgba(240,237,230,0.6);margin-bottom:6px;font-weight:500;line-height:1.3}
.hm-val{font-family:var(--fh);font-size:20px;font-weight:700}

.panic-overlay{display:none;position:fixed;inset:0;z-index:300;background:rgba(6,8,14,0.97);align-items:center;justify-content:center;flex-direction:column}
.panic-overlay.active{display:flex}
.panic-mode-card{background:rgba(226,75,74,0.06);border:1.5px solid rgba(226,75,74,0.28);border-radius:20px;padding:48px;text-align:center;max-width:520px;width:90%;position:relative}
.panic-label{font-size:11px;font-weight:700;letter-spacing:0.1em;color:var(--red);margin-bottom:16px;text-transform:uppercase}
.panic-task{font-family:var(--fh);font-size:30px;font-weight:800;margin-bottom:8px}
.panic-due{font-size:15px;color:var(--red);margin-bottom:26px}
.panic-actions{display:flex;gap:12px;justify-content:center}
.panic-actions button{padding:10px 20px;border-radius:10px;font-size:14px;font-family:var(--fb);cursor:pointer;font-weight:500;transition:all 0.2s}
.pa-start{background:rgba(226,75,74,0.18);border:1px solid rgba(226,75,74,0.38);color:#F09595}
.pa-start:hover{background:rgba(226,75,74,0.28)}
.pa-skip {background:var(--surface2);border:1px solid var(--border);color:var(--muted)}
.pa-skip:hover{color:var(--text)}
.pa-exit{position:absolute;top:16px;right:16px;background:transparent;border:none;color:var(--muted);cursor:pointer;font-size:22px;display:flex;align-items:center;padding:4px;transition:color 0.2s}
.pa-exit:hover{color:var(--text)}

.toast{position:fixed;bottom:28px;right:28px;background:rgba(10,12,20,0.95);border:1px solid var(--border);border-radius:10px;padding:12px 18px;font-size:13px;color:var(--text);z-index:500;transform:translateY(80px);opacity:0;transition:all 0.35s;backdrop-filter:blur(12px);max-width:340px;line-height:1.4}
.toast.show{transform:translateY(0);opacity:1}
.toast.green{border-color:rgba(76,175,130,0.3)}
.toast.redT{border-color:rgba(226,75,74,0.3)}

.storage-chip{display:inline-flex;align-items:center;gap:4px;font-size:10px;color:var(--green);background:rgba(76,175,130,0.08);border:1px solid rgba(76,175,130,0.2);padding:2px 7px;border-radius:10px;font-family:var(--fb);font-weight:500}

.add-task-row{display:flex;gap:8px;margin-top:10px}
.add-task-row input{flex:1;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:7px 11px;color:var(--text);font-size:12px;font-family:var(--fb);outline:none}
.add-task-row input:focus{border-color:rgba(245,166,35,0.4)}
.add-task-row input::placeholder{color:var(--muted)}
.add-task-row button{background:rgba(245,166,35,0.13);border:1px solid rgba(245,166,35,0.28);color:var(--gold);padding:7px 12px;border-radius:8px;cursor:pointer;font-size:12px;font-family:var(--fb);font-weight:500;white-space:nowrap;transition:all 0.2s}
.add-task-row button:hover{background:rgba(245,166,35,0.22)}

.install-bar{display:none;align-items:center;gap:10px;padding:10px 22px;background:rgba(245,166,35,0.07);border-bottom:1px solid rgba(245,166,35,0.18);font-size:13px;color:var(--text)}
.install-bar.show{display:flex}
.install-bar button.ib{background:var(--gold);border:none;color:#0D0F14;padding:5px 13px;border-radius:6px;cursor:pointer;font-size:12px;font-weight:600;font-family:var(--fb);margin-left:auto}
.install-bar .ib-close{background:transparent;border:none;color:var(--muted);cursor:pointer;font-size:20px;padding:0 4px}

@media(max-width:900px){.grid-2{grid-template-columns:1fr}.search-bar{max-width:180px}.standup-btn span,.panic-btn span{display:none}}
</style>
</head>
<body>
<div id="installBar" class="install-bar">
  <i class="ti ti-device-mobile" style="color:var(--gold)"></i>
  <span>Install ScholarBrain as a PWA for offline access</span>
  <button class="ib" id="installBtn">Install App</button>
  <button class="ib-close" id="installClose">×</button>
</div>

<div id="app">
  <div class="hero-bg"></div>
  <div class="hero-overlay"></div>

  <div class="panic-overlay" id="panicOverlay">
    <button class="pa-exit" id="panicClose"><i class="ti ti-x"></i></button>
    <div class="panic-mode-card">
      <div class="panic-label">⚡ Panic Mode — One Task at a Time</div>
      <div class="panic-task" id="panicTask">Compiler Design Assignment</div>
      <div class="panic-due" id="panicDue">Due: Tonight 11:59 PM · Cognitive Weight: 9/10</div>
      <div class="panic-actions">
        <button class="pa-start" id="panicStart"><i class="ti ti-player-play"></i> Start Now</button>
        <button class="pa-skip" id="panicSkip"><i class="ti ti-chevron-right"></i> Next Priority</button>
      </div>
    </div>
  </div>
  <div class="toast" id="toast"></div>

  <div class="app">
    <nav class="sidebar">
      <div class="logo">SB</div>
      <button class="nav-btn active"><i class="ti ti-layout-dashboard"></i><span class="tooltip">Dashboard</span></button>
      <button class="nav-btn"><i class="ti ti-calendar"></i><span class="tooltip">Calendar</span></button>
      <button class="nav-btn"><i class="ti ti-checklist"></i><span class="tooltip">Smart Tasks</span></button>
      <button class="nav-btn"><i class="ti ti-brand-telegram"></i><span class="tooltip">Bot Parser</span></button>
      <div class="nav-sep"></div>
      <button class="nav-btn"><i class="ti ti-package"></i><span class="tooltip">Capsules</span></button>
      <button class="nav-btn"><i class="ti ti-search"></i><span class="tooltip">NLP Search</span></button>
      <button class="nav-btn"><i class="ti ti-briefcase"></i><span class="tooltip">Placement</span></button>
      <div class="nav-sep"></div>
      <div class="nav-bottom">
        <button class="nav-btn"><i class="ti ti-settings"></i><span class="tooltip">Settings</span></button>
      </div>
    </nav>

    <div class="main">
      <header class="topbar">
        <div class="topbar-title">Scholar<span id="brandSpan">Brain</span>&nbsp;<span class="storage-chip"><i class="ti ti-cloud-check"></i> localStorage</span></div>
        <div class="search-bar">
          <i class="ti ti-search si"></i>
          <input type="text" id="globalSearch" placeholder="Ask anything — 'When is my quiz?', 'Show urgent tasks'..."/>
          <button class="voice-btn" id="voiceBtn" title="Voice Search (Web Speech API)"><i class="ti ti-microphone" id="voiceIcon"></i></button>
        </div>
        <div class="topbar-right">
          <button class="standup-btn" id="standupBtn"><i class="ti ti-microphone"></i> Daily Standup</button>
          <button class="panic-btn" id="panicTrigger"><i class="ti ti-alert-triangle"></i> Panic Mode</button>
          <div class="avatar">KS</div>
        </div>
      </header>

      <div class="content">
        <div class="greeting-bar">
          <div>
            <div class="date-label" id="dateLabel"></div>
            <h2 class="greet-heading" id="greetHead">Good morning, <span class="gold">Krish</span> &#128075;</h2>
            <p class="greet-sub">You have 3 urgent items and 2 placement alerts today.</p>
          </div>
          <div class="energy-chip"><div class="energy-dot"></div>&nbsp;Peak Energy: 9 AM &#8211; 1 PM</div>
        </div>

        <div class="stat-row">
          <div class="stat-box"><div class="val red">3</div><div class="lbl">Urgent Tasks</div></div>
          <div class="stat-box"><div class="val gold">7</div><div class="lbl">Due This Week</div></div>
          <div class="stat-box"><div class="val green">2</div><div class="lbl">Placement Alerts</div></div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-head">
              <h3><i class="ti ti-brain" style="color:var(--gold)"></i> Cognitive Scheduler</h3>
              <span class="badge badge-gold">Energy-Aware + Persistent</span>
            </div>
            <div class="scheduler-blocks" id="schedulerBlocks"></div>
            <div class="add-task-row">
              <input type="text" id="newTaskInput" placeholder="Add custom task to schedule..."/>
              <button id="addTaskBtn">+ Add</button>
            </div>
          </div>
          <div class="card">
            <div class="card-head">
              <h3><i class="ti ti-calendar-event" style="color:var(--blue)"></i> Calendar</h3>
              <span class="badge badge-blue">May 2026</span>
            </div>
            <div class="cal-grid" id="calGrid"></div>
            <div class="event-list" id="eventList"></div>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-head">
              <h3><i class="ti ti-brand-whatsapp" style="color:var(--green)"></i> Forward-to-Brain Bot</h3>
              <span class="badge badge-green">NLP Intent Engine</span>
            </div>
            <div class="bot-chat" id="botChat"></div>
            <div class="bot-input-row">
              <input type="text" id="botInput" placeholder="Forward any WhatsApp / Telegram message..."/>
              <button id="botSend"><i class="ti ti-arrow-right"></i> Parse</button>
            </div>
          </div>
          <div class="card">
            <div class="card-head">
              <h3><i class="ti ti-upload" style="color:var(--gold)"></i> OCR Ingestor <span class="live-tag">LIVE</span></h3>
              <span class="badge badge-gold">Tesseract.js</span>
            </div>
            <input type="file" id="ocrFile" accept="image/*" style="display:none"/>
            <div class="ocr-zone" id="ocrZone">
              <i class="ti ti-photo-scan"></i>
              <p>Drop image or click to upload</p>
              <small>Real OCR via Tesseract.js &#8212; extracts text from any image</small>
            </div>
            <div class="ocr-progress" id="ocrProgress" style="display:none">
              <div id="ocrStatus">Initializing OCR engine...</div>
              <div class="ocr-bar-wrap"><div class="ocr-bar-fill" id="ocrBarFill"></div></div>
            </div>
            <div class="ocr-result" id="ocrResult" style="display:none"></div>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-head">
              <h3><i class="ti ti-microphone" style="color:var(--gold)"></i> AI Voice Daily Standup</h3>
              <span class="badge badge-gold">Web Speech TTS</span>
            </div>
            <div class="audio-player">
              <div class="audio-waveform" id="waveform"></div>
              <div class="audio-controls">
                <button class="play-btn" id="playBtn"><i class="ti ti-player-play" id="playIcon"></i></button>
                <div class="audio-info">
                  <div class="a-title">Morning Briefing &#8212; <span id="briefDate"></span></div>
                  <div class="a-sub">3 urgent &#183; 2 alerts &#183; 5 events &#183; ~60 sec</div>
                </div>
                <span class="audio-time" id="audioTime">0:00</span>
              </div>
              <div class="audio-progress" id="audioProg"><div class="audio-fill" id="audioFill" style="width:0%"></div></div>
            </div>
            <div class="briefing-text">"Good morning, Krish. You have <strong>3 urgent tasks</strong>. Compiler Design is due <strong>tonight at 11:59 PM</strong>. Peak energy window is active &#8212; tackle it first. <strong style="color:var(--gold)">TCS shortlist is out</strong>: drive at 4:30 PM in the Seminar Hall. CN Quiz at 2 PM in LT-3. Lab is in Room 402. Stay focused. You&#8217;ve got this."</div>
          </div>
          <div class="card">
            <div class="card-head">
              <h3><i class="ti ti-package" style="color:var(--purple)"></i> Context Capsules</h3>
              <span class="badge badge-purple">1-Click Focus + Persistent</span>
            </div>
            <div class="capsule-list" id="capsuleList"></div>
            <div class="cap-actions">
              <button class="cap-btn" id="addCapsuleBtn"><i class="ti ti-plus"></i> New Capsule</button>
              <button class="cap-btn purple"><i class="ti ti-puzzle"></i> Extension Guide</button>
            </div>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-head">
              <h3><i class="ti ti-search" style="color:var(--blue)"></i> Semantic Search</h3>
              <span class="badge badge-blue">NLP + Vector Matching</span>
            </div>
            <div class="search-input-row">
              <input type="text" id="vSearch" placeholder="'When is the quiz?' / 'Urgent tasks today?'"/>
              <button id="vSearchBtn">Search</button>
            </div>
            <div id="vResults"></div>
          </div>
          <div class="card">
            <div class="card-head">
              <h3><i class="ti ti-bell-ringing" style="color:var(--red)"></i> Placement Webhooks</h3>
              <span class="badge badge-red">2 New Alerts</span>
            </div>
            <div id="webhookList"></div>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-head">
              <h3><i class="ti ti-chart-line" style="color:var(--blue)"></i> Weekly Focus Score</h3>
              <span class="badge badge-blue">Chart.js Live</span>
            </div>
            <div class="chart-wrap"><canvas id="focusChart"></canvas></div>
          </div>
          <div class="card">
            <div class="card-head">
              <h3><i class="ti ti-flame" style="color:var(--red)"></i> Cognitive Load Heatmap</h3>
              <span class="badge badge-red">Per Subject</span>
            </div>
            <div class="heatmap-grid" id="heatmapGrid"></div>
          </div>
        </div>

        <div style="height:28px"></div>
      </div>
    </div>
  </div>
</div>

<script>
// ═══════════ ScholarBrain v2.0 — Live JS Engine ═══════════

// localStorage persistence
const LS={
  get(k,d){try{const v=localStorage.getItem('sb_'+k);return v?JSON.parse(v):d}catch{return d}},
  set(k,v){try{localStorage.setItem('sb_'+k,JSON.stringify(v))}catch{}}
};

let tasks=LS.get('tasks',[
  {id:1,task:'Compiler Design Assignment',type:'high', weight:9,due:'Tonight 11:59 PM'},
  {id:2,task:'OS Lab Report',            type:'med',  weight:6,due:'Monday 9 AM'},
  {id:3,task:'Email Triage + Review',    type:'low-b',weight:2,due:'8 AM'},
  {id:4,task:'CN Quiz Prep',             type:'med',  weight:5,due:'Today 2 PM'},
  {id:5,task:'Feedback Form',            type:'low-b',weight:1,due:'This week'},
]);
let capsules=LS.get('capsules',[
  {icon:'ti-code',    name:'Compiler Design',tabs:'LMS Page · Notion Notes · GFG Lex/Yacc · YouTube'},
  {icon:'ti-network', name:'CN Quiz Prep',   tabs:'Past Papers · Slides · GFG OSI Model'},
  {icon:'ti-cpu',     name:'OS Lab Report',  tabs:'LMS Submit · Lab Manual · Notion Template'},
]);

const events=[
  {time:'10:30 AM',name:'Compiler Design Lab',  loc:'Room 402 · Prof. Sharma',    color:'#E24B4A'},
  {time:'2:00 PM', name:'CN Quiz',              loc:'LT-3 · Assignment due before',color:'#F5A623'},
  {time:'4:30 PM', name:'Placement Drive — TCS',loc:'Seminar Hall · Bring ID',     color:'#4A9EE0'},
];
const panicTasks=[
  {task:'Compiler Design Assignment',due:'Due: Tonight 11:59 PM · Weight: 9/10'},
  {task:'CN Quiz Prep',              due:'Due: Today 2:00 PM · Weight: 5/10'},
  {task:'OS Lab Report',             due:'Due: Monday 9 AM · Weight: 6/10'},
];

function $id(id){return document.getElementById(id)}
function toast(msg,type){
  const t=$id('toast');
  t.textContent=msg;t.className='toast show '+(type||'');
  setTimeout(()=>t.className='toast',2800);
}

// DATE
function initDate(){
  const now=new Date();
  $id('dateLabel').textContent=now.toLocaleDateString('en-IN',{weekday:'long',year:'numeric',month:'long',day:'numeric'});
  const short=now.toLocaleDateString('en-IN',{weekday:'long',month:'short',day:'numeric'});
  $id('briefDate').textContent=short;
  const h=now.getHours();
  const gr=h<12?'Good morning':h<17?'Good afternoon':'Good evening';
  $id('greetHead').innerHTML=gr+', <span class="gold">Krish</span> \uD83D\uDC4B';
}

// SCHEDULER
const schedBlocks=[
  {time:'8\u20139 AM',  task:'Email Triage + Review',  type:'low-b',weight:2},
  {time:'9\u201311 AM', task:'',                        type:'high', weight:9},
  {time:'11\u201312 PM',task:'',                        type:'med',  weight:6},
  {time:'12\u20132 PM', task:'Lunch (Protected)',        type:'empty',weight:null},
  {time:'2\u20134 PM',  task:'',                        type:'med',  weight:5},
  {time:'4\u20135 PM',  task:'Feedback Form + Admin',   type:'low-b',weight:1},
];
function renderScheduler(){
  const b=[...schedBlocks];
  if(tasks[0])b[1].task=tasks[0].task;
  if(tasks[1])b[2].task=tasks[1].task;
  if(tasks[3])b[4].task=tasks[3].task;
  $id('schedulerBlocks').innerHTML=b.map(s=>`
    <div class="time-block">
      <span class="time-label">${s.time}</span>
      <div class="block-bar ${s.type}">${s.task||'Free Slot'}</div>
      <span class="block-weight">${s.weight!==null?'Wt:'+s.weight:'&#8212;'}</span>
    </div>`).join('');
}
$id('addTaskBtn').onclick=()=>{
  const v=$id('newTaskInput').value.trim();if(!v)return;
  tasks.push({id:Date.now(),task:v,type:'med',weight:5,due:'TBD'});
  LS.set('tasks',tasks);$id('newTaskInput').value='';
  renderScheduler();toast('\u2705 Task saved to localStorage!','green');
};

// CALENDAR
function renderCalendar(){
  const evDays=[2,5,8,11,14,16,17,18,20,22,25,28,30];
  const days=['Su','Mo','Tu','We','Th','Fr','Sa'];
  let h=days.map(d=>`<div class="cal-day-header">${d}</div>`).join('');
  const prefix=[26,27,28,29,30].map(d=>({d,o:true}));
  const may=Array.from({length:31},(_,i)=>({d:i+1,o:false}));
  const cells=[...prefix,...may];
  while(cells.length<35)cells.push({d:cells.length-34,o:true});
  h+=cells.map(({d,o})=>{
    const iT=!o&&d===16,hE=!o&&evDays.includes(d);
    return `<div class="cal-day${o?' other-month':''}${iT?' today':''}${hE?' has-event':''}">${d}</div>`;
  }).join('');
  $id('calGrid').innerHTML=h;
  $id('eventList').innerHTML=events.map(e=>`
    <div class="ev">
      <span class="ev-time">${e.time}</span>
      <div class="ev-bar" style="background:${e.color}"></div>
      <div class="ev-text"><div class="name">${e.name}</div><div class="loc">${e.loc}</div></div>
    </div>`).join('');
}

// BOT — NLP intent parsing
function parseIntent(msg){
  if(/room|lab|shift|moved|venue/i.test(msg)){
    const rm=msg.match(/room\s*\d+/i);
    return `\uD83D\uDCCD Location update \u2192 ${rm?rm[0]:'New venue detected'}\n\u23F0 Calendar updated automatically\n\uD83D\uDD14 Alert pushed to dashboard`;
  }
  if(/due|deadline|submit|tonight/i.test(msg))
    return `\u23F0 Deadline extracted\n\uD83D\uDCCB Task injected into Cognitive Scheduler\n\uD83D\uDD14 Reminder: 3h before`;
  if(/tcs|infosys|wipro|shortlist|placement/i.test(msg))
    return `\uD83C\uDFAF Placement keyword detected\n\uD83D\uDCE7 High-priority webhook triggered\n\uD83D\uDCC5 Drive added to Calendar`;
  if(/quiz|exam|test|viva/i.test(msg))
    return `\uD83D\uDCDD Academic event detected\n\uD83D\uDCC5 Added to Calendar\n\u23F0 Study block auto-scheduled`;
  if(/cancel|postponed|off|holiday/i.test(msg))
    return `\uD83D\uDDD1\uFE0F Cancellation detected\n\uD83D\uDCC5 Event removed from Calendar`;
  return `\uD83D\uDD0D Saved as note in localStorage\n\uD83D\uDCA1 Include time/date for auto-scheduling`;
}
function addBotMsg(type,text,parsed){
  const d=document.createElement('div');d.className='msg '+type;
  if(type==='incoming')d.textContent=text;
  else d.innerHTML=`<div class="parse-tag">\u2736 AI PARSED</div><div class="parse-body">${parsed.replace(/\n/g,'<br>')}</div>`;
  $id('botChat').appendChild(d);$id('botChat').scrollTop=99999;
}
function initBot(){
  [
    {f:'Prof shifted the lab to Room 402, due tonight \uD83D\uDE4F',p:'\uD83D\uDCCD Lab \u2192 Room 402\n\u23F0 Deadline Tonight 11:59 PM\n\uD83D\uDCC5 Calendar updated'},
    {f:'TCS shortlist is out \u2014 check email NOW!!',p:'\uD83C\uDFAF TCS Shortlist detected\n\uD83D\uDCE7 High-priority alert pushed\n\uD83D\uDCC5 Drive: Today 4:30 PM'},
  ].forEach(s=>{addBotMsg('incoming',s.f);addBotMsg('parsed',null,s.p)});
  const send=()=>{
    const v=$id('botInput').value.trim();if(!v)return;
    addBotMsg('incoming',v);$id('botInput').value='';
    setTimeout(()=>addBotMsg('parsed',null,parseIntent(v)),600);
  };
  $id('botSend').onclick=send;
  $id('botInput').addEventListener('keydown',e=>{if(e.key==='Enter')send()});
}

// LIVE OCR — Tesseract.js
function initOCR(){
  const zone=$id('ocrZone'),fi=$id('ocrFile');
  zone.onclick=()=>fi.click();
  zone.ondragover=e=>{e.preventDefault();zone.classList.add('drag-over')};
  zone.ondragleave=()=>zone.classList.remove('drag-over');
  zone.ondrop=e=>{e.preventDefault();zone.classList.remove('drag-over');handleOCR(e.dataTransfer.files[0])};
  fi.onchange=()=>{if(fi.files[0])handleOCR(fi.files[0])};
}
async function handleOCR(file){
  if(!file||!file.type.startsWith('image/'))return toast('\u26A0\uFE0F Upload an image file','redT');
  const zone=$id('ocrZone'),prog=$id('ocrProgress'),result=$id('ocrResult');
  zone.style.display='none';prog.style.display='block';result.style.display='none';
  $id('ocrBarFill').style.width='0%';
  try{
    const worker=await Tesseract.createWorker('eng',1,{
      logger:m=>{
        if(m.status==='recognizing text'){
          const p=Math.round(m.progress*100);
          $id('ocrBarFill').style.width=p+'%';
          $id('ocrStatus').textContent='Extracting text... '+p+'%';
        } else {
          $id('ocrStatus').textContent=m.status.charAt(0).toUpperCase()+m.status.slice(1)+'...';
        }
      }
    });
    const {data:{text}}=await worker.recognize(file);
    await worker.terminate();
    prog.style.display='none';result.style.display='block';
    renderOCR(text);
    toast('\u2705 OCR complete! Text extracted.','green');
  }catch(e){
    prog.style.display='none';zone.style.display='block';
    toast('\u26A0\uFE0F OCR error: '+e.message,'redT');
  }
}
function renderOCR(raw){
  const lines=raw.split('\n').map(l=>l.trim()).filter(l=>l.length>4).slice(0,5);
  const items=lines.length?lines.map((l,i)=>({
    dot:i===0?'urgent':i===1?'medium':'low',
    title:l.length>70?l.slice(0,70)+'…':l,
    meta:(/due|submit|deadline|exam|quiz/i.test(l)?'\u23F0 Deadline detected':'📝 Extracted item')+' · Saved to localStorage'
  })):[{dot:'low',title:'No readable text found',meta:'Try a clearer image with printed text'}];

  const saved=LS.get('ocrItems',[]);saved.push({ts:Date.now(),raw,items});LS.set('ocrItems',saved);

  $id('ocrResult').innerHTML=`
    <div class="ocr-result-label">\u2736 TESSERACT OCR + AI ACTION EXTRACTION</div>
    <div class="ocr-raw">${raw.slice(0,250)||'(No text detected)'}${raw.length>250?'...':''}</div>
    ${items.map(it=>`<div class="task-item">
      <div class="task-dot ${it.dot}"></div>
      <div class="task-info"><div class="t-title">${it.title}</div><div class="t-meta">${it.meta}</div></div>
      <button class="task-del" onclick="this.closest('.task-item').remove()">\u00D7</button>
    </div>`).join('')}
    <button onclick="$id('ocrZone').style.display='block';$id('ocrResult').style.display='none';$id('ocrProgress').style.display='none'"
      style="margin-top:10px;background:var(--surface2);border:1px solid var(--border);color:var(--muted);padding:5px 11px;border-radius:6px;font-size:12px;cursor:pointer;font-family:var(--fb)">
      <i class="ti ti-refresh"></i> Scan Another Image
    </button>`;
}

// AUDIO — Web Speech API TTS
let playing=false,ttsU=null,audInv=null,audPct=0,audSec=0;
function initWaveform(){
  for(let i=0;i<14;i++){const b=document.createElement('div');b.className='wave-bar';b.id='wb'+i;b.style.height=(8+Math.random()*18)+'px';$id('waveform').appendChild(b)}
}
function animWave(){
  for(let i=0;i<14;i++){const b=$id('wb'+i);if(b){b.style.height=(6+Math.random()*32)+'px';b.style.background=`rgba(245,166,35,${(0.3+Math.random()*0.55).toFixed(2)})`}}
}
function buildBriefing(){
  const now=new Date();
  const ds=now.toLocaleDateString('en-IN',{weekday:'long',month:'long',day:'numeric',year:'numeric'});
  return `Good morning Krish. Today is ${ds}. You have 3 urgent tasks. Your Compiler Design submission is due tonight at 11:59 PM. Your peak energy window is active now, so tackle it first. TCS shortlist is out, placement drive is at 4:30 PM in the Seminar Hall. CN Quiz at 2 PM in LT-3. Lab is in Room 402. Stay focused. ScholarBrain has your back.`;
}
function togglePlay(){
  playing=!playing;
  $id('playIcon').className=playing?'ti ti-player-pause':'ti ti-player-play';
  if(playing){
    if('speechSynthesis' in window){
      window.speechSynthesis.cancel();
      ttsU=new SpeechSynthesisUtterance(buildBriefing());
      ttsU.rate=0.95;ttsU.pitch=1.0;ttsU.volume=1.0;
      const vs=window.speechSynthesis.getVoices();
      const en=vs.find(v=>v.lang.startsWith('en')&&v.name.toLowerCase().includes('female'))||vs.find(v=>v.lang.startsWith('en'))||vs[0];
      if(en)ttsU.voice=en;
      ttsU.onend=()=>{playing=false;$id('playIcon').className='ti ti-player-play';clearInterval(audInv)};
      window.speechSynthesis.speak(ttsU);
      toast('\uD83C\uDFA4 Speaking via Web Speech TTS...','green');
    }
    audInv=setInterval(()=>{
      audPct=Math.min(100,audPct+100/60/5);
      audSec=Math.round(audPct/100*60);
      $id('audioFill').style.width=audPct+'%';
      $id('audioTime').textContent='0:'+String(audSec).padStart(2,'0');
      animWave();
      if(audPct>=100){clearInterval(audInv);playing=false;$id('playIcon').className='ti ti-player-play'}
    },200);
  } else {
    window.speechSynthesis&&window.speechSynthesis.cancel();
    clearInterval(audInv);
  }
}
$id('audioProg').onclick=e=>{
  const r=$id('audioProg').getBoundingClientRect();
  audPct=Math.round((e.clientX-r.left)/r.width*100);
  audSec=Math.round(audPct/100*60);
  $id('audioFill').style.width=audPct+'%';
  $id('audioTime').textContent='0:'+String(audSec).padStart(2,'0');
};
$id('playBtn').onclick=togglePlay;
$id('standupBtn').onclick=()=>{if(!playing)togglePlay();else toast('\u25B6\uFE0F Already playing briefing','')};

// CAPSULES (persistent)
function renderCapsules(){
  $id('capsuleList').innerHTML=capsules.map((c,i)=>`
    <div class="capsule-item" onclick="launchCap(${i})">
      <div class="capsule-icon"><i class="ti ${c.icon}"></i></div>
      <div class="capsule-info"><div class="c-name">${c.name}</div><div class="c-tabs">${c.tabs}</div></div>
      <div class="capsule-launch">Launch \u2192</div>
    </div>`).join('');
}
function launchCap(i){
  const c=capsules[i];
  toast(`\uD83D\uDE80 "${c.name}" launched\nIn production: opens tabs + blocks YouTube/Instagram via Chrome Extension API`,'green');
}
$id('addCapsuleBtn').onclick=()=>{
  const n=prompt('Capsule name:');if(!n)return;
  const t=prompt('Tab descriptions (comma separated):');if(!t)return;
  capsules.push({icon:'ti-bookmark',name:n,tabs:t});
  LS.set('capsules',capsules);renderCapsules();
  toast('\u2705 Capsule saved!','green');
};

// NLP SEMANTIC SEARCH
const searchDB=[
  {kw:['quiz','cn quiz','when is quiz','network quiz','computer network'],  src:'LMS',   cls:'source-lms',  text:'CN Quiz scheduled &#8212; May 16, 2:00 PM in LT-3',           when:'Computer Networks \xB7 3 days ago'},
  {kw:['lab','room','which room','lab room','where is lab'],                src:'WhatsApp',cls:'source-wa', text:'Lab shifted to Room 402 &#8212; Prof. Sharma confirmed',         when:'CS-B Group \xB7 2h ago'},
  {kw:['placement','tcs','shortlist','drive','company'],                   src:'Email',  cls:'source-mail', text:'TCS Shortlist announced &#8212; Drive today 4:30 PM',           when:'placements@college.edu \xB7 1h ago'},
  {kw:['assignment','compiler','due','tonight'],                           src:'LMS',   cls:'source-lms',  text:'Compiler Design assignment due Tonight 11:59 PM',               when:'CS-B LMS \xB7 Today'},
  {kw:['urgent','all tasks','pending','what is urgent'],                   src:'System', cls:'source-lms', text:'3 urgent tasks: Compiler Design, CN Quiz, OS Lab',              when:'ScholarBrain \xB7 Real-time'},
  {kw:['infosys','reschedule','postpone'],                                 src:'Email',  cls:'source-mail', text:'Infosys Drive rescheduled to May 20',                          when:'careers@infosys.com \xB7 3h ago'},
  {kw:['os','operating system','lab report'],                              src:'LMS',   cls:'source-lms',  text:'OS Lab Report due Monday 9 AM',                                 when:'CS-B LMS \xB7 2 days ago'},
  {kw:['feedback','form'],                                                 src:'LMS',   cls:'source-lms',  text:'Course Feedback Form due this week',                            when:'Department \xB7 4 days ago'},
];
function nlpSearch(q){
  const l=q.toLowerCase().trim();if(!l)return null;
  let best=null,bestScore=0;
  const tokens=l.split(/\s+/);
  for(const item of searchDB){
    let score=0;
    for(const kw of item.kw){
      if(l.includes(kw))score+=kw.split(' ').length*2;
      else for(const t of tokens)if(t.length>2&&kw.includes(t))score+=1;
    }
    if(score>bestScore){bestScore=score;best=item}
  }
  return bestScore>0?best:null;
}
function runSearch(){
  const q=$id('vSearch').value.trim();if(!q)return;
  const m=nlpSearch(q);
  $id('vResults').innerHTML=m
    ?`<div class="search-result-item"><span class="result-source ${m.cls}">${m.src}</span><div class="r-text"><span class="highlight">${m.text}</span><div class="when">${m.when}</div></div></div>`
    :`<div class="nlp-hint">No match. Try: "quiz", "lab room", "TCS placement", "urgent tasks"</div>`;
}
$id('vSearchBtn').onclick=runSearch;
$id('vSearch').addEventListener('keydown',e=>{if(e.key==='Enter')runSearch()});
$id('globalSearch').addEventListener('keydown',e=>{
  if(e.key==='Enter'){$id('vSearch').value=$id('globalSearch').value;runSearch();$id('vSearch').scrollIntoView({behavior:'smooth',block:'center'})}
});

// VOICE SEARCH — Web Speech API
function initVoice(){
  const btn=$id('voiceBtn');
  if(!('webkitSpeechRecognition' in window||'SpeechRecognition' in window)){btn.title='Not supported in this browser';return}
  const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  const sr=new SR();sr.lang='en-IN';sr.continuous=false;sr.interimResults=false;
  sr.onresult=e=>{const t=e.results[0][0].transcript;$id('globalSearch').value=t;$id('vSearch').value=t;runSearch();toast('\uD83C\uDFA4 Heard: "'+t+'"','green')};
  sr.onend=()=>{btn.classList.remove('listening');$id('voiceIcon').className='ti ti-microphone'};
  sr.onerror=()=>{btn.classList.remove('listening');toast('\u26A0\uFE0F Mic access denied','redT')};
  btn.onclick=()=>{
    if(btn.classList.contains('listening'))sr.stop();
    else{sr.start();btn.classList.add('listening');$id('voiceIcon').className='ti ti-microphone-off';toast('\uD83C\uDFA4 Listening... Speak now','');}
  };
}

// WEBHOOKS
function renderWebhooks(){
  const data=[
    {cls:'placement',icon:'ti-briefcase',  title:'TCS Shortlist Announced',       from:'Gmail \xB7 keyword: "Shortlist"',        time:'1h ago',  urgent:true},
    {cls:'placement',icon:'ti-building',   title:'Infosys Drive Rescheduled',     from:'Gmail \xB7 keyword: "Rescheduled"',      time:'3h ago',  urgent:true},
    {cls:'deadline', icon:'ti-alert-circle',title:'Compiler Design \u2014 Final Reminder',from:'LMS \xB7 keyword: "deadline tonight"', time:'5h ago',  urgent:false},
    {cls:'schedule', icon:'ti-clock',      title:'Lab Room Changed to 402',       from:'WhatsApp Bot \xB7 Injected to Calendar', time:'2h ago',  urgent:false},
  ];
  $id('webhookList').innerHTML=data.map(w=>`
    <div class="webhook-item">
      <div class="wh-icon ${w.cls}"><i class="ti ${w.icon}"></i></div>
      <div class="wh-body"><div class="wh-title">${w.title}</div><div class="wh-from">${w.from}</div></div>
      <div class="wh-time">${w.time}</div>
      ${w.urgent?'<div class="urgent-dot"></div>':''}
    </div>`).join('');
}

// CHARTS — Chart.js
function initCharts(){
  new Chart($id('focusChart').getContext('2d'),{
    type:'line',
    data:{
      labels:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
      datasets:[
        {label:'Focus Score',data:[72,85,61,90,78,92,88],borderColor:'#F5A623',backgroundColor:'rgba(245,166,35,0.07)',borderWidth:2,pointBackgroundColor:'#F5A623',pointRadius:4,fill:true,tension:0.4},
        {label:'Study Hours',data:[5,7,4,8,6,9,7],borderColor:'#4A9EE0',backgroundColor:'rgba(74,158,224,0.05)',borderWidth:2,pointBackgroundColor:'#4A9EE0',pointRadius:4,fill:true,tension:0.4,yAxisID:'y1'},
      ]
    },
    options:{
      responsive:true,maintainAspectRatio:false,
      plugins:{legend:{labels:{color:'rgba(240,237,230,0.6)',font:{size:11,family:'DM Sans'}}}},
      scales:{
        x:{grid:{color:'rgba(255,255,255,0.05)'},ticks:{color:'rgba(240,237,230,0.5)',font:{size:10}}},
        y:{grid:{color:'rgba(255,255,255,0.05)'},ticks:{color:'rgba(240,237,230,0.5)',font:{size:10}},max:100,min:0},
        y1:{position:'right',grid:{display:false},ticks:{color:'rgba(74,158,224,0.6)',font:{size:10}},max:12,min:0},
      }
    }
  });

  const subjects=[
    {name:'Compiler Design',weight:9,c:'rgba(226,75,74'},
    {name:'DSA Practice',   weight:7,c:'rgba(169,159,232'},
    {name:'OS Lab',         weight:6,c:'rgba(245,166,35'},
    {name:'CN Quiz',        weight:5,c:'rgba(245,166,35'},
    {name:'Email Triage',   weight:2,c:'rgba(76,175,130'},
    {name:'Feedback Form',  weight:1,c:'rgba(76,175,130'},
  ];
  $id('heatmapGrid').innerHTML=subjects.map(s=>{
    const a=(s.weight/10*0.65+0.12).toFixed(2);
    const tc=s.weight>=7?'#F09595':s.weight>=4?'#F5C475':'#4CAF82';
    return `<div class="hm-cell" style="background:${s.c},${a})" title="Weight: ${s.weight}/10">
      <div class="hm-label">${s.name}</div>
      <div class="hm-val" style="color:${tc}">${s.weight}<span style="font-size:10px;font-family:var(--fb)">/10</span></div>
    </div>`;
  }).join('');
}

// PANIC
let pIdx=0;
function refreshPanic(){
  const p=panicTasks[pIdx];
  $id('panicTask').textContent=p.task;
  $id('panicDue').textContent=p.due;
  if(p.weight>=9||p.task.includes('Compiler'))document.body.classList.add('panic-urgent');
  else document.body.classList.remove('panic-urgent');
}
$id('panicTrigger').onclick=()=>{$id('panicOverlay').classList.add('active');refreshPanic()};
$id('panicClose').onclick=()=>{$id('panicOverlay').classList.remove('active');document.body.classList.remove('panic-urgent')};
$id('panicSkip').onclick=()=>{pIdx=(pIdx+1)%panicTasks.length;refreshPanic()};
$id('panicStart').onclick=()=>{toast('\uD83D\uDE80 Focus timer started for: '+panicTasks[pIdx].task,'green');$id('panicOverlay').classList.remove('active');document.body.classList.remove('panic-urgent')};

// PWA
let dInstall=null;
window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();dInstall=e;$id('installBar').classList.add('show')});
$id('installBtn').onclick=async()=>{
  if(!dInstall){toast('Open in Chrome or Edge for PWA install','');return}
  dInstall.prompt();const{outcome}=await dInstall.userChoice;
  if(outcome==='accepted')toast('\u2705 ScholarBrain installed as PWA!','green');
  dInstall=null;$id('installBar').classList.remove('show');
};
$id('installClose').onclick=()=>$id('installBar').classList.remove('show');

// NAV
document.querySelectorAll('.nav-btn').forEach(b=>b.onclick=()=>{
  document.querySelectorAll('.nav-btn').forEach(x=>x.classList.remove('active'));b.classList.add('active');
});

// INIT
window.addEventListener('DOMContentLoaded',()=>{
  initDate();renderScheduler();renderCalendar();
  initBot();initOCR();initWaveform();
  renderCapsules();renderWebhooks();initCharts();initVoice();
  // Voice list needs trigger in some browsers
  window.speechSynthesis&&window.speechSynthesis.getVoices();
  window.speechSynthesis&&window.speechSynthesis.addEventListener('voiceschanged',()=>{});
});
</script>
</body>
</html>"""

html = html.replace('CAMPUS_IMG_HERE', dataurl)

out = '/mnt/user-data/outputs/scholarbrain_v2.html'
with open(out,'w',encoding='utf-8') as f:
    f.write(html)

sz = len(html)
print(f"Written: {out}")
print(f"Size: {sz/1024:.1f} KB")
print(f"Campus image embedded: {'YES' if 'data:image/jpeg' in html else 'NO'}")
