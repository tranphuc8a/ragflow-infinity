# DoXA Contract And Config

## Scope

This contract defines how DoXA parsing is integrated into both RAGFlow ingest lanes.

- Lane A: traditional ingest via `rag/app/naive.py`
- Lane B: dataflow parser node via `rag/flow/parser/parser.py`

## Required Runtime Dependency

- Python package: `doxa-sdk` (import path `doxa.parser.DoxaParser`)

If SDK is missing, parser returns/raises a clear installation error.

## Environment Variables

- `DOXA_API_TOKEN`: DoXA API token
- `DOXA_API_BASE`: DoXA API base URL
- `DOXA_IPAAS_TOKEN`: optional private gateway token

Parser-level form config can override these values.

## Config Keys

### Lane A (`parser_config.*`)

- `layout_recognize`: set to `DoXA`
- `doxa_token`: optional, overrides env token
- `doxa_url`: optional, overrides env base URL
- `doxa_ipaas_token`: optional, overrides env iPaaS token
- `doxa_parse_method`: optional, default `default`
- `doxa_options`: optional object for future parser options

### Lane B (`setups.pdf.*`)

- `parse_method`: set to `DoXA` / `doxa`
- `doxa_token`
- `doxa_url`
- `doxa_ipaas_token`
- `doxa_parse_method` (default: `default`)
- `doxa_options` (optional object)

## Output Mapping Contract

DoXA output is normalized by `deepdoc/parser/doxa_parser.py`.

Expected parser return:

- `sections`: list of tuple `(text, "")`
- `tables`: empty list for current DoXA path

Lane mapping behavior:

- Lane A consumes `sections`/`tables` directly.
- Lane B maps normalized section text into parser node bboxes as:
  - `{ "text": "..." }`

## Error Contract

`check_installation()` enforces:

- SDK availability
- token presence
- base URL presence

Failure messages are explicit and surfaced via callback (Lane A) or exception (Lane B).

## Security Notes

- Tokens are never logged.
- UI token fields are password inputs.
- Prefer env-based secrets in production; use form overrides only when needed.
