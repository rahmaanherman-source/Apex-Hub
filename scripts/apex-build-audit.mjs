import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const root = process.cwd();
const packagePath = resolve(root, 'package.json');
if (!existsSync(packagePath)) {
  console.error('BUILD_AUDIT_FAIL: package.json not found');
  process.exit(1);
}

let pkg;
try {
  pkg = JSON.parse(readFileSync(packagePath, 'utf8'));
} catch (error) {
  console.error(`BUILD_AUDIT_FAIL: invalid package.json: ${error.message}`);
  process.exit(1);
}

if (!pkg.scripts?.build) {
  console.error('BUILD_AUDIT_FAIL: package.json is valid but scripts.build is missing');
  process.exit(1);
}

console.log(`BUILD_AUDIT_OK: build script = ${pkg.scripts.build}`);
try {
  execFileSync(process.platform === 'win32' ? 'npm.cmd' : 'npm', ['run', 'build'], {
    stdio: 'inherit',
    cwd: root,
  });
  console.log('BUILD_AUDIT_OK: npm run build passed');
} catch (error) {
  console.error(`BUILD_AUDIT_FAIL: npm run build exited with code ${error.status ?? 1}`);
  process.exit(error.status ?? 1);
}
