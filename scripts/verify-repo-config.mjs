import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();
const ignored = new Set([".git", "node_modules", "dist"]);
const failures = [];
const jsonFiles = [];

function walk(dir) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (ignored.has(entry.name)) continue;
    const full = join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (entry.isFile() && entry.name.endsWith(".json")) jsonFiles.push(full);
  }
}

walk(root);

for (const file of jsonFiles) {
  try {
    JSON.parse(readFileSync(file, "utf8"));
  } catch (error) {
    failures.push(`${file}: invalid JSON — ${error.message}`);
  }
}

const requiredFiles = [
  "package.json",
  "vercel.json",
  "index.html",
  "tsconfig.json",
  "vite.config.ts",
  "src/main.tsx",
  "src/App.tsx",
];

for (const relative of requiredFiles) {
  if (!existsSync(join(root, relative))) {
    failures.push(`${relative}: required deployment file is missing`);
  }
}

const packageJson = JSON.parse(readFileSync(join(root, "package.json"), "utf8"));
const expectedBuild = "node scripts/verify-repo-config.mjs && tsc --noEmit && vite build";

if (packageJson.scripts?.build !== expectedBuild) {
  failures.push(`package.json: build script must be exactly: ${expectedBuild}`);
}

const vercelJson = JSON.parse(readFileSync(join(root, "vercel.json"), "utf8"));
if (vercelJson.framework !== "vite") {
  failures.push('vercel.json: framework must be "vite"');
}
if (vercelJson.buildCommand !== "npm run build") {
  failures.push('vercel.json: buildCommand must be "npm run build"');
}
if (vercelJson.outputDirectory !== "dist") {
  failures.push('vercel.json: outputDirectory must be "dist"');
}

if (failures.length) {
  console.error("APEX DEPLOYMENT CONFIGURATION FAILED");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`APEX deployment configuration verified: ${jsonFiles.length} JSON file(s), required Vite files present.`);
