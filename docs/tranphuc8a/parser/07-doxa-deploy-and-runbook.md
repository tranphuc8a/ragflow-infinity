# DoXA Deploy And Runbook

## Deploy Checklist

1. Install DoXA SDK in runtime environment.
2. Configure env vars:
   - `DOXA_API_TOKEN`
   - `DOXA_API_BASE`
   - `DOXA_IPAAS_TOKEN` (optional)
3. Restart backend service.
4. Verify parser options show `DoXA` in Dataset and Agent PDF parser form.

## Smoke Test

### Lane A (Dataset)

1. Open dataset settings.
2. Set `PDF parser` to `DoXA`.
3. Optionally set DoXA URL/token in parser config fields.
4. Parse one PDF document.
5. Verify chunks are generated and indexed.

### Lane B (Dataflow)

1. Open Agent parser node for PDF.
2. Set `Parser method` to `DoXA`.
3. Optionally set DoXA URL/token.
4. Run pipeline for one PDF.
5. Verify parser node emits text chunks.

## Failure Handling

### Error: DoXA SDK not installed

- Symptom: `DoXA SDK not installed. Please install doxa-sdk.`
- Action: install dependency into active environment.

### Error: token missing

- Symptom: `DoXA token is required...`
- Action: set `DOXA_API_TOKEN` or provide form token.

### Error: URL missing

- Symptom: `DoXA URL is required...`
- Action: set `DOXA_API_BASE` or provide form URL.

### Empty parse result

- Check source PDF validity.
- Check DoXA service reachability.
- Confirm token/base URL are from same DoXA environment.

## Regression Checklist

Run at least:

- `test/unit_test/common/test_parser_config_utils.py`
- `test/unit_test/deepdoc/parser/test_doxa_parser.py`
- `test/unit_test/rag/test_doxa_lane_wiring.py`
- Existing parser sanity test:
  - `test/unit_test/deepdoc/parser/test_pdf_garbled_detection.py`

## Rollout Notes

- Roll out behind environment-based enablement first.
- Monitor parse failure rate and parser latency.
- If failure rate increases, switch parser method back to existing parser for impacted datasets.
