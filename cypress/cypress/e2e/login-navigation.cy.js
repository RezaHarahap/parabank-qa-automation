describe('ParaBank login and navigation smoke', () => {
  beforeEach(() => cy.visit('/index.htm'));

  it('shows the login form on the home page', () => {
    cy.title().should('contain', 'ParaBank');
    cy.get('input[name="username"]').should('be.visible');
    cy.get('input[name="password"]').should('be.visible');
  });

  it('shows feedback for invalid credentials', () => {
    cy.get('input[name="username"]').type('invalid_portfolio_user');
    cy.get('input[name="password"]').type('invalid_password');
    cy.get('input[type="submit"]').click();
    cy.get('#rightPanel .error').should('be.visible').and(($error) => { expect($error.text().trim()).to.not.equal(''); });
  });

  it('logs in with configured disposable demo credentials and opens account overview', function () {
    const username = Cypress.env('username');
    const password = Cypress.env('password');
    if (!username || !password) {
      this.skip();
    }
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(password, { log: false });
    cy.get('input[type="submit"]').click();
    cy.get('#leftPanel').should('be.visible');
    cy.contains('a', 'Accounts Overview').click();
    cy.url().should('include', 'overview.htm');
  });
});
