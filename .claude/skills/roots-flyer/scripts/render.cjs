#!/usr/bin/env node
/*
 * Render a flyer HTML file to a 1080x1350 PNG (2x = 2160x2700) with headless Chromium.
 *
 *   node render.cjs input.html output.png
 *
 * Playwright ships with this environment. We try, in order:
 *   1. require('playwright') from the local node_modules or the global install
 *   2. chromium.launch() with no executablePath (uses PLAYWRIGHT_BROWSERS_PATH)
 *   3. a globbed chrome binary under /opt/pw-browsers (Claude Code web sandbox)
 * so the script keeps working even when the exact browser path changes.
 */
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

function loadPlaywright() {
  const candidates = [
    "playwright",
    "/opt/node22/lib/node_modules/playwright",
    "/usr/lib/node_modules/playwright",
    "/usr/local/lib/node_modules/playwright",
  ];
  for (const c of candidates) {
    try { return require(c); } catch (_) {}
  }
  // last resort: ask npm where the global root is
  try {
    const root = execSync("npm root -g").toString().trim();
    return require(path.join(root, "playwright"));
  } catch (_) {}
  throw new Error("Could not locate the 'playwright' module.");
}

function findChromium() {
  const globRoots = ["/opt/pw-browsers", process.env.PLAYWRIGHT_BROWSERS_PATH].filter(Boolean);
  for (const root of globRoots) {
    try {
      for (const dir of fs.readdirSync(root)) {
        if (!/^chromium(-\d+)?$/.test(dir)) continue;
        const bin = path.join(root, dir, "chrome-linux", "chrome");
        if (fs.existsSync(bin)) return bin;
      }
    } catch (_) {}
  }
  return null;
}

(async () => {
  const [, , input, output] = process.argv;
  if (!input || !output) {
    console.error("usage: node render.cjs input.html output.png");
    process.exit(1);
  }
  const { chromium } = loadPlaywright();

  let browser;
  try {
    browser = await chromium.launch();            // preferred: env-configured browser
  } catch (e) {
    const bin = findChromium();
    if (!bin) throw e;
    browser = await chromium.launch({ executablePath: bin });
  }

  const page = await browser.newPage({
    viewport: { width: 1080, height: 1350 },
    deviceScaleFactor: 2,
  });
  await page.goto("file://" + path.resolve(input));
  await page.evaluate(() => document.fonts && document.fonts.ready);
  await page.waitForTimeout(250);
  const el = (await page.$(".flyer")) || page;
  await el.screenshot({ path: output });
  await browser.close();
  console.log("wrote " + output);
})().catch((e) => { console.error(e); process.exit(1); });
