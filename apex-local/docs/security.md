# Security standard

- Secrets remain in `secrets/.env`; `.gitignore` excludes the directory.
- Mutating commerce/payment/shell/file operations require explicit approval.
- Local inference is the default and cloud fallback is disabled.
- Audit logs must not contain secrets; prompt/response logging is disabled by default.
- Review Windows optimization changes with `-DryRun` before applying them.
