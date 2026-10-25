# Cypress suite

Install Node.js, then run `npm install`, `npx cypress verify`, and `npm run cy:run`.

Override credentials only with disposable demo credentials:

```bash
# macOS/Linux
CYPRESS_BASE_URL=https://parabank.parasoft.com/parabank npx cypress run
# Windows PowerShell
$env:CYPRESS_BASE_URL='https://parabank.parasoft.com/parabank'; npx cypress run
```

The selectors and expected text are starter assumptions based on the known ParaBank UI and must be verified against the live DOM before a test is considered stable. If the demo copy/credentials have changed, record the observed behavior and adjust the test based on evidence.
