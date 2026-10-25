const { defineConfig } = require('cypress');

module.exports = defineConfig({
  video: true,
  screenshotOnRunFailure: true,
  e2e: {
    baseUrl: process.env.CYPRESS_BASE_URL || 'https://parabank.parasoft.com/parabank',
    specPattern: 'cypress/e2e/**/*.cy.js',
    defaultCommandTimeout: 10000,
  },
});
