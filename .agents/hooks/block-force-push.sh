#!/bin/bash
# Hook PreToolUse: blokir "git push --force" (atau -f) yang dijalankan agen lewat run_command.
# Dipicu tiap kali agen mau jalankan tool run_command (lihat matcher di .agents/hooks.json).
# Input: JSON dari stdin, field command ada di .toolCall.args.CommandLine.
# Output: JSON {"decision": "allow"} atau {"decision": "deny", "reason": "..."} ke stdout.
#
# CATATAN: skema hook Antigravity CLI masih bisa berubah antar versi — kalau hook ini
# tidak jalan seperti diharapkan, cek ulang lewat `agy inspect` dan dokumentasi resmi
# https://antigravity.google/docs/hooks sebelum menganggap ini rusak.

input=$(cat)

# Ambil isi command dari JSON tanpa bergantung ke jq (belum tentu terpasang di semua mesin).
command_line=$(echo "$input" | grep -o '"CommandLine"[[:space:]]*:[[:space:]]*"[^"]*"' | sed -E 's/.*: *"(.*)"/\1/')

if echo "$command_line" | grep -qiE "git[[:space:]]+push.*(--force|-f\b)"; then
  echo '{"decision":"deny","reason":"Force push ke remote diblokir hook keamanan project Lentera Pudar. Kalau memang perlu (mis. rebase lokal yang sudah didiskusikan), jalankan manual dari terminal biasa di luar Antigravity, bukan lewat agen."}'
  exit 0
fi

echo '{"decision":"allow"}'
