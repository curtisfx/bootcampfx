// Mirrors the gesture classifier in runner.html (SWIPE_DIST/TAP_DIST/TAP_MS + conditions).
const SWIPE_DIST = 40, TAP_DIST = 12, TAP_MS = 320;

// Classify a completed monotonic gesture: pointerdown at (x0,y0,t0) -> pointerup at (x1,y1,t1).
// The real handler classifies on the first threshold crossing; for monotonic swipes the final
// displacement is equivalent. Returns 'slide' | 'jump-swipe' | 'jump-tap' | 'none'.
function classify(x0, y0, t0, x1, y1, t1) {
  const dx = x1 - x0, dy = y1 - y0, dt = t1 - t0;
  if (dy > SWIPE_DIST && dy > Math.abs(dx)) return 'slide';
  if (dy < -SWIPE_DIST && Math.abs(dy) > Math.abs(dx)) return 'jump-swipe';
  if (dt < TAP_MS && Math.hypot(dx, dy) < TAP_DIST) return 'jump-tap';
  return 'none';
}

const cases = [
  // name, x0,y0,t0, x1,y1,t1, expected
  ['tap, no movement',            0,0,0,  0,0,100,      'jump-tap'],
  ['tap, tiny drift (8px)',       0,0,0,  6,5,120,      'jump-tap'],
  ['down swipe 60px',             0,0,0,  0,60,150,     'slide'],
  ['down swipe 45px',             0,0,0,  0,45,150,     'slide'],
  ['down swipe with drift (50/20)',0,0,0, 20,50,150,    'slide'],
  ['SHALLOW down swipe 30px FAST',0,0,0,  0,30,150,     'none'],   // the old bug: used to jump
  ['SHALLOW down swipe 30px SLOW',0,0,0,  0,30,500,     'none'],
  ['up swipe 60px',               0,0,0,  0,-60,150,    'jump-swipe'],
  ['diagonal horizontal-dominant', 0,0,0, 40,30,150,    'none'],
  ['long press, no movement',     0,0,0,  0,0,500,      'none'],
  ['down 40px exactly (threshold)',0,0,0, 0,40,150,     'none'],
];

let fail = 0;
for (const [name, x0,y0,t0, x1,y1,t1, want] of cases) {
  const got = classify(x0, y0, t0, x1, y1, t1);
  const ok = got === want;
  if (!ok) fail++;
  console.log((ok ? 'PASS' : 'FAIL') + '  ' + name + '  -> ' + got + (ok ? '' : ' (wanted ' + want + ')'));
}
console.log('\n' + (fail === 0 ? 'ALL ' + cases.length + ' PASS' : fail + ' FAILURES'));
process.exit(fail === 0 ? 0 : 1);
