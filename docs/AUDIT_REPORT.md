# Initial Project Audit Report

Audit date: 2026-10-25

## Summary

- Static checks: **Passed** for Python syntax, JavaScript syntax, JSON parsing, JMeter XML parsing, CSV column consistency, and ZIP integrity/content parity.
- Browser/API/performance test suites: **Not yet executed successfully**.
- Target connectivity from the build container: **Blocked** because DNS resolution for `parabank.parasoft.com` failed (`curl: (6) Could not resolve host`). This does not establish that the public website is down.

## Issues found and corrected during audit

1. Removed the unverified assumption that a seeded `john/demo` ParaBank account exists. Selenium and Cypress valid-login scenarios now skip unless disposable demo credentials are configured.
2. Cypress no longer asserts one exact invalid-login sentence; it checks for visible non-empty error feedback.
3. Removed hardcoded customer ID assumptions from the Postman environment and deferred customer/business API tests until the live API contract is verified.
4. The Postman collection now starts with read-only service-index and OpenAPI-document discovery checks. The OpenAPI path is still a hypothesis to verify against the live service index; failures must not automatically be reported as application defects.
5. Changed the JMeter smoke sampler from a login endpoint containing credentials in the URL path to a single read-only homepage GET. The plan uses one virtual user and one loop.
6. Rebuilt the ZIP after the corrections and checked that every project file is present in the archive.

## Actual local checks

| Check | Result | Evidence / notes |
|---|---|---|
| Python syntax | Passed | `selenium-tests/tests/*.py` compile successfully |
| JavaScript syntax | Passed | `node --check` for Cypress config and spec |
| JSON parsing | Passed | Postman collection, Postman environment, Cypress package manifest |
| JMeter XML parse | Passed | `jmeter/ParaBank_ReadOnly_Smoke.jmx` parses as XML |
| Test case CSV | Passed | 13 data rows; all rows have 11 columns |
| ZIP integrity/content | Passed | Archive integrity passes; archive contents match project files |
| Selenium pytest execution | Blocked | `ModuleNotFoundError: No module named 'selenium'` during collection; tests did not execute |
| Website HTTP access | Blocked | DNS resolution failure from build container |
| Browser/tool binaries | Partial | Chromium exists; no `chromedriver`, `jmeter`, or `katalon` command was found in PATH |
| Cypress runtime | Not run | Cypress package is not installed in this environment |
| Postman Runner | Not run | Requires Postman and reachable target |
| Katalon execution | Not run | Repository contains setup instructions, not a validated native Katalon project |
| JMeter execution | Not run | Only the JMX file's XML structure was validated |

## Remaining actions before calling this portfolio execution-ready

1. On a machine with internet access, install dependencies from `selenium-tests/requirements.txt` and `cypress/package.json`.
2. Confirm ParaBank is reachable and inspect its current DOM and service index.
3. Create a disposable demo user through the website if registration is supported; set `PARABANK_USERNAME` and `PARABANK_PASSWORD` locally only.
4. Execute Selenium and Cypress, review selectors and expected messages, and save reports/evidence.
5. Import and run the Postman collection; verify the OpenAPI endpoint path and schema against the live service index.
6. Open the JMX in Apache JMeter and run only the single-user, single-loop read-only smoke.
7. Create and execute the Katalon suite in Katalon Studio; record its real report.

**No functional test is marked Passed in this audit because none of the live browser/API/performance suites has completed.**
