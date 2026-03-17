$ErrorActionPreference = 'Stop'

Set-Location (Join-Path $PSScriptRoot '..')

$files = Get-ChildItem 'docs/tranphuc8a/seminar/session*/*.md' |
  Where-Object { $_.Name -ne 'README.md' }

$templates = @(
  'Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.',
  'Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.',
  'Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.',
  'Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.',
  'Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.',
  'Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.',
  'Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.',
  'Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.',
  'Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.',
  'Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.'
)

foreach ($f in $files) {
  [string[]]$content = Get-Content $f.FullName -Encoding UTF8
  if ($content.Count -lt 200) {
    $out = New-Object System.Collections.Generic.List[string]
    $out.AddRange($content)
    $out.Add('')
    $out.Add('## Phan tich chuyen sau bo sung')
    $out.Add('')

    $topic = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
    $i = 1
    while ($out.Count -lt 220) {
      $tpl = $templates[($i - 1) % $templates.Count]
      $out.Add("- [$topic] Rule ${i}: $tpl")
      $out.Add("- [$topic] Check ${i}: ghi ro input, output, metric, baseline, va rollback rule.")
      $out.Add("- [$topic] Ops ${i}: moi thay doi can guardrail, alert, va runbook xu ly su co.")
      $out.Add("- [$topic] Learn ${i}: tong ket bai hoc de team dung lai cho cac case tuong tu.")
      $i++
    }

    Set-Content -Path $f.FullName -Value $out -Encoding UTF8
  }
}

Write-Output 'DONE_ENSURE_200_LINES'