describe('funcionário vai filtrar as ordens por status', () => {
    it('cenario1', () => {

        cy.visit('http://127.0.0.1:8000/');
        cy.wait(60);
        cy.get('.custom-span > a').click()
        cy.wait(60);
        cy.get('#id_username').type('projetos2')
        cy.wait(60);
        cy.get('#id_password').type('cesar2024')
        cy.wait(60);
        cy.get('#customer-register-btn').click()
        cy.wait(60);
        cy.get('[name="choosen_date"]').select('Todos')
        cy.wait(60);
        cy.get('[name="choosen_status"]').select('Cancelada')
        cy.wait(60);
        cy.get('.main-header > :nth-child(1) > button').click()
        cy.wait(60);
        cy.get('tbody > tr > :nth-child(4)').should('have.text', 'Cancelada');

    })

})