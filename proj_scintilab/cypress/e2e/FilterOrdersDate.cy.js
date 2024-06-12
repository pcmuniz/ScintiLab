describe('funcionário vai cancelar a ordem emitida', () => {
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
        cy.get('[name="choosen_date"]').select('12/06/2024')
        cy.wait(60);
        cy.get('[name="choosen_status"]').select('Todos')
        cy.wait(60);
        cy.get('.main-header > :nth-child(1) > button').click()
        cy.wait(60);
        cy.get(':nth-child(3) > tr > :nth-child(1)').should('have.text', '12/06/2024');

    })

})