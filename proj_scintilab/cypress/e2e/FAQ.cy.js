describe('Modal do FAQ', () => {
    it('Eu, como cliente, gostaria acessar o FAQ', () => {
        cy.visit('http://127.0.0.1:8000/');
        cy.wait(120);
        cy.get('.btn').click();
        cy.get('.help-icon > img').click();
        cy.wait(120);
        cy.get('h2').should('have.text', 'Dúvidas Frequentes');
    })

})