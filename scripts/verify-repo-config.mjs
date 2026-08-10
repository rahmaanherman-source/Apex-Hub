import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
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
  if (!existsSync(join(root, relative))) failures.push(`${relative}: required deployment file is missing`);
}

const packageJson = JSON.parse(readFileSync(join(root, "package.json"), "utf8"));
if (packageJson.scripts?.build !== "tsc --noEmit && vite build") {
  failures.push("package.json: build script is not the deterministic Vercel build command");
}

if (failures.length) {
  console.error("APEX DEPLOYMENT CONFIGURATION FAILED");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`APEX deployment configuration verified: ${jsonFiles.length} JSON file(s), required Vite files present.`);
